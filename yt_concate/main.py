from yt_concate.pipline.pipline import Pipeline
from yt_concate.pipline.steps.preflight import PreFlight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.download_caption import DownloadCaptions
from yt_concate.pipline.steps.postflight import PostFlight
from yt_concate.utils import Utils

CHANNEL_ID = 'UC-3sBKh8YYbG2KyVHnSyA1A'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        PreFlight(),
        GetVideoList(),
        DownloadCaptions(),
        PostFlight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
