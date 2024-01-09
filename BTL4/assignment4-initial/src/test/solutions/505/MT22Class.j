.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_2
	istore_2
	iload_2
	iload_1
	idiv
	istore_2
	iload_1
	iload_2
	iadd
	istore_1
	iload_1
	iload_2
	imul
	istore_1
	iload_2
	iconst_2
	irem
	istore_2
	iload_1
	iconst_1
	isub
	invokestatic io/printInteger(I)V
.var 3 is b1 Z from Label0 to Label1
	iconst_1
	istore_3
.var 4 is b2 Z from Label0 to Label1
	iconst_0
	istore 4
	iload_3
	iload 4
	ior
	istore_3
	iload_3
	iload 4
	iand
	invokestatic io/printBoolean(Z)V
	iload_2
	iload_1
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/printBoolean(Z)V
.var 5 is s1 Ljava/lang/String; from Label0 to Label1
	ldc "hello"
	astore 5
.var 6 is s2 Ljava/lang/String; from Label0 to Label1
	ldc "world"
	astore 6
	aload 5
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload 6
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore 5
	aload 5
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 7
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
