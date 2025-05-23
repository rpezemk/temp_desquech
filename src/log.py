from tabulate import tabulate
from pathlib import Path

def err(msg):
    print(f"\033[31m{msg}\033[0m")

def nice(*args):
    __nice(lambda msg: print(f"\033[32m{msg}\033[0m"), *args)

def nice_err(*args):
    __nice(lambda msg: print(f"\033[31m{msg}\033[0m"), *args)

def __nice(method, *args):
    arg_len = len(args)
    headers = []
    lines = []
    pre = None
    if arg_len == 1:
        headers = args[0]
    elif arg_len == 2:
        headers = args[0]
        lines = args[1]
    elif arg_len > 2:
        pre = args[0]
        headers = args[1]
        lines = args[2]
        
    indent = 4 * " "
    if isinstance(headers, str) or isinstance(headers, Path):
        headers = [headers]
    
    if not lines:
        method("\n" + str(headers[0]))
        return
    
    if isinstance(lines, dict):
        lines = [(k, lines[k]) for k in lines.keys()]
    first = lines[0]
    
    h_len = len(headers)
    row_len = len(first) if not isinstance(first, Path) and is_iterable(first) else 1
    headers = (
        headers[0:row_len] if h_len > row_len < 5 else
        headers if h_len == row_len < 15 else
        [(headers[i] if i < row_len else f"h_{i}") for i in range(row_len)] if h_len < row_len < 25 else
        []
    )
    row_iterable = is_iterable(first)
    lines = [[str(l)] for l in lines] if not row_iterable  else [[str(k) for k in l] for l in lines]
    table = tabulate(lines, headers=headers, tablefmt="")
    table = "\n".join([indent + l for l in table.splitlines()])
    tabbed = "\n" + table if pre is None else "\n" + pre + "\n" + table
    method("\n" + tabbed + "\n")

def is_iterable(first):
    return isinstance(first, list) or isinstance(first, tuple) or isinstance(first, set)