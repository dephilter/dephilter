import os
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from PIL import Image
import pygame
import math
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import shutil

import helpers


def dephilter_clip(clip, config):
    # Getting Clip Information
    frame_count = clip.duration * config['TARGET_FPS']
    file_name = helpers.name_from_path(clip.filename)

    frames = clip.iter_frames()
    counter = 0
    new_frames = []
    for frame in frames:
        if not(((counter) % 10) == 0):
            new_frames.append(frame)
        counter += 1

    cut_clip = mp.ImageSequenceClip(new_frames, fps=clip.fps)

    return cut_clip


def get_filenames(folder):
    """Trawls through your videos directory and scrapes all webm files

    Returns:
    file_list (List of Strings): Webm files to process
    """
    file_list = []
    directory = os.getcwd() + "/" + folder

    for filename in os.listdir(directory):
        if filename.endswith(".webm") or filename.endswith(".mp4") or filename.endswith(".m4v") or filename.endswith(".gif"):
            file_list.append(os.path.join(directory, filename))
        else:
            continue
    return file_list


def dephilter_directory(config):
    file_list = get_filenames(config['REFACE_DIR'])
    for file_path in file_list:
        print("[" + str(file_list.index(file_path)+1) +
              "/" + str(len(file_list)) + "]")
        clip = mp.VideoFileClip(file_path)
        file_name = helpers.name_from_path(clip.filename)
        clip = dephilter_clip(clip, config)
        clip.write_videofile(config['DEPHILTERED_DIR'] + '/' +
                             file_name + ".mp4", audio=False, bitrate='3M', codec='libx264')
        shutil.move(file_path, config['REFACE_DIR']+'/processed')
