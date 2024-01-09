.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "7"
	astore_1
	aload_1
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
