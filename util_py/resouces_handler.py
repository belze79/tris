import os
import sys
from pathlib import Path


def get_asset_path(resource_path : str) -> str:
    base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
    return os.path.join(base_path, resource_path)

def collect_folder_file(folder : str):
    file_list : list[tuple[str, str]] = []
    base_path = Path(__file__).parent.parent
    folder_path = base_path / folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, base_path)
            file_list.append((full_path, relative_path))
    return file_list


