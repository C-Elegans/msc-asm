#opcodes
opcodes = {
    "nop" : 0,
    "mov" : 1,
    "ldr" : 2,
    "str" : 3,
    "add" : 4,
    "sub" : 5,
    "and" : 6,
    "not" : 7,
    "or" : 8,
    "xor" : 9,
    "lsl" : 10,
    "lsr" : 11,
    "cmp" : 12,
    "in" : 13,
    "out" : 14,
    "jmp" : 15,
    "call" : 16,
    "ret" : 17,
    "asr" : 18,
    "asl" : 19
}
opcode_types = {
    "nop" : 0,
    "mov" : 2,
    "ldr" : 2,
    "str" : 2,
    "add" : 3,
    "sub" : 3,
    "and" : 3,
    "not" : 3,
    "or" : 3,
    "xor" : 3,
    "lsl" : 3,
    "lsr" : 3,
    "cmp" : 3,
    "in" : 2,
    "out" : 2,
    "jmp" : 1,
    "call" : 1,
    "ret" : 0,
    "asr" : 3,
    "asl" : 3,
}
#registers
registers = {
    "r0": 0,
    "r1": 1,
    "r2": 2,
    "r3": 3,
    "r4": 4,
    "r5": 5,
    "r6": 6,
    "r7": 7,
    "r8": 8,
    "r9": 9,
    "r10": 10,
    "r11": 11,
    "r12": 12,
    "r13": 13,
    "r14": 14,
    "r15": 15,
    "sp": 13,
    "lr": 14,
    "pc": 15,
}
instructions = {
    0: "nop",
    1: "mov", 
    2:"ldr", 
    3:"str", 
    4:"add", 
    5:"sub", 
    6:"and", 
    7:"not", 
    8:"or", 
    9:"xor", 
    10:"lsl",
    11:"lsr",
    12:"cmp",
    13:"in",
    14:"out",
    15:"jmp",
    16:"call",
    17:"ret",
    18:"asr",
    19:"asl", 


}
WORD_LENGTH = 4
OPCODE_SHIFT = 32-6
RD_SHIFT = 32-10
RS_SHIFT = 32-14
RN_SHIFT = 32-18
IMM_SHIFT = 6
SHIFTER_SHIFT = 1
