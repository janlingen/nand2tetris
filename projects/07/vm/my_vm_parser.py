class MyVMParser:
    def __init__(self, path):
        self.current_cmd = ("", -1)
        self.all_cmds = []
        file = open(path, "r")
        for line in file:
            line = line.partition("//")[0].strip()
            if line:
                self.all_cmds.append(line)
        file.close()
    
    def has_more_commands(self):
        return self.current_cmd[1] + 1 < len(self.all_cmds)
    
    def advance(self):
        self.current_cmd = (self.all_cmds[self.current_cmd[1] + 1], self.current_cmd[1] + 1)

    # assuming all cmds are viable
    def command_type(self):
        cur_cmd = self.current_cmd[0].split(" ")[0]
        if cur_cmd == "push":
            return "C_PUSH"
        elif cur_cmd == "pop":
            return "C_POP"
        return "C_ARITHMETIC"
    
    def arg1(self):
        if self.command_type() == "C_ARITHMETIC":
            return self.current_cmd[0].split(" ")[0]
        else:
            return self.current_cmd[0].split(" ")[1]
        
    def arg2(self):
        return int(self.current_cmd[0].split(" ")[2])