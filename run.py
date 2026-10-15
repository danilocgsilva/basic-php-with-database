from app.FsWritter import FsWritter
from app.functions import generate_date_file_string
from app.Recipe import Recipe

fs_writter = FsWritter()
folder_string_path = generate_date_file_string()
result = fs_writter.write_folder(folder_string_path)
print(f"Folder {result} generated.")

recipe = Recipe()
recipe_files = recipe.get_files()
for recipe in recipe_files:
    print(recipe.path)
