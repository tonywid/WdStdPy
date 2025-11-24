# Python script that lists all items in a folder and builds a list where each entry contains:
# - element[0]: filename or folder name (without extension)
# - element[1]: extension (empty for folders)
# - element[2]: "file" or "folder"
# - element[3]: folder path

import os


def get_filelist(folder_path):
    file_list = []
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        name, ext = os.path.splitext(item)

        if os.path.isfile(full_path):
            ext = ext.lstrip('.')  # Remove dot from extension
            type_flag = 'file'
        elif os.path.isdir(full_path):
            ext = ''  # No extension for folders
            type_flag = 'folder'
        else:
            continue  # Skip if not file or folder

        file_list.append([item, name, ext, type_flag, folder_path])
    return file_list



if __name__ == "__main__":
    folder_path = 'D:/Wd/Fam-Hobby/Chancel-Chor/Mappe_aktuell/LiederEinzeln/lyrics-pdf'  # Replace with your actual folder path
    file_list = get_filelist(folder_path)
    # Print the result
    for entry in file_list:
        print(entry)