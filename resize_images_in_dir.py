import sys;
from os import listdir
from os.path import isfile, join
from os import walk
import os
from socket import herror

import numpy as np
import argparse
import cv2

# def get_dict_folder_files(path):
#     onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#     return onlyfiles

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='main_folder', help='Folder containing photo folders')
    parser.add_argument('-o', dest='out_dir', help='Output directory')
    args = parser.parse_args()

    mypath = args.main_folder

    print(f'{args.main_folder}___{args.out_dir}')
    mypath = 'zbior_danych'
    my_save_path = 'resized'

    # get folders in path
    dirpath, dirnames, filenames = next(walk(mypath))

    # folders -> list of filenames
    dictionary = dict()
    for dirname in dirnames:
        dirpath, dirnames, filenames = next(walk(os.path.join(mypath, dirname)))
        dictionary[dirname] = filenames

    # check image, if so copy to dir otherwise resize -> copy
    for folder, value in dictionary.items():
        searching_path = os.path.join(mypath, folder)
        print(searching_path)
        counter = 1
        for v in value:
            img = cv2.imread(os.path.join(searching_path, v))
            # cv2.imshow("Display window", img)
            # k = cv2.waitKey(0)
            height, width = img.shape[:2]
            # print(height)
            # print(width)

            if height != 256 or width != 256:
                dim = (256, 256)
                img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            # name = str(v)
            # name = name.split('.')[0]
            save_path = join(f'{my_save_path}/{folder}')

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # save_path = save_path.join(f'/{folder}{counter: 0000006d}.jpg')

            # save_path = os.path.join(save_path, f'/{folder}{counter: 0000006d}.jpg')

            path = os.path.join(f'{my_save_path}/{folder}/{folder}{counter:0000006d}.jpg')

            cv2.imwrite(str(path), img)
            counter += 1
