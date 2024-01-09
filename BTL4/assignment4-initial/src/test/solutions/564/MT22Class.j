.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
	fload_1
	fload_2
	fmul
	fload_2
	fload_2
	fdiv
	fsub
	ldc 0.6
	fadd
	fload_2
	ldc 0.2
	fsub
	invokestatic MT22Class/add(FF)F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static add(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_1
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
