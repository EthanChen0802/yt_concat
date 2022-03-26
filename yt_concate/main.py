from yt_concate.pipline.pipline import Pipeline
from yt_concate.pipline.steps.preflight import PreFlight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.initialize_yt import InitializeYT
from yt_concate.pipline.steps.download_caption import DownloadCaptions
from yt_concate.pipline.steps.read_caption import ReadCaption
from yt_concate.pipline.steps.search import Search
from yt_concate.pipline.steps.postflight import PostFlight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCVXM96yuiXY3ZT73Dy8HgCA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'fabulous'
    }

    steps = [
        PreFlight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        PostFlight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
