class VideoLoader:
    def __init__(self, video_path):
        self.video_path = video_path
        self.metadata = self.load_metadata()

    def load_metadata(self):
        import cv2
        video = cv2.VideoCapture(self.video_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        resolution = (video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return {'fps': fps, 'duration': duration, 'resolution': resolution}

    def sample_frames(self, num_samples):
        import cv2
        video = cv2.VideoCapture(self.video_path)
        frames = []
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        interval = total_frames // num_samples
        for i in range(num_samples):
            video.set(cv2.CAP_PROP_POS_FRAMES, i * interval)
            ret, frame = video.read()
            if ret:
                frames.append(frame)
        return frames

    def __str__(self):
        return f"VideoLoader(video_path='{self.video_path}', metadata={self.metadata})"