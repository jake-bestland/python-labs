# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/Users/jakebestland/Desktop")

# Create a new folder
new_path = pathlib.Path('/Users/jakebestland/Desktop/screenshots')
new_path.mkdir(exist_ok=True)

# Filter for screenshots only
for filepath in desktop.iterdir():
    if filepath.suffix == ".png":
        print(filepath.name)

# Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)

# Move the screenshot there
        filepath.replace(new_filepath)


#added a counter of the files on Desktop
desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

desk_dict = {x: desk_files.count(x) for x in desk_files}
print(desk_dict)