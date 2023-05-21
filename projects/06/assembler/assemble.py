import sys
from my_parser import MyParser
from my_code import MyCode
from my_symboltable import MySymbolTable

def main():
    # give full path for example: /Users/janlingen/Desktop/nand2tetris/projects/06/add/Add.asm
    input_path = sys.argv[1]
    output_path = sys.argv[1].replace(".asm", ".hack")
    output_file = open(output_path, "w")

    parser = MyParser(input_path)
    code = MyCode()
    symbol_table = MySymbolTable()

    current_line = 0
    current_user_address = 16

    # 500 years later, i discovered preprocessing ......
    # first i did everything in one loop, to be more efficient, but it failed for
    # obvious reasons, then i've thought too replace everything in the end after knowing every address
    # but this results in the same double loop
    while parser.has_more_commands():
        parser.advance()
        if parser.command_type() == "L":
            symbol_table.addEntry(parser.symbol(), current_line)
        else:
            current_line += 1

    parser.after_pre()

    while parser.has_more_commands():
        print(parser.command_type())
        parser.advance()
        if parser.command_type() == "A":
            tmp_num = 0
            if str(parser.symbol()).isdecimal():
                tmp_num = int(parser.symbol())
            elif symbol_table.contains(parser.symbol()):
                tmp_num = symbol_table.getAddress(parser.symbol())
            else:
                tmp_num = current_user_address
                current_user_address += 1
                symbol_table.addEntry(parser.symbol(), tmp_num)
            output_file.write('{0:016b}'.format(tmp_num) + "\n")
        elif parser.command_type() == "C":
            output_file.write("111" + code.comp(parser.comp())
                                    + code.dest(parser.dest())
                                    + code.jump(parser.jump()) + "\n")
        else:
            pass
    output_file.close()

if __name__ == "__main__":
    main()