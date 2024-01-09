.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i1 I from Label0 to Label1
	iconst_2
	iconst_1
	imul
	istore_1
.var 2 is i2 I from Label0 to Label1
	iconst_3
	iconst_1
	idiv
	istore_2
.var 3 is i3 I from Label0 to Label1
	iconst_4
	iconst_0
	isub
	istore_3
.var 4 is b1 Z from Label0 to Label1
	iconst_1
	iconst_0
	iand
	istore 4
.var 5 is b2 Z from Label0 to Label1
	iconst_1
	iconst_0
	ior
	istore 5
.var 6 is s Ljava/lang/String; from Label0 to Label1
	ldc "hi"
	astore 6
.var 7 is f F from Label0 to Label1
	ldc 9.0
	iconst_2
	i2f
	fmul
	fstore 7
	fload 7
	iload_1
	i2f
	fmul
	fload 7
	iconst_2
	i2f
	fdiv
	fadd
	fstore 7
	aload 6
	aload 6
	aload 6
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload 6
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore 6
	ldc 7.0
	iload_2
	i2f
	fadd
	iload_1
	ineg
	iload_3
	imul
	iconst_2
	idiv
	i2f
	fsub
	invokestatic io/writeFloat(F)V
	iload_3
	iload_2
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload 4
	iand
	invokestatic io/printBoolean(Z)V
	fload 7
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 8
.limit locals 8
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
