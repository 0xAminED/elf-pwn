# ELF-PWN

A Python script for analyzing **ELF (Executable and Linkable Format)** files. This tool extracts detailed information about ELF file structures such as headers, sections, segments, symbols, and dynamic entries. It is useful for reverse engineering, system programming, and analyzing Linux-based executable files.

---

## Features

- **ELF Header**: Displays basic information such as the magic number, entry point, machine type, and offsets for program and section headers.
- **Sections**: Lists all sections in the ELF file with information like section type, address, size, and flags.
- **Program Headers (Segments)**: Provides details about segments such as virtual address, physical address, file size, memory size, flags, and offset.
- **Symbols**: Displays symbols in the ELF file, including their names and corresponding addresses (if available).
- **Dynamic Section**: Displays entries from the dynamic section, useful for inspecting dynamically linked libraries.

---

## Requirements

- Python 3.x
- `pyelftools` library

### Install dependencies

You can install the required library using pip:

```bash
pip install pyelftools
```
OR
```bash
pip install -r requirements.txt
```

## Usage

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/0xAminED/elf-pwn.git
cd elf-pwn
```
### 2. Run the Script
Use the following command to analyze a PE file. Replace <path_to_pe_file> with the path to the PE file you want to analyze.
```bash
python elf_pwn.py <path_to_pe_file>
```
Example:
```bash
python elf_pwn.py /path/to/your/file.elf
```
### 3. Output
The script will display detailed information about the ELF file, including headers, sections, segments, symbols, and dynamic entries. Here is an example of the output format:

```bash
====== ELF File Analysis ======
File: /path/to/your/file.elf

== ELF Header ==
Magic: b'\x7fELF'
Class: 2
Data Encoding: 1
Version: 1
OS/ABI: 0
Type: 2
Machine: 62
Entry Point: 0x401000
Program Header Offset: 64
Section Header Offset: 1234
Flags: 0
Size of Program Headers: 56
Size of Section Headers: 40
Number of Program Headers: 8
Number of Section Headers: 30

== Sections ==
Section: .text
  Type: 1
  Address: 0x401000
  Size: 0x500
  Flags: 6

...

== Program Headers (Segments) ==
Segment Type: 1
  Virtual Address: 0x401000
  Physical Address: 0x0
  File Size: 0x1000
  Memory Size: 0x1000
  Flags: 4
  Offset: 0

...

== Symbols (if any) ==
Symbols in section: .symtab
  _start at 0x401000

== Dynamic Section ==
  3 : 0x0000000000000000

```

## Supported File Formats
This tool works with ELF files, which are commonly used on Linux-based systems. Supported ELF file types include:
- **Executable files (.elf)**
- **Shared libraries (.so)**
- **Object files (.o)**


## License
This project is licensed under the MIT License - see the LICENSE file for details.



