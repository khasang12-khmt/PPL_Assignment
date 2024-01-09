.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is e [F from Label0 to Label1
	iconst_2
	anewarray [[F
	dup
	iconst_0
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_1
	ldc 200000.0
	fastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 0.0003
	fastore
	dup
	iconst_1
	ldc 0.04
	fastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.5
	fneg
	fastore
	dup
	iconst_1
	ldc 3.0
	fastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 3456.0
	fastore
	dup
	iconst_1
	ldc 5.1
	fastore
	aastore
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	ldc 7.0
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	faload
	fadd
	fastore
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	faload
	invokestatic io/writeFloat(F)V
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
