# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib

desktop = pathlib.Path("/Users/jakebestland/Desktop")
new_path = pathlib.Path('/Users/jakebestland/Desktop/screenshots')
count = 0
for filepath in desktop.iterdir():
    if filepath.suffix == ".png":
        count += 1
        new_name = filepath.rename(f"Screenshot #{count}.png")
        print(new_name.name)
        new_filepath = new_path.joinpath(new_name.name)
        new_name.replace(new_filepath)



