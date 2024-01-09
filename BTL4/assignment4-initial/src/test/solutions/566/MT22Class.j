.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static getSum([II)I
.var 0 is arr [I from Label0 to Label1
.var 1 is size I from Label0 to Label1
Label0:
.var 2 is res I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
	iconst_0
	istore_3
Label4:
	iload_3
	iload_1
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	iload_2
	aload_0
	iload_3
	iaload
	iadd
	istore_2
Label2:
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
	iload_2
	ireturn
Label1:
.limit stack 5
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is nums [I from Label0 to Label1
	iconst_5
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
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
	aload_1
	iconst_5
	invokestatic MT22Class/getSum([II)I
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
