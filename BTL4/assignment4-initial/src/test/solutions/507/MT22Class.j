.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
.var 3 is c F from Label0 to Label1
	iload_1
	i2f
	fload_2
	fadd
	fstore_3
	fload_3
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
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
