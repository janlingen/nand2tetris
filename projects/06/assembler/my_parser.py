# slide 18 and 19
class MyParser:
    def __init__(self, path):
        self.current_cmd = ("", -1)
        self.all_cmds = []
        file = open(path, "r")
        for line in file:
            line = line.partition("//")[0].strip().replace(" ", "")
            if line:
                self.all_cmds.append(line)
        print(self.all_cmds)
        file.close()

    def after_pre(self):
        self.current_cmd = ("", -1)

    def has_more_commands(self):
        return self.current_cmd[1] + 1 < len(self.all_cmds)
    
    def advance(self):
        self.current_cmd = (self.all_cmds[self.current_cmd[1] + 1], self.current_cmd[1] + 1)

    def command_type(self):
        if self.current_cmd[0].startswith("@"):
            return "A"
        elif self.current_cmd[0].startswith("("):
            return "L"
        return "C"
    
    def symbol(self):
        if self.command_type() == "A":
            return self.current_cmd[0][1:]
        if self.command_type() == "L":
            return self.current_cmd[0][1:-1]
        return ""
    
    def dest(self):
        if self.command_type() == "C":
            if "=" in self.current_cmd[0]:
                return self.current_cmd[0].partition("=")[0]
        return ""
    
    def comp(self):
        if self.command_type() == "C":
            if "=" in self.current_cmd[0]:
                return self.current_cmd[0].partition("=")[2].partition(";")[0]
            else:
                return self.current_cmd[0].partition(";")[0]
        return ""
    
    def jump(self):
        if self.command_type() == "C":
            if "=" in self.current_cmd[0]:
                return self.current_cmd[0].partition("=")[2].partition(";")[2]
            else: 
                return self.current_cmd[0].partition(";")[2]
        return ""
        
    
