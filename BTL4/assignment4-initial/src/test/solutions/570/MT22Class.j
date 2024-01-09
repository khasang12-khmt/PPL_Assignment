.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static findGCD(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	ireturn
Label4:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MT22Class/findGCD(II)I
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 24
	iastore
	astore_1
.var 2 is gcd I from Label0 to Label1
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_1
	iaload
	invokestatic MT22Class/findGCD(II)I
	istore_2
	iload_2
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 3
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
