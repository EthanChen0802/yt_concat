from yt_concate.pipline.pipline import Pipeline
from yt_concate.pipline.steps.preflight import PreFlight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.initialize_yt import InitializeYT
from yt_concate.pipline.steps.download_caption import DownloadCaptions
from yt_concate.pipline.steps.read_caption import ReadCaption
from yt_concate.pipline.steps.search import Search
from yt_concate.pipline.steps.download_videos import DownloadVideos
from yt_concate.pipline.steps.edit_video import EditVideo
from yt_concate.pipline.steps.postflight import PostFlight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCgNg3vwj3xt7QOrcIDaHdFg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'fabulous',
        'limits': 3
    }

    steps = [
        PreFlight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        PostFlight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
