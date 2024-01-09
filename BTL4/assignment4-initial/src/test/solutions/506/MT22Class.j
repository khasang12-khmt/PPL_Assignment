.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	ineg
	istore_1
	iload_1
	ineg
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
.var 2 is b F from Label0 to Label1
	ldc 100.0
	fstore_2
	fload_2
	fneg
	fstore_2
	fload_2
	invokestatic io/writeFloat(F)V
.var 3 is c Z from Label0 to Label1
	iconst_1
	istore_3
	iload_3
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	iload_3
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 5
.limit locals 4
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
