from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # 將youtube url list 轉成 set, 排除重複的影片網址
        yt_set = set([found.yt for found in data])
        print(f"Total {len(yt_set)} videos to download")

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'Founding a existing video file: {yt.video_filepath} for {url} ')
                continue

            print('Downloading video: ' + url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')

        return data
