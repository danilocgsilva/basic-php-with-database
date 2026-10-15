from datetime import datetime
from pathlib import Path
import os

def generate_date_file_string():
    return datetime.now().strftime("%Y%m%d-%Hh%Mm%Ss")

def generate_folder(folder_name: str) -> None:
    folder_path = os.path.join("output", folder_name)
    directory = Path(folder_path)
    print(folder_path)
    directory.mkdir()
