# Directory Tree Visualizer

A Python script that generates a tree-like visualization of directory structures in the terminal, similar to the `tree` command. This tool provides a clear and organized view of your file system hierarchy while allowing you to exclude specific directories from the visualization.

## Features

- Tree-like visualization of directory structures
- Automatically skips common build and dependency directories (node_modules, dist, build, etc.)
- Custom directory exclusion support
- Permission error handling
- Sorted output (directories first, then files)
- Unicode characters for better visualization
- Support for both relative and absolute paths

## Installation

1. Clone this repository or download the script
2. Ensure you have Python 3.6 or later installed
3. No additional dependencies required - uses only Python standard library

## Usage

Basic usage:
```bash
python directorytree.py [path] [options]
```

### Arguments

- `path`: The directory path to visualize (optional, defaults to current directory)
- `--no-recurse` or `-nr`: Additional directory names to exclude from recursion

### Examples

Display the structure of the current directory:
```bash
python directorytree.py
```

Display the structure of a specific directory:
```bash
python directorytree.py /path/to/directory
```

Exclude additional directories from recursion:
```bash
python directorytree.py --no-recurse tests cache temp
```

### Default Excluded Directories

The following directories are excluded by default:
- node_modules
- dist
- build
- .next
- .git
- husky

## Output Example

```
📁 /path/to/directory
├── src
│   ├── components
│   │   ├── Header.js
│   │   └── Footer.js
│   └── utils
│       └── helpers.js
├── tests
│   └── test_main.py
└── README.md
```

## Error Handling

- The script handles permission errors gracefully by displaying "[Permission Denied]" for directories it cannot access
- Invalid paths will raise appropriate error messages

## Contributing

Feel free to open issues or submit pull requests with improvements or bug fixes.

## License

This project is open source and available under the MIT License.