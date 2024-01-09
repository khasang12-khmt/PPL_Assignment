.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is e [Ljava/lang/String; from Label0 to Label1
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "1"
	aastore
	dup
	iconst_1
	ldc "2"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "3"
	aastore
	dup
	iconst_1
	ldc "4"
	aastore
	aastore
	astore_1
.var 2 is f [I from Label0 to Label1
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
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
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
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	aastore
	astore_2
	aload_1
	iconst_1
	aaload
	iconst_1
	aaload
	invokestatic io/printString(Ljava/lang/String;)V
	aload_2
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_1
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 10
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
