.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 7
	istore_1
	iload_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_1
	bipush 10
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	ldc "x>10"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label8
Label7:
	iload_1
	bipush 10
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	iload_1
	iconst_5
	if_icmplt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	iand
	ifle Label13
	ldc "5<=x<=10"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label14
Label13:
	ldc "x<5"
	invokestatic io/printString(Ljava/lang/String;)V
Label14:
Label8:
	goto Label15
Label4:
	ldc "x<0"
	invokestatic io/printString(Ljava/lang/String;)V
Label15:
Label1:
	return
.limit stack 10
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
