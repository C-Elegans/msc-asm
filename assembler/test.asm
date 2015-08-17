label MAIN
mov r15,#255 ;comment
mov r10,r5
sub r15,#1 ;another comment
call END ;call to function
jmp MAIN
jmp MAIN
jmp MAIN

nop
ret
label END
	jmp END


label SUB
add r0, #1
lsl r0, #2
ret
