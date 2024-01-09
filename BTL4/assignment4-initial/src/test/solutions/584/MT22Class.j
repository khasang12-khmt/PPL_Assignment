.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static phil_a [I
.field static phil_b [I
.field static phil_d [Ljava/lang/String;

.method public static phil(IIILjava/lang/String;)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is d Ljava/lang/String; from Label0 to Label1
Label0:
	iload_1
	iconst_5
	iadd
	istore_1
	iload_0
	iload_2
	iadd
	iconst_4
	iadd
	istore_1
	iload_0
	invokestatic io/printInteger(I)V
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	aload_3
	aload_3
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	getstatic MT22Class.phil_a [I
	iconst_0
	iload_0
	iastore
	getstatic MT22Class.phil_b [I
	iconst_0
	iload_1
	iastore
	getstatic MT22Class.phil_d [Ljava/lang/String;
	iconst_0
	aload_3
	aastore
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is k I from Label0 to Label1
	bipush 15
	istore_2
.var 3 is s Ljava/lang/String; from Label0 to Label1
	ldc "Hi"
	astore_3
	iload_1
	iload_1
	iload_1
	iload_2
	iadd
	aload_3
	invokestatic MT22Class/phil(IIILjava/lang/String;)V
	getstatic MT22Class.phil_a [I
	iconst_0
	iaload
	istore_1
	getstatic MT22Class.phil_b [I
	iconst_0
	iaload
	istore_1
	getstatic MT22Class.phil_d [Ljava/lang/String;
	iconst_0
	aaload
	astore_3
	iload_1
	invokestatic io/printInteger(I)V
	iload_2
	invokestatic io/printInteger(I)V
	aload_3
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 4
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
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	putstatic MT22Class.phil_d [Ljava/lang/String;
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	putstatic MT22Class.phil_b [I
	iconst_1
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	putstatic MT22Class.phil_a [I
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
