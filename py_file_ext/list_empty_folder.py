#!python3

import os
import argparse


def get_empty_dirs(path):
    dirs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        if len(d) == 0 and len(f) == 0:
            dirs.append(r)

    return dirs


def remove_dir(dirs):
    deleted_dirs = []
    error_dirs = []
    for dir in dirs:
        try:
            print(f"Deleting file {dir}")
            os.rmdir(dir)
            print(f"Deleted with sucess")
            deleted_dirs.append(dir)
        except:
            print(f"Error on Delete Dir")
            error_dirs.append(dir)
    return deleted_dirs, error_dirs


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
    parser.add_argument("path", type=str, help="Path to check the dirs empty list")
    parser.add_argument("-o", "--output", type=str, help="Path to save a log output")
    parser.add_argument("-r", "--remove", type=bool, help="Remove Empty Dir")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = arg_parser()
    print("##########")
    print("List All Dir Emptys")
    print(f"Search on: {args.path}")

    dirs = get_empty_dirs(args.path)
    save_output(args.output, dirs)

    if args.remove:
        deleted, error = remove_dir(dirs)

        if len(deleted) > 0:
            save_output("./deleted_dir.log", deleted)
            print(f"List of deleted files save on: ./deleted_dir.log")

        if len(error) > 0:
            save_output("./error_dir.log", error)
            print(f"List of errors files save on: ./error_dir.log")

        if len(deleted) + len(error) == 0:
            print(f"No Dir Emptys Find")

    print(f"Extensions: {dirs}")
    print("##########")
