.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(III)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 3
.end method

.method public static foo1(I)I
.var 0 is b I from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is c I from Label0 to Label1
	iconst_3
	istore_2
	iload_1
	iload_0
	iadd
	iload_2
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	invokestatic MT22Class/foo1(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 1
.limit locals 1
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
