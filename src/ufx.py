from dataclasses import dataclass
import json


@dataclass
class UnixFilesystem:
    inode: int
    pathname: str
    filetype: str
    permissions: int
    owner: int
    group_id: int
    PID: int
    unit_file: str
    unit_file_addr: str
    size: int
    mtime: int
    atime: int
    ctime: int
    links_count: int
    blocks: int
    block_size: int
    st_dev: int # ID of device containing file
    st_nlink: int # number of hard links  
    st_uid: int # user ID of owner
    st_gid: int # group ID of owner
    st_rdev: int # device ID (if special file)
    st_blksize: int # blocksize for filesystem I/O
    st_blocks: int # number of 512B blocks allocated
    
    def __repr__(self):
        return f"UnixFilesystem(inode={self.inode}, pathname={self.pathname}, filetype={self.filetype}, permissions={self.permissions}, owner={self.owner}, group_id={self.group_id}, PID={self.PID}, unit_file={self.unit_file}, unit_file_addr={self.unit_file_addr}, size={self.size}, mtime={self.mtime}, atime={self.atime}, ctime={self.ctime}, links_count={self.links_count}, blocks={self.blocks}, block_size={self.block_size})"

    def write(self, fp):
        fp.write(self.inode.to_bytes(8, "big"))
        fp.write(self.pathname.encode('utf-8'))
        fp.write(self.filetype.encode('utf-8'))
        fp.write(self.permissions.to_bytes(8, "big"))
        fp.write(self.owner.to_bytes(8, "big"))
        fp.write(self.group_id.to_bytes(8, "big"))
        fp.write(self.PID.to_bytes(8, "big"))
        fp.write(self.unit_file.encode('utf-8'))
        fp.write(self.unit_file_addr.encode('utf-8'))
        fp.write(self.size.to_bytes(8, "big"))
        fp.write(self.mtime.to_bytes(8, "big"))
        fp.write(self.atime.to_bytes(8, "big"))
        fp.write(self.ctime.to_bytes(8, "big"))
        fp.write(self.links_count.to_bytes(8, "big"))
        fp.write(self.blocks.to_bytes(8, "big"))
        fp.write(self.block_size.to_bytes(8, "big"))

    def read(self, fp):
        self.inode = int.from_bytes(fp.read(8), "big")
        self.pathname = fp.read().decode('utf-8')
        self.filetype = fp.read().decode('utf-8')
        self.permissions = int.from_bytes(fp.read(8), "big")
        self.owner = int.from_bytes(fp.read(8), "big")
        self.group_id = int.from_bytes(fp.read(8), "big")
        self.PID = int.from_bytes(fp.read(8), "big")
        self.unit_file = fp.read().decode('utf-8')
        self.unit_file_addr = fp.read().decode('utf-8')
        self.size = int.from_bytes(fp.read(8), "big")
        self.mtime = int.from_bytes(fp.read(8), "big")
        self.atime = int.from_bytes(fp.read(8), "big")
        self.ctime = int.from_bytes(fp.read(8), "big")
        self.links_count = int.from_bytes(fp.read(8), "big")
        self.blocks = int.from_bytes(fp.read(8), "big")
        self.block_size = int.from_bytes(fp.read(8), "big")

    def to_json(self):
        return json.dumps(self.__dict__)

ufs = UnixFilesystem(
    inode=123456789,
    pathname="/home/user/file.txt",
    filetype="regular file",
    permissions=0o644,
    owner=1000,
    group_id=100,
    PID=1234,
    unit_file="file.service",
    unit_file_addr="/etc/systemd/system/file.service",
    size=1024,
    mtime=1658012800,
    atime=1658012800,
    ctime=1658012800,
    links_count=1,
    blocks=1,
    block_size=1024
)

"""
with open("ufs.bin", "wb") as fp:
    ufs.write(fp)

with open("ufs.bin", "rb") as fp:
    ufs2 = UnixFilesystem()
    ufs2.read(fp)

print(ufs2)

json_string = ufs2.to_json()
print(json_string)

This code creates a `UnixFilesystem` object, writes it to a binary file, reads it from the binary file, and then prints it and converts it to a JSON string.
"""
