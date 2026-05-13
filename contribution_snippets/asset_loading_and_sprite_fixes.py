"""
Selected code contributions for a Python/Pygame 2D platformer game.

Original game developed by Edward Albert Jaros.
Final fixes contributed by Amir Edalati.
Used with permission.

This file contains only selected helper functions and fixes contributed
for portfolio purposes. It does not include the full original game.
"""

import os
import re
from os.path import join


def asset_path(base_dir, *parts):
    """
    Build an absolute path to a file in the game's project folder.
    """
    return join(base_dir, *parts)


def find_game_file(base_dir, *candidate_paths):
    """
    Return the first existing file from several possible relative paths.

    This improves asset loading by allowing the game to check multiple
    possible locations for music, sound effects, sprites, and other files.
    """
    for rel_path in candidate_paths:
        if not rel_path:
            continue

        if os.path.isabs(rel_path) and os.path.isfile(rel_path):
            return rel_path

        normalized = rel_path.replace("\\", "/")
        path = asset_path(base_dir, *normalized.split("/"))

        if os.path.isfile(path):
            return path

    return None


def find_existing_folder(parent_folder, folder_names):
    """
    Try several possible folder names and return the first one that exists.

    This is useful when asset folders may have slightly different names
    across machines, submissions, or project versions.
    """
    for folder_name in folder_names:
        folder_path = os.path.join(parent_folder, folder_name)

        if os.path.isdir(folder_path):
            return folder_path

    return None


def clean_sprite_name(filename):
    """
    Normalize sprite filenames into stable animation keys.

    Example outputs:
    - idle
    - run
    - jump
    - double_jump
    - wall_jump
    - fall
    - on
    - off

    Important fix:
    double_jump must be checked before jump because the string
    "double_jump" contains "jump".
    """
    stem = os.path.splitext(filename)[0].lower()

    # Remove dimension text such as "(32x32)" from sprite filenames.
    stem = re.sub(r"\(\d+x\d+\)", "", stem)

    # Normalize separators.
    stem = stem.replace("-", "_").replace(" ", "_")
    stem = re.sub(r"_+", "_", stem).strip("_")

    known_names = [
        "double_jump",
        "wall_jump",
        "idle",
        "run",
        "jump",
        "fall",
        "hit",
        "appear",
        "disappear",
        "blink",
        "spiked_ball",
        "spike_head",
        "on",
        "off",
    ]

    for name in known_names:
        if name in stem:
            return name

    return stem or "default"
