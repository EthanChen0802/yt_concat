from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        for yt in data:
            if utils.caption_file_exists(yt):  # 如果當前影片的字幕檔案已存在就跳過這一個影片
                print("Found a exist caption file: " + yt.caption_filepath + '.txt')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                print('Downloading captions from url: ', yt.url)
            except (KeyError, AttributeError):
                print('Error when downloading caption from: ', yt.url)
                continue

            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        return data
