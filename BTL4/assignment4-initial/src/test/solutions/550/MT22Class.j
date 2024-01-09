.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
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
	putstatic MT22Class.a [I
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is l I from Label0 to Label1
	iconst_5
	istore_2
	iconst_0
	istore_1
Label4:
	iload_1
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	getstatic MT22Class.a [I
	iload_1
	iaload
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
	getstatic MT22Class.a [I
	iload_1
	iaload
	invokestatic io/printInteger(I)V
	goto Label12
Label11:
	goto Label2
Label12:
Label2:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 6
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
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	putstatic MT22Class.a [I
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
