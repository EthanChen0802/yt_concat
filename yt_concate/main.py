from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipline import Pipeline

CHANNEL_ID = 'UCVGd0u4nxuFzaXgflOoikaA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList()
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
