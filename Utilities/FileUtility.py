import os


def format_filename(original_filename):
    # os.path.split removes the file extension from the filename. ie name.jpg becomes ("name",
    # ".jpeg") os.path.splitext removes the filepath from the filename. ie filetopath/filename becomes
    # ("filetopath/", "filename")
    return os.path.splitext(os.path.split(original_filename)[1])[0]
