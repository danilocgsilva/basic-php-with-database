from app.functions import generate_date_file_string, generate_folder

date_file_string = generate_date_file_string()
print(date_file_string)

generate_folder(date_file_string)