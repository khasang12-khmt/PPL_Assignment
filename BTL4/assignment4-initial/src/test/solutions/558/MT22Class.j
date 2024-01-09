.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.i I
	invokestatic MT22Class/inc(I)I
	invokestatic MT22Class/double(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static inc(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/printInteger(I)V
	iload_0
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static double(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/printInteger(I)V
	iload_0
	iconst_2
	imul
	ireturn
Label1:
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
	iconst_0
	putstatic MT22Class.i I
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
