.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iconst_5
	istore_1
	iconst_5
	istore_1
Label4:
	iload_1
	iconst_0
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	goto Label3
Label11:
	iload_1
	invokestatic io/printInteger(I)V
Label2:
Label6:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 6
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
