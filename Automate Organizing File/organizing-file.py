"""
    Automate Organizing File
    - Organizing your files into logical folder
    
    Author : Re-Creators
    Date : 02/10/22
"""
from pathlib import Path

# Getting current path
currentDirectory = Path().resolve()
files_in_directories = Path(currentDirectory)

# Variable that hold directory name based on file type
types = {}
types["documents"] =  ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
types["images"] =  ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
types["softwares"] =  ('.exe', '.pkg', '.dmg')
types["videos"] =  ('.mkv', '.mp4', '.3gp', '.m4v', '.avi', 'flv', '.webm')
types["music"] = ('.mp3', '.ogg', '.m4a', '.wav')
types["compressed"] =  ('.rar', '.zip', '.gzip')

for file in files_in_directories.iterdir():
    if file.is_file() and file.stem != ".DS_Store":
        for dir_name, type_list in types.items():
            # Checking exstension file, then
            # Make new folder or move file into existing folder
            if file.suffix.lower() in type_list:
                new_dir = currentDirectory.joinpath(dir_name.capitalize())
                
                if not new_dir.exists():
                    new_dir.mkdir()
                 
                new_file_path = new_dir.joinpath(file.name)
                
                # Don't move file when exists inside a new folder
                if not new_file_path.exists():
                    file.replace(new_file_path)
                    print(f"Moving file {file.name} into {new_dir}")
                    break
                print("File exists, skipped..")