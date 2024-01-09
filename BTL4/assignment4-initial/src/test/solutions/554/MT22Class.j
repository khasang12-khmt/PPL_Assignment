.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	putstatic MT22Class.a [I
.var 1 is l I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
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
	getstatic MT22Class.a [I
	iload_2
	iaload
	iconst_1
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	ldc "Wrong"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label12
Label11:
	ldc "Right"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label3
Label12:
Label2:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iload_2
	invokestatic io/printInteger(I)V
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
	putstatic MT22Class.a [I
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
