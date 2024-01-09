# premable
main:
	li $s0, 1
	li $t0, 0
	sub $t0, $s0, $t0
	slt $t1, $zero, $t0
	beq $t1, $zero, Label3
	li $t0, 1
	addi $a0, $t0, 0
	li $v0, 1
	syscall
	j Label4
Label3:
	li $t0, 0
	addi $a0, $t0, 0
	li $v0, 1
	syscall
Label4: