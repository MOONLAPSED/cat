import os
from dataclasses import dataclass, field
from typing import Optional, Annotated, Literal, Any
from datetime import datetime
from enum import Enum


@dataclass
class UnixFilesystem:
    inode: Optional[int] = None
    pathname: str = field(default='')
    permissions: Literal[0o400, 0o600, 0o111] = field(default=None)
    filetype: Literal['file', 'directory']
    owner: Optional[int] = None
    group_id: Optional[int] = None
    pid: Optional[int] = None
    size: Optional[int] = None
    mtime: datetime = field(default_factory=datetime.now)
    atime: datetime = field(default_factory=datetime.now)
    ctime: datetime = field(default_factory=datetime.now)
    links_count: Optional[int] = None
    blocks: Optional[int] = None
    block_size: Optional[int] = None
    unit_file: Optional[Any] = None  #simd
    unit_file_addr: Optional[Any] = None  # simd
    def __repr__(self):
        permissions_str = self._permissions_to_string(self.permissions)
        return (f"UnixFilesystem(inode={self.inode}, pathname='{self.pathname}', "
                f"filetype={self.filetype.value}, permissions={permissions_str}, owner={self.owner}, "
                f"group_id={self.group_id}, pid={self.pid}, size={self.size}, mtime={self.mtime}, "
                f"atime={self.atime}, ctime={self.ctime}, links_count={self.links_count}, "
                f"blocks={self.blocks}, block_size={self.block_size})")

    @staticmethod
    def _permissions_to_string(permissions: Optional[int]) -> str:
        if permissions is None:
            return '---'
        modes = [
            permissions & 0o400, permissions & 0o200, permissions & 0o100,
            permissions & 0o040, permissions & 0o020, permissions & 0o010,
            permissions & 0o004, permissions & 0o002, permissions & 0o001,
        ]
        rwx = ['r', 'w', 'x']
        permissions_str = ''.join([
            rwx[i] if modes[i] else '-'
            for i in range(9)
        ])
        return permissions_str

# Function to create UnixFilesystem instances from os.stat
def create_unix_filesystem(path: str) -> UnixFilesystem:
    stat_info = os.stat(path)
    return UnixFilesystem(
        inode=stat_info.st_ino,
        pathname=path,
        filetype= 'file' if stat_info.st_mode & 0o40000 else 'directory',
        permissions=stat_info.st_mode & 0o777,  # To extract permission bits
        owner=stat_info.st_uid,
        group_id=stat_info.st_gid,
        pid=os.getpid(),
        size=stat_info.st_size,
        mtime=datetime.fromtimestamp(stat_info.st_mtime),
        atime=datetime.fromtimestamp(stat_info.st_atime),
        ctime=datetime.fromtimestamp(stat_info.st_ctime),
        links_count=stat_info.st_nlink,
        blocks=stat_info.st_blocks,
        block_size=stat_info.st_blksize
    )
