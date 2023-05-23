class MyVMCodeWriter:
    def __init__(self, path):
        self.file_name = self.set_file_name(path)
        self.output_file = open(path, "w")
        self.labels = 0
        self.translation_dict = {"add"      : "M=D+M",
                                 "sub"      : "M=M-D",
                                 "neg"      : "M=-M",
                                 "eq"       : "D;JEQ",
                                 "gt"       : "D;JGT",
                                 "lt"       : "D;JLT",
                                 "and"      : "M=D&M",
                                 "or"       : "M=D|M",
                                 "not"      : "M=!M",
                                 "local"    : "@LCL",
                                 "argument" : "@ARG",
                                 "this"     : "@THIS",
                                 "that"     : "@THAT",
                                 "constant" : "",
                                 "static"   : "",
                                 "pointer"  : "@3",
                                 "temp"     : "@5"}

    def set_file_name(self, path):
        return str(path).split("/")[-1].replace(".vm", "")
    
    def write_arithmetic(self, cmd):
        if cmd in ["add", "sub", "and", "or"]:
            self.write_lines(["@SP", 
                              "AM=M-1",
                              "D=M",
                              "@SP",
                              "A=M-1",
                              self.translation_dict[cmd]])
        elif cmd in ["neg", "not"]:
            self.write_lines(["@SP",
                              "A=M-1",
                              self.translation_dict[cmd]])
        else:
            self.labels += 1
            self.write_lines(["@SP",
                              "AM=M-1",
                              "D=M",
                              "@SP",
                              "A=M-1",
                              "D=M-D",
                              "M=-1",
                              "@LABEL" + str(self.labels),
                              self.translation_dict[cmd],
                              "@SP",
                              "A=M-1",
                              "M=0",
                              "(LABEL" + str(self.labels) + ")"])
            
    def write_push_pop(self, cmd, seg, i):
        if cmd == "C_PUSH":
            if seg == "constant":
                self.write_lines(["@" + str(i),
                                  "D=A",
                                  "@SP",
                                  "AM=M+1",
                                  "A=A-1",
                                  "M=D"])
            elif seg == "static":
                self.write_lines(["@" + self.file_name + "." + str(i),
                                 "D=M",
                                 "@SP",
                                 "A=M",
                                 "M=D",
                                 "@SP",
                                 "M=M+1"])
            else:
                self.write_lines(["@" + str(i),
                                  "D=A"])
                if seg in ["temp", "pointer"]:
                    self.write_lines([self.translation_dict[seg]])
                else:
                    self.write_lines([self.translation_dict[seg],
                                      "A=M"])
                self.write_lines(["A=D+A",
                                  "D=M",
                                  "@SP",
                                  "A=M",
                                  "M=D",
                                  "@SP",
                                  "M=M+1"])
        else:
            if seg == "static":
                self.write_lines(["@SP",
                                  "AM=M-1",
                                  "D=M",
                                  "@" + self.file_name + "." + str(i),
                                  "M=D"])
            else:
                self.write_lines(["@" + str(i),
                                  "D=A"])
                if seg in ["temp", "pointer"]:
                    self.write_lines([self.translation_dict[seg]])
                else:
                    self.write_lines([self.translation_dict[seg],
                                      "A=M"])
                self.write_lines(["D=D+A",
                                  "@R13",
                                  "M=D",
                                  "@SP",
                                  "AM=M-1",
                                  "D=M",
                                  "@R13",
                                  "A=M",
                                  "M=D"])
                


    def close(self):
        self.output_file.close()

    def write_lines(self, strs):
        for string in strs:
            self.output_file.write(string)
            self.output_file.write("\n")

