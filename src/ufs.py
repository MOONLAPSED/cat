import json
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import Optional
import os


class FileType(Enum):
    REGULAR_FILE = 'regular file'
    DIRECTORY = 'directory'


@dataclass
class UnixFilesystem:
    _inode: int
    _pathname: str
    _filetype: FileType
    _permissions: int
    _owner: int
    _group_id: int
    _PID: int
    _unit_file: str
    _unit_file_addr: str
    _size: int
    _mtime: int
    _atime: int
    _ctime: int
    _links_count: int
    _blocks: int
    _block_size: int

    def __repr__(self):
        return f"UnixFilesystem(inode={self._inode}, pathname={self._pathname}, filetype={self._filetype}, " \
               f"permissions={self._permissions}, owner={self._owner}, group_id={self._group_id}, " \
               f"PID={self._PID}, unit_file={self._unit_file}, unit_file_addr={self._unit_file_addr}, " \
               f"size={self._size}, mtime={self._mtime}, atime={self._atime}, ctime={self._ctime}, " \
               f"links_count={self._links_count}, blocks={self._blocks}, block_size={self._block_size})"

    @property
    def inode(self) -> int:
        return self._inode

    @inode.setter
    def inode(self, value: int) -> None:
        self._inode = value

    @property
    def pathname(self) -> str:
        return self._pathname

    @pathname.setter
    def pathname(self, value: str) -> None:
        self._pathname = value

    @property
    def filetype(self) -> FileType:
        return self._filetype

    @filetype.setter
    def filetype(self, value: FileType) -> None:
        self._filetype = value

    # Implement getters and setters for other attributes similarly

    def to_json(self, file_path: str) -> None:
        attributes = {
            "inode": self._inode,
            "pathname": self._pathname,
            "filetype": self._filetype.value,
            # Include other attributes
        }
        with open(file_path, 'w') as json_file:
            json.dump(attributes, json_file)

    @classmethod
    def from_json(cls, file_path: str) -> Optional['UnixFilesystem']:
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                return cls(
                    _inode=data["inode"],
                    _pathname=data["pathname"],
                    _filetype=FileType[data["filetype"]],
                    # Initialize other attributes from JSON data
                )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading file: {e}")
            return None

    # Other methods...

# Usage example:

# Write object attributes to a JSON file
ufs = UnixFilesystem(
    _inode=123456789,
    _pathname="/home/user/file.txt",
    _filetype=FileType.REGULAR_FILE,
    # Include other attributes
)
ufs.to_json("unix_filesystem.json")

# Read object attributes from the JSON file
loaded_ufs = UnixFilesystem.from_json("unix_filesystem.json")
if loaded_ufs:
    print(loaded_ufs)

import os
from typing import Generator

class UnixFilesystemGenerator:
    def __init__(self, directory: str = './'):
        self.directory = directory

    def generate_filesystem_info(self) -> Generator:
        for root, dirs, files in os.walk(self.directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_stats = os.stat(file_path)
                    yield {
                        "file_path": file_path,
                        "file_stats": file_stats
                        # Include other attributes from os.stat() as needed
                    }
                except OSError as e:
                    print(f"Error accessing file {file_path}: {e}")

# Usage example:
generator = UnixFilesystemGenerator(directory='/path/to/directory')
file_system_info = generator.generate_filesystem_info()

for file_info in file_system_info:
    print(f"File: {file_info['file_path']}")
    print(f"Stats: {file_info['file_stats']}")