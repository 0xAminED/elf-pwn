import sys
from elftools.elf.elffile import ELFFile

def analyze_elf(file_path):
    try:
        with open(file_path, 'rb') as f:
            elf = ELFFile(f)

            print("\n====== ELF File Analysis ======")
            print(f"File: {file_path}\n")

            # ELF Header
            print("== ELF Header ==")
            print(f"Magic: {elf.header['e_ident']}")
            print(f"Class: {elf.header['e_ident'][4]}")
            print(f"Data Encoding: {elf.header['e_ident'][5]}")
            print(f"Version: {elf.header['e_ident'][6]}")
            print(f"OS/ABI: {elf.header['e_ident'][7]}")
            print(f"Type: {elf.header['e_type']}")
            print(f"Machine: {elf.header['e_machine']}")
            print(f"Entry Point: 0x{elf.header['e_entry']:X}")
            print(f"Program Header Offset: {elf.header['e_phoff']}")
            print(f"Section Header Offset: {elf.header['e_shoff']}")
            print(f"Flags: {elf.header['e_flags']}")
            print(f"Size of Program Headers: {elf.header['e_phentsize']}")
            print(f"Size of Section Headers: {elf.header['e_shentsize']}")
            print(f"Number of Program Headers: {elf.header['e_phnum']}")
            print(f"Number of Section Headers: {elf.header['e_shnum']}")

            # Sections
            print("\n== Sections ==")
            for section in elf.iter_sections():
                print(f"Section: {section.name}")
                print(f"  Type: {section['sh_type']}")
                print(f"  Address: 0x{section['sh_addr']:X}")
                print(f"  Size: 0x{section['sh_size']:X}")
                print(f"  Flags: {section['sh_flags']}\n")

            # Program Headers (Segments)
            print("\n== Program Headers (Segments) ==")
            for segment in elf.iter_segments():
                print(f"Segment Type: {segment['p_type']}")
                print(f"  Virtual Address: 0x{segment['p_vaddr']:X}")
                print(f"  Physical Address: 0x{segment['p_paddr']:X}")
                print(f"  File Size: 0x{segment['p_filesz']:X}")
                print(f"  Memory Size: 0x{segment['p_memsz']:X}")
                print(f"  Flags: {segment['p_flags']}")
                print(f"  Offset: {segment['p_offset']}\n")

            # Symbols (if any)
            print("\n== Symbols (if any) ==")
            for section in elf.iter_sections():
                if isinstance(section, elftools.elf.sections.SymbolTableSection):
                    print(f"Symbols in section: {section.name}")
                    for symbol in section.iter_symbols():
                        print(f"  {symbol.name} at 0x{symbol['st_value']:X}")

            # Dynamic section (if any)
            if elf.get_section_by_name('.dynamic'):
                print("\n== Dynamic Section ==")
                dynamic_section = elf.get_section_by_name('.dynamic')
                for entry in dynamic_section.iter_entries():
                    print(f"  {entry.tag} : {entry.value}")

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python elf_explorer.py <path_to_elf_file>")
    else:
        analyze_elf(sys.argv[1])
