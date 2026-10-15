from app.interfaces.IRecipe import IRecipe
from app.functions import generate_date_file_string, generate_folder
from app.File import File
from pathlib import Path
import os

class Recipe(IRecipe):
    def get_files(self) -> list[File]:
        files_list = []
        template_files_directory = Path(os.path.join("assets", "templates"))
        for file in template_files_directory.rglob("*"):
            if file.is_file():
                full_file_string = str(file)
                target_file_string = self.remove_two_first_folders(full_file_string)
                files_list.append(File(target_file_string, "a"))
        return files_list

    def remove_two_first_folders(self, file_path: str) -> str:
        file = Path(file_path)
        result_removed_two_folder = Path(*file.parts[2:])
        return result_removed_two_folder

