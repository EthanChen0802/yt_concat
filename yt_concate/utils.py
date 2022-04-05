import os
from yt_concate.settings import DOWNLOADS_DIR, VIDEOS_DIR, CAPTION_DIR, OUTPUT_DIR


# noinspection PyMethodMayBeStatic
class Utils:
    def __init__(self):
        pass

    def create_dirs(self):  # 創建資料夾
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):  # 影片清單檔存放路徑
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):  # 檢查影片清單檔是否已經存在
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):  # 檢查字幕檔是否已經存在
        return os.path.exists(yt.caption_filepath) and os.path.getsize(yt.caption_filepath) > 0  #

    def video_file_exists(self, yt):  # 檢查影片檔是否已經存在
        return os.path.exists(yt.video_filepath) and os.path.getsize(yt.video_filepath) > 0  #

    def get_output_filepath(self, channel_id, search_word):
        filename = f'{channel_id}_{search_word}.mp4'
        return os.path.join(OUTPUT_DIR, filename)
