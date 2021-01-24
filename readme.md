# How to run

To run this project you need:
* [Python3](https://www.python.org/downloads/)
* Python package manager [pip](https://pip.pypa.io/en/stable/installing/https://pip.pypa.io/en/stable/installing/)
* [MoviePy](https://zulko.github.io/moviepy/install.html)
* [PyGame](https://www.pygame.org/wiki/GettingStarted)
* scikit-image

## Quickstart

* [Run main.py](https://stackoverflow.com/questions/1522564/how-do-i-run-a-python-program), and run through the initial setup. This will create the directories that the program needs to run. It'll also create a params.json. Here you'll find the project parameters. You can change these whenever.
* After that, you want to populate your 'videos' folder with webms or mp4's that you would like to be processed.
* Run main.py again, and this time press 1 to philter the videos. This will convert them to gifs and place them in the 'philtered' directory.
* Open up your face-swapping software of choice, and run these philtered files through the app. By default, these photos go into your 'Reface' directory.
* Run main.py again, and this time press 2 to 'dephilter', this will take every 10n+1th frame out of the video, and you'll have your output video in the 'dephiltered' directory.

