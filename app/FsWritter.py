import abc
from pathlib import Path
import os
from app.interfaces.IFsWritter import IFsWritter
from app.Log import Log

class FsWritter(IFsWritter):
    def write_folder(self, directory) -> str:
        try:
            folder_path = os.path.join("output", directory)
            folder_object = Path(folder_path)
            folder_object.mkdir()
            return folder_path
        except Exception as ex:
            Log.message(str(e))
            return ""

    def write_file_with_path(self, full_path: str, content: str) -> str:
        file_path = Path(full_path)
        file_path.parent.mkdir(parents=True, exists_ok=True)
        file_path.write_text(content, encoding="utf-8")
