
from sys import argv
from isa import isa

def main(argv: list[str]) -> None:
    # read command line args
    if len(argv) != 2:
        print("Usage: python3 isa.py FILE_NAME.txt")
        return
    
    # read file contents and add into ISA

    raw_data: list[tuple[str]] = []
    f = open(argv[1], "r")
    lines: list[str] = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix("\n")
        raw_data.append(tuple(lines[i].split())) # parse lines into words

    print(f"Creating ISA with signals {raw_data[0]}")
    isa_con = isa(raw_data[0])
    for line in raw_data[1:]:
        print(f"Adding {line} to isa")
        isa_con.add_instr(line)

    f.close()

if __name__ == "__main__":
    main(argv)
