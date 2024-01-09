.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	astore_1
.var 2 is l I from Label0 to Label1
	iconst_5
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
	iconst_0
	istore_3
Label4:
	iload_3
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	aload_1
	iload_3
	iload_3
	iastore
	aload_1
	iload_3
	iaload
	invokestatic io/printInteger(I)V
Label2:
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
Label1:
	return
.limit stack 5
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
