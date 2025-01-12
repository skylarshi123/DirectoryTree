import os
import argparse
from pathlib import Path

def print_directory_structure(path, prefix="", no_recurse_dirs=None):
    """
    Print the directory structure in a tree-like format.
    
    Args:
        path: Path to the directory
        prefix: Prefix for the current line (used for indentation)
        no_recurse_dirs: Set of directory names where we won't show contents
    """
    
    try:
        contents = list(os.scandir(path))
    except PermissionError:
        print(f"{prefix}├── {os.path.basename(path)} [Permission Denied]")
        return
    
    # Sort contents (directories first, then files)
    contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    
    for i, entry in enumerate(contents):
        is_last = i == len(contents) - 1
        
        if is_last:
            current_prefix = prefix + "└── "
            next_prefix = prefix + "    "
        else:
            current_prefix = prefix + "├── "
            next_prefix = prefix + "│   "
        
        print(f"{current_prefix}{entry.name}")
        
        # Only recurse if it's a directory and not in no_recurse_dirs
        if entry.is_dir() and entry.name not in no_recurse_dirs:
            print_directory_structure(entry.path, next_prefix, no_recurse_dirs)

def main():
    parser = argparse.ArgumentParser(description='Display directory structure in terminal')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Path to the directory (default: current directory)')
    parser.add_argument('--no-recurse', '-nr', nargs='+', 
                       help='Additional directories to not recurse into')
    
    args = parser.parse_args()
    
    # Prepare the set of directories to not recurse into
    no_recurse_dirs = {'node_modules', 'dist', 'build', '.next', '.git', 'husky'}
    if args.no_recurse:
        no_recurse_dirs.update(args.no_recurse)
    
    target_path = Path(args.path).resolve()
    print(f"📁 {target_path}")
    print_directory_structure(target_path, no_recurse_dirs=no_recurse_dirs)

if __name__ == "__main__":
    main()