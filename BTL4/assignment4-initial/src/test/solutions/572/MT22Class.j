.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static i(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static s(Ljava/lang/String;)Ljava/lang/String;
.var 0 is c Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static f(F)F
.var 0 is b F from Label0 to Label1
Label0:
	fload_0
	freturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static b(Z)Z
.var 0 is d Z from Label0 to Label1
Label0:
	iload_0
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	invokestatic MT22Class/f(F)F
	iconst_2
	invokestatic MT22Class/i(I)I
	i2f
	fadd
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
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
