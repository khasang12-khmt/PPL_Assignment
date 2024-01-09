import unittest
from TestUtils import TestChecker
from AST import *
class CheckerSuite(unittest.TestCase): 
    def test_401(self):
        self.assertTrue(TestChecker.test(
            """
            a : integer;
            main: function void() {
                a : integer;
                b : float = 1;
            }
            a:function void() {}
        """, 
            """Redeclared Function: a""", 
            401))
             
    def test_402(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {}
            a : auto = {1,foo()};
            main: function void() {}
        """, 
            """""", 
            402))
             
    def test_403(self):
        self.assertTrue(TestChecker.test(
            """
            a,b,c : float = 1,2,3;
            main: function void() {
                b : integer;
                a:float = 1;
                writeFloat(b);
            }
        """, 
            """""", 
            403))
             
    def test_404(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i:integer;
                for(i = 1, i < 10, i + 1) {
                    i = 1;
                }
            }
        """, 
            """""", 
            404))
             
    def test_405(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i:integer;
                for(i = 1, i < 10, i + 1) {
                    i = 1;
                }
            }
        """, 
            """""", 
            405))
             
    def test_406(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a : integer = 2;
                a : integer = 1;
            }
        """, 
            """Redeclared Variable: a""", 
            406))
             
    def test_407(self):
        self.assertTrue(TestChecker.test(
            """
            a : function void() {}
            a : integer;
            main:function void(){}
        """, 
            """Redeclared Variable: a""", 
            407))
             
    def test_408(self):
        self.assertTrue(TestChecker.test(
            """
            a : integer;
            a : float;
            a : function void() {}
            main:function void(){}
        """, 
            """Redeclared Variable: a""", 
            408))
             
    def test_409(self):
        self.assertTrue(TestChecker.test(
            """
            a : function integer() {}
            a : function void() {}
            main:function void(){}
        """, 
            """Redeclared Function: a""", 
            409))
             
    def test_410(self):
        self.assertTrue(TestChecker.test(
            """
            a : function integer() {}
            b : function void() {}
            c : function void() {}
            e : function void() {} 
            a : function void() {}
            main:function void(){}
        """, 
            """Redeclared Function: a""", 
            410))
             
    def test_411(self):
        self.assertTrue(TestChecker.test(
            """
            a : function void(a:integer, b:float, e: float, a:float, g: float ) {}
            main:function void(){}
        """, 
            """Redeclared Parameter: a""", 
            411))
             
    def test_412(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                
                for(i = 1, i < 10, i + 1) {
                    i = 1;
                }
            }
        """, 
            """Undeclared Identifier: i""", 
            412))
             
    def test_413(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a:auto = readString();
                printString(a);
                foo();
            }
        """, 
            """Undeclared Function: foo""", 
            413))
             
    def test_414(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a:auto = readString();
                printString(a);
            }
            goo:function auto(inherit a:integer) inherit foo {}
        """, 
            """Undeclared Function: foo""", 
            414))
             
    def test_415(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a:auto = readString();
                printString(b);
            }
            goo:function auto(inherit a:integer) inherit foo {}
        """, 
            """Undeclared Identifier: b""", 
            415))
             
    def test_416(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : auto = "string" + 2.0;
                writeFloat(i);
                printInt(i);
            }
        """, 
            """Type mismatch in expression: BinExpr(+, StringLit(string), FloatLit(2.0))""", 
            416))
             
    def test_417(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : auto = 1 + 2.0;
                writeFloat(i);
                printInteger(i);
            }
        """, 
            """Type mismatch in statement: CallStmt(printInteger, Id(i))""", 
            417))
             
    def test_418(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function auto() {}
            main: function void() {
                a : auto = {{1,2,3},{4,5,6},{7,8,9}};
                a[foo()] = a[1];
            }
            a:function void() {}
        """, 
            """Type mismatch in statement: AssignStmt(ArrayCell(a, [FuncCall(foo, [])]), ArrayCell(a, [IntegerLit(1)]))""", 
            418))
             
    def test_419(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a,b:integer;
                a = b;
            }
        """, 
            """""", 
            419))
             
    def test_420(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a = b;
            }
        """, 
            """Undeclared Identifier: b""", 
            420))
             
    def test_421(self):
        self.assertTrue(TestChecker.test(
            """
            goo: function auto() {}
            foo : function auto(b:auto) {
                b = 1;
                b = "string";
            }
            main:function void() {
                return;
            }
        """, 
            """Type mismatch in statement: AssignStmt(Id(b), StringLit(string))""", 
            421))
             
    def test_422(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : float;
                for(i = 1, i < 10, i + 1) {
                    i = 1;
                }
            }
        """, 
            """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(1))]))""", 
            422))
             
    def test_423(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : float;
                for(i = 1, i + 10, i + 1) {
                    i = 1;
                }
            }
        """, 
            """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(1))]))""", 
            423))
             
    def test_424(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : float;
                for(i = 1, i < 10, i < 1) {
                    i = 1;
                }
            }
        """, 
            """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(1))]))""", 
            424))
             
    def test_425(self):
        self.assertTrue(TestChecker.test(
            """
        a : array[2,3,2] of integer = {{{1,2},{3,4},{5,6}},{{7,8},{9,10},{11,12}}};
        a_: array[1,2] of boolean = {{1,2}};
        b : auto = a[1,2,3];
        c : float = b + 1;
        d : boolean = (!true == 2) || (1 < 2);
        foo: function void (a:integer) inherit goo {
            i : integer;
            for (a_[0,0] = 0, i < 10, i + 1) {break;}
            while(i == 0) {
                if(i == 1) {
                    break;
                }
            }

        }
        goo: function void () {}""", 
            """Type mismatch in Variable Declaration: VarDecl(a_, ArrayType([1, 2], BooleanType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)])]))""", 
            425))
             
    def test_426(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                break;
            }
        """, 
            """Must in loop: BreakStmt()""", 
            426))
             
    def test_427(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                continue;
            }
        """, 
            """Must in loop: ContinueStmt()""", 
            427))
             
    def test_428(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                if(true)
                    break;
            }
        """, 
            """Must in loop: BreakStmt()""", 
            428))
             
    def test_429(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                if(true) {
                     {
                        break;
                     }
                }
            }
        """, 
            """Must in loop: BreakStmt()""", 
            429))
             
    def test_430(self):
        self.assertTrue(TestChecker.test(
            """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a : auto = {{1,2},{goo(),4},{3,4}, b};
                a[4,goo()] = 1;
                return;
            }
            main:function void() {
                return;
            }
        """, 
            """""", 
            430))
             
    def test_431(self):
        self.assertTrue(TestChecker.test(
            """
            main : function integer () {
                a : auto = {{{{1,2,3,4}},{{1,2,3,4}},{{1,2,3,4}}}};
            }
        """, 
            """No entry point""", 
            431))
             
    def test_432(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {1,2,{3}};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3)])])""", 
            432))
             
    def test_433(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {1,2,3.0};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.0)])""", 
            433))
             
    def test_434(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {{1,4},{2,{4}},{3,4}};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(2), ArrayLit([IntegerLit(4)])])""", 
            434))
             
    def test_435(self):
        self.assertTrue(TestChecker.test(
            """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a : auto = {{1,2},{goo(),4},{3,4}, b};
                a[0,0] = 1;
                return;
            }
            main:function void() {
                return;
            }
        """, 
            """""", 
            435))
             
    def test_436(self):
        self.assertTrue(TestChecker.test(
            """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a : auto = {{1,2},{goo(),4},{3,4}, b};
                a[0] = 1;
                return;
            }
            main:function void() {
                return;
            }
        """, 
            """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(1))""", 
            436))
             
    def test_437(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a : auto = {{1,2},{3,4},{3.0,4}};
            }
        """, 
            """Illegal array literal: ArrayLit([FloatLit(3.0), IntegerLit(4)])""", 
            437))
             
    def test_438(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a : auto = {{1,2},{3,4},{3.0,4}};
            }
        """, 
            """Illegal array literal: ArrayLit([FloatLit(3.0), IntegerLit(4)])""", 
            438))
             
    def test_439(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super();
            }
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            439))
             
    def test_440(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super();
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: """, 
            440))
             
    def test_441(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: """, 
            441))
             
    def test_442(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1,2,3);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: IntegerLit(3)""", 
            442))
             
    def test_443(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1,2.0);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: FloatLit(2.0)""", 
            443))
             
    def test_444(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                preventDefault();
            }
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            444))
             
    def test_445(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer(a:integer) inherit goo{
                preventDefault();
            }
            goo:function integer(inherit a:integer) {}
            main:function void() {}
        """, 
            """Invalid Parameter: a""", 
            445))
             
    def test_446(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{}
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            446))
             
    def test_447(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer(){}
        """, 
            """No entry point""", 
            447))
             
    def test_448(self):
        self.assertTrue(TestChecker.test(
            """
            main:function integer(){}
        """, 
            """No entry point""", 
            448))
             
    def test_449(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(a:integer){}
        """, 
            """No entry point""", 
            449))
             
    def test_450(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void (inherit a:integer) {}
            main: function void() inherit foo{
                super(1);
            }
        """, 
            """""", 
            450))
            