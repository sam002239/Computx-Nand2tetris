@2
M=0

(loop)
@1
D=M
@END
D;JEQ

@0           
D=M
@2
M=D+M;
@1
D=M
D=D-1
M=D
@loop
D;JMP


