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
@0
M=-1
@1
M=-1
@16384
D=A
@0
M=D

@8192
D=A
@1
M=D


(CHECK)
@24576
D=M
@4
M=D
@ITER2
D;JEQ
(ITER1)
//STORING BASE ADDRESS OF KEYBOARD
//FOR ITERRATIONS
@0
D=M
@2
M=D//2=16384
//STORING BASE ADDRESS OF SCREEN
//FOR ITERRATIONS
@1
D=M
@3
M=D//3 =18224
(ITER1STR)
@2
A=M
M=-1
@2
D=M
D=D+1
M=D
@3
D=M
D=D-1
M=D
@CHECK
D;JEQ
@ITER1STR
0;JMP




(ITER2)
//STORING BASE ADDRESS OF KEYBOARD
//FOR ITERRATIONS
@0
D=M
@2
M=D//2=16384
//STORING BASE ADDRESS OF SCREEN
//FOR ITERRATIONS
@1
D=M
@3
M=D//3 =18224
(ITER2STR)
@2
A=M
M=0
@2
D=M
D=D+1
M=D
@3
D=M
D=D-1
M=D
@CHECK
D;JEQ
@ITER2STR
0;JMP

