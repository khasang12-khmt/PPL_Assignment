.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static inc([II)V
.var 0 is a [I from Label0 to Label1
.var 1 is l I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	aload_0
	iload_2
	aload_0
	iload_2
	iaload
	iconst_1
	iadd
	iastore
Label2:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	astore_1
	aload_1
	iconst_3
	invokestatic MT22Class/inc([II)V
	aload_1
	iconst_2
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
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
