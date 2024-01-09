.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MT22Class.b I
Label4:
	getstatic MT22Class.b I
	iconst_5
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	getstatic MT22Class.b I
	invokestatic io/printInteger(I)V
Label2:
Label6:
	getstatic MT22Class.b I
	iconst_1
	iadd
	putstatic MT22Class.b I
	goto Label4
Label3:
	getstatic MT22Class.b I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
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
	putstatic MT22Class.b I
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
