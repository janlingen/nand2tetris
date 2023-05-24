import sys
from my_vm_codewriter import MyVMCodeWriter
from my_vm_parser import MyVMParser

def main():
    # give full path for example: /Users/janlingen/Desktop/nand2tetris/projects/06/add/Add.asm
    input_path = sys.argv[1]
    output_path = sys.argv[1].replace(".vm", ".asm")

    parser = MyVMParser(input_path)
    code_writer = MyVMCodeWriter(output_path)

    while parser.has_more_commands():
        parser.advance()
        if parser.command_type() == "C_ARITHMETIC":
            code_writer.write_arithmetic(parser.arg1())
        else:
            code_writer.write_push_pop(parser.command_type(),
                                       parser.arg1(),
                                       parser.arg2())
    
    code_writer.close()

if __name__ == "__main__":
    main()