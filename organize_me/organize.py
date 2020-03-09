import os
from pathlib import Path

SUBDIRECTORIES = {
    "documents": ['.pdf', '.rtf', '.txt'],
    "audio": ['.m4a', '.m4b', '.mp3'],
    "videos": ['.mov', '.avi', '.mp4'],
    "images": ['.jpg', '.jpeg', '.png']
}


def get_sub_directory(postfix):
    for k, v in SUBDIRECTORIES.items():
        if postfix in v:
            return k


def organize():
    for file in os.scandir():
        if not file.is_dir():
            file_path = Path(file)
            file_extension = file_path.suffix.lower()
            sub_directory = get_sub_directory(file_extension)
            if sub_directory is not None:
                dir_path = Path(get_sub_directory(file_extension))
                if not dir_path.is_dir():
                    dir_path.mkdir()
                file_path.rename(dir_path.joinpath(file_path))


organize()
