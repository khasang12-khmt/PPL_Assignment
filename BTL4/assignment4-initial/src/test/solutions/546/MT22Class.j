.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
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
	aastore
	dup
	iconst_1
	iconst_3
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
	aastore
	astore_1
.var 2 is r I from Label0 to Label1
	iconst_2
	istore_2
.var 3 is c I from Label0 to Label1
	iconst_3
	istore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is j I from Label0 to Label1
	iconst_0
	istore 5
	iconst_0
	istore 4
Label4:
	iload 4
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	iconst_0
	istore 5
Label11:
	iload 5
	iload_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
Label12:
	aload_1
	iload 4
	aaload
	iload 5
	iload 4
	iload 5
	imul
	iload 5
	iadd
	iastore
	aload_1
	iload 4
	aaload
	iload 5
	iaload
	invokestatic io/printInteger(I)V
Label9:
Label13:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label11
Label10:
Label2:
Label6:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label4
Label3:
Label1:
	return
.limit stack 8
.limit locals 6
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
