from pathlib import Path

valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}

def get_graphical_files(dir_path: Path|str) -> list[Path]:
    res: list[Path] = []
    path = Path(dir_path)
    if not path.is_dir():
        return res  # Return empty if not a directory

    for file_path in path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in valid_extensions:
            res.append(file_path)
            
    return res

def check_file_paths(file_paths: list[Path|str]) -> tuple[list[Path], list[str]]:
    '''

    '''
    ok_paths = []
    err_paths = []
    for path in file_paths:
        if isinstance(path, str):
            path = Path(path) 
        if not path.is_absolute():    
            path = path = Path.cwd() / path
        if not path.exists() or path.is_dir() or path.suffix.lower() not in valid_extensions:
            err_paths.append(path)
        else:
            ok_paths.append(path)

    return (ok_paths, err_paths)
    