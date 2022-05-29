
intarr=[str(i) for i in range(10)]
intarr5=[str(i) for i in range(5)]

dic={}
print("Enter the name of file you want to compile in .asm with complete path maybe put it in same folder as the assembler:\n")
inu=input()
M=[0 for i in range(30000)]
f=open(inu, 'r')
Line=f.readline()
i=0
# k=30
while Line:
    # k=k-1
    # print(Line)
    # print(Line)
    if Line[0]=="\n":
        Line=f.readline()
        continue;
    elif Line[0]=="/" and Line[1]=="/":
        Line=f.readline()
        continue;
    elif "/" in Line :
        for t in range(len(Line)):
            if Line[t]=="/":
                j=t+1
                if Line[j]=="/":
                    Linea=Line[:t]
                    Line=f.readline()

                    break;
    elif "/" not in Line and Line[0]!="(":
        s=-1
        for t in range(len(Line)):
            # print(Line[t])
            if Line[t]!=" " and s==-1:
                
                s=t
                
                # print("spacestart",t)
            if s!=-1 and (Line[t]==" " or Line[t]=="\n"):
                # print("spaceend",t)
                Linea=Line[s:t]
                Line=f.readline()
                break
    else:
        Linea=Line
    while Linea[0]==" ":
        Linea=Linea[1:]
    while Linea[-2]==" ":
        Linea=Linea[:-2]
    # print("khj",Linea,len(Linea))
    if Linea[0]=="(":
        dic[Linea[1:-2]]=i
        # print("jbkmjb")
        # print("dic is here:",i)
        # print(i)
        Line=f.readline()
        continue

    # print(i)
    # print(Linea)
    M[i]=Linea
    # print(Linea)
    i=i+1
f.close()
# print(sp)
# print(dic)
for t in range(i):
    print(M[t])
dict={}
no=i
Ans=[0 for i in range(no)]
sym=16
for i in range(no):
    inst=M[i]
    # print(inst)
    if M[i][0]=="@":
        # print(dic)
        if M[i][1:]=="SP"or M[i][1:]=="R0":
            Ans[i]="0"*16
            continue
        elif M[i][1:]=="LCL" or M[i][1:]=="R1" :
            Ans[i]="0"*15+"1"
            continue
        elif M[i][1:]=="ARG"or M[i][1:]=="R2":
            Ans[i]="0"*14+"10"
            continue
        elif M[i][1:]=="THIS"or M[i][1:]=="R3":
            Ans[i]="0"*14+"11"
            continue
        elif M[i][1:]=="THAT"or M[i][1:]=="R4":
            Ans[i]="0"*13+"100"
            continue
        elif M[i][1:]=="R5":
            Ans[i]=bin(5)[2:].zfill(16)
            continue
        elif M[i][1:]=="R6":
            Ans[i]=bin(6)[2:].zfill(16)
            continue
        elif M[i][1:]=="R7":
            Ans[i]=bin(7)[2:].zfill(16)
            continue
        elif M[i][1:]=="R8":
            Ans[i]=bin(8)[2:].zfill(16)
            continue
        elif M[i][1:]=="R9":
            Ans[i]=bin(9)[2:].zfill(16)
            continue
        elif M[i][1:]=="R10":
            Ans[i]=bin(10)[2:].zfill(16)
            continue
        elif M[i][1:]=="R11":
            Ans[i]=bin(11)[2:].zfill(16)
            continue
        elif M[i][1:]=="R12":
            Ans[i]=bin(12)[2:].zfill(16)
            continue
        elif M[i][1:]=="R13":
            Ans[i]=bin(13)[2:].zfill(16)
            continue
        elif M[i][1:]=="R14":
            Ans[i]=bin(14)[2:].zfill(16)
            continue
        elif M[i][1:]=="R15":
            Ans[i]=bin(15)[2:].zfill(16)
            continue
        elif M[i][1:]=="SCREEN":
            Ans[i]="01"+"0"*14
            continue
        if M[i][1:] in dic:
            Ans[i]=bin(dic[M[i][1:]])[2:].zfill(16)
            continue
        elif M[i][1] in intarr:
            Ans[i]=bin(int(M[i][1:]))[2:].zfill(16)
            continue
        else :
            Ans[i]=bin(sym)[2:].zfill(16)
            dict[M[i]]=sym
            dic[M[i][1:]]=sym
            sym=sym+1

        continue
    else:
        if "=" in inst and ";" not in inst:
            for t in range(len(inst)):
                if inst[t]=="=":
                    dest=inst[:t]
                    comp=inst[t+1:]
                    jump="000"
        elif "=" in inst and ";" in inst:
            for t in range(len(inst)):
                if inst[t]=="=":
                    dest=inst[:t]
                    k=t+1
                elif inst[t]==";":
                    comp=inst[k:t]
                    jump=inst[t+1:]
        elif "=" not in inst and ";" in inst:
            for t in range(len(inst)):
                if inst[t]==";":
                    dest=" "
                    comp=inst[:t]
                    jump=inst[t+1:]
        # print("dest",dest,"comp",comp,"jump",jump)

        if dest==" ":
            ds="000"
        elif dest=="M":
            ds="001"
        elif dest=="D":
            ds="010"
        elif dest=="MD":
            ds="011"
        elif dest=="A":
            ds="100"
        elif dest=="AM":
            ds="101"
        elif dest=="AD":
            ds="110"
        elif dest=="AMD":
            ds="111"
        
        if jump=="JGT":
            jumpa="001"
        elif jump=="JEQ":
            jumpa="010"
        elif jump=="JGE":
            jumpa="011"
        elif jump=="JLT":
            jumpa="001"
        elif jump=="JNE":
            jumpa="101"
        elif jump=="JLE":
            jumpa="110"
        elif jump=="JMP":
            jumpa="111"
        else:
             jumpa="000"
        
        if comp=="0":
           compa="0101010"
        elif comp=="1":
            compa="0111111"
        elif comp=="-1":
            compa="0111010"
        elif comp=="D":
            compa="0001100"
        elif comp=="A":
            compa="0110000"
        elif comp=="!D":
            compa="0001101"
        elif comp=="!A":
            compa="0110001"
        elif comp=="-D":
            compa="00011111"
        elif comp=="-A":
            compa="0110011"
        elif comp=="D+1":
            compa="0011111"
        elif comp=="A+1":
            compa="0110111"
        elif comp=="D-1":
            compa="0001110"
        elif comp=="A-1":
            compa="0110010"
        elif comp=="D+A":
            compa="0000010"
        elif comp=="D-A":
            compa="0010011"
        elif comp=="A-D":
            compa="0000111"
        elif comp=="D&A":
            compa="0000000"
        elif comp=="D|A":
            compa="0010101"
            
        if "M" in comp:
            if comp=="0":
                compa="0101010"
            elif comp=="1":
                compa="0111111"
            elif comp=="-1":
                compa="0111010"
            elif comp=="D":
                compa="0001100"
            elif comp=="A":
                compa="0110000"
            elif comp=="!D":
                compa="0001101"
            elif comp=="!A":
                compa="0110001"
            elif comp=="-D":
                compa="00011111"
            elif comp=="-A":
                compa="0110011"
            elif comp=="D+1":
                compa="0011111"
            elif comp=="A+1":
                compa="0110111"
            elif comp=="D-1":
                compa="0001110"
            elif comp=="A-1":
                compa="0110010"
            elif comp=="D+A":
                compa="0000010"
            elif comp=="D-A":
                compa="0010011"
            elif comp=="A-D":
                compa="0000111"
            elif comp=="D&A":
                compa="0000000"
            elif comp=="D|A":
                compa="0010101"
            
            elif comp=="M":
                compa="1110000"
            elif comp=="!M":
                compa="1110001"
            elif comp=="-M":
                compa="1110011"
            elif comp=="M+1":
                compa="1110111"
            elif comp=="M-1":
                compa="1110010"
            elif comp=="D+M":
                compa="1000010"
            elif comp=="D-M":
                compa="1010011"
            elif comp=="M-D":
                compa="1000111"
            elif comp=="D&M":
                compa="1000000"
            elif comp=="D|M":
                compa="1010101"
        Ans[i]="111"+compa+ds+jumpa



print(dic)
Ansss=inu[:-4]+"ans.hack"
f=open(Ansss,"w")
# k=0
for i in Ans:
    # print(k)
    # k=k+1
    print(i)
    f.write(i)
    f.write("\n")
f.close()
print(dict)
# print(dic)
print("Assembled data stored in :",Ansss)