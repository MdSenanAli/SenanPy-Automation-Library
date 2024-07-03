"""
Package: AnimPy
Author: Mohammad Senan Ali
Version: 1.0
License: MIT License

Description:
This package provides configuration functions for the animations.
"""

from manim import *

from .constants import *

# Define __all__ to include specific functions
__all__ = [
    "set_resolution",
    "set_background_color",
    "set_media_directory",
    "set_num_cache_files",
]


def set_resolution(resolution="1080p") -> None:
    """
    To set the resolution of the animation screen
    Input: Resolution in string
           Ex.: 540p, 1080p or 2160p (Defaults to 1080p)
    Output: None
    """
    dimension = RESOLUTION[resolution]
    try:
        config.pixel_width = dimension[0]
        config.pixel_height = dimension[1]
    except:
        print("Unable To Set Resoluion")
        print("Exiting...")
        sys.exit()

    return resolution


def set_background_color(color=BG_COLOR) -> None:
    """
    To set the background color of the animation screen
    Input: Manim parsable hexadecimal Color (Defaults to BLACK)
    Output: None
    """
    try:
        config.background_color = color
    except:
        print("Unable To Set Background Color")
        print("Exiting...")
        sys.exit()


def set_media_directory(media_directory_path=MEDIA_DIRECTORY) -> None:
    """
    Re-initializes the path to the media directory

    Args:
        media_directory_path (str): Directory path to media folder. Defaults to MEDIA_DIRECTORY.
    """
    config.media_dir = media_directory_path


def set_num_cache_files(num=500) -> None:
    """
    Re-sets to number of cache files to num

    Args:
        num (str): Number of files to cache. Defaults to 500.
    """
    config.max_files_cached = num
