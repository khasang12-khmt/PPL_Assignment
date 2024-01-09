.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static isOdd(I)Z
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static getString(Ljava/lang/String;)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "GetString: "
	aload_0
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	areturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 7
	invokestatic MT22Class/isOdd(I)Z
	invokestatic io/printBoolean(Z)V
	ldc "Ez"
	invokestatic MT22Class/getString(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
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
