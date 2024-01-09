.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	aastore
	astore_1
.var 2 is n I from Label0 to Label1
	iconst_3
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is j I from Label0 to Label1
	iconst_0
	istore 4
	iconst_0
	istore_3
Label4:
	iload_3
	iload_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
Label5:
	iconst_0
	istore 4
Label11:
	iload 4
	iload_2
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
Label12:
	iload_3
	iload 4
	if_icmpeq Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label9
Label18:
	aload_1
	iload_3
	aaload
	iload 4
	iconst_1
	iastore
Label9:
Label13:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label11
Label10:
Label2:
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
	iconst_0
	istore_3
Label21:
	iload_3
	iload_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label20
Label22:
	iconst_0
	istore 4
Label28:
	iload 4
	iload_2
	if_icmpge Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label27
Label29:
	aload_1
	iload_3
	aaload
	iload 4
	iaload
	invokestatic io/printInteger(I)V
Label26:
Label30:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label28
Label27:
Label19:
Label23:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label21
Label20:
Label1:
	return
.limit stack 12
.limit locals 5
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
