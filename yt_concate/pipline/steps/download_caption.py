from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        for url in data:
            if utils.caption_file_exists(url):  # 如果當前影片的字幕檔案已存在就跳過這一個影片
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for ', url)
                continue

            text_file = open(utils.get_caption_filepath(url) + '.txt', "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
