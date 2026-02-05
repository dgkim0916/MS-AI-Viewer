# import socket
# import struct
# import uuid

# def discover_onvif_devices(timeout=2):
#     # WS-Discovery 멀티캐스트 주소와 포트
#     multicast_address = "239.255.255.250"
#     multicast_port = 3702

#     # WS-Discovery 요청 메시지
#     message_id = uuid.uuid4()  # 고유 메시지 ID 생성
#     soap_message = f"""<?xml version="1.0" encoding="UTF-8"?>
#     <Envelope xmlns="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:dn="http://www.onvif.org/ver10/device/wsdl">
#         <Header>
#             <wsa:MessageID>urn:uuid:{message_id}</wsa:MessageID>
#             <wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To>
#             <wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action>
#         </Header>
#         <Body>
#             <Probe xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery">
#                 <Types>dn:Device</Types>
#             </Probe>
#         </Body>
#     </Envelope>"""

#     # UDP 소켓 생성 (멀티캐스트용)
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#     sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)  # 멀티캐스트 TTL 설정
#     sock.settimeout(timeout)  # 타임아웃 설정

#     # 멀티캐스트 요청 전송
#     print("Sending WS-Discovery probe...")
#     sock.sendto(soap_message.encode(), (multicast_address, multicast_port))

#     # 응답 수신
#     print("Waiting for responses...")
#     devices = []
#     try:
#         while True:
#             data, addr = sock.recvfrom(4096)  # 응답 수신
#             devices.append((data.decode(), addr))
#     except socket.timeout:
#         pass

#     # 결과 출력
#     print(f"Discovered {len(devices)} ONVIF devices:\n")
#     for response, addr in devices:
#         print(f"Device at {addr[0]}:{addr[1]}:\n{response}\n")

#     sock.close()
#     return devices


# if __name__ == "__main__":
#     discover_onvif_devices()


# import gi
# gi.require_version('Gst', '1.0')
# gi.require_version('GstRtspServer', '1.0')
# from gi.repository import Gst, GstRtspServer, GObject

# class RTSPServer:
#     def __init__(self):
#         # GStreamer 초기화
#         Gst.init(None)
#         # RTSP 서버 생성
#         self.server = GstRtspServer.RTSPServer()
#         self.factory = GstRtspServer.RTSPMediaFactory()

#         # self.rtsp_input_url = "admin:m20190301!@117.17.159.206/stream1"
#         self.rtsp_input_url = "admin:admin13579!@117.17.159.195/stream1"

        
#         # # 인증 추가
        # auth = GstRtspServer.RTSPAuth()
        # token = GstRtspServer.RTSPToken.new()
        # token.set_string("media.factory.role", "user")  # 역할(role) 추가
        # auth.set_default_token(token)  # 기본 토큰 설정

        # # 사용자 이름과 비밀번호 추가
        # basic = GstRtspServer.RTSPAuth.make_basic("admin", "admin123")
        # auth.add_basic(basic, token)

        # # RTSP 서버에 인증 설정
        # self.server.set_auth(auth)


        # self.factory.set_launch(
        #     'v4l2src device=/dev/video4 ! videoconvert ! x264enc tune=zerolatency bitrate=1024 speed-preset=superfast ! rtph264pay name=pay0 pt=96'
        # )
        # self.factory.set_launch(
        #     'v4l2src device=/dev/video4 ! videoconvert ! x265enc tune=zerolatency bitrate=2048 speed-preset=ultrafast ! rtph265pay name=pay0 pt=96 ! queue ! appsink sync=false'
        # )

        # self.factory.set_launch(
        #     'v4l2src device=/dev/video4 ! videoconvert ! x265enc tune=zerolatency bitrate=2048 speed-preset=ultrafast ! rtph265pay name=pay0 pt=96'
        # )
        # self.factory.set_launch(
        #     f'rtspsrc location=rtsp://{self.rtsp_input_url} protocols=tcp latency=50 ! rtph264depay ! rtph264pay name=pay0 pt=96'
        # )
 
        # self.factory.set_launch(
        #     f'rtspsrc location=rtsp://{self.rtsp_input_url} protocols=tcp latency=0 ! rtph265depay ! rtph265pay name=pay0 pt=96'
        # )

        # self.factory.set_launch(
        #     f'rtspsrc location=rtsp://{self.rtsp_input_url} protocols=tcp latency=0 ! rtph265depay ! queue max-size-buffers=2 leaky=downstream ! rtph265pay name=pay0 pt=96 sync=false'
        # )




        # self.factory.set_launch(
            # 'v4l2src device=/dev/video4 ! videoconvert ! '
            # 'x264enc tune=zerolatency bitrate=2048 speed-preset=ultrafast ! '
            # 'rtph264pay config-interval=1 pt=96 ! application/x-rtp,media=video,encoding-name=H264,payload=96 !'
            # ' queue ! appsink sync=false'
        # )
#         self.factory.set_shared(True)
#         self.server.get_mount_points().add_factory("/stream1", self.factory)
#         self.server.set_service("8554")

#     def start(self):
#         # GLib의 메인 루프 실행
#         loop = GObject.MainLoop()
#         self.server.attach(None)
#         print("RTSP server is running at rtsp://127.0.0.1:8554/stream1")
#         loop.run()

# if __name__ == "__main__":
#     server = RTSPServer()
#     server.start()

# # import cv2
# import gi
# gi.require_version('Gst', '1.0')
# gi.require_version('GstRtspServer', '1.0')
# from gi.repository import Gst, GstRtspServer, GLib

# class CustomRTSPMediaFactory(GstRtspServer.RTSPMediaFactory):
#     def __init__(self):
#         super().__init__()
#         self.cap = cv2.VideoCapture(4)  # 카메라 ID
#         if not self.cap.isOpened():
#             raise RuntimeError("Error: Could not open video source.")
#         self.number_frames = 0
#         self.fps = int(self.cap.get(cv2.CAP_PROP_FPS)) or 30
#         self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.appsrc = None

#     def on_need_data(self, src, length):
#         """appsrc에서 데이터가 필요할 때 호출됩니다."""
#         ret, frame = self.cap.read()
#         if not ret:
#             return

#         self.number_frames += 1
#         data = frame.tobytes()

#         # 버퍼 생성 및 설정
#         buffer = Gst.Buffer.new_allocate(None, len(data), None)
#         buffer.fill(0, data)
#         buffer.pts = buffer.dts = int(self.number_frames * Gst.SECOND / self.fps)
#         buffer.duration = int(Gst.SECOND / self.fps)

#         # appsrc로 버퍼 푸시
#         retval = src.emit("push-buffer", buffer)
#         if retval != Gst.FlowReturn.OK:
#             print("Error pushing buffer to appsrc")

#     def do_create_element(self, url):
#         """파이프라인 생성"""
#         pipeline = Gst.parse_launch(
#             "appsrc name=appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=4096 speed-preset=ultrafast ! rtph264pay name=pay0 pt=96"
#         )
#         return pipeline

#     def do_configure(self, rtsp_media):
#         """RTSPMedia 생성 시 appsrc 설정"""
#         self.appsrc = rtsp_media.get_element().get_child_by_name("appsrc")
#         self.appsrc.set_property("caps", Gst.Caps.from_string(
#             f"video/x-raw,format=BGR,width={self.width},height={self.height},framerate={self.fps}/1"
#         ))
#         self.appsrc.set_property("is-live", True)
#         self.appsrc.set_property("block", True)
#         self.appsrc.set_property("format", Gst.Format.TIME)

#         # on-need-data 신호 연결
#         self.appsrc.connect("need-data", self.on_need_data)

# class RTSPServer:
#     def __init__(self):
#         Gst.init(None)
#         self.server = GstRtspServer.RTSPServer()
#         self.factory = CustomRTSPMediaFactory()
#         self.factory.set_shared(True)
#         self.server.get_mount_points().add_factory("/stream1", self.factory)

#     def start(self):
#         self.server.attach(None)
#         print("RTSP server is running at rtsp://127.0.0.1:8554/stream1")
#         GLib.MainLoop().run()

# if __name__ == "__main__":
#     server = RTSPServer()
#     server.start()


import cv2


# cap = cv2.VideoCapture("rtsp://admin:admin13579!@117.17.159.195/stream1")
cap = cv2.VideoCapture("rtsp://admin:1234@192.168.0.102/video1")



while True:
    ret, img = cap.read()

    if ret:
        cv2.imshow("frame", img)
        cv2.waitKey(1)
        
        
