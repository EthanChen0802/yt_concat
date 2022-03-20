import os
from yt_concate.settings import DOWNLOADS_DIR, VIDEOS_DIR, CAPTION_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')  # 影片清單存放路徑

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0  # 檢查影片清單的檔案是否已經存在

    @staticmethod
    def get_video_id_from_url(url):
        return url.split("watch?v=")[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id_from_url(url) + '.txt')  # 字幕檔案存放路徑

    def caption_file_exists(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0  # 檢查字幕檔案是否已經存在
