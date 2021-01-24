import moviepy.editor as mp
import moviepy.video.fx.all as vfx
import shutil

from PIL import Image
import pygame
import math
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import helpers


def process_file(clip, grid, config):
    """Processes a single VideoFileClip, and returns a gif that attempts to bypass the philter.

    Parameters:
    clip (VideoFileClip): An instance of a Video file clip read by the MoviePy Library
    grid (ImageClip): The file that is to be overlaid to bypass the philter.

    Returns:

    """
    # Clip processing
    if clip.w > clip.h:
        clip = clip.resize(width=config['MAX_SIZE'])
    else:
        clip = clip.resize(height=config['MAX_SIZE'])

    if clip.duration > 10:
        clip = clip.subclip(0, 10)
    clip = clip.set_fps(config['TARGET_FPS'])

    # Getting Clip Information
    width = clip.w
    height = clip.h
    frame_count = clip.duration * config['TARGET_FPS']
    file_name = helpers.name_from_path(clip.filename)

    # Grid Processing
    grid = grid.resize((width, height))
    grid = grid.fx(vfx.painting, saturation=1.6, black=0.06)

    insertions = [clip]
    # Create Composition Array
    for insertion in range(math.ceil(frame_count/10)):
        start_time = ((insertion * config['FRAME_INTERVAL']) +
                      config['INITIAL_FRAME'])/config['TARGET_FPS']
        duration = (1/config['TARGET_FPS']) * 1
        insertions.append(grid.set_start(start_time).set_duration(duration))

    #frame_number * clip.fps
    np_frame = clip.get_frame(1)  # get frame by index

    final = mp.CompositeVideoClip(insertions)

    final.write_gif(config['FINAL_DIR'] + '/' + file_name +
                    ".gif", verbose=False)
    clip.close()
    final.close()
    print(file_name + " processed.")


def philter_directory(config):
    grid = mp.ImageClip(config['GRID_TYPE'])
    file_list = helpers.get_filenames(config['SOURCE_DIR'])
    for file_name in file_list:
        print("[" + str(file_list.index(file_name)+1) +
              "/" + str(len(file_list)) + "]")
        clip = mp.VideoFileClip(file_name)
        process_file(clip, grid, config)
        shutil.move(file_name, config['SOURCE_DIR']+'/processed')
