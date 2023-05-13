// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// sum
@R2
M=0

(LOOP)
    // check RAM[0] value for zero
    @R0
    D=M
    @END
    D;JEQ

    // add RAM[1] to RAM[2]
    @R1
    D=M
    @R2
    M=M+D

    // dec RAM[0]
    @R0
    M=M-1
    
    @LOOP
    0;JMP

(END)
    @END
    0;JMP // Infinite loop