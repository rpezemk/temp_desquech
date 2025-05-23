import argparse

def main():
    parser = argparse.ArgumentParser(description="DeSquech project main script.")
    parser.add_argument("--mode", choices=["detect", "train"], required=False, help="Default is 'detect' mode.")
    parser.add_argument("--input-dir", type=str, help="Directory with images for detection.")
    parser.add_argument("--files", nargs="+", help="List of image files for detection.")
    args = parser.parse_args()

    if args.mode == "detect":
        if args.input_dir:
            ...
        elif args.files:
            ...
        else:
            parser.error("You must provide --input-dir or --files in detect mode.")

    elif args.mode == "train":
        ...
        
if __name__ == "__main__":
    main()