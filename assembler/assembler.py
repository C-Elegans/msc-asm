from isa import *
import re, sys, struct
labels = {}

input = open(sys.argv[1],'r')
output = open(sys.argv[2],'wb')

input_file = input.readlines();
def removeComments(string):
    string = re.sub(re.compile(";.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string
#first pass
line_count = 0
for line in input_file:

    filtered_line = removeComments(line)
    print(filtered_line)

    instruction = filtered_line.split();

    if(len(instruction)!=0):
        if(instruction[0] == "label"):
            print instruction[1]
            labels[instruction[1]] = line_count * WORD_LENGTH
        else:
            line_count += 1;
print labels

#second pass
line_count = 0;
for line in input_file:
    filtered_line = removeComments(line)
    filtered_line = filtered_line.replace(","," ")
    instruction = filtered_line.split();
    if(len(instruction)==0):
        continue

    if(instruction[0] == "label"):
        continue
    type = opcode_types[instruction[0]]
    data = 0
    code = opcodes[instruction[0]]
    if(type ==0):
        data = code << (OPCODE_SHIFT)
    elif(type == 1):
        if(len(instruction) == 2):
            imm_flag = 0
            imm = 0
            if( not (instruction[1] in registers)):
                imm_flag = 1
                imm = (labels[instruction[1]] - (line_count * WORD_LENGTH)) >>2
                print "instruction offset " + str(imm)
                imm = imm & 1048575 #2^20 -1
            else:
                rD = registers[instruction[1]]
            data = code << OPCODE_SHIFT | rD << RD_SHIFT | imm << IMM_SHIFT | imm_flag
        else:
            data = code << (OPCODE_SHIFT)
        
    elif(type == 2):
        rS = 0
        rD = 0
        imm = 0
        imm_flag = 0
        rN = 0
        print "register " + str(instruction[2])
        rS = registers[instruction[1]]
        rD = rS
    
        if('#' in instruction[2]):
            imm_flag = 1
            imm = int(instruction[2][1:])
            rS = 0

        else:
            rS=registers[instruction[2]]

        data = code << (OPCODE_SHIFT) | imm_flag | rD << (RD_SHIFT) | rS << (RS_SHIFT) |rN << (RN_SHIFT)| imm << 6
    elif(type == 3):
        rS = 0
        rD = 0
        imm = 0
        imm_flag = 0
        rN = 0
        if(len(instruction) == 3):
            rS = registers[instruction[1]]
            
            rD=rS
            if('#'in instruction[2]):
                rN = 0;
                imm_flag = 1;
                imm = int(instruction[2][1:])
            else:
                rS=registers[instruction[2]]
        else:
            rD = registers[instruction[1]]
            rS = registers[instruction[2]]
            if('#'in instruction[3]):
                rN = 0;
                imm_flag = 1;
                imm = int(instruction[3][1:])
            else:
                rN=registers[instruction[3]];
        data = code << (OPCODE_SHIFT) | imm_flag | rD << (RD_SHIFT) | rS << (RS_SHIFT) |rN << (RN_SHIFT)| imm << 6
    else:
        pass
    print code
    print instruction[0] + " " + format(data, '#034b')
    print "ins 0b71111122223333444455555555666669"
    line_count += 1
    output.write(struct.pack('i', data))
