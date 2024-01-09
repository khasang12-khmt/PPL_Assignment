from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl_list EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # flatten first
        flatten = [item for sublist in self.visit(ctx.decl_list()) for item in sublist]
        return Program(flatten)

    # decl_list: decl decl_list | decl;
    def visitDecl_list(self, ctx: MT22Parser.Decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())

    # decl: func | init_stmt;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.func():
            return [self.visit(ctx.func())]
        else:
            return self.visit(ctx.init_stmt())

    # int_list: (INT_LIT | ZERO_LIT) COMMA int_list | (INT_LIT | ZERO_LIT);
    def visitInt_list(self, ctx: MT22Parser.Int_listContext):
        lit = str(ctx.getChild(0).getText())
        if ctx.int_list():
            return [lit] + self.visit(ctx.int_list())
        return [lit]

    ###### TYPES ######

    # vtype: atomic_type | array_type | void_type | auto_type;
    def visitVtype(self, ctx: MT22Parser.VtypeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        if ctx.auto_type():
            return self.visit(ctx.auto_type())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        if ctx.void_type():
            return self.visit(ctx.void_type())

    # atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()

    # array_type: ARRAY LSB int_list RSB OF atomic_type;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        dims = self.visit(ctx.int_list())
        typ = self.visit(ctx.atomic_type())
        return ArrayType(dims, typ)

    # void_type: VOID;
    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return VoidType()

    # auto_type: AUTO;
    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()

    ##### EXPRESSIONS #####

    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        else:
            op = ctx.CONCAT().getText()
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            return BinExpr(op, left, right)

    # expr1: expr2 rel_ops expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        else:
            op = self.visit(ctx.rel_ops())
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinExpr(op, left, right)

    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinExpr(op, left, right)

    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinExpr(op, left, right)

    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinExpr(op, left, right)

    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expr5()))

    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expr6()))

    # expr7: IDENTIFIER idx_ops | LB expr RB | operands;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.operands():
            return self.visit(ctx.operands())
        elif ctx.expr():
            return self.visit(ctx.expr())
        else:
            id = ctx.IDENTIFIER().getText()
            list_exp = self.visit(ctx.idx_ops())
            return ArrayCell(id, list_exp)

    # scalar_variable: IDENTIFIER (idx_ops |);
    def visitScalar_variable(self, ctx: MT22Parser.Scalar_variableContext):
        id = ctx.IDENTIFIER().getText()
        if ctx.idx_ops():
            return ArrayCell(id, self.visit(ctx.idx_ops()))
        return Id(id)

    # expr_list: expr COMMA expr_list | expr;
    def visitExpr_list(self, ctx: MT22Parser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())

    # const: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | bool_lit | array_lit;
    def visitConst(self, ctx: MT22Parser.ConstContext):
        if ctx.ZERO_LIT():
            return IntegerLit(0)
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            f = ctx.FLOAT_LIT().getText()
            if f[0]==".": return FloatLit(float("0"+f))
            return FloatLit(float(f))
        if ctx.STRING_LIT():
            return StringLit(str(ctx.STRING_LIT().getText()))
        if ctx.bool_lit():
            return self.visit(ctx.bool_lit())
        if ctx.array_lit():
            return self.visit(ctx.array_lit())

    # array_lit: LP (expr_list |) RP;
    def visitArray_lit(self, ctx: MT22Parser.Array_litContext):
        if ctx.expr_list():
            return ArrayLit(self.visit(ctx.expr_list()))
        return ArrayLit([])

    # bool_lit: TRUE | FALSE;
    def visitBool_lit(self, ctx: MT22Parser.Bool_litContext):
        return BooleanLit(True) if ctx.TRUE() else BooleanLit(False)

    # rel_ops: EQ | NEQ | GT | GTE | LT | LTE;
    def visitRel_ops(self, ctx: MT22Parser.Rel_opsContext):
        return ctx.getChild(0).getText()

    # idx_ops: LSB expr_list RSB;
    def visitIdx_ops(self, ctx: MT22Parser.Idx_opsContext):
        return self.visit(ctx.expr_list())

    # call_expr: IDENTIFIER LB (expr_list |) RB;
    def visitCall_expr(self, ctx: MT22Parser.Call_exprContext):
        name = ctx.IDENTIFIER().getText()
        if ctx.expr_list():
            return FuncCall(name, self.visit(ctx.expr_list()))
        return FuncCall(name, [])

    # operands: const | variable | LB expr RB | call_expr | IDENTIFIER;
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if ctx.const():
            return self.visit(ctx.const())
        if ctx.variable():
            return self.visit(ctx.variable())
        if ctx.expr():
            return self.visit(ctx.expr())
        if ctx.call_expr():
            return self.visit(ctx.call_expr())
        else:
            return Id(ctx.IDENTIFIER().getText())

    ##### STATEMENTS ######

    # stmt: asm_stmt SEMICOLON | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | call_stmt | return_stmt | block_stmt;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # asm_stmt: scalar_variable ASM expr;
    def visitAsm_stmt(self, ctx: MT22Parser.Asm_stmtContext):
        lhs = self.visit(ctx.scalar_variable())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)

    # block_stmt: LP stmt_list RP;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        stmtlst = self.visit(ctx.stmt_list())
        return BlockStmt(stmtlst)

    # stmt_list: (stmt | init_stmt) stmt_list |;
    def visitStmt_list(self, ctx: MT22Parser.Stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        if ctx.stmt():
            first = [self.visit(ctx.stmt())]
        else:
            first = self.visit(ctx.init_stmt())
        return first + self.visit(ctx.stmt_list())

    # if_stmt: IF LB expr RB stmt (ELSE stmt |);
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        fstmt = self.visit(ctx.stmt(1)) if ctx.stmt(1) else None
        return IfStmt(cond, tstmt, fstmt)

    # for_stmt: FOR LB asm_stmt COMMA expr COMMA expr RB stmt;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        init = self.visit(ctx.asm_stmt())
        cond = self.visit(ctx.expr(0))
        upd = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)

    # while_stmt: WHILE LB expr RB stmt;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)

    # dowhile_stmt: DO block_stmt WHILE LB expr RB SEMICOLON;
    def visitDowhile_stmt(self, ctx: MT22Parser.Dowhile_stmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.block_stmt())
        return DoWhileStmt(cond, stmt)

    # break_stmt: BREAK SEMICOLON;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()

    # continue_stmt: CONTINUE SEMICOLON;
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN (expr |) SEMICOLON;
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    # call_stmt: IDENTIFIER LB (expr_list |) RB SEMICOLON;
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        name = ctx.IDENTIFIER().getText()
        if ctx.expr_list():
            return CallStmt(name, self.visit(ctx.expr_list()))
        return CallStmt(name, [])

    # init_stmt: variable SEMICOLON;
    def visitInit_stmt(self, ctx: MT22Parser.Init_stmtContext):
        return self.visit(ctx.variable())

    ##### DECLARATIONS ########

    # func:
    # 	IDENTIFIER ':' FUNCTION vtype LB (param_list |) RB (
    # 		INHERIT IDENTIFIER
    # 		|
    # 	) block_stmt;
    def visitFunc(self, ctx: MT22Parser.FuncContext):
        name = ctx.IDENTIFIER(0).getText()
        return_type = self.visit(ctx.vtype())
        params = self.visit(ctx.param_list()) if ctx.param_list() else []
        inherit = ctx.IDENTIFIER(1).getText() if ctx.INHERIT() else None
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name, return_type, params, inherit, body)

    # variable:
    # 	id_list ':' vtype (
    # 		ASM value_list_stmt[$id_list.count] (
    # 			{$value_list_stmt.count_diff == 0}?
    # 		)
    # 		|
    # 	);
    def visitVariable(self, ctx: MT22Parser.VariableContext):
        id_list = self.visit(ctx.id_list())
        vtype = self.visit(ctx.vtype())
        if ctx.value_list_stmt():
            value_list = self.visit(ctx.value_list_stmt())
            return [
                VarDecl(id_list[i], vtype, value_list[i])
                for i in range(0, len(id_list))
            ]
        else:
            return [VarDecl(id_list[i], vtype) for i in range(0, len(id_list))]

    # id_list
    # 	returns[count = 0]:
    # 	IDENTIFIER {$count+=1} (COMMA IDENTIFIER {$count+=1})*;
    def visitId_list(self, ctx: MT22Parser.Id_listContext):
        return list(map(lambda x: x.getText(), ctx.IDENTIFIER()))

    # value_list_stmt[count]
    # 	returns[count_diff]:
    # 	expr {$count-=1} ({$count > 0}? COMMA expr {$count-=1})* {$count_diff = $count};
    def visitValue_list_stmt(self, ctx: MT22Parser.Value_list_stmtContext):
        if not ctx.expr():
            return []
        return list(map(lambda x: self.visit(x), ctx.expr()))

    # param: (INHERIT |) (OUT |) IDENTIFIER ':' vtype;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        name = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.vtype())
        return ParamDecl(name, typ, out, inherit)

    # param_list: param COMMA param_list | param;
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.param_list())
