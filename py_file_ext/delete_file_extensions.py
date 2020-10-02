#!python3

import os
import argparse


def get_extesions_del(path):
    with open(path) as f:
        ext = f.read().splitlines()
    return ext


def get_files_to_del(path, ext):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if check_extension(file, ext):
                files.append(os.path.join(r, file))

    return files


def del_files(files):
    deleted_files = []
    error_files = []
    for file in files:
        try:
            print(f"Deleting file {file}")
            os.remove(file)
            print(f"Deleted with sucess")
            deleted_files.append(file)
        except:
            print(f"Error on Delete File")
            error_files.append(file)
    return deleted_files, error_files


def check_extension(file, ext):
    _, file_ext = os.path.splitext(file)
    return file_ext.lower() in ext


def get_files_by_extensions(file_list):
    file_by_ext = {}

    for file in file_list:
        _, file_ext = os.path.splitext(file)

        file_ext = file_ext.lower()

        if file_by_ext.get(file_ext):
            file_by_ext.get(file_ext).append(file)
        else:
            file_by_ext[file_ext] = [file]

    return file_by_ext


def save_output(output, list_to_save):
    if not output:
        print("Output file: not set")
    else:
        with open(output, "w") as f:
            for item in list_to_save:
                f.write("%s\n" % item)
        print(f"Output file: {output}")


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to Clean Files")
    parser.add_argument("ext_files", type=str, help="Path to Files Extensions")
    parser.add_argument("-o", "--output", type=str, help="Path to save a log output")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = arg_parser()
    print("##########")

    print("Delete All File by Extensions on directory and sub directory")
    print(f"Search on: {args.path}")

    exts_del = get_extesions_del(args.ext_files)

    print(f"Extensions to delete: {exts_del}")

    files = get_files_to_del(args.path, exts_del)

    deleted, error = del_files(files)

    if len(deleted) > 0:
        save_output("./deleted.log", deleted)
        print(f"List of deleted files save on: ./deleted.log")

    if len(error) > 0:
        save_output("./error.log", error)
        print(f"List of errors files save on: ./error.log")

    if len(deleted) + len(error) == 0:
        print(f"No Files With Listed Extensions Find")

    print(f"Delete Finish")
    print("##########")
