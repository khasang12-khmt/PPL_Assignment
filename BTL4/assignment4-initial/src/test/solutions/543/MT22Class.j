.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 10
	istore_1
Label2:
	iload_1
	bipush 15
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_1
	iconst_4
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label11:
Label8:
	iload_1
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 8
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
