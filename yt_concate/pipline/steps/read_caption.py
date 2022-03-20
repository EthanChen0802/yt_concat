import os
from pprint import pprint

from yt_concate.settings import CAPTION_DIR
from .step import Step


class ReadCaption(Step):

    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTION_DIR):
            captions = {}
            with open(os.path.join(CAPTION_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions

        pprint(data)
        return data
