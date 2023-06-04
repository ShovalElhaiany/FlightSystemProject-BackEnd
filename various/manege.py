import os
from flask import current_app


def save_file(file, folder, filename=None):
    if not file:
        return None

    if not filename:
        filename = file.filename

    # Generate a unique filename to avoid conflicts
    filename = get_unique_filename(filename)

    # Create the full path for saving the file
    save_path = os.path.join(current_app.root_path, 'static', folder)
    os.makedirs(save_path, exist_ok=True)
    file.save(os.path.join(save_path, filename))

    # Return the saved filename
    return filename


def delete_file(folder, filename):
    file_path = os.path.join(current_app.root_path, 'static', folder, filename)

    if os.path.exists(file_path):
        os.remove(file_path)


def get_unique_filename(filename):
    path = os.path.join(current_app.root_path, 'static')
    basename, extension = os.path.splitext(filename)
    counter = 1

    while os.path.exists(os.path.join(path, filename)):
        filename = f"{basename}_{counter}{extension}"
        counter += 1

    return filename
