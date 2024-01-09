.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iconst_5
	istore_1
	iconst_2
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
.var 2 is i I from Label0 to Label1
	iconst_2
	istore_2
Label11:
	iload_2
	iconst_0
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
Label12:
	iload_1
	iload_2
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label9
	goto Label19
Label18:
	iload_2
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
Label19:
Label9:
Label13:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label11
Label10:
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
.limit stack 8
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
