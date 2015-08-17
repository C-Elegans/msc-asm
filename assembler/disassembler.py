from isa import *
import sys, struct
def sign_extend(i):
    print format(i,'0x')
    if i & (1<<19):
        i = i - (1<<20)
    return i
with open(sys.argv[1], 'rb') as file:
    filedata = file.read()
for i in range(0, len(filedata), 4):
    instruction = int(struct.unpack('i', filedata[i:i+4])[0])
    
    
    opcode = instructions[instruction >> OPCODE_SHIFT]
    rD = (instruction >> RD_SHIFT) & 15
    type = opcode_types[opcode]
    imm_flag = instruction &1;
    imm = (((instruction >> IMM_SHIFT)) & 1048575 -1)
    if type == 0:
        print "%s " % opcode
    if type == 1:
        if(imm_flag):
        
            print "%s #%d" % (opcode, sign_extend(int(imm)))
    
    print format(instruction, '#034b')
    
