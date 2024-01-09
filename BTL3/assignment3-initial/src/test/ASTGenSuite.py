import unittest
from TestUtils import TestAST
from AST import *

# Name: Nguyễn Hữu Danh
# StudentID: 2010174

class ASTGenSuite(unittest.TestCase):
    # Variable declarations
    def test1(self):
        input = """a: integer = 5;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """str: string = "Ohhh";"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(Ohhh))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """flag: boolean = true;"""
        expect = """Program([
	VarDecl(flag, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """pi: float = 3.14;"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(3.14))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """arr: array [1,2] of integer = {};"""
        expect = """Program([
	VarDecl(arr, ArrayType([1, 2], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """a, b, c: integer = 5, 6, 7;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(5))
	VarDecl(b, IntegerType, IntegerLit(6))
	VarDecl(c, IntegerType, IntegerLit(7))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """x, y, z: string = 5.2, {1,2,3}, "aaa";"""
        expect = """Program([
	VarDecl(x, StringType, FloatLit(5.2))
	VarDecl(y, StringType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(z, StringType, StringLit(aaa))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = """a, b, c: float = 1, 2, 3;"""
        expect = """Program([
	VarDecl(a, FloatType, IntegerLit(1))
	VarDecl(b, FloatType, IntegerLit(2))
	VarDecl(c, FloatType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """a, b, c: string = "aa", "bb", "cc";"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(aa))
	VarDecl(b, StringType, StringLit(bb))
	VarDecl(c, StringType, StringLit(cc))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = """n, h, d: integer = 1, 5, 0;"""
        expect = """Program([
	VarDecl(n, IntegerType, IntegerLit(1))
	VarDecl(h, IntegerType, IntegerLit(5))
	VarDecl(d, IntegerType, IntegerLit(0))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    # Function declarations
    def test11(self):
        input = """main: function void(n: integer, out d: string) {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(n, IntegerType), OutParam(d, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = """f: function integer(inherit out a:integer) inherit main {}"""
        expect = """Program([
	FuncDecl(f, IntegerType, [InheritOutParam(a, IntegerType)], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """xyz: function auto() {}"""
        expect = """Program([
	FuncDecl(xyz, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """cal: function float(out arr: array [3] of integer) {}"""
        expect = """Program([
	FuncDecl(cal, FloatType, [OutParam(arr, ArrayType([3], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """tft_rate: function float(win_per: float, champ_list: array [9] of string, name: string) inherit Riot {}"""
        expect = """Program([
	FuncDecl(tft_rate, FloatType, [Param(win_per, FloatType), Param(champ_list, ArrayType([9], StringType)), Param(name, StringType)], Riot, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = """BFS: function void(inherit node: string) {}"""
        expect = """Program([
	FuncDecl(BFS, VoidType, [InheritParam(node, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """Genetic_al: function void(params: string) inherit algorithm {}"""
        expect = """Program([
	FuncDecl(Genetic_al, VoidType, [Param(params, StringType)], algorithm, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """how_to_pass_SE: function string(out rate: float) inherit CSE {}"""
        expect = """Program([
	FuncDecl(how_to_pass_SE, StringType, [OutParam(rate, FloatType)], CSE, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """roll_at_level_8: function boolean(champ: string, rate: array [5] of float) {}"""
        expect = """Program([
	FuncDecl(roll_at_level_8, BooleanType, [Param(champ, StringType), Param(rate, ArrayType([5], FloatType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """findtheroad: function array [10] of string(roadmap: string) inherit ggmap {}"""
        expect = """Program([
	FuncDecl(findtheroad, ArrayType([10], StringType), [Param(roadmap, StringType)], ggmap, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    # Assignment statements
    def test21(self):
        input = """main: function void() {
    a = 2;
    b = "string";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), StringLit(string))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """main: function void() {
    c = true;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(c), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = """main: function void() {
    d[1] = {1,2,3};
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(d, [IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = """main: function void() {
    pi = 3.14;
    S = r * r * pi;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(pi), FloatLit(3.14)), AssignStmt(Id(S), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(pi)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """main: function void() {
    math = 10;
    physics = 9.25;
    chemistry = 8.25;
    ovr = math + physics + chemistry;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(math), IntegerLit(10)), AssignStmt(Id(physics), FloatLit(9.25)), AssignStmt(Id(chemistry), FloatLit(8.25)), AssignStmt(Id(ovr), BinExpr(+, BinExpr(+, Id(math), Id(physics)), Id(chemistry)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """main: function void() {
    a = 5 + 2;
    b[2] = 5 * 4;
    c = 5 / 3;
    d[1] = (a + b) * (c / 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(5), IntegerLit(2))), AssignStmt(ArrayCell(b, [IntegerLit(2)]), BinExpr(*, IntegerLit(5), IntegerLit(4))), AssignStmt(Id(c), BinExpr(/, IntegerLit(5), IntegerLit(3))), AssignStmt(ArrayCell(d, [IntegerLit(1)]), BinExpr(*, BinExpr(+, Id(a), Id(b)), BinExpr(/, Id(c), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """main: function void() {
    a = true;
    b = false;
    flag = a && b || (a && b);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BooleanLit(True)), AssignStmt(Id(b), BooleanLit(False)), AssignStmt(Id(flag), BinExpr(||, BinExpr(&&, Id(a), Id(b)), BinExpr(&&, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """main: function void() {
    result = cal(a,b,c);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), FuncCall(cal, [Id(a), Id(b), Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """main: function void() {
    a = 5 > 2;
    b = 7 <= 3;
    c = (1 < 5) >= (5 % 2);
    d = !(5 < 4);
    e = !a && b || c && (d && 1);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, IntegerLit(5), IntegerLit(2))), AssignStmt(Id(b), BinExpr(<=, IntegerLit(7), IntegerLit(3))), AssignStmt(Id(c), BinExpr(>=, BinExpr(<, IntegerLit(1), IntegerLit(5)), BinExpr(%, IntegerLit(5), IntegerLit(2)))), AssignStmt(Id(d), UnExpr(!, BinExpr(<, IntegerLit(5), IntegerLit(4)))), AssignStmt(Id(e), BinExpr(&&, BinExpr(||, BinExpr(&&, UnExpr(!, Id(a)), Id(b)), Id(c)), BinExpr(&&, Id(d), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """main: function void() {
    str[0] = "111" + "222";
    str1[1,2] = str::"333";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(str, [IntegerLit(0)]), BinExpr(+, StringLit(111), StringLit(222))), AssignStmt(ArrayCell(str1, [IntegerLit(1), IntegerLit(2)]), BinExpr(::, Id(str), StringLit(333)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    # If statements
    def test31(self):
        input = """is_pass: function void(grade: float) {
    if (grade >= 5.0) print("Is passed");
}"""
        expect = """Program([
	FuncDecl(is_pass, VoidType, [Param(grade, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(grade), FloatLit(5.0)), CallStmt(print, StringLit(Is passed)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """is_pass: function void(grade: float) {
    if (grade >= 5.0) print("Is passed");
    else print("You still pass, but pass away");
}"""
        expect = """Program([
	FuncDecl(is_pass, VoidType, [Param(grade, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(grade), FloatLit(5.0)), CallStmt(print, StringLit(Is passed)), CallStmt(print, StringLit(You still pass, but pass away)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """is_pass: function void(grade: float) {
    if (grade >= 8.0) print("Excellent");
    else if (grade >= 5.0) print("Is passed");
}"""
        expect = """Program([
	FuncDecl(is_pass, VoidType, [Param(grade, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(grade), FloatLit(8.0)), CallStmt(print, StringLit(Excellent)), IfStmt(BinExpr(>=, Id(grade), FloatLit(5.0)), CallStmt(print, StringLit(Is passed))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """is_pass: function void(grade: float) {
    if (grade >= 8.0) print("Excellent");
    else if (grade >= 5.0) print("Is passed");
    else print("Good luck next time");
}"""
        expect = """Program([
	FuncDecl(is_pass, VoidType, [Param(grade, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(grade), FloatLit(8.0)), CallStmt(print, StringLit(Excellent)), IfStmt(BinExpr(>=, Id(grade), FloatLit(5.0)), CallStmt(print, StringLit(Is passed)), CallStmt(print, StringLit(Good luck next time))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """nenkiembokhong: function string() {
    if (random(seed) >= 0.5) return "nen";
    else {
        print("Random lai di");
        return "khong";
    }
}"""
        expect = """Program([
	FuncDecl(nenkiembokhong, StringType, [], None, BlockStmt([IfStmt(BinExpr(>=, FuncCall(random, [Id(seed)]), FloatLit(0.5)), ReturnStmt(StringLit(nen)), BlockStmt([CallStmt(print, StringLit(Random lai di)), ReturnStmt(StringLit(khong))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """truonganhngoc: function string(cmt: string) {
    if (cmt == "Tin chuan chua anh") return "Chuan em nhe";
    else return "Admin Lan blog ban nay cho anh";
}"""
        expect = """Program([
	FuncDecl(truonganhngoc, StringType, [Param(cmt, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(cmt), StringLit(Tin chuan chua anh)), ReturnStmt(StringLit(Chuan em nhe)), ReturnStmt(StringLit(Admin Lan blog ban nay cho anh)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """NicoloZaniolo: function string(quote: string) {
    if (dribble) return "Chuyen di dung sut";
    else if (shoot) return "Anh khong nghe toi";
    else if (no_goal) return "Anh khong an mung";
}"""
        expect = """Program([
	FuncDecl(NicoloZaniolo, StringType, [Param(quote, StringType)], None, BlockStmt([IfStmt(Id(dribble), ReturnStmt(StringLit(Chuyen di dung sut)), IfStmt(Id(shoot), ReturnStmt(StringLit(Anh khong nghe toi)), IfStmt(Id(no_goal), ReturnStmt(StringLit(Anh khong an mung)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """quote_list: function array [3] of string() {
    if (is_reply) return {"Comment nang ne qua, ban thua do a`"
            , "Em dien hoi canh sat Los Angeles nhe"
            , "Khoan da chung ta can phai check VAR"};
    else return "Ban se bi block";
}"""
        expect = """Program([
	FuncDecl(quote_list, ArrayType([3], StringType), [], None, BlockStmt([IfStmt(Id(is_reply), ReturnStmt(ArrayLit([StringLit(Comment nang ne qua, ban thua do a`), StringLit(Em dien hoi canh sat Los Angeles nhe), StringLit(Khoan da chung ta can phai check VAR)])), ReturnStmt(StringLit(Ban se bi block)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """roll_or_die: function boolean (flag: boolean) inherit main {
    if (random > 3) return true;
    else return false;
}"""
        expect = """Program([
	FuncDecl(roll_or_die, BooleanType, [Param(flag, BooleanType)], main, BlockStmt([IfStmt(BinExpr(>, Id(random), IntegerLit(3)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """quamonPPL: function auto() {
    if (1 == 1) return "Rot mon";
    else print("Cung la rot mon");
}"""
        expect = """Program([
	FuncDecl(quamonPPL, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, IntegerLit(1), IntegerLit(1)), ReturnStmt(StringLit(Rot mon)), CallStmt(print, StringLit(Cung la rot mon)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    # For statements
    def test41(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 1) {
        writleInt(i);
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writleInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """main: function void() {
    for (i = 5*8, a < 10+2, b / 2) writleInt(i);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(*, IntegerLit(5), IntegerLit(8))), BinExpr(<, Id(a), BinExpr(+, IntegerLit(10), IntegerLit(2))), BinExpr(/, Id(b), IntegerLit(2)), CallStmt(writleInt, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """main: function void() {
    for (abc = z, i < y, a + func(5)) {}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(abc), Id(z)), BinExpr(<, Id(i), Id(y)), BinExpr(+, Id(a), FuncCall(func, [IntegerLit(5)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = """main: function void() {
    for (y = a && b, a || b, a::c) z = 1;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(y), BinExpr(&&, Id(a), Id(b))), BinExpr(||, Id(a), Id(b)), BinExpr(::, Id(a), Id(c)), AssignStmt(Id(z), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = """main: function void() {
    for (i = z, i < 5, j >= 1) a = func(1*2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), Id(z)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(>=, Id(j), IntegerLit(1)), AssignStmt(Id(a), FuncCall(func, [BinExpr(*, IntegerLit(1), IntegerLit(2))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 1) {
        writleInt(i);
    }
    for (i = 1, i < 10, i + 1) {
        writleInt(i);
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writleInt, Id(i))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writleInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 1) continue;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 1) {
        if (i == 5) break;
        else print(i);
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt(), CallStmt(print, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 2) {
        i = i + 1;
        foo(xyz);
        {
            a = a + 1;
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(foo, Id(xyz)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = """main: function void() {
    for (i = 1, i < 10, i + 1) {
        while (i == 1) i = 0;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(==, Id(i), IntegerLit(1)), AssignStmt(Id(i), IntegerLit(0)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    # While statements
    def test51(self):
        input = """main: function void() {
    while (i < 5) {
        i = i + 1;
        print("Its fine");
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(print, StringLit(Its fine))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = """main: function void() {
    while (i < 10) {}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """main: function void() {
    while (ity < yza) print(a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(ity), Id(yza)), CallStmt(print, Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = """main: function void() {
    while (i + 5) a = "str";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, Id(i), IntegerLit(5)), AssignStmt(Id(a), StringLit(str)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = """main: function void() {
    while (i :: 0.5) {
        for (t = 0, t < 5, t + 1) {
            break;
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(::, Id(i), FloatLit(0.5)), BlockStmt([ForStmt(AssignStmt(Id(t), IntegerLit(0)), BinExpr(<, Id(t), IntegerLit(5)), BinExpr(+, Id(t), IntegerLit(1)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """main: function void() {
    while (i < 7) {
        do {
            check(count,b,z,t);
        }
        while (x + y);
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(7)), BlockStmt([DoWhileStmt(BinExpr(+, Id(x), Id(y)), BlockStmt([CallStmt(check, Id(count), Id(b), Id(z), Id(t))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """main: function void() {
    while (j == 0) {
        call(0.5,2,"str",{1,2,3});
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(j), IntegerLit(0)), BlockStmt([CallStmt(call, FloatLit(0.5), IntegerLit(2), StringLit(str), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = """main: function void() {
    while (i + i + z) break;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, BinExpr(+, Id(i), Id(i)), Id(z)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = """main: function void() {
    while (z / 5) {
        i = i + 1;
        continue;
        iyz = ppl(hk222);
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(/, Id(z), IntegerLit(5)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt(), AssignStmt(Id(iyz), FuncCall(ppl, [Id(hk222)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """main: function void() {
    while (i < 5) if (i == 1) {
        i = 5; break;
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(5)), BreakStmt()])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    # Do-while statements
    def test61(self):
        input = """main: function void() {
    do {} while (i + 1);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """main: function void() {
    do {call(xyz);} while (a * b);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(*, Id(a), Id(b)), BlockStmt([CallStmt(call, Id(xyz))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """main: function void() {
    do 
    {
        {
            a = a + a + a * a;
        }
    } 
    while (i + 1);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, Id(a), Id(a)), BinExpr(*, Id(a), Id(a))))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """main: function void() {
    do { tr = true; } while ("str" + false + 1 + 0.5);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, BinExpr(+, BinExpr(+, StringLit(str), BooleanLit(False)), IntegerLit(1)), FloatLit(0.5)), BlockStmt([AssignStmt(Id(tr), BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """main: function void() {
    do {_tttt = 1 + 2;} while (expr + expr);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(expr), Id(expr)), BlockStmt([AssignStmt(Id(_tttt), BinExpr(+, IntegerLit(1), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """main: function void() {
    do {return 1;} while (a && b);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(&&, Id(a), Id(b)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """main: function void() {
    do {break;} while (foo(abc));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(FuncCall(foo, [Id(abc)]), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """main: function void() {
    do {while (t+z*a) {}} while (2 + a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, IntegerLit(2), Id(a)), BlockStmt([WhileStmt(BinExpr(+, Id(t), BinExpr(*, Id(z), Id(a))), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """main: function void() {
    do {call(22,11,33); continue; return 1;} while (aa);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(aa), BlockStmt([CallStmt(call, IntegerLit(22), IntegerLit(11), IntegerLit(33)), ContinueStmt(), ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """main: function void() {
    do {{{{return 1;} return 2;} return 3;} return 4;} while (z);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(z), BlockStmt([BlockStmt([BlockStmt([BlockStmt([ReturnStmt(IntegerLit(1))]), ReturnStmt(IntegerLit(2))]), ReturnStmt(IntegerLit(3))]), ReturnStmt(IntegerLit(4))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    # Combine all declarations and statements
    def test71(self):
        input = """main: function void() {
    pi: float = 3.14;
    n: float;
    n = 5.0;
    S = pi * square(n);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(pi, FloatType, FloatLit(3.14)), VarDecl(n, FloatType), AssignStmt(Id(n), FloatLit(5.0)), AssignStmt(Id(S), BinExpr(*, Id(pi), FuncCall(square, [Id(n)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """main: function void() {
    sum: integer = 0;
    arr: array[5] of integer;
    arr = {5,6,7,8,9};
    for (i = 0, i < 5, i+1) {
        print(cube(arr[i]));
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(arr, ArrayType([5], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, FuncCall(cube, [ArrayCell(arr, [Id(i)])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """main: function void() {
    x = x + 1;
    y = y + 1;
    z = z + 1;
    a, b, c: string = "How", "are", "you";
    if (x == y) {
        a = b;
        b = c;
    }
    else if (y == z) {
        b = c;
        c = a;
    }
    else {
        c = a;
        a = b;
    }
    concat(a, b, c);    
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1))), AssignStmt(Id(z), BinExpr(+, Id(z), IntegerLit(1))), VarDecl(a, StringType, StringLit(How)), VarDecl(b, StringType, StringLit(are)), VarDecl(c, StringType, StringLit(you)), IfStmt(BinExpr(==, Id(x), Id(y)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c))]), IfStmt(BinExpr(==, Id(y), Id(z)), BlockStmt([AssignStmt(Id(b), Id(c)), AssignStmt(Id(c), Id(a))]), BlockStmt([AssignStmt(Id(c), Id(a)), AssignStmt(Id(a), Id(b))]))), CallStmt(concat, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """main: function void() {
    while (a) {
        do {
            a = a + 1;
        }
        while (i + 1);
        return a;
    }
    for (a = 2, tg + wer, df + a) {
        for (j = 0, j < 5, j+1) {
            if (j == 2) continue;
            else if (j == 4) return j;
        }
        return "abc";
    }
    t = f + z;
    print(t);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(a), BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(Id(a))])), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(+, Id(tg), Id(wer)), BinExpr(+, Id(df), Id(a)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(j), IntegerLit(2)), ContinueStmt(), IfStmt(BinExpr(==, Id(j), IntegerLit(4)), ReturnStmt(Id(j))))])), ReturnStmt(StringLit(abc))])), AssignStmt(Id(t), BinExpr(+, Id(f), Id(z))), CallStmt(print, Id(t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """main: function void() {
    y = (a + z) && (t || y) :: (z / r % iopd);
    for (j = z, t < n, io / 5) break;
    foo(123);
    call(xsdf,ysdadfs,zdsasfd);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(::, BinExpr(&&, BinExpr(+, Id(a), Id(z)), BinExpr(||, Id(t), Id(y))), BinExpr(%, BinExpr(/, Id(z), Id(r)), Id(iopd)))), ForStmt(AssignStmt(Id(j), Id(z)), BinExpr(<, Id(t), Id(n)), BinExpr(/, Id(io), IntegerLit(5)), BreakStmt()), CallStmt(foo, IntegerLit(123)), CallStmt(call, Id(xsdf), Id(ysdadfs), Id(zdsasfd))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """main: function void() {
    sdffds(sadlfsd, sdfljfsdh, dsfhjsfda);
    y = a * b[1,2] + fdsfsd / sdffds;
    z[0,2,3] = sdflk(sfdsjsdl, wqheol);
    do {
        adfsfsd = adsffsd - 12123321 + {sdfd, fsdfdsdfs};
        continue;
    } while (safsaf + dslhfsd - dfshkfd);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(sdffds, Id(sadlfsd), Id(sdfljfsdh), Id(dsfhjsfda)), AssignStmt(Id(y), BinExpr(+, BinExpr(*, Id(a), ArrayCell(b, [IntegerLit(1), IntegerLit(2)])), BinExpr(/, Id(fdsfsd), Id(sdffds)))), AssignStmt(ArrayCell(z, [IntegerLit(0), IntegerLit(2), IntegerLit(3)]), FuncCall(sdflk, [Id(sfdsjsdl), Id(wqheol)])), DoWhileStmt(BinExpr(-, BinExpr(+, Id(safsaf), Id(dslhfsd)), Id(dfshkfd)), BlockStmt([AssignStmt(Id(adfsfsd), BinExpr(+, BinExpr(-, Id(adsffsd), IntegerLit(12123321)), ArrayLit([Id(sdfd), Id(fsdfdsdfs)]))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """main: function void() {
    { aa = 1; } {
        sfaldfsdf = sdfhdfsfds + sdlffdhs - sdfksdfsdf;
        sjdffsd: integer = 5232;
        if (asdfdfs < ttt + fds) {
            do {i = i+1;} while (i+1);
            return fdfds+fdfdsdf[0,-1] + wssdf[9];
        }
        return fdsfd[0,2,3,4] * xcvs[0,0] / dfsdf[0,1];
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([AssignStmt(Id(aa), IntegerLit(1))]), BlockStmt([AssignStmt(Id(sfaldfsdf), BinExpr(-, BinExpr(+, Id(sdfhdfsfds), Id(sdlffdhs)), Id(sdfksdfsdf))), VarDecl(sjdffsd, IntegerType, IntegerLit(5232)), IfStmt(BinExpr(<, Id(asdfdfs), BinExpr(+, Id(ttt), Id(fds))), BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(BinExpr(+, BinExpr(+, Id(fdfds), ArrayCell(fdfdsdf, [IntegerLit(0), UnExpr(-, IntegerLit(1))])), ArrayCell(wssdf, [IntegerLit(9)])))])), ReturnStmt(BinExpr(/, BinExpr(*, ArrayCell(fdsfd, [IntegerLit(0), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayCell(xcvs, [IntegerLit(0), IntegerLit(0)])), ArrayCell(dfsdf, [IntegerLit(0), IntegerLit(1)])))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """main: function void() {
    ewr: string = "343dsfsd";
    fdsfsdfds, sdfsdffdosv: float = 12332, "strings";
    rtrwuepa, odsfodew, sohqodls: string = 123321, 12321, {"Stroihsd", fdsfds, dfsfsd};
    break; {
        if (dsfhfdsl + fsdkfdsfdcv > dsffdfdsfd) {
            return sdflfhewlfh;
        }
        else {
            return sdfoqrpsdp;
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(ewr, StringType, StringLit(343dsfsd)), VarDecl(fdsfsdfds, FloatType, IntegerLit(12332)), VarDecl(sdfsdffdosv, FloatType, StringLit(strings)), VarDecl(rtrwuepa, StringType, IntegerLit(123321)), VarDecl(odsfodew, StringType, IntegerLit(12321)), VarDecl(sohqodls, StringType, ArrayLit([StringLit(Stroihsd), Id(fdsfds), Id(dfsfsd)])), BreakStmt(), BlockStmt([IfStmt(BinExpr(>, BinExpr(+, Id(dsfhfdsl), Id(fsdkfdsfdcv)), Id(dsffdfdsfd)), BlockStmt([ReturnStmt(Id(sdflfhewlfh))]), BlockStmt([ReturnStmt(Id(sdfoqrpsdp))]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """main: function void() {
    dsffsd: string = sdfdfsfsd;
    wofewp = dflfd + dfskhdos && 312973 / hdsofd :: ofdfdf;
    sdfdsdfssdf = dsflhfdlhfdshfld + sfdslfdkhlsdf - fdskhiwqds;
    continue; {
        ewrwhro[0,1,2] = fdshlfshdlfds + 123465464 / 546461;
        sdfhds: boolean = "sdhfdsfd";
        fdsfds = 165461;
        return fdsjfwp;
        return 4213165;
        return {1,2,3,4};
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(dsffsd, StringType, Id(sdfdfsfsd)), AssignStmt(Id(wofewp), BinExpr(::, BinExpr(&&, BinExpr(+, Id(dflfd), Id(dfskhdos)), BinExpr(/, IntegerLit(312973), Id(hdsofd))), Id(ofdfdf))), AssignStmt(Id(sdfdsdfssdf), BinExpr(-, BinExpr(+, Id(dsflhfdlhfdshfld), Id(sfdslfdkhlsdf)), Id(fdskhiwqds))), ContinueStmt(), BlockStmt([AssignStmt(ArrayCell(ewrwhro, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]), BinExpr(+, Id(fdshlfshdlfds), BinExpr(/, IntegerLit(123465464), IntegerLit(546461)))), VarDecl(sdfhds, BooleanType, StringLit(sdhfdsfd)), AssignStmt(Id(fdsfds), IntegerLit(165461)), ReturnStmt(Id(fdsjfwp)), ReturnStmt(IntegerLit(4213165)), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """main: function void() {
    do {return 132213;} while (dsfdw / dfsfdsl + (sdfds - fdbkfds));
    rewdsjfewp = dfshdfsfds + _dfshdfs_sdfhdfssdf;
    fdfdhwf(sdfdsf,{123,213,13,aaa,weew});
    for (i = 0, i > 5, i - 1) {
        for (i = 0, i > 5, i - 1) {
            for (i = 0, i > 5, i - 1) {
                for (i = 0, i > 5, i - 1) {
                    return;
                }
            }
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, BinExpr(/, Id(dsfdw), Id(dfsfdsl)), BinExpr(-, Id(sdfds), Id(fdbkfds))), BlockStmt([ReturnStmt(IntegerLit(132213))])), AssignStmt(Id(rewdsjfewp), BinExpr(+, Id(dfshdfsfds), Id(_dfshdfs_sdfhdfssdf))), CallStmt(fdfdhwf, Id(sdfdsf), ArrayLit([IntegerLit(123), IntegerLit(213), IntegerLit(13), Id(aaa), Id(weew)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt()]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    # Catch errors
    def test81(self):
        input = """dsfhfdslfds: integer = false;
fsdffsdsdf: float = fdsfdsfds;
sfw, sdfhsdfo, dsfodsfhw: string = {1,2,3,4}, sdhfowe, "sfsdhow";
fhslfdsf: function array [1,1,1,1,1,1,1,1,1] of string (inherit out dshfsdldsffd: float) inherit main {
    return;
    return;
    return;
    return;
    dfdsfds = fdslfdsf + dsjkfkds;
    eqwr = fdshlfw[0,1,fdsfdsfds] + fdslfdldfsjlfd;
}
fsdhdfsdf, sdfwe, fwewro: integer = 432, 324432, "adsfsfad";
dfsfsd: function string () {
    sdfdsfds[1,2,2+3,(223+22+dsafr)] = dfshfdsl + fdshlfdsf[0,1,{2.4}];
    call(dsfhfdsldsf,rewro,"123213");
}
"""
        expect = """Program([
	VarDecl(dsfhfdslfds, IntegerType, BooleanLit(False))
	VarDecl(fsdffsdsdf, FloatType, Id(fdsfdsfds))
	VarDecl(sfw, StringType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(sdfhsdfo, StringType, Id(sdhfowe))
	VarDecl(dsfodsfhw, StringType, StringLit(sfsdhow))
	FuncDecl(fhslfdsf, ArrayType([1, 1, 1, 1, 1, 1, 1, 1, 1], StringType), [InheritOutParam(dshfsdldsffd, FloatType)], main, BlockStmt([ReturnStmt(), ReturnStmt(), ReturnStmt(), ReturnStmt(), AssignStmt(Id(dfdsfds), BinExpr(+, Id(fdslfdsf), Id(dsjkfkds))), AssignStmt(Id(eqwr), BinExpr(+, ArrayCell(fdshlfw, [IntegerLit(0), IntegerLit(1), Id(fdsfdsfds)]), Id(fdslfdldfsjlfd)))]))
	VarDecl(fsdhdfsdf, IntegerType, IntegerLit(432))
	VarDecl(sdfwe, IntegerType, IntegerLit(324432))
	VarDecl(fwewro, IntegerType, StringLit(adsfsfad))
	FuncDecl(dfsfsd, StringType, [], None, BlockStmt([AssignStmt(ArrayCell(sdfdsfds, [IntegerLit(1), IntegerLit(2), BinExpr(+, IntegerLit(2), IntegerLit(3)), BinExpr(+, BinExpr(+, IntegerLit(223), IntegerLit(22)), Id(dsafr))]), BinExpr(+, Id(dfshfdsl), ArrayCell(fdshlfdsf, [IntegerLit(0), IntegerLit(1), ArrayLit([FloatLit(2.4)])]))), CallStmt(call, Id(dsfhfdsldsf), Id(rewro), StringLit(123213))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """wfdwfupwe_2g3o : function void () {
    eqrspsf, whfe, dsdwp: array [2] of integer = {1123,123214,13232132132}, 42143, "SDhoreht";
    return 13124;
    do {
        e3prwf = ewp1 / dfofhdq + fdjspfew * hdshfdwf;
        return;
        return;
        break;
        continue;
        wqp, aa: string = 43243, 324324;
    }
    while (1 + 2);
    qewqwe = csfwwef + dfjsfwe / eepfpm * hofdsfho - fdhsfd * (132 + dsf);
    aaaf_sfew = 3243240;
    return 432 - 7432 - 432403;
}
dsfsdffd: integer = 5;
dsfweewree: function void(a: string) {
    return;
}
"""
        expect = """Program([
	FuncDecl(wfdwfupwe_2g3o, VoidType, [], None, BlockStmt([VarDecl(eqrspsf, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1123), IntegerLit(123214), IntegerLit(13232132132)])), VarDecl(whfe, ArrayType([2], IntegerType), IntegerLit(42143)), VarDecl(dsdwp, ArrayType([2], IntegerType), StringLit(SDhoreht)), ReturnStmt(IntegerLit(13124)), DoWhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), BlockStmt([AssignStmt(Id(e3prwf), BinExpr(+, BinExpr(/, Id(ewp1), Id(dfofhdq)), BinExpr(*, Id(fdjspfew), Id(hdshfdwf)))), ReturnStmt(), ReturnStmt(), BreakStmt(), ContinueStmt(), VarDecl(wqp, StringType, IntegerLit(43243)), VarDecl(aa, StringType, IntegerLit(324324))])), AssignStmt(Id(qewqwe), BinExpr(-, BinExpr(+, Id(csfwwef), BinExpr(*, BinExpr(/, Id(dfjsfwe), Id(eepfpm)), Id(hofdsfho))), BinExpr(*, Id(fdhsfd), BinExpr(+, IntegerLit(132), Id(dsf))))), AssignStmt(Id(aaaf_sfew), IntegerLit(3243240)), ReturnStmt(BinExpr(-, BinExpr(-, IntegerLit(432), IntegerLit(7432)), IntegerLit(432403)))]))
	VarDecl(dsfsdffd, IntegerType, IntegerLit(5))
	FuncDecl(dsfweewree, VoidType, [Param(a, StringType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """sdfdsf, sdfsd, dsfsdfsfd: integer = 2,3,4;
reerwrewr: string = 324324432;
ffddsfdssdsdfdsf: function void() {

}"""
        expect = """Program([
	VarDecl(sdfdsf, IntegerType, IntegerLit(2))
	VarDecl(sdfsd, IntegerType, IntegerLit(3))
	VarDecl(dsfsdfsfd, IntegerType, IntegerLit(4))
	VarDecl(reerwrewr, StringType, IntegerLit(324324432))
	FuncDecl(ffddsfdssdsdfdsf, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """sdfddsfd: function void() {
    return;
}"""
        expect = """Program([
	FuncDecl(sdfddsfd, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """sdffwfwef: function boolean(out dfwew: string, fddsf: boolean) {
    ewrewewrwerrew = dsffsd + fwqrdsf;
    return;
}"""
        expect = """Program([
	FuncDecl(sdffwfwef, BooleanType, [OutParam(dfwew, StringType), Param(fddsf, BooleanType)], None, BlockStmt([AssignStmt(Id(ewrewewrwerrew), BinExpr(+, Id(dsffsd), Id(fwqrdsf))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """abc: function string(inherit out sdd: string) inherit a123 {
    dsfd = fsdferwer + fsdlhfep / fdsofdsf;
    for (idwewr = 1, fdsfewpfew, fdspwer) {
        {
            ohohohohohohohohoho = 111111;
        }
    }
    rewrpwer, sdfsfdsfd: string = "32432434", {13232,{2133,21321},{abdfgfgf}};
}"""
        expect = """Program([
	FuncDecl(abc, StringType, [InheritOutParam(sdd, StringType)], a123, BlockStmt([AssignStmt(Id(dsfd), BinExpr(+, Id(fsdferwer), BinExpr(/, Id(fsdlhfep), Id(fdsofdsf)))), ForStmt(AssignStmt(Id(idwewr), IntegerLit(1)), Id(fdsfewpfew), Id(fdspwer), BlockStmt([BlockStmt([AssignStmt(Id(ohohohohohohohohoho), IntegerLit(111111))])])), VarDecl(rewrpwer, StringType, StringLit(32432434)), VarDecl(sdfsfdsfd, StringType, ArrayLit([IntegerLit(13232), ArrayLit([IntegerLit(2133), IntegerLit(21321)]), ArrayLit([Id(abdfgfgf)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """aaa123: function string(out trrtet: string) inherit trrtetre {
    return fgwedewrrew;
}"""
        expect = """Program([
	FuncDecl(aaa123, StringType, [OutParam(trrtet, StringType)], trrtetre, BlockStmt([ReturnStmt(Id(fgwedewrrew))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """aaaa: function string(out a: integer) {
    do {
        return;
    } while (asdffsd);
    while (i+i) a = 5;
    sdfdwwprew();
    aaaa, bnbbb, sdfdssdf: string = "a123213", dfsfde, 123214;
    return wer_123abfds;
}"""
        expect = """Program([
	FuncDecl(aaaa, StringType, [OutParam(a, IntegerType)], None, BlockStmt([DoWhileStmt(Id(asdffsd), BlockStmt([ReturnStmt()])), WhileStmt(BinExpr(+, Id(i), Id(i)), AssignStmt(Id(a), IntegerLit(5))), CallStmt(sdfdwwprew, ), VarDecl(aaaa, StringType, StringLit(a123213)), VarDecl(bnbbb, StringType, Id(dfsfde)), VarDecl(sdfdssdf, StringType, IntegerLit(123214)), ReturnStmt(Id(wer_123abfds))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """fewrewrewrewrewr: function void() {
    a = ewwerewr * 11;
    return;
    return;
    return;
    sdfdfdww = fgdshsfdsdffsd + fdsfsdsdf;
    fssdfdsf, rewrerewwer: string = 1,2;
}"""
        expect = """Program([
	FuncDecl(fewrewrewrewrewr, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(*, Id(ewwerewr), IntegerLit(11))), ReturnStmt(), ReturnStmt(), ReturnStmt(), AssignStmt(Id(sdfdfdww), BinExpr(+, Id(fgdshsfdsdffsd), Id(fdsfsdsdf))), VarDecl(fssdfdsf, StringType, IntegerLit(1)), VarDecl(rewrerewwer, StringType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """wrewprsd: function array [1,1,1,1,1,2] of string() {}"""
        expect = """Program([
	FuncDecl(wrewprsd, ArrayType([1, 1, 1, 1, 1, 2], StringType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """sdfdsfdsf: function string() {
    a = dfsfwer / 34324 ;
    wqeqe = 1234 * ab + fdsfd2 ;
    {
        return;
        return;
    }
    if (a == 2) {} else {}
}"""
        expect = """Program([
	FuncDecl(sdfdsfdsf, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(dfsfwer), IntegerLit(34324))), AssignStmt(Id(wqeqe), BinExpr(+, BinExpr(*, IntegerLit(1234), Id(ab)), Id(fdsfd2))), BlockStmt([ReturnStmt(), ReturnStmt()]), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """aaa: boolean = {123213,213213};
fdewew, strings: string = {2313,213123}, 123213;
aaaa, aaaaa, bbbb: string = 111, 23112, 32_42_34.1321;
fdsfsdfsdfds, rewwer: string = 24234, 32432432.213321;"""
        expect = """Program([
	VarDecl(aaa, BooleanType, ArrayLit([IntegerLit(123213), IntegerLit(213213)]))
	VarDecl(fdewew, StringType, ArrayLit([IntegerLit(2313), IntegerLit(213123)]))
	VarDecl(strings, StringType, IntegerLit(123213))
	VarDecl(aaaa, StringType, IntegerLit(111))
	VarDecl(aaaaa, StringType, IntegerLit(23112))
	VarDecl(bbbb, StringType, FloatLit(324234.1321))
	VarDecl(fdsfsdfsdfds, StringType, IntegerLit(24234))
	VarDecl(rewwer, StringType, FloatLit(32432432.213321))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """aaaa3324, stringgg: float = 43432234432, {123,123+1123,52.432};
aaa32132121312: function auto () {
    aaaa2432, treter, were: string = "321321213", 12321, 12312321_2333;
    dsfff = f24324432;
}"""
        expect = """Program([
	VarDecl(aaaa3324, FloatType, IntegerLit(43432234432))
	VarDecl(stringgg, FloatType, ArrayLit([IntegerLit(123), BinExpr(+, IntegerLit(123), IntegerLit(1123)), FloatLit(52.432)]))
	FuncDecl(aaa32132121312, AutoType, [], None, BlockStmt([VarDecl(aaaa2432, StringType, StringLit(321321213)), VarDecl(treter, StringType, IntegerLit(12321)), VarDecl(were, StringType, IntegerLit(123123212333)), AssignStmt(Id(dsfff), Id(f24324432))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """dsrwewre, fdssfd: integer = 213214_213213, dffdsb;
ewqrew: function void() {}
dsffwer: boolean = 324324;
ewrerwerw: function auto(inherit out asadf: string) {

}"""
        expect = """Program([
	VarDecl(dsrwewre, IntegerType, IntegerLit(213214213213))
	VarDecl(fdssfd, IntegerType, Id(dffdsb))
	FuncDecl(ewqrew, VoidType, [], None, BlockStmt([]))
	VarDecl(dsffwer, BooleanType, IntegerLit(324324))
	FuncDecl(ewrerwerw, AutoType, [InheritOutParam(asadf, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """mainnn: function auto(inherit aaaaaaa: string) {
    return;
}"""
        expect = """Program([
	FuncDecl(mainnn, AutoType, [InheritParam(aaaaaaa, StringType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """rrewrerw: integer = 432432234+234324342342;
aaaaaa: float = 32442343 / 23423443 * 234324234 :: 1213;
"""
        expect = """Program([
	VarDecl(rrewrerw, IntegerType, BinExpr(+, IntegerLit(432432234), IntegerLit(234324342342)))
	VarDecl(aaaaaa, FloatType, BinExpr(::, BinExpr(*, BinExpr(/, IntegerLit(32442343), IntegerLit(23423443)), IntegerLit(234324234)), IntegerLit(1213)))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """abcxyz: function string(fsdffsdfsd: string) {
    return;
    return;
    break;
    continue;
}"""
        expect = """Program([
	FuncDecl(abcxyz, StringType, [Param(fsdffsdfsd, StringType)], None, BlockStmt([ReturnStmt(), ReturnStmt(), BreakStmt(), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """ffwer: function auto(t: string) {
    do {return 132213;} while (dsfdw / dfsfdsl + (sdfds - fdbkfds));
    rewdsjfewp = dfshdfsfds + _dfshdfs_sdfhdfssdf;
    fdfdhwf(sdfdsf,{123,213,13,aaa,weew});
    for (i = 0, i > 5, i - 1) {
        for (i = 0, i > 5, i - 1) {
            for (i = 0, i > 5, i - 1) {
                for (i = 0, i > 5, i - 1) {
                    return;
                }
            }
        }
    }
}"""
        expect = """Program([
	FuncDecl(ffwer, AutoType, [Param(t, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(+, BinExpr(/, Id(dsfdw), Id(dfsfdsl)), BinExpr(-, Id(sdfds), Id(fdbkfds))), BlockStmt([ReturnStmt(IntegerLit(132213))])), AssignStmt(Id(rewdsjfewp), BinExpr(+, Id(dfshdfsfds), Id(_dfshdfs_sdfhdfssdf))), CallStmt(fdfdhwf, Id(sdfdsf), ArrayLit([IntegerLit(123), IntegerLit(213), IntegerLit(13), Id(aaa), Id(weew)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt()]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """rewrweuerw: string = 5;"""
        expect = """Program([
	VarDecl(rewrweuerw, StringType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """QuaMonPPL: function auto(aaaaa: string) {
    return "Co cai nit";
}"""
        expect = """Program([
	FuncDecl(QuaMonPPL, AutoType, [Param(aaaaa, StringType)], None, BlockStmt([ReturnStmt(StringLit(Co cai nit))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))