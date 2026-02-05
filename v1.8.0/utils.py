import sys

import os
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)

import os
from pathlib import Path

from PySide6.QtWidgets import (QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QMainWindow, QMenu, QGraphicsDropShadowEffect)
from PySide6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QBrush, QMouseEvent, QPixmap, QAction, QDesktopServices, QGuiApplication
from PySide6.QtCore import Qt, QThread, Signal, QPoint, QObject, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize, QUrl
import cv2
import numpy as np
import requests
import random
from datetime import datetime, timezone, timedelta
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import base64

import time
import threading
import queue

import webbrowser
from cryptography.fernet import Fernet
import traceback
import subprocess

ROOT = Path(__file__).resolve().parents[1]
COLOR = {
    0: (0, 150, 95),     # Grass Green - person
    1: (0, 242, 255),    # yellow - bicycle (변경)
    2: (180, 130, 70),   # Steel Blue - car
    3: (0, 140, 255),    # Dark Orange - motorcycle
    4: (219, 112, 147),  # Medium Purple - bus
    5: (204, 209, 72),   # Medium Turquoise - truck
    6: (147, 20, 255),   # Deep Pink - fire
}

class Video_Buffer:
    def __init__(self, pipe="video1", appsink_name="video_sink", resolution=(640,480), chg_fps_mode = False, fps = 30):
        self._frame = None
        self.connection_status = True  # RTSP 연결 상태를 추적하는 변수
        self.video_source = f'rtspsrc location=rtsp://{pipe} latency=10 buffer-mode=0 protocols=tcp'
        print(self.video_source)
        if chg_fps_mode == True:
            self.video_codec = '! rtph264depay ! h264parse '  # 'application/x-rtp' 생략
            self.video_decode = f'! decodebin ! videorate ! capsfilter name=capsfilter0 caps=video/x-raw,framerate={fps}/1 ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'
            # self.video_decode = f'! nvh264dec ! videorate ! capsfilter name=capsfilter0 caps=video/x-raw,framerate={fps}/1 ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'

        else:
            self.video_codec = '! application/x-rtp, encoding-name=(string)H264, payload=96 ! rtph264depay ! h264parse '
            # self.video_decode = f'! decodebin ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
            # self.video_decode = f'! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'
            # self.video_decode = f'! nvh264dec ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'
            # self.video_decode = f'! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
            self.video_decode = f'! decodebin ! videorate ! capsfilter name=capsfilter0 caps=video/x-raw ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=5 drop=true'

        self.video_pipe = None
        self.video_sink = None
        self.appsink_name = appsink_name
        self.run()

    def start_gst(self, config=None):
        if not config:
            config = [
                'videotestsrc ! decodebin',
                f'! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={self.appsink_name}'
            ]

        command = ' '.join(config)
        try:
            self.video_pipe = Gst.parse_launch(command)
        except:
            self.video_pipe = Gst.parse_launch(command)

        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name(self.appsink_name)
        
        if not self.video_sink:
            print(f"Failed to get appsink named {self.appsink_name}")
            return
        
        self.video_sink.set_property("emit-signals", True)
        self.video_sink.set_property("sync", False)

    @staticmethod
    def gst_to_opencv(sample):
        buf = sample.get_buffer()
        caps = sample.get_caps()
        array = np.ndarray(
            (
                caps.get_structure(0).get_value('height'),
                caps.get_structure(0).get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def read(self):
        if self.frame_available():
            return self.frame_available(), self._frame
        else:
            return self.frame_available(), np.zeros((640, 480, 3), dtype=np.uint8)
        
    def frame_available(self):
        # 연결 상태를 먼저 확인하고, 끊겨있으면 False를 리턴
        if not self.connection_status:
            return False
        return self._frame is not None

    def run(self):
        try:
            self.start_gst(
                [
                    self.video_source,
                    self.video_codec,
                    ' ! queue leaky=downstream max-size-buffers=10 ',
                    self.video_decode
                ]
            )

            if self.video_sink:
                self.video_sink.connect('new-sample', self.callback)

            bus = self.video_pipe.get_bus()
            bus.add_signal_watch()
            bus.connect("message", self.on_message)
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.ERROR or t == Gst.MessageType.EOS:
            self.connection_status = False  # 연결 상태를 False로 설정
            print(f"Error or EOS detected. Reconnecting...")

            if self.video_pipe:
                self.video_pipe.set_state(Gst.State.NULL)

            # self.run()  # 파이프라인이 NULL 상태가 된 후에 재시작

    def callback(self, sink):
        try:
            sample = sink.emit('pull-sample')
            if sample is None:
                print("No sample received, returning...")
                return Gst.FlowReturn.ERROR  # 적절한 예외 처리가 이루어져야 함
            
            new_frame = self.gst_to_opencv(sample)
            self._frame = new_frame

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error in callback at {current_time}: {e}\n{tb}", file=sys.stderr)
            return Gst.FlowReturn.ERROR

        return Gst.FlowReturn.OK

    def change_framerate(self, fps):
        """Change the framerate dynamically using capsfilter."""
        if fps == 30:
            fps = 10
        if self.video_pipe:
            # Get the capsfilter element from the pipeline
            capsfilter = self.video_pipe.get_by_name("capsfilter0")
            if capsfilter:
                # Create new caps with the updated framerate
                new_caps = Gst.Caps.from_string(f"video/x-raw,framerate={fps}/1")
                capsfilter.set_property("caps", new_caps)
                # print(f"Framerate changed to {fps} FPS")
            else:
                print("Could not find capsfilter element.")

    def release(self):
        if self.video_pipe:
            self.video_pipe.set_state(Gst.State.NULL)  # 파이프라인을 중지 상태로 설정
            self.connection_status = False  # 연결 상태를 False로 설정
            self.video_pipe = None
            # print("RTSP stream stopped.")


class RtspVideoReader:
    """
    타임아웃 가능한 비디오 리더기.
    cv2.VideoCapture.read()가 네트워크 문제로 멈추는 현상을 방지합니다.
    """
    def __init__(self, rtsp_url):
        self.url = rtsp_url
        self.queue = queue.Queue(maxsize=30)  # 프레임 버퍼
        self.cap = None
        self.__thread_active = False
        self.read_thread = None
        
        # 스레드 시작
        self.start()

    def _reader_thread(self):
        """백그라운드에서 프레임을 읽어 큐에 넣는 스레드 함수"""
        print(f"[Reader Thread] 스레드 시작. {self.url} 연결 시도...")
        self.cap = cv2.VideoCapture(self.url)
        
        if not self.cap.isOpened():
            print(f"[Reader Thread] 에러: 스트림을 열 수 없습니다.")
            self.queue.put(None)  # 시작 실패 신호
            return

        print("[Reader Thread] 스트림 열기 성공. 읽기 시작.")
        while self.__thread_active:
            # grab() / retrieve() 방식 사용
            ret_grab = self.cap.grab()
            
            if not ret_grab:
                # 스트림이 정상적으로 종료된 경우
                print("[Reader Thread] grab()=False. 스트림이 정상 종료되었습니다.")
                break
            
            # 가져온 프레임을 디코딩
            ret_retrieve, frame = self.cap.retrieve()
            
            if not ret_retrieve:
                # 디코딩 실패 (드물게 발생)
                continue
            
            # 큐가 가득 찼으면 가장 오래된 프레임을 버림
            if self.queue.full():
                try:
                    self.queue.get_nowait()
                except queue.Empty:
                    pass  # 혹시 모를 동시성 문제 방지
            
            self.queue.put(frame)
            time.sleep(0.001)  # CPU 과점유 방지

        # 루프 종료 시 (정상 종료 또는 stop() 호출)
        print("[Reader Thread] 스레드 종료 중...")
        if self.cap:
            self.cap.release()
        self.queue.put(None)  # 종료 신호

    def start(self):
        """읽기 스레드를 시작합니다."""
        if self.__thread_active:
            print("[Reader] 이미 스레드가 실행 중입니다.")
            return
            
        self.__thread_active = True
        self.read_thread = threading.Thread(target=self._reader_thread)
        self.read_thread.daemon = True  # 메인 스레드 종료 시 함께 종료
        self.read_thread.start()

    def read(self, timeout=5.0):
        """
        큐에서 프레임을 읽어옵니다.
        'timeout' 초 동안 새 프레임이 없으면 (False, None)을 반환합니다.
        """
        try:
            # 타임아웃을 걸고 큐에서 프레임을 기다림
            frame = self.queue.get(timeout=timeout)
            
            if frame is None:
                # 스레드에서 보낸 종료 신호
                return False, None
                
            return True, frame
        except queue.Empty:
            # 큐가 비어있고 'timeout'이 경과함 -> 스트림이 멈춘 것으로 간주
            print(f"[Reader] {timeout}초 동안 새 프레임 없음. 타임아웃.")
            return False, None

    def stop(self):
        """읽기 스레드를 중지시킵니다."""
        print("[Reader] 중지 신호 전송...")
        self.__thread_active = False
        
        # 큐를 비워서 스레드가 멈출 수 있게 함
        while not self.queue.empty():
            try:
                self.queue.get_nowait()
            except queue.Empty:
                break
        
        if self.read_thread:
            self.read_thread.join(timeout=1.0)  # 스레드 종료 대기


class Connect_Camera(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)
    doubleClicked = Signal()

    def __init__(self, pipe, host, port, camera_name, viewer, plot_bbox = True, plot_label = True,  plot_roi = True, roi_thickness = 1, ai_active = False, live_viewer_blcok_active = False) -> None:
        super(Connect_Camera, self).__init__()
        # Declare and initialize instance variables.
        self.pipe = pipe
        self.__thread_active = True
        self.disconnect_cnt = 0
        self.__thread_pause = False
        self.camera_connect_flag = False
        # self.camera_num = camera_num
        self.camera_name = camera_name

        self.ai_active = ai_active

        self.viewer = viewer

        self.host = host
        self.port = port

        self.back_url = f"http://{self.host}:{self.port}/get-camera-ai-plot-data"

        self.roi_thickness = roi_thickness
        self.live_viewer_blcok_active = live_viewer_blcok_active
        # self.live_screen_block_img = cv2.imread(u":/ui/ui/images/ico_video_on.svg")
        self.plot_bbox = plot_bbox
        self.plot_label = plot_label
        self.plot_roi = plot_roi

        self.fps = 15

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()  # 더블 클릭 시 시그널 발생

    def run(self) -> None:
        if self.live_viewer_blcok_active:
            self.cap = None
            while self.__thread_active:
                # 로고 이미지를 뷰어 크기에 맞게 padding하여 emit
                width, height = self.viewer.width(), self.viewer.height()
                logo_pixmap = QPixmap(u":/ui/ui/images/logo.png")
                
                # 뷰어 크기에 맞는 빈 캔버스 생성 (검은색 배경)
                canvas = QPixmap(width, height)
                canvas.fill(Qt.black)
                
                # 로고를 캔버스 중앙에 배치
                painter = QPainter(canvas)
                x = (canvas.width() - logo_pixmap.width()) // 2
                y = (canvas.height() - logo_pixmap.height()) // 2
                painter.drawPixmap(x, y, logo_pixmap)
                painter.end()
                
                logo_image = canvas.toImage()
                self.ImageUpdated.emit(logo_image)
        else:
            self.cap = Video_Buffer(pipe=self.pipe, resolution=(640,480), fps = self.fps)
            self.camera_connect_flag = False

            session = requests.Session()
            # While the thread is active.
            t0 = time.time()
            while self.__thread_active:
                
                ret, self.frame_ori = self.cap.read()
                # print(ret)

                if ret == False : 
                    if time.time() - t0 > 5:
                        # self.cap.release()
                        # self.cap = cv2.VideoCapture(self.pipe)
                        continue
                    
                t0 = time.time()
                self.camera_connect_flag = True
                # If frame is read correctly.
                # self.frame = cv2.resize(self.frame_ori, dsize=(self.viewer.width(), self.viewer.height()))
                self.frame = np.array(self.frame_ori)

                if self.ai_active and  (self.plot_bbox or self.plot_label or self.plot_roi):
                    try:
                        receive_data = session.get(self.back_url, json={"msg" : self.camera_name}).json()

                        if receive_data[self.camera_name]:
                            line_thickness = 3 if self.frame.shape[1] == 1920 else 1
                            self.frame = plot_detect_info(img = self.frame, detect_info = receive_data[self.camera_name], line_thickness = line_thickness, roi_thickness = self.roi_thickness, plot_bbox = self.plot_bbox, plot_label = self.plot_label, plot_roi = self.plot_roi)
                    except:
                        pass                
                self.disconnect_cnt = 0
                height, width, channels = self.frame.shape
                bytes_per_line = width * channels
                cv_rgb_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

                qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)


                self.ImageUpdated.emit(qt_rgb_image)

                # time.sleep(0.033)
                sleep_time = max(0, (1 / self.fps) - (time.time() - t0))
                time.sleep(sleep_time)


        if self.cap is not None:
            self.cap.release()
        self.quit()

    def stop(self) -> None:
        self.__thread_active = False
        self.wait()

    def pause(self) -> None:
        self.__thread_pause = True

    def unpause(self) -> None:
        self.__thread_pause = False

class Connect_Playback(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)

    def __init__(self, url, viewers_widget) -> None:
        super(Connect_Playback, self).__init__()
        # Declare and initialize instance variables.
        self.pipe = url
        self.__thread_active = True
        self.fps = 0
        self.disconnect_cnt = 0

        self.viewers_widget = viewers_widget
        self.reader = None

    def run(self) -> None:
        try:
            self.pipe = "rtsp://" + self.pipe
            
            # RtspVideoReader 사용 (타임아웃 기능 포함)
            self.reader = RtspVideoReader(self.pipe)
            
            t0 = time.time()

            while self.__thread_active:
                # 타임아웃 5초로 프레임 읽기
                ret, self.frame_ori = self.reader.read(timeout=5.0)
                
                # print(f"Playback read: ret={ret}")
                
                if ret == False:
                    # 타임아웃 또는 스트림 종료
                    print("Playback: 스트림 종료 또는 타임아웃. 루프를 종료합니다.")
                    break

                # 프레임 리사이즈 및 표시
                frame = cv2.resize(self.frame_ori, dsize=(self.viewers_widget.width(), self.viewers_widget.height()))

                height, width, channels = frame.shape
                # Calculate the number of bytes per line.
                bytes_per_line = width * channels
                self.ImageUpdated.emit(QImage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).data, width, height, bytes_per_line, QImage.Format_RGB888))
                
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
        finally:
            if self.reader:
                self.reader.stop()
            self.quit()

    def stop(self) -> None:
        self.__thread_active = False
        if self.reader:
            self.reader.stop()
        self.wait()         

class Plot_Camera_Viewer(QLabel):
    clicked = Signal(QPoint)  # 사용자가 클릭한 위치를 전달하는 시그널

    def __init__(self, parent=None):
        super().__init__(parent)
        self.point_list = []
        self.non_active_point_list = []
        self.zoom_factor = 1.0  # 초기 확대 배율
        self.offset = QPoint(0, 0)  # 확대/축소의 오프셋을 저장
        self.setScaledContents(True)  # QLabel이 이미지 크기에 맞게 조정됨

        # self.setMinimumSize(1, 1)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(event.pos())  # 클릭 위치를 emit

        if event.button() == Qt.RightButton:
            self.clicked.emit(QPoint(-1, -1))  # 클릭 위치를 emit

    def set_point(self, point_list, img_size = None):
        # self.point_list = [QPoint(int(img_size[0] * point[0]), int(img_size[1] * point[1])) for point in point_list]  # QPoint 객체로 변환
        self.point_list = []
        for point in point_list:
            self.point_list.append([point[0], point[1]])
        
        self.update()

    def set_gray_point(self, non_active_point_list, img_size = None):
        self.non_active_point_list = []
        for point_list in non_active_point_list:
            non_point_list = []

            for point in point_list:
                non_point_list.append([point[0], point[1]])

            self.non_active_point_list.append(non_point_list)

            # self.non_active_point_list.append([QPoint(int(img_size[0] * point[0]), int(img_size[1] * point[1])) for point in point_list]  )
            # self.non_active_point_list.append([[point[0], point[1]] for point in point_list])
                                  
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        gray_painter = QPainter(self)
        gray_pen = QPen(QColor(QColor(84,84,84)))
        
        gray_pen.setWidth(5)  # 펜의 두께 설정
        gray_painter.setPen(gray_pen)

        fillColor = QColor(84,84,84,127)
        brush = QBrush(fillColor)
        gray_painter.setBrush(brush)

        for gray_point_list in self.non_active_point_list:
            if len(gray_point_list) > 2:
                gray_point_list = [QPoint(int(self.width() * point[0]), int(self.height() * point[1])) for point in gray_point_list]  # QPoint 객체로 변환
                gray_polygon = QPolygon(gray_point_list)
                gray_painter.drawPolygon(gray_polygon)
                # gray_painter.drawPolygon([x * self.width(), y * self.height()])  # 제공된 좌표에 점을 그림


        painter = QPainter(self)
        pen = QPen(QColor(QColor(83,195,2)))
        
        pen.setWidth(5)  # 펜의 두께 설정
        painter.setPen(pen)

        fillColor = QColor(129,215,66,127)
        brush = QBrush(fillColor)
        painter.setBrush(brush)

        for point in self.point_list:
            painter.drawPoint(int(point[0] * self.width()), int(point[1] * self.height()))  # 제공된 좌표에 점을 그림
        if len(self.point_list) > 2:
            point_list = [QPoint(int(self.width() * point[0]), int(self.height() * point[1])) for point in self.point_list]  # QPoint 객체로 변환
            polygon = QPolygon(point_list)
            painter.drawPolygon(polygon)

    def reset(self):
        self.point_list = []
        self.non_active_point_list = []

        self.update()

    def reset_green_area(self):
        self.point_list = []

        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update()


class FadeOutWindow(QWidget):
    def __init__(self, parent=None, msg="None"):
        super().__init__(parent=parent)
        self.msg = msg
        self.initUI()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.startFadeOut()

    def initUI(self):
        self.setWindowTitle('Information')
        self.setFixedSize(381, 61)  # 고정 크기
        self.setStyleSheet("background-color: rgba(255, 255, 255, 255); border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.info_label = QLabel(self.msg, self)
        self.info_label.setObjectName(u"info_label")
        # self.info_label.setGeometry(QRect(0, 0, 381, 61))

        self.info_label.setStyleSheet("background-color: rgb(47, 129, 247); border-radius: 10px; color: white; font-size: 14px;")
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        # self.fadeout_window.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)


    def startFadeOut(self):
        QTimer.singleShot(1000, self.fadeOut)

    def fadeOut(self):
        self.anim = QPropertyAnimation(self, b'windowOpacity')
        self.anim.setDuration(1500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(self.close)
        self.anim.start()

class FadeOutInWindow(QWidget):
    def __init__(self, parent=None, camera_name = 0, data = {}, window_num = 0):
        super().__init__(parent=parent)
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # print(data)
        self.window_title = f"Alarm {window_num}"
        if len(data):
            self.msg = f"{camera_name} 카메라 : {Eng2kor(data[0])} \n {data[2]}"

        self.initUI()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.toggleFade()

    def initUI(self):
        self.setWindowTitle(self.window_title)
        self.setFixedSize(381, 61)  # 고정 크기
        self.setStyleSheet("background-color: rgba(255, 255, 255, 255); border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.info_label = QLabel(self.msg, self)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet("background-color: rgb(53, 132, 228); border-radius: 10px; color: white; font-size: 14px;")
        # self.info_label.setStyleSheet("background-color: rgb(19, 193, 13); border-radius: 10px; color: white; font-size: 14px;")
        
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)


    def toggleFade(self):
        self.anim = QPropertyAnimation(self, b'windowOpacity')
        self.anim.setDuration(1500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(self.fadeIn)
        self.anim.start()

    def fadeIn(self):
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.finished.connect(self.toggleFade)
        self.anim.start()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.close()  # 창을 닫습니다.

def plot_one_box(x, img, color=None, label=None, bbox=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    if bbox:
        cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def draw_roi(points, image, color, thickness=1, is_closed=True):
    """ 이미지에 관심 영역(ROI)를 그립니다. """
    cv2.polylines(image, [np.int32(points)], is_closed, color, thickness)

def TF_detect_area(detect_info, img_size):
    TF_detect_area_list = []
    if len(detect_info):
        if isinstance(detect_info[0], list): 
            for item in detect_info:
                # 새로운 리스트의 첫 번째 요소는 기존 문자열 그대로 유지
                label = item[0]
                coordinates = item[1:]

                # 좌표에 대한 변환 수행
                transformed_coordinates = [[int(x[0] * img_size[0]), int(x[1] * img_size[1])] for x in coordinates]
                
                # 변환된 좌표를 포함하는 새로운 리스트 생성
                TF_detect_area_list.append([label] + transformed_coordinates)

        elif isinstance(detect_info[0], str): 
            label = detect_info[0]
            coordinates = detect_info[1:]

            # 좌표에 대한 변환 수행
            transformed_coordinates = [[int(x[0] * img_size[0]), int(x[1] * img_size[1])] for x in coordinates]
            
            # 변환된 좌표를 포함하는 새로운 리스트 생성
            TF_detect_area_list.append([label] + transformed_coordinates)

    return TF_detect_area_list

def TF_bbox(bbox, ori_imsz=(640, 360), target_imsz=(1920, 1080)):
    # 원본 이미지와 목표 이미지의 크기 비율 계산
    width_ratio = target_imsz[0] / ori_imsz[0]
    height_ratio = target_imsz[1] / ori_imsz[1]
    
    # 변환된 바운딩 박스를 저장할 리스트 초기화
    TF_boxes = []
    
    # 각 바운딩 박스에 대해 좌표 변환 수행
    for box in bbox:
        if len(box) == 8:
            x1, y1, x2, y2, id, conf, cls, ind  = box  # 좌표 추출
            # 좌표를 int(새로운 이미지 크기에 맞게 조정
            new_x1 = int(x1 * width_ratio)
            new_y1 = int(y1 * height_ratio)
            new_x2 = int(x2 * width_ratio)
            new_y2 = int(y2 * height_ratio)
        
            # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
            TF_boxes.append([new_x1, new_y1, new_x2, new_y2, id, conf, cls, ind])
        
        elif len(box) == 6:
            x1, y1, x2, y2, conf, cls, = box  # 좌표 추출

            # 좌표를 int(새로운 이미지 크기에 맞게 조정
            new_x1 = int(x1 * width_ratio)
            new_y1 = int(y1 * height_ratio)
            new_x2 = int(x2 * width_ratio)
            new_y2 = int(y2 * height_ratio)
            
            # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
            TF_boxes.append([new_x1, new_y1, new_x2, new_y2, conf, cls])

        if len(box) == 9:
                x1, y1, x2, y2, id, conf, cls, ind, status = box  # 좌표 추출
                # 좌표를 int(새로운 이미지 크기에 맞게 조정
                new_x1 = int(x1 * width_ratio)
                new_y1 = int(y1 * height_ratio)
                new_x2 = int(x2 * width_ratio)
                new_y2 = int(y2 * height_ratio)
            
                # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
                TF_boxes.append([new_x1, new_y1, new_x2, new_y2, id, conf, cls, ind, status])
        
    return TF_boxes

def plot_detect_info(img, detect_info, line_thickness = 1 , roi_thickness = 1, plot_bbox = True, plot_label = True, plot_roi = True):
    ROI_color_dict = {"Loitering": [53, 225, 225], "Intrusion": [35, 28, 255], "Fire": [33, 145, 237],
                                "Fight": [255, 0, 127], "Falldown": [230, 255, 121], "Trash": [0, 165, 255]}
    # names = { 0 : "person", 1 : "fire"}
    names = { 0 : "person", 1 : "bicycle", 2 : "car", 3 : "motorcycle", 4 : "bus", 5 : "truck", 6 : "fire"}


    # person_bbox = TF_bbox(detect_info["person_bbox"], ori_imsz=(1280, 720), target_imsz=(img.shape[1], img.shape[0]))
    # non_person_bbox = TF_bbox(detect_info["non_person_bbox"], ori_imsz=(1280, 720), target_imsz=(img.shape[1], img.shape[0]))

    person_bbox = TF_bbox(detect_info["person_bbox"], ori_imsz=(640, 480), target_imsz=(img.shape[1], img.shape[0]))
    non_person_bbox = TF_bbox(detect_info["non_person_bbox"], ori_imsz=(640, 480), target_imsz=(img.shape[1], img.shape[0]))

    for person_box in person_bbox:
        if len(person_box) == 9:
            x1, y1, x2, y2, id, conf, cls, ind, status = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                label = f'{id} {names[cls]} {100 * conf:.1f}%'
            else:
                label = False

            if status == 1 :
                bbox_color = (0,75,150)

            elif status == 2 :
                bbox_color = (60,20,220)

            elif status == 0 :
                bbox_color = (0,150,95)

            else:
                bbox_color = COLOR[int(cls)]
                # bbox_color = COLOR(int(cls))

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

        elif len(person_box) == 8:
            x1, y1, x2, y2, id, conf, cls, ind = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                label = f'{id} {names[cls]} {100 * conf:.1f}%'
            else:
                label = False

            # bbox_color = COLOR(int(cls))
            bbox_color = COLOR[int(cls)]

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    for (x1, y1, x2, y2, conf, cls) in non_person_bbox: #fire bbox
        xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
        conf = conf
        cls = int(cls)

        # bbox_color = (4,19,190)
        bbox_color = COLOR[int(cls)]
        if plot_label:
            label = f'{names[cls]} {100 * conf:.1f}%'
        else:
            label = False

        plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    if plot_roi:
        TF_roi_info = TF_detect_area(detect_info["ROI_ori"], img_size=(img.shape[1], img.shape[0]))
        for roi_info in TF_roi_info:
            draw_roi(points = roi_info[1:], 
                        image = img,
                        color = ROI_color_dict[roi_info[0]], 
                        thickness = roi_thickness, 
                        is_closed = True)

    return img

def load_info(host, port, file_name):
    data = {"msg" : {"file_name" : file_name}}

    # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
    url = f'http://{host}:{port}/load-info'
    # receive_data = requests.post(url, json=data).json()
    try:
        receive_data = requests.get(url, json=data).json()
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tb = traceback.format_exc()
        print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
        print(requests.get(url, json=data))
    if receive_data["success"] == True:
        return receive_data["data"]

    else: raise(f"{file_name} 파일을 찾을 수 없습니다.")

def save_info(host, port, file_name, info):
    data = {"msg" : {"file_name" : file_name, "info" : info}}
    url = f'http://{host}:{port}/save-info'

    receive_data = requests.put(url, json=data).json()

def Eng2kor(eng):
    if eng == "Intrusion": return "침입"
    elif eng == "Loitering": return "배회"
    elif eng == "Falldown": return "쓰러짐"
    elif eng == "Fire": return "방화"
    elif eng == "Fight": return "싸움"
    elif eng == "Trash": return "무단투기"


def Kor2eng(kor):
    if kor == "침입" : return "Intrusion"
    elif kor == "배회": return "Loitering"
    elif kor == "쓰러짐": return "Falldown"
    elif kor == "방화": return "Fire"
    elif kor == "싸움": return "Fight"
    elif kor == "무단투기": return "Trash"


    # gmail_sender = 'diddytpq5@gmail.com'
    # gmail_passwd = 'zqpx escp ebme yjyf'
    # TO = 'ysyang@microsystems.co.kr'

def get_datetime_from_path(path):
    parts = path.split('/')  # 경로를 '/'로 분할
    date_time_str = parts[-1].split('_')[0]  # 파일 이름에서 시간 부분 추출 ('08.54.48')
    date_str = parts[-3]  # 날짜 부분 추출 ('24.04.29')
    # 날짜와 시간 문자열 결합
    full_datetime_str = f"{date_str} {date_time_str}"
    # datetime 객체로 변환
    return datetime.strptime(full_datetime_str, "%y.%m.%d %H.%M.%S")

def get_datetime_from_list(list):
    img_base64, camera_name, date, video_time, label_info = list

    return datetime.strptime(date + " " + video_time, "%y-%m-%d %H:%M:%S")


def print_error(e):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tb = traceback.format_exc()
    print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

def check_nvidia_gpu():
    try:
        # 'nvidia-smi' 명령어 실행
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("NVIDIA GPU is available.")
            return True
        else:
            print("NVIDIA GPU is not available.")
            return False

    except FileNotFoundError:
        print("nvidia-smi command not found. No NVIDIA GPU available or drivers not installed.")
        return False


# ----------------------------------------------------------------------
# 커스텀 알림 시스템
# ----------------------------------------------------------------------
class CustomNotification(QWidget):
    """
    개별 알림 창을 담당하는 위젯 클래스.
    애니메이션, 타이머, 클릭 이벤트를 처리합니다.
    """
    # 닫힐 때 매니저에게 알리기 위한 시그널
    closed = Signal()
    clicked = Signal(dict)  # 클릭 시 알림 정보 전달

    def __init__(self, title, message, notification_data=None, duration=10000, parent=None):
        super().__init__(parent)
        self.duration = duration
        self.notification_data = notification_data  # 카메라 이름, 시간 등 정보 저장
        self.created_time = time.time()  # 생성 시간 기록
        self.title_text = title  # 디버깅용 타이틀 저장
        print(f"[DEBUG] 알림 생성: '{title}' | 생성시간: {time.strftime('%H:%M:%S', time.localtime(self.created_time))} | duration: {duration}ms")

        # --- 윈도우 설정 ---
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |    # 프레임(제목표시줄) 없음
            Qt.WindowType.Tool |                   # 태스크바에 표시 안 함
            Qt.WindowType.WindowStaysOnTopHint   # 항상 다른 창 위에 표시
        )
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) # 닫힐 때 메모리에서 삭제

        # --- 레이아웃 및 위젯 ---
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # 좌측 accent bar (색상 강조선)
        self.accent_bar = QLabel()
        self.accent_bar.setFixedWidth(4)
        self.accent_bar.setStyleSheet("background-color: #4A90E2; border-radius: 0px;")
        
        # 컨텐츠 영역
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(12, 10, 12, 10)
        content_layout.setSpacing(10)
        
        # 아이콘 영역
        self.icon_label = QLabel()  # 알림 아이콘
        self.icon_label.setFixedSize(24, 24)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.setStyleSheet("font-size: 18px;")
        
        # 텍스트 영역
        text_widget = QWidget()
        text_layout = QVBoxLayout(text_widget)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(4)
        
        self.title_label = QLabel(title)
        self.message_label = QLabel(message)
        self.message_label.setWordWrap(True)
        
        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.message_label)
        
        # 닫기 버튼
        self.close_button = QLabel("✕")
        self.close_button.setFixedSize(20, 20)
        self.close_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.close_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_button.mousePressEvent = lambda e: self.fade_out()
        
        # 컨텐츠 레이아웃에 추가
        content_layout.addWidget(self.icon_label)
        content_layout.addWidget(text_widget, 1)
        content_layout.addWidget(self.close_button)
        
        # 메인 레이아웃에 추가
        main_layout.addWidget(self.accent_bar)
        main_layout.addWidget(content_widget)

        # --- 모던한 스타일시트 (QSS) ---
        self.setStyleSheet("""
                CustomNotification {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                stop:0 #ffffff, stop:1 #fafbfc);
                    border-radius: 12px;
                    border: 1px solid #e1e4e8;
                }
                QLabel {
                    background-color: transparent;
                }
                #title_label {
                    font-size: 13px;
                    font-weight: bold;
                    color: #1a1a1a;
                    letter-spacing: -0.3px;
                }
                #message_label {
                    font-size: 12px;
                    color: #586069;
                    line-height: 1.5;
                }
                #close_button {
                    font-size: 16px;
                    color: #959da5;
                    font-weight: bold;
                }
                #close_button:hover {
                    color: #d73a49;
                }
                #icon_label {
                    color: #4A90E2;
                }
            """)

        # 객체 이름 설정
        self.title_label.setObjectName("title_label")
        self.message_label.setObjectName("message_label")
        self.close_button.setObjectName("close_button")
        self.icon_label.setObjectName("icon_label")

        # --- 위젯 크기 설정 ---
        self.setFixedWidth(360) # 알림창 너비
        self.adjustSize() # 내용에 맞게 높이 자동 조정
        
        # 그림자 효과를 위한 그래픽 효과 (더 모던한 느낌)
        self.setGraphicsEffect(self._create_shadow_effect())

        # --- 자동 닫기 타이머 ---
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fade_out) # 시간이 다 되면 fade_out 호출

        # --- 애니메이션 ---
        self.animation_geometry = QPropertyAnimation(self, b"geometry")
        self.animation_geometry.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation_geometry.setDuration(400) # 0.4초

        # slide-out 애니메이션 (사라질 때) - 라즈베리파이 호환을 위해 투명도 대신 위치 애니메이션 사용
        self.animation_slide_out = QPropertyAnimation(self, b"geometry")
        self.animation_slide_out.setEasingCurve(QEasingCurve.Type.InCubic)
        self.animation_slide_out.setDuration(300) # 0.3초
        # slide-out 애니메이션이 끝나면 위젯을 닫음
        self.animation_slide_out.finished.connect(self.close)

    def _create_shadow_effect(self):
        """
        그림자 효과를 생성하여 반환합니다.
        """
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)  # 블러 반경
        shadow.setXOffset(0)  # X 오프셋
        shadow.setYOffset(4)  # Y 오프셋 (아래로)
        shadow.setColor(QColor(0, 0, 0, 60))  # 반투명 검정
        return shadow

    def slide_in(self, target_pos):
        """
        알림을 화면 밖에서 'target_pos' 위치로 슬라이드 인.
        """
        # 이미 표시되었으면 중복 호출 방지
        if self.isVisible():
            return
            
        # 크기 재계산 (내용에 맞게)
        self.adjustSize()
        
        # 시작 위치 (목표 위치에서 살짝 아래, 약간의 오프셋 추가)
        start_x = target_pos.x()
        start_y = target_pos.y() + 100  # 최종 위치에서 100px 아래에서 시작
        start_rect = QRect(start_x, start_y, self.width(), self.height())
        
        # 종료 위치 (목표 지점)
        end_rect = QRect(target_pos, self.size())

        self.setGeometry(start_rect)
        self.show() # 위젯 보이기

        # 위치 애니메이션 (slide-in)
        self.animation_geometry.setStartValue(start_rect)
        self.animation_geometry.setEndValue(end_rect)
        self.animation_geometry.start()
        
        # 자동 닫기 타이머 시작 (duration이 -1이면 자동 닫기 안 함)
        if self.duration > 0 and not self.timer.isActive():
            self.timer.start(self.duration)
            print(f"[DEBUG] 타이머 시작: '{self.title_text}' | 예정 종료: {self.duration/1000:.1f}초 후")

    def move_to(self, target_pos):
        """
        알림을 현재 위치에서 'target_pos'로 부드럽게 이동 (스태킹 재정렬용)
        """
        # 이미 목표 위치에 있으면 애니메이션 스킵
        if self.pos() == target_pos:
            return
            
        # 현재 진행 중인 애니메이션이 있다면 중지
        self.animation_geometry.stop()
        
        # 새 이동 애니메이션 설정 및 시작
        self.animation_geometry.setStartValue(self.geometry())
        self.animation_geometry.setEndValue(QRect(target_pos, self.size()))
        self.animation_geometry.start()
        
    def fade_out(self):
        """
        알림을 부드럽게 사라지게 함 (Slide-out으로 대체 - 라즈베리파이 호환).
        """
        # 이미 fade_out이 호출된 경우 중복 실행 방지
        if hasattr(self, '_fading_out') and self._fading_out:
            return
        self._fading_out = True
        
        elapsed = time.time() - self.created_time
        print(f"[DEBUG] fade_out 호출: '{self.title_text}' | 경과시간: {elapsed:.1f}초 | 설정된 duration: {self.duration/1000:.1f}초 | 타이머활성: {self.timer.isActive()}")
        
        self.timer.stop() # 혹시 모를 타이머 중복 실행 방지
        
        # 현재 위치에서 오른쪽 화면 밖으로 슬라이드
        current_rect = self.geometry()
        end_rect = QRect(
            current_rect.x() + current_rect.width() + 50,  # 오른쪽으로 이동
            current_rect.y(),
            current_rect.width(),
            current_rect.height()
        )
        
        self.animation_slide_out.setStartValue(current_rect)
        self.animation_slide_out.setEndValue(end_rect)
        self.animation_slide_out.start()
        
        # 백업: 애니메이션이 완료되지 않을 경우를 대비해 강제 종료 타이머
        QTimer.singleShot(500, self._force_close)
    
    def _force_close(self):
        """애니메이션이 완료되지 않은 경우 강제로 닫기"""
        if self.isVisible():
            print(f"[DEBUG] 강제 종료: '{self.title_text}'")
            self.close()


    def mousePressEvent(self, event):
        """
        알림을 클릭하면 즉시 닫고 클릭 이벤트 전달.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.notification_data if self.notification_data else {})
            self.fade_out() # 닫기 애니메이션 시작
            event.accept()

    def closeEvent(self, event):
        """
        위젯이 닫힐 때 매니저에게 알림.
        """
        self.closed.emit()
        super().closeEvent(event)


class NotificationManager(QObject):
    """
    여러 개의 CustomNotification 인스턴스를 관리.
    알림을 생성하고, 스태킹(stacking) 및 재정렬을 담당.
    """
    MAX_NOTIFICATIONS = 10  # 최대 알림 개수
    
    def __init__(self, on_click_callback=None, parent=None):
        super().__init__(parent)
        self.notifications = [] # 현재 활성화된 알림 위젯 목록
        self.padding = 10       # 알림 간의 여백 및 화면 가장자리 여백
        self.on_click_callback = on_click_callback  # 알림 클릭 시 호출할 콜백

    def show(self, title, message, notification_data=None, duration=10000):
        """
        새 알림을 생성하고 표시합니다.
        """
        # 최대 개수 초과 시 가장 오래된 알림 강제 제거
        while len(self.notifications) >= self.MAX_NOTIFICATIONS:
            oldest = self.notifications.pop(0)  # 리스트에서 먼저 제거
            oldest.timer.stop()  # 타이머 중지
            oldest.closed.disconnect(self.on_notification_closed)  # 시그널 연결 해제 (중복 호출 방지)
            oldest.close()  # 즉시 닫기
        
        notification = CustomNotification(title, message, notification_data, duration=duration)
        # 알림이 닫힐 때 on_notification_closed 슬롯이 호출되도록 연결
        notification.closed.connect(self.on_notification_closed)
        # 알림 클릭 시 콜백 호출
        if self.on_click_callback:
            notification.clicked.connect(self.on_click_callback)
        
        self.notifications.append(notification) # 목록에 추가
        self.reposition() # 알림 위치 재정렬
        
        # 타이머가 확실히 시작되도록 보장
        if duration > 0 and not notification.timer.isActive():
            notification.timer.start(duration)
            print(f"[DEBUG] Manager에서 타이머 강제 시작: '{title}'")
        
        # 현재 알림 상태 출력
        self._debug_print_status()

    def _debug_print_status(self):
        """현재 알림 상태를 디버그 출력"""
        print(f"[DEBUG] === 현재 알림 상태 (총 {len(self.notifications)}개) ===")
        for i, n in enumerate(self.notifications):
            elapsed = time.time() - n.created_time
            remaining = (n.duration / 1000) - elapsed if n.duration > 0 else -1
            print(f"  [{i}] '{n.title_text}' | 경과: {elapsed:.1f}초 | 남은시간: {remaining:.1f}초 | 타이머활성: {n.timer.isActive()}")
        print(f"[DEBUG] =====================================")

    def on_notification_closed(self):
        """
        알림이 닫혔을 때 호출되는 슬롯.
        """
        sender_widget = self.sender() # 시그널을 보낸 위젯 (닫힌 알림)
        
        if hasattr(sender_widget, 'title_text'):
            elapsed = time.time() - sender_widget.created_time
            print(f"[DEBUG] 알림 닫힘: '{sender_widget.title_text}' | 총 경과시간: {elapsed:.1f}초")
        
        try:
            self.notifications.remove(sender_widget) # 목록에서 제거
        except ValueError:
            # 이미 제거되었거나 목록에 없는 경우 무시
            pass
        
        self.reposition() # 나머지 알림 위치 재정렬

    def reposition(self):
        """
        활성화된 모든 알림의 위치를 재조정합니다.
        화면 우측 하단에 차곡차곡 쌓이도록 합니다.
        """
        screen_geo = QGuiApplication.primaryScreen().availableGeometry()
        
        
        # 화면의 절대 좌표 (라즈베리파이 등에서 0이 아닐 수 있음)
        screen_x = screen_geo.x()
        screen_y = screen_geo.y()
        
        # 현재 y 위치 (화면 하단에서 시작) - 절대 좌표 반영
        current_y = screen_y + screen_geo.height() - self.padding
        
        # 목록의 역순으로 순회 (최신 알림이 맨 아래에 위치)
        for notification in self.notifications:
            # 높이 계산을 위해 크기 조정
            if not notification.isVisible():
                notification.adjustSize()
            
            widget_height = notification.height()
            
            # 이 알림이 위치할 목표 y 좌표
            target_y = current_y - widget_height
            
            # 절대 좌표 반영하여 x 좌표 계산
            target_x = screen_x + screen_geo.width() - notification.width() - self.padding
            target_pos = QPoint(target_x, target_y)
            
            
            # 알림이 아직 표시되지 않았다면(새 알림) -> slide_in
            if not notification.isVisible():
                notification.slide_in(target_pos)
            # 이미 표시된 알림이라면(기존 알림) -> move_to
            else:
                notification.move_to(target_pos)

            # 다음 알림이 쌓일 y 위치 업데이트 (위쪽으로 이동)
            current_y = target_y - self.padding

    def close_all(self):
        """
        모든 알림을 즉시 닫습니다. (프로그램 종료 시 사용)
        """
        # 리스트 복사본으로 순회 (원본 수정 중 순회 오류 방지)
        for notification in self.notifications[:]:
            try:
                notification.timer.stop()
                notification.closed.disconnect(self.on_notification_closed)
            except:
                pass
            notification.close()
        self.notifications.clear()