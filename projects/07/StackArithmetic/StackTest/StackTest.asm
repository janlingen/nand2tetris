@17
D=A
@SP
AM=M+1
A=A-1
M=D
@17
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL1
D;JEQ
@SP
A=M-1
M=0
(LABEL1)
@17
D=A
@SP
AM=M+1
A=A-1
M=D
@16
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL2
D;JEQ
@SP
A=M-1
M=0
(LABEL2)
@16
D=A
@SP
AM=M+1
A=A-1
M=D
@17
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL3
D;JEQ
@SP
A=M-1
M=0
(LABEL3)
@892
D=A
@SP
AM=M+1
A=A-1
M=D
@891
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL4
D;JLT
@SP
A=M-1
M=0
(LABEL4)
@891
D=A
@SP
AM=M+1
A=A-1
M=D
@892
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL5
D;JLT
@SP
A=M-1
M=0
(LABEL5)
@891
D=A
@SP
AM=M+1
A=A-1
M=D
@891
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL6
D;JLT
@SP
A=M-1
M=0
(LABEL6)
@32767
D=A
@SP
AM=M+1
A=A-1
M=D
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL7
D;JGT
@SP
A=M-1
M=0
(LABEL7)
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
@32767
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL8
D;JGT
@SP
A=M-1
M=0
(LABEL8)
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@LABEL9
D;JGT
@SP
A=M-1
M=0
(LABEL9)
@57
D=A
@SP
AM=M+1
A=A-1
M=D
@31
D=A
@SP
AM=M+1
A=A-1
M=D
@53
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
M=D+M
@112
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
@SP
A=M-1
M=-M
@SP
AM=M-1
D=M
@SP
A=M-1
M=D&M
@82
D=A
@SP
AM=M+1
A=A-1
M=D
@SP
AM=M-1
D=M
@SP
A=M-1
M=D|M
@SP
A=M-1
M=!M
