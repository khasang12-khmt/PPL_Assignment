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
                printFloat(b);
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
                printFloat(i);
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
                printFloat(i);
                printInt(i);
            }
        """, 
            """Undeclared Function: printInt""", 
            417))
             
    def test_418(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : auto = "string" :: 2.0;
                printFloat(i);
                printInt(i);
            }
        """, 
            """Type mismatch in expression: BinExpr(::, StringLit(string), FloatLit(2.0))""", 
            418))
             
    def test_419(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                i : auto = 1 + 2;
                j : auto = 1 + 2.0;
                z : auto = (1 == 2) && true;
                printInt(i);
                printFloat(j);
                printBoolean(z);
            }
        """, 
            """Undeclared Function: printInt""", 
            419))
             
    def test_420(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void() {}
            foo1 : function integer(b:auto) inherit goo{
                super(1.0);
                b = a;
                printFloat(a);
                printFloat(b);
            }
            goo : function integer(inherit a: auto) {
                
            }
            main:function void(){}
        """, 
            """""", 
            420))
             
    def test_421(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void() {}
            foo1 : function integer(b:auto, c:auto) inherit goo{
                super(c);
                b = a;
                printFloat(a);
                printFloat(b);
                printFloat(c);
            }
            goo : function integer(inherit a: float){
                
            }
            main:function void(){}
        """, 
            """""", 
            421))
             
    def test_422(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void() {}
            foo1 : function integer(b:auto, c:float) inherit goo{
                super(c);
                b = a;
                printFloat(a);
                printFloat(b);
            }
            goo : function integer(inherit a: auto){
                
            }
            main:function void(){}
        """, 
            """""", 
            422))
             
    def test_423(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void() {}
            foo1 : function integer(b:auto, c:float) inherit goo{
                super({1,2,3});
                e:auto = {{1},{2},{3}};
                b = e;
                printInt(a[0]);
                printInt(b[0,1]);
            }
            goo : function integer(inherit a: auto){
                
            }
            main:function void(){}
        """, 
            """Undeclared Function: printInt""", 
            423))
             
    def test_424(self):
        self.assertTrue(TestChecker.test(
            """
           foo : function void() {}
            foo1 : function integer(b:auto, c:float) inherit goo{
                super({1,2,3});
                goo(b);
                printInt(a[0]);
                printInt(b[0]);
            }
            goo : function integer(inherit a: auto){
                
            }
            main:function void(){}
        """, 
            """Undeclared Function: printInt""", 
            424))
             
    def test_425(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {}
            main:function void(){
                foo();
                a:auto = foo() + 1;
                printInt(foo());
                printInt(a);
            }
        """, 
            """Undeclared Function: printInt""", 
            425))
             
    def test_426(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {}
            main:function void(){
                a : auto = {{1,2},{3,4},{5,foo()}};
                printInt(foo());
            }
        """, 
            """Undeclared Function: printInt""", 
            426))
             
    def test_427(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {}
            main:function void(){
                a : auto = {{{1,2,3},{4,5,6}},{{7,8,9},{9,9,9}},foo()};
                b:auto = foo();
                printInt(b[0,0]);
            }
        """, 
            """Undeclared Function: printInt""", 
            427))
             
    def test_428(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {
                return;
            }
            main:function void(){
                foo();
                a:auto = foo() + 1;
                printInt(foo());
                printInt(a);
            }
        """, 
            """Type mismatch in expression: FuncCall(foo, [])""", 
            428))
             
    def test_429(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {
                return 1.0;
            }
            main:function void(){
                foo();
                a:auto = foo() + 1;
                printFloat(foo());
                printFloat(a);
            }
        """, 
            """""", 
            429))
             
    def test_430(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {
                if(true)
                    return true;
                else 
                    return false;
            }
            main:function void(){
                foo();
                a:auto = foo() && (1==2);
                printBoolean(foo());
                printBoolean(a);
            }
        """, 
            """""", 
            430))
             
    def test_431(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function auto() {
                if(true)
                    return true;
                else 
                    return false;
            }
            main:function void(){
                foo();
                a:auto = foo() && (1==2);
                printBoolean(foo());
                printBoolean(a);
            }
        """, 
            """""", 
            431))
             
    def test_432(self):
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
            432))
             
    def test_433(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a,b:integer;
                a = b;
            }
        """, 
            """""", 
            433))
             
    def test_434(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a = b;
            }
        """, 
            """Undeclared Identifier: b""", 
            434))
             
    def test_435(self):
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
            435))
             
    def test_436(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void() {
                a : auto = {{1,2},{2,3},{3,4}};
                b:auto = a;
                b[0,0] = 1;
                b[1] = 1;
            }
        """, 
            """Type mismatch in statement: AssignStmt(ArrayCell(b, [IntegerLit(1)]), IntegerLit(1))""", 
            436))
             
    def test_437(self):
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
            437))
             
    def test_438(self):
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
            438))
             
    def test_439(self):
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
            439))
             
    def test_440(self):
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
            440))
             
    def test_441(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                break;
            }
        """, 
            """Must in loop: BreakStmt()""", 
            441))
             
    def test_442(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                continue;
            }
        """, 
            """Must in loop: ContinueStmt()""", 
            442))
             
    def test_443(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                if(true)
                    break;
            }
        """, 
            """Must in loop: BreakStmt()""", 
            443))
             
    def test_444(self):
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
            444))
             
    def test_445(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                while(true)
                    break;
                while(true)
                    continue;
                while(true) {
                    break;
                    continue;
                }
            }
        """, 
            """""", 
            445))
             
    def test_446(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                do {
                    break;
                    break;
                    continue;
                } while(true);
            }
        """, 
            """""", 
            446))
             
    def test_447(self):
        self.assertTrue(TestChecker.test(
            """
            main: function void() {
                i : integer;
                for(i = 0, i < 10, i+1) 
                    break;
                for(i = 0, i < 10, i+1) 
                    continue;
                for(i = 0, i < 10, i+1) {
                    break;
                    continue;
                } 
            }
        """, 
            """""", 
            447))
             
    def test_448(self):
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
            448))
             
    def test_449(self):
        self.assertTrue(TestChecker.test(
            """
            main : function integer () {
                a : auto = {{{{1,2,3,4}},{{1,2,3,4}},{{1,2,3,4}}}};
            }
        """, 
            """No entry point""", 
            449))
             
    def test_450(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {1,2,{3}};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3)])])""", 
            450))
             
    def test_451(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {1,2,3.0};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.0)])""", 
            451))
             
    def test_452(self):
        self.assertTrue(TestChecker.test(
            """

            main:function void() {
                a : auto = {{1,4},{2,{4}},{3,4}};
                return;
            }
        """, 
            """Illegal array literal: ArrayLit([IntegerLit(2), ArrayLit([IntegerLit(4)])])""", 
            452))
             
    def test_453(self):
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
            453))
             
    def test_454(self):
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
            454))
             
    def test_455(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a : auto = {{1,2},{3,4},{3.0,4}};
            }
        """, 
            """Illegal array literal: ArrayLit([FloatLit(3.0), IntegerLit(4)])""", 
            455))
             
    def test_456(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(){
                a : auto = {{1,2},{3,4},{3.0,4}};
            }
        """, 
            """Illegal array literal: ArrayLit([FloatLit(3.0), IntegerLit(4)])""", 
            456))
             
    def test_457(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super();
            }
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            457))
             
    def test_458(self):
        print(458)
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                break;
            }
            goo:function integer() {}
            main:function void() {}
        """, 
            """Must in loop: BreakStmt()""", 
            458))
             
    def test_459(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                break;
            }
            goo:function integer(a : integer) {}
            main:function void() {}
        """, 
            """Invalid statement in function: foo""", 
            459))
             
    def test_460(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super();
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: """, 
            460))
             
    def test_461(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: """, 
            461))
             
    def test_462(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1,2,3);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: IntegerLit(3)""", 
            462))
             
    def test_463(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                super(1,2.0);
            }
            goo:function integer(inherit a:integer, inherit b: integer) {}
            main:function void() {}
        """, 
            """Type mismatch in expression: FloatLit(2.0)""", 
            463))
             
    def test_464(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{
                preventDefault();
            }
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            464))
             
    def test_465(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer(a:integer) inherit goo{
                preventDefault();
            }
            goo:function integer(inherit a:integer) {}
            main:function void() {}
        """, 
            """Invalid Parameter: a""", 
            465))
             
    def test_466(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer() inherit goo{}
            goo:function integer() {}
            main:function void() {}
        """, 
            """""", 
            466))
             
    def test_467(self):
        self.assertTrue(TestChecker.test(
            """
            foo:function integer(){}
        """, 
            """No entry point""", 
            467))
             
    def test_468(self):
        self.assertTrue(TestChecker.test(
            """
            main:function integer(){}
        """, 
            """No entry point""", 
            468))
             
    def test_469(self):
        self.assertTrue(TestChecker.test(
            """
            main:function void(a:integer){}
        """, 
            """No entry point""", 
            469))
             
    def test_470(self):
        self.assertTrue(TestChecker.test(
            """
            foo : function void (inherit a:integer) {}
            main: function void() inherit foo{
                super(1);
            }
        """, 
            """""", 
            470))
        
    def test71(self):
        print(471)
        input= """
        x: integer = 1;
        a,b,c: auto = true,false,true;
        z: array [2] of boolean = {a,b};
        t: array [3] of boolean = {z[1],z[2],c};
        foo: function auto(inherit a: auto, b:auto){
            h : auto = a == 1;
            b = true != b;
            return h;
        }
        k: auto = foo(x,z[1]);
        bar: function void(c: float, b: auto, d: auto) inherit foo{
            super(x,b);
            n: auto = foo(d,b);
            n = n && b ;
            c = c + a;
        }
        inc: function auto(){
            return 1.1;
        }
        main: function void(){
            x = readInteger();
            printInteger(x);
            bar(x,true,run(12));
            x = x + inc();
        }
        """
        output= "Undeclared Function: run"
        
        self.assertTrue(TestChecker.test(input, output, 471))
    
    def test72(self):
        input= """
        x: integer = 1;
        a,b,c: auto = true,false,true;
        z: array [2] of boolean = {a,b};
        t: array [3] of boolean = {z[1],z[2],c};
        foo: function auto(inherit a: auto, b:auto){
            h : auto = a == 1;
            b = true != b;
            return h;
        }
        k: auto = foo(x,z[1]);
        bar: function void(c: float, b: auto, d: auto) inherit foo{
            super(x,b);
            n: auto = foo(d,b);
            n = n && b ;
            c = c + a;
        }
        inc: function auto(){
            return 1.1;
        }
        readInteger: function integer (printFloat: float){
            return 1;
        }
        main: function void(){
            x = readInteger();
            printInteger(x);
            bar(x,true,run(12));
            x = x + inc();
        }
        """
        output= "Redeclared Function: readInteger"
        
        self.assertTrue(TestChecker.test(input, output, 472))
    
    def test73(self):
        input= """
        x: integer = 1;       
        printString: function integer (printFloat: float){
            return 1;
        }
        main: function void(){
            x = readInteger();
            printInteger(x);
            bar(x,true,run(12));
            x = x + inc();
        }
        """
        output= "Redeclared Function: printString"
        
        self.assertTrue(TestChecker.test(input, output, 473))
    
    def test74(self):
        input= """
        x: integer = 1;       
        foo: function integer (printFloat: float){
            return 1;
        }
        main: function void(){
            x = readInteger();
            printInteger(x);
            bar(x,true,run(12));
            x = x + inc();
        }
        """
        output= "Undeclared Function: bar"
        
        self.assertTrue(TestChecker.test(input, output, 474))
    
    def test75(self):
        input= """
        x: integer = 1;      
        printBoolean: auto = 1.1; 
        foo: function integer (printFloat: float){
            return 1;
        }
        main: function void(){
            x = readInteger();
            printInteger(x);
            bar(x,true,run(12));
            x = x + inc();
        }
        """
        output= "Redeclared Variable: printBoolean"
        
        self.assertTrue(TestChecker.test(input, output, 475))
    
    def test76(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            if(a>1){
                return a;
            }
            else{
                a: float = 1.0;
                return a;
            }
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Type mismatch in statement: ReturnStmt(Id(a))"
        
        self.assertTrue(TestChecker.test(input, output, 476))
    
    def test77(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a = 5.0;
            }
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.0))"
        
        self.assertTrue(TestChecker.test(input, output, 477))
    
    def test78(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a: float;
                a = 5.0;
            }
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Undeclared Identifier: z"
        
        self.assertTrue(TestChecker.test(input, output, 478))
    
    def test79(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a: float;
                a = 5.0;
            }
            a = 5.0;
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.0))"
        
        self.assertTrue(TestChecker.test(input, output, 479))
    
    def test80(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a: float;
                a = 5.0;
            }
            if(a >=b){
                continue;
            }
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Must in loop: ContinueStmt()"
        
        self.assertTrue(TestChecker.test(input, output, 480))
    
    def test81(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a: float;
                a = 5.0;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                b = b+1;
            }
        }
        k: auto = foo(x,z[1]);
        main: function void(){
           
        }
        """
        output= "Type mismatch in expression: BinExpr(+, Id(b), IntegerLit(1))"
        
        self.assertTrue(TestChecker.test(input, output, 481))
    
    def test82(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            for(x=1, x != a , x/2){
                continue;
                a: float;
                a = 5.0;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
           
        }
        """
        output= ""
        
        self.assertTrue(TestChecker.test(input, output, 482))
    
    def test83(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            
            for(i=1, i != a , i/2){
                continue;
                a: float;
                a = 5.0;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
        }
        """
        output= "Undeclared Identifier: i"
        
        self.assertTrue(TestChecker.test(input, output, 483))
    
    def test84(self):
        input= """
        x: integer = 1;      
        foo: function auto(inherit a: auto, b:auto){
            i : float ;
            for(i=1, i != a , i/2){
                continue;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
        }
        """
        output= "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(!=, Id(i), Id(a)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([ContinueStmt()]))"
        
        self.assertTrue(TestChecker.test(input, output, 484))
    
    def test85(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: auto, b:auto){
            i : float ;
            for(arr[2]=1, i != a , i/2){
                continue;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
        }
        """
        output= "Type mismatch in expression: BinExpr(!=, Id(i), Id(a))"
        
        self.assertTrue(TestChecker.test(input, output, 485))
    
    def test86(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: auto, b:auto){
            i : float ;
            for(arr[2]=1, arr[2] != a , x/2){
                continue;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
        }
        """
        output= ""
        
        self.assertTrue(TestChecker.test(input, output, 486))
    
    def test87(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: auto, b:auto){
            i : float ;
            for(arr[2]=1, arr[2] != a , i/2){
                continue;
            }
            if(a >=b){
                b= b*a-x;
                b: boolean;
                b= true;
                return b;
            }
        }
        k: auto = foo(x,1);
        main: function void(){
        }
        """
        output= "Type mismatch in statement: ForStmt(AssignStmt(ArrayCell(arr, [IntegerLit(2)]), IntegerLit(1)), BinExpr(!=, ArrayCell(arr, [IntegerLit(2)]), Id(a)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([ContinueStmt()]))"
        
        self.assertTrue(TestChecker.test(input, output, 487))
    
    def test88(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: integer, b:float){
        }
        k: auto = foo(x,1);
        main: function void(){
            foo(1);
        }
        """
        output= "Type mismatch in statement: CallStmt(foo, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, output, 488))
    
    def test89(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: integer, b:float){
        }
        k: auto = foo(x,1);
        main: function void(){
            foo(1,true);
        }
        """
        output= "Type mismatch in statement: CallStmt(foo, IntegerLit(1), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, output, 489))
    
    def test90(self):
        input= """
        x: integer = 1;     
        arr : array[2] of integer; 
        foo: function auto(inherit a: integer, b:float){
        }
        k: auto = foo(x,1);
        main: function void(){
            foo(1,1,12);
        }
        """
        output= "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(1), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, output, 490))
    
    def test91(self):
        input= """
        inc : function void (out n : integer, a:float) inherit foo{
            
        } 
        foo : function auto (){}
        main: function void (){}
        """
        output= ""
        self.assertTrue(TestChecker.test(input, output, 491))
    
    def test92(self):
        print(492)
        input= """
        inc : function void (out n : integer, a:float) inherit foo{
            
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Invalid statement in function: inc"
        self.assertTrue(TestChecker.test(input, output, 492))
    
    def test93(self):
        input= """
        bar: function auto (out a: auto, out b:boolean){
            if (a&&b){
                return;
            }
            else{
                return b;
            }
        }
        inc : function auto (out n : integer, a:float) inherit foo{
            
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, output, 493))
    
    def test94(self):
        input= """
        bar: function auto (out a: auto, out b:boolean){
            if (a&&b){
                return;
            }
            return 1;
        }
        inc : function auto (out n : integer, a:float) inherit foo{
            super(1);
            n = bar(true,true);
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, output, 494))
    
    def test95(self):
        input= """
        bar: function float (out a: auto, out b:boolean){
            if (a&&b){
                return;
            }
            return 1;
        }
        inc : function auto (out n : integer, a:float) inherit foo{
            super(1);
            n = bar(true,true);
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, output, 495))
    
    def test96(self):
        print(496)
        input= """
        inc : function auto (out n : integer, a:float) inherit foo{
            super(1);
        } 
        super: function void(){}
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Redeclared Function: super"
        self.assertTrue(TestChecker.test(input, output, 496))
    
    def test97(self):
        input= """
        inc : function auto (out n : integer, a:float) inherit foo{
            super(1);
            {
                n: float=foo(2);
                m: boolean = true;
            }
            m = m&&true;
            return foo(2);
        } 
        super: function void(){}
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= "Type mismatch in expression: BinExpr(&&, Id(m), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, output, 497))
    
    def test98(self):
        input= """
        inc : function auto (out n : integer, a:float) inherit foo{
            super(1);
            {
                n: float=foo(2);
                m: boolean = true;
            }
            m = m+n;
            return foo(2);
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= ""
        self.assertTrue(TestChecker.test(input, output, 498))
    
    def test99(self):
        print(499)
        input= """
        inc : function auto (out n : integer, a:float) inherit foo{
            preventDefault();
            {
                n: float=foo(2);
                m: boolean = true;
            }
            printFloat(m);
            printInteger(n);
            m = m+n;
            return foo(2);
        } 
        foo : function auto (inherit m: float){}
        main: function void (){}
        """
        output= ""
        self.assertTrue(TestChecker.test(input, output, 499))
    
    def test100(self):
        input= """
        inc : function auto (out n : integer, a:float) inherit foo{
            preventDefault();
            {
                n: float=foo(2);
                m: boolean = true;
            }
            return foo(2);
        } 
        foo : function auto (inherit m: float){}
        main: function void (){
            hihi : float = foo(foo(2));
        }
        """
        output= ""
        self.assertTrue(TestChecker.test(input, output, 500))
    

            