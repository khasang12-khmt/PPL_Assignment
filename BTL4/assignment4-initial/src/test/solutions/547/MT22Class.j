.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
	aload_1
	iconst_0
	iconst_3
	iastore
Label4:
	aload_1
	iconst_0
	iaload
	iconst_0
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	aload_1
	iconst_0
	iaload
	invokestatic io/printInteger(I)V
Label2:
Label6:
	aload_1
	iconst_0
	aload_1
	iconst_0
	iaload
	iconst_1
	isub
	iastore
	goto Label4
Label3:
	aload_1
	iconst_0
	iaload
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
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
