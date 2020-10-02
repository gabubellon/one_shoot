#!python3

import os
import argparse


def get_files_dir(path):
    files = []
    dirs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
        for dir in d:
            dirs.append(os.path.join(r, dir))

    return files, dirs


def get_extesions(file_list):
    ext = []
    for file in file_list:
        _, file_ext = os.path.splitext(file)
        ext.append(file_ext.lower())

    return list(set(ext))


def save_output(output, list_to_save):
    if not args.output:
        print("Output file: not set")
    else:
        with open(output, "w") as f:
            for item in list_to_save:
                f.write("%s\n" % item)
        print(f"Output file: {output}")


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to check the extension list")
    parser.add_argument("-o", "--output", type=str, help="Path to save a log output")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = arg_parser()
    print("##########")
    print("List All File Extensions on directory and sub directory")
    print(f"Search on: {args.path}")
    files, dirs = get_files_dir(args.path)
    ext = get_extesions(files)
    save_output(args.output, ext)

    print(f"Extensions: {ext}")
    print("##########")
