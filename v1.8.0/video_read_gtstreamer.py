

import numpy as np

import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst



class Video_Buffer():
    """BlueRov video capture class constructor
    Attributes:
        port (int): Video UDP port
        video_codec (string): Source h264 parser
        video_decode (string): Transform YUV (12bits) to BGR (24bits)
        video_pipe (object): GStreamer top-level pipeline
        video_sink (object): Gstreamer sink element
        video_sink_conf (string): Sink configuration
        video_source (string): Udp source ip and port
    """

    def __init__(self, camera_name = "video1", appsink_name = "camera1"):
        """Summary
        Args:
            port (int, optional): UDP port
        """

        """
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 latency=100 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink emit-signals=true sync=false max-buffers=3 drop=true
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 ! decodebin ! queue ! autovideosink sync=false recover-policy=keyframe
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 ! rtph264depay ! h264parse ! decodebin ! autovideosink
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 latency=10 ! queue ! rtpjitterbuffer latency=10 ! rtph264depay ! avdec_h264 ! autovideosink sync=false
        rtspsrc location=rtsp://admin:admin13579@117.17.159.197:554/stream2 latency=10 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw ! videoconvert ! appsink emit-signals=true sync=false max-buffers=2 drop=true"""


        Gst.init(None)

        self._frame = None
        # [Software component diagram](https://www.ardusub.com/software/components.html)
        # self.video_source = 'rtspsrc location=rtsp://admin:admin13579@117.17.159.141/video1s2 latency=10'
        # self.video_source = 'rtspsrc location=rtsp://admin:1234@117.17.159.143/normal10 latency=10'
        # self.video_source = f'rtspsrc location=rtsp://admin:1234@117.17.159.143/{camera_name} latency=30'
        self.video_source = f'rtspsrc location=rtsp://admin:m20190301!@117.17.159.205/{camera_name} latency=30'

        # self.video_source = f'rtspsrc location=rtsp://USER:Admin13579@192.168.0.249/{camera_name} latency=30'
        # self.video_source = f'rtspsrc location=rtsp://127.0.0.1:8554/{camera_name} latency=30'



        # self.video_source = 'rtspsrc location=rtsp://admin:1234@117.17.159.143/normal10 latency=10 protocols=0x00000004 ! '

        # Cam -> CSI-2 -> H264 Raw (YUV 4-4-4 (12bits) I420)
        # self.video_codec = '! application/x-rtp, encoding-name=(string)H264, payload=96 ! rtph264depay ! h264parse ' # ! avdec_h264 ! queue '
        # self.video_codec = '! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 '
        self.video_codec = '! application/x-rtp, encoding-name=(string)H264, payload=96 ! rtph264depay ! h264parse '
        # self.video_codec = 'rtph264depay ! h264parse ! '
        
        # self.video_codec = "! x264enc ! avdec_h264 ! videoconvert "
        # Python don't have nibble, convert YUV nibbles (4-4-4) to OpenCV standard BGR bytes (8-8-8)
        self.video_decode =  '! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert'
        # self.video_decode =  'avdec_h264 ! videoconvert ! '

        # Create a sink to get data
        self.video_sink_conf = f'! appsink name={appsink_name} emit-signals=true sync=false max-buffers=10 drop=true'
        # self.video_sink_conf = 'appsink max-buffers=1 drop=true'

            # f'! appsink name={appsink_name} emit-signals=true sync=false '
        
        print(self.video_source)

        self.video_pipe = None
        self.video_sink = None
        self.appsink_name = appsink_name

        self.run()

    def start_gst(self, config=None):
        """ Start gstreamer pipeline and sink
        Pipeline description list e.g:
            [
                'videotestsrc ! decodebin', \
                '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                '! appsink'
            ]
        Args:
            config (list, optional): Gstreamer pileline description list
        """

        if not config:
            config = \
                [
                    'videotestsrc ! decodebin',
                    '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                    '! appsink'
                ]

        command = ' '.join(config)
        self.video_pipe = Gst.parse_launch(command)
        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name(self.appsink_name)

    @staticmethod
    def gst_to_opencv(sample):
        """Transform byte array into np array
        Args:
            sample (TYPE): Description
        Returns:
            TYPE: Description
        """
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

    def get_frame(self):
        """ Get Frame
        Returns:
            iterable: bool and image frame, cap.read() output
        """
        # self._frame = cv2.resize(self._frame, (640,480))
        return self._frame

    def frame_available(self):
        """Check if frame is available
        Returns:
            bool: true if frame is available
        """
        return type(self._frame) != type(None)

    def run(self):
        try:
            """ Get frame to update _frame
            """

            self.start_gst(
                [
                    self.video_source,
                    self.video_codec,
                    self.video_decode,
                    self.video_sink_conf
                ])

            self.video_sink.connect('new-sample', self.callback)

            bus = self.video_pipe.get_bus()
            bus.add_signal_watch()
            bus.connect("message", self.on_message)
        except Exception as e :
            print(e)
            pass

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.ERROR or t == Gst.MessageType.EOS:
            self.video_pipe.set_state(Gst.State.NULL)
            self.run()

    def callback(self, sink):
        sample = sink.emit('pull-sample')
        new_frame = self.gst_to_opencv(sample)
        self._frame = new_frame

        return Gst.FlowReturn.OK
    
    def stop(self):
        """Stop the pipeline"""
        self.video_pipe.set_state(Gst.State.NULL)

    def get_pipeline_state(self):
        state = self.video_pipe.get_state(1 * Gst.SECOND)
        return state.state.value_nick
    
if __name__ == '__main__':
    import time

    # video_list = []
    # for i in range(1,12):
    #     # name = f"video{i}"
    #     camera_name = f"normal{i}"
    #     appsink_name = f"camera{i}"

    #     video_list.append(Video_Buffer(camera_name=camera_name, appsink_name=appsink_name)) 

    # time.sleep(1)
    # import cv2

    # while True:
    #     frames = []
    #     for video in video_list:
    #         if video.frame_available():
    #             frames.append(video.get_frame())
    #         else:
    #             # frames.append(np.zeros_like(frames[0] if frames else np.zeros((1080, 1920, 3), dtype=np.uint8)))
    #             frames.append(np.zeros_like(frames[0] if frames else np.zeros((480, 640, 3), dtype=np.uint8)))

    #     if frames:
    #         # Combine frames into a grid
    #         rows = 3  # Number of rows in the grid
    #         cols = 4  # Number of columns in the grid
    #         grid_frame = np.vstack([
    #             np.hstack(frames[r * cols:(r + 1) * cols])
    #             for r in range(rows)
    #         ])

    #         cv2.imshow('Combined Frame', cv2.resize(grid_frame,(0,0), fx = 0.5, fy = 0.5))

    #         for video in video_list:
    #             print(f"{video.appsink_name} pipeline state: {video.get_pipeline_state()}")

    #         if cv2.waitKey(1) & 0xFF == 27:
    #             break

    # cv2.destroyAllWindows()


    # camera_name = f"video7"
    camera_name = f"stream1"

    appsink_name = f"camera15"

    video = Video_Buffer(camera_name=camera_name, appsink_name=appsink_name)

    time.sleep(1)
    import cv2

    while True:
        if video.frame_available():
            frames = video.get_frame()
            print(frames.shape)


            cv2.imshow('Combined Frame', frames)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cv2.destroyAllWindows()