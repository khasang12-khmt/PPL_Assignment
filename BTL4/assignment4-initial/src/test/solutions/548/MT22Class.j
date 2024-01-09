.source MT22Class.java
.class public MT22Class
.super java.lang.Object

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
.var 2 is l I from Label0 to Label1
	iconst_3
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
	aload_1
	iload_3
	iaload
	iastore
Label11:
	aload_1
	iload_3
	iaload
	iconst_0
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
Label12:
	aload_1
	iload_3
	iaload
	invokestatic io/printInteger(I)V
Label9:
Label13:
	aload_1
	iload_3
	aload_1
	iload_3
	iaload
	iconst_1
	isub
	iastore
	goto Label11
Label10:
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
.limit stack 8
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
