import cv2


def make_hz_videos(width, height, hz, file_name):
    black_img_path = "img/black.png"
    frameSize = (width, height)
    out_put = cv2.VideoWriter(
        file_name + "_video_" + str(hz) + ".mp4", cv2.VideoWriter_fourcc(*"avc1"), hz * 2, frameSize
    )

    black_img = cv2.resize(cv2.imread(black_img_path), frameSize)
    img = cv2.resize(cv2.imread(file_name + ".png"), frameSize)

    for i in range(hz):
        out_put.write(black_img)
        out_put.write(img)

    out_put.release()


"""example

from video import make_hz_videos

make_hz_videos(150, 150, 60, "eraser")

"""
