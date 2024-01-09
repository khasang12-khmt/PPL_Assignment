.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 7
	istore_1
	bipush 8
	istore_1
	bipush 9
	putstatic MT22Class.a I
	getstatic MT22Class.a I
	iload_1
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
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
	bipush 6
	putstatic MT22Class.a I
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
