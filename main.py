import argparse
import cv2 as cv
import src.io_helper as io_helper
import logging
import sys
import src.preprocessor as preprocessor
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser(description="DeSquech project main script.")
    parser.add_argument("--mode", choices=["detect", "train"], required=False, help="Default is 'detect' mode.", default="detect")
    parser.add_argument("--input-dir", type=str, help="Directory with images for detection.")
    parser.add_argument("--files", nargs="+", help="List of image files for detection.")
    parser.add_argument("--ignore-file-errors", help="ignores errors for non existing files")
    parser.add_argument("--test-elementary", help="use ./data/elementary/* images ", action="store_true")

    args = parser.parse_args()

    for arg, value in vars(args).items():
        print(f"{arg}: {value}")
        
    ok_files, err_files = [], []

    if args.test_elementary:
        ok_files = io_helper.get_graphical_files(Path(Path.cwd()) / "data" / "elementary")

    if args.input_dir:
        ok_files, err_files = io_helper.get_graphical_files(args.input_dir), []
    elif args.files:
        ok_files, err_files = io_helper.check_file_paths(args.files)
        ...
        
    # error exits:    
    if err_files and not args.ignore_file_errors:
        logging.error("following images could not be read:\n" + "\n".join(err_files))
        sys.exit(1)

    if args.mode == "detect" and not (args.input_dir or args.files or ok_files):
        logging.error("no input files or dir provided for 'detect' mode")
        sys.exit(1)
    
    
    if args.mode == "detect":
        preprocessor.load_images(ok_files)


if __name__ == "__main__":
    main()