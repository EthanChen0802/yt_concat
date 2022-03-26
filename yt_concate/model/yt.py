import os
from yt_concate.settings import VIDEOS_DIR, CAPTION_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = url.split("watch?v=")[-1]  # 影片的id(作為字幕檔的檔名)
        self.caption_filepath = os.path.join(CAPTION_DIR, self.id)  # 字幕檔存放路徑
        self.video_filepath = os.path.join(VIDEOS_DIR, self.id)  # 影片檔存放路徑
        self.captions = None

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath)
        ])

        return '<YT(' + content + ')>'
