import argparse
from os.path import join
import os
import cv2


def video_to_image(file, out_dir):
    vidcap = cv2.VideoCapture(file)
    success, image = vidcap.read()
    counter = 0
    actual_frame = 0
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    frame_no = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    name = os.path.splitext(str(file))
    name = os.path.split(str(name[0]))
    # print(name)
    step = fps
    # print(f'frame no {frame_no}\nactual frame {actual_frame}\nstep {step}')
    while True:

        vidcap.set(cv2.CAP_PROP_POS_FRAMES, actual_frame)
        # Capture frame-by-frame
        ret, image = vidcap.read()
        # success and frame_no > actual_frame + step:
        if not ret or not frame_no > actual_frame + step:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        width = 256
        height = 256

        dim = (width, height)

        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        counter += 1
        save_path = join(f'{out_dir}/{name[1]}_{counter:0003d}.jpg')
        print(save_path)
        cv2.imwrite(str(save_path), image)
        actual_frame += int(step/2)

    # When everything done, release the capture
    vidcap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='')
    parser.add_argument('-o', '--out_dir', default='')
    args = parser.parse_args()
    video_to_image(args.file, args.out_dir)
    # video_to_image('hol/hol1.mp4', 'hol/files')
