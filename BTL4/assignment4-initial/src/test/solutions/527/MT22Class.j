.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 7
	istore_1
	iload_1
	bipush 10
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "x>10"
	invokestatic io/printString(Ljava/lang/String;)V
	iload_1
	iconst_2
	imul
	istore_1
	goto Label5
Label4:
	iload_1
	bipush 10
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_1
	iconst_5
	if_icmplt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ifle Label10
	iload_1
	iconst_1
	iadd
	istore_1
	ldc "5<=x<=10;"
	invokestatic io/printString(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label11
Label10:
	iload_1
	bipush 6
	isub
	istore_1
	ldc "x<5"
	invokestatic io/printString(Ljava/lang/String;)V
Label11:
Label5:
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 8
.limit locals 2
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
