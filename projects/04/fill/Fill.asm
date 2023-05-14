// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// current color
@current_color  
M=-1      

(LOOP)
  @SCREEN
  D=A
  // 8192 pixel bits based on slide 17
  @pixels
  M=D    

  // keyboard address
  @KBD
  D=M
  // goes to (BLACK) when key pressed (>0)
  @BLACK
  D;JEQ
  
  // default (WHITE)
  @current_color
  M=-1 
  @COLOR_SCREEN
  0;JMP
  
  (BLACK)
    @current_color
    M=0

  // colors screen based on @current_color
  (COLOR_SCREEN)
    @current_color
    D=M
    // RAM[PIXELS] to (BLACK) or (WHITE)
    @pixels
    A=M         
    M=D       
    
    @pixels
    M=M+1
    D=M

    // [16384, 24576]    
    @24576
    D=D-A
    @COLOR_SCREEN
    D;JLT

@LOOP
0;JMP // Infinite loop