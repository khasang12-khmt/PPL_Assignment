.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is f [I from Label0 to Label1
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iconst_2
	iadd
	iastore
	dup
	iconst_1
	iconst_2
	iconst_4
	imul
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iconst_5
	isub
	iastore
	dup
	iconst_1
	iconst_4
	iconst_1
	iadd
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iconst_1
	irem
	iastore
	dup
	iconst_1
	iconst_2
	iconst_2
	idiv
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 30
	bipush 6
	isub
	iastore
	dup
	iconst_1
	iconst_4
	iconst_5
	iadd
	iastore
	aastore
	aastore
	astore_1
	aload_1
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_1
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 11
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
