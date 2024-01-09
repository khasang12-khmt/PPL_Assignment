.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	iconst_1
	i2f
	fstore_1
.var 2 is b I from Label0 to Label1
	iconst_2
	istore_2
	fload_1
	iload_2
	invokestatic MT22Class/add(FI)F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static add(FI)F
.var 0 is a F from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	fload_0
	iload_1
	i2f
	fadd
	freturn
Label1:
.limit stack 2
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
