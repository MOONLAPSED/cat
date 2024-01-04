from src.ufs import *


if __name__ == "__main__":
    fs_info = create_unix_filesystem('/path/to/some/file')
    print(fs_info)


"""
Add methods like chmod(), rename(), etc to modify metadata
Implement a parent pointer, path parsing etc to model full directory tree
Integrate with an in-memory file class to simulate file I/O
"""
