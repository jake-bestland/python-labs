# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib

lab_folder = pathlib.Path.cwd()

for filepath in lab_folder.iterdir():
    if filepath.suffix == ".py":
        print(f"{filepath.name}")
    if filepath.is_dir():
        print(f"{filepath.name:}/")
        for path_2 in filepath.iterdir():
            if path_2.suffix == ".py":
                print(f"{path_2.name:^70}")