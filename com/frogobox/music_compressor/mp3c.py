#!/usr/bin/env python
"""
Compress mp3 files to frame rate 11025 to reduce file size.

Usage:
- Compress all mp3 files in the current directory
$ mp3c.py *

- Compress sample.mp3 file
$ mp3c.py sample1.mp3 sample2.mp3

Requirements to run the script:
1. ffmpeg
$ brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
2. pydub
$ pip install pydub
"""

import os
import sys
from pydub import AudioSegment
from os.path import basename

# folder path
dir_path = "/Users/faisalamir/Downloads/musc"

# list file and directories
list_files = os.listdir(dir_path)

# Directory
dir_compressed = "compressed"
# Path
path = os.path.join(dir_path, dir_compressed)

try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % dir_compressed)
except OSError as error:
    print("Directory '%s' can not be created" % dir_compressed)


def compress_mp3_file(mp3_file_path):
    if not mp3_file_path.endswith(".mp3"): return

    output_file_path = dir_path + "/" + dir_compressed + "/" + "{}.mp3".format(
        os.path.splitext(basename(mp3_file_path))[0])
    print("\nProcessing {} ==> {}".format(mp3_file_path, output_file_path))

    audio_file = AudioSegment.from_file(mp3_file_path, "mp3")
    frame_rate = audio_file.frame_rate
    bytes_per_sample = audio_file.sample_width

    if frame_rate == 11025:
        print("frame rate is already 11025, ignore.")
        return

    print("frame_rate {} ==> {}".format(frame_rate, "11025"))
    audio_file.export(output_file_path, format="mp3", parameters=["-ar", "11025"])


for list_file in list_files:
    data = dir_path + "/" + list_file
    compress_mp3_file(data)

print("\nDONE......................")
