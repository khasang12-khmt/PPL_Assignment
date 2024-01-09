.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_2
	istore_1
.var 2 is b Z from Label0 to Label1
	iconst_1
	istore_2
.var 3 is s Ljava/lang/String; from Label0 to Label1
	ldc "str"
	astore_3
.var 4 is f F from Label0 to Label1
	ldc 9.0
	fstore 4
	fload 4
	iload_1
	i2f
	fmul
	fload 4
	iconst_2
	i2f
	fdiv
	fadd
	fstore 4
	aload_3
	aload_3
	aload_3
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_3
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	bipush 7
	iload_1
	iadd
	iload_1
	ineg
	iload_1
	imul
	iconst_2
	idiv
	isub
	invokestatic io/printInteger(I)V
	iload_1
	iload_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_2
	iand
	invokestatic io/printBoolean(Z)V
	fload 4
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 5
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
