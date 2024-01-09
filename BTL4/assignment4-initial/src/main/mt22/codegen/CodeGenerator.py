from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, value_init=None,inherit=None,out=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.value_init = value_init
        self.inherit = inherit
        self.out = out

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) +"," + str(self.value) +"," + str(self.value_init) + "," + str(self.inherit) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()],VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()],VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()],VoidType()), CName(self.libName)),
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value


class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class PremCodeGenVisitor(Visitor):
    def __init__(self, astTree, env):
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"

    def visitProgram(self, ast, c):
        e = SubBody(None, self.env)
        for x in ast.decls:
            if type(x) is FuncDecl:
                e = self.visit(x, e)
        self.env = e
        return c

    def visitFuncDecl(self, ast, o):
        o.sym = [Symbol(ast.name, MType([(x.typ,x.name,x.inherit,x.out) for x in ast.params], ast.return_type), CName(self.className), None, ast.inherit)] + o.sym
        return SubBody(None, o.sym)
    
    
class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        
    def getDefaultAtomicData(self,typ):
        if type(typ) is IntegerType: return IntegerLit(0)
        if type(typ) is StringType: return StringLit("")
        if type(typ) is FloatType: return FloatLit(0.0)
        if type(typ) is BooleanType: return BooleanLit(False)
        if type(typ) is ArrayType: return ArrayLit([self.getDefaultAtomicData(typ.typ)])
        

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        premenv = PremCodeGenVisitor(self.astTree,self.env)
        premenv.visit(self.astTree,self.env)
        e = SubBody(None, premenv.env.sym)
        for x in ast.decls:
            e = self.visit(x, e)
        # e.sym now contains only global_var
        # e.sym = list(filter(lambda x: type(x.mtype) is not MType, e.sym))
        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", None, list(), None,BlockStmt([])), c, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl("<clinit>", None, list(), None,BlockStmt([])), e, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.name == "<init>"
        isClinit = consdecl.name == "<clinit>"
        isMain = str(consdecl.name) == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        return_type = VoidType() if isInit or isClinit else consdecl.return_type
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType([0], StringType())] if isMain else list(map(lambda x: x.typ, consdecl.params))
        mtype = MType(intype, return_type)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for other declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isClinit:
            for global_var in o.sym:
                if hasattr(global_var.mtype,"rettype"): continue # skip functions
                init = global_var.value_init if global_var.value_init else self.getDefaultAtomicData(global_var.mtype)
                code_value_init, type_value_init = self.visit(init, Access(frame, o.sym, False, False)) 
                code = code_value_init
                code += self.emit.emitI2F(o.frame) if (isinstance(global_var.mtype, FloatType) and isinstance(type_value_init, IntegerType)) else ""
                code += self.emit.emitPUTSTATIC(self.className + "." + global_var.name, global_var.mtype, frame)
                self.emit.printout(code)
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                [0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            if consdecl.params:
                local = reduce(lambda env, ele: SubBody(
                    frame, [self.visit(ele, env)]+env.sym), consdecl.params, SubBody(frame, []))
                glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            
        env = SubBody(frame, glenv)
        retCheck = False
        for stmtdecl in body.body:
            if type(stmtdecl) is VarDecl:
                env = self.visit(stmtdecl, env)
            elif type(stmtdecl) is ReturnStmt:
                retCheck = True
                for x in consdecl.params:
                    if x.out:
                        self.visit(AssignStmt(ArrayCell(consdecl.name+"_"+x.name,[IntegerLit(0)]),Id(x.name)),env)
                self.visit(stmtdecl, env)
            else:
                self.visit(stmtdecl, env)
        if not retCheck:
            for x in consdecl.params:
                if x.out:
                    self.visit(AssignStmt(ArrayCell(consdecl.name+"_"+x.name,[IntegerLit(0)]),Id(x.name)),env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(return_type) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.return_type)
        for x in ast.params:
            if x.out:
                self.visit(VarDecl(ast.name+"_"+x.name,ArrayType([1],x.typ),self.getDefaultAtomicData(ArrayType([1],x.typ))),o)
        o.sym = [Symbol(ast.name, MType([(x.typ,x.name,x.inherit,x.out) for x in ast.params], ast.return_type), CName(self.className), None, ast.inherit)] + o.sym
        self.genMETHOD(ast, o.sym, frame)
        return SubBody(None, o.sym)
    
    def visitParamDecl(self, ast, o):
        code = None
        if o.frame:
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index,ast.name.lower(),ast.typ,o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame))
            code = SubBody(o.frame, [Symbol(ast.name.lower(),ast.typ,Index(index),None,ast.inherit)]+o.sym)
        return code

    def visitVarDecl(self, ast, o):
        code = None
        if o.frame: #local
            index = o.frame.getNewIndex()
            o.sym = [[Symbol(ast.name,ast.typ,Index(index))]] + o.sym
            self.emit.printout(self.emit.emitVAR(index,ast.name,ast.typ,o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame))
            code = SubBody(o.frame, o.sym)
            if not ast.init and type(ast.typ) is ArrayType:
                # self-generate ast.init from ast.typ.dimensions
                def generate(dimensions):
                    if len(dimensions) == 1:
                        return ArrayLit([self.getDefaultAtomicData(ast.typ.typ) for _ in range(int(dimensions[0]))])
                    else:
                        return ArrayLit([generate(dimensions[1:]) for _ in range(int(dimensions[0]))])
                init = generate(ast.typ.dimensions)
                self.visit(AssignStmt(Id(ast.name),init),o)
            if ast.init:
                self.visit(AssignStmt(Id(ast.name),ast.init),o)
        else: #global
            o.sym = [Symbol(ast.name,ast.typ,CName(self.className), ast.init if ast.init else self.getDefaultAtomicData(ast.typ))] + o.sym
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name,ast.typ,False,""))
            code = SubBody(None, o.sym)
        return code
    
    def visitAssignStmt(self, ast, o):
        array_cell, data_type = (self.visit(ast.lhs, (Access(o.frame, o.sym, True, True), ast.rhs))) if isinstance(ast.lhs, ArrayCell) else ("", VoidType())
        if array_cell != "":
            self.emit.printout(array_cell)
            return o
        right,righttyp = self.visit(ast.rhs,Access(o.frame, o.sym, False))
        left,lefttyp = self.visit(ast.lhs,Access(o.frame, o.sym, True))
        self.emit.printout(right)
        if isinstance(righttyp, IntegerType) and isinstance(lefttyp, FloatType):
            self.emit.printout(self.emit.emitI2F(o.frame))
        self.emit.printout(left)
        return o
        
    def visitBlockStmt(self, ast, o):
        for inst in ast.body:
            self.visit(inst, o)
    
    def visitIfStmt(self, ast, o):
        #expr
        exp_c, exp_t = self.visit(ast.cond, Access(o.frame,o.sym,False,True))
        self.emit.printout(exp_c)
        
        #fLabel
        fLabel = o.frame.getNewLabel()
        # skip to fLabel if False
        self.emit.printout(self.emit.emitIFFALSE(fLabel,o.frame))
        # tstmt
        self.visit(ast.tstmt,o)
        # fstmt 
        if ast.fstmt is None:
            # put fLabel here
            code = self.emit.emitLABEL(fLabel,o.frame)
            self.emit.printout(code)
        else:
            # eLabel
            eLabel = o.frame.getNewLabel()
            # skip to eLabel
            code = self.emit.emitGOTO(eLabel,o.frame)
            self.emit.printout(code)
            # put fLabel here
            code = self.emit.emitLABEL(fLabel,o.frame)
            self.emit.printout(code)
            # estmt
            self.visit(ast.fstmt,o)
            # put eLabel here
            code = self.emit.emitLABEL(eLabel,o.frame)
            self.emit.printout(code)
            
    def visitForStmt(self, ast, o):
        # Initial
        self.visit(ast.init, o)
        
        # -> Loop
        o.frame.enterLoop()
        
        # Labels
        conLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()
        chkLabel, bodyLabel,updLabel = o.frame.getNewLabel(),o.frame.getNewLabel(),o.frame.getNewLabel()
        
        # Condition Check
        self.emit.printout(self.emit.emitLABEL(chkLabel, o.frame))
        ccode,ctyp = self.visit(ast.cond, Access(o.frame, o.sym, False, True))
        self.emit.printout(ccode)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel,o.frame))
        
        # Body
        self.emit.printout(self.emit.emitLABEL(bodyLabel, o.frame))
        self.visit(ast.stmt,o)
        
        ## Put Continue: Update->Check Cond
        self.emit.printout(self.emit.emitLABEL(conLabel,o.frame))
        
        # Update
        self.emit.printout(self.emit.emitLABEL(updLabel, o.frame))
        self.visit(AssignStmt(ast.init.lhs,ast.upd),o)
        self.emit.printout(self.emit.emitGOTO(chkLabel,o.frame))
        
        ## Put Break
        self.emit.printout(self.emit.emitLABEL(brkLabel,o.frame))
        
        # <- Loop
        o.frame.exitLoop()
    
    def visitWhileStmt(self, ast, o):
        o.frame.enterLoop()
        # cont, break
        cntLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()
        # Put cont
        code = self.emit.emitLABEL(cntLabel, o.frame)
        self.emit.printout(code)
        # expr
        ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(ec)
        # break if False
        code = self.emit.emitIFFALSE(brkLabel, o.frame)
        self.emit.printout(code)
        # stmt
        self.visit(ast.stmt,o)
        # Jump to cont
        code = self.emit.emitGOTO(cntLabel, o.frame)
        self.emit.printout(code)
        # Put break
        code = self.emit.emitLABEL(brkLabel, o.frame)
        self.emit.printout(code)
        # exit
        o.frame.exitLoop()
    
    def visitDoWhileStmt(self, ast, o):
        o.frame.enterLoop()
        # cont, break
        cntLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()
        
        # Put cont
        code = self.emit.emitLABEL(cntLabel, o.frame)
        self.emit.printout(code)
        
        # stmt
        self.visit(ast.stmt,o)
        
        # expr
        ec, et = self.visit(ast.cond, Access(o.frame, o.sym, False))
        self.emit.printout(ec)
        # break if False
        code = self.emit.emitIFFALSE(brkLabel, o.frame)
        self.emit.printout(code)
        
        # Jump to cont
        code = self.emit.emitGOTO(cntLabel, o.frame)
        self.emit.printout(code)
        # Put break
        code = self.emit.emitLABEL(brkLabel, o.frame)
        self.emit.printout(code)
        # exit
        o.frame.exitLoop()
    
    def visitCallStmt(self, ast, o):
        astt = o
        frame = astt.frame
        nenv = astt.sym
        sym = None
        isSuper = ast.name == "super"
        
        #print("ct",ast.name,[sym for sym in o.sym])
        #print("ctf",o.sym[1].sym.mtype.partype)
        
        # Find Parent Function (Super/ Prevent Default)
        if ast.name == "preventDefault": return
        if isSuper: ast.name = o.sym[1].inherit
        
        for symbol in o.sym:
            if isinstance(symbol,SubBody): continue
            if isinstance(symbol,list): # local
                sym = list(filter(lambda x: x.name==ast.name,symbol))
                if sym != []: 
                    sym = sym[0]
                    break
                else: sym = None
            elif symbol.name == ast.name:
                sym = symbol
                break
        
        # Inheritance
        if isSuper:
            for idx,par in enumerate(sym.mtype.partype):
                if par[2]:
                    self.visit(VarDecl(par[1],par[0],ast.args[idx]),o)
        else:
            cname = sym.value.value
            inputtyp = None
            ctype = sym.mtype
            if type(ctype) is MType:
                inputtyp = ctype.partype
            in_ = ("", list())
            for i,x in enumerate(ast.args):
                str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
                if inputtyp:
                    paramtyp = inputtyp[i] if type(inputtyp[i]) is not tuple else inputtyp[i][0]
                    if type(paramtyp) is FloatType and type(typ1) is IntegerType:
                        str1 = str1 + self.emit.emitI2F(frame)
                in_ = (in_[0] + str1, in_[1]+[typ1])
            self.emit.printout(in_[0])
            self.emit.printout(self.emit.emitINVOKESTATIC(
                cname + "/" + ast.name, ctype, frame))
            
            for i,x in enumerate(sym.mtype.partype):
                if(type(x) is tuple and x[3]):
                    self.visit(AssignStmt(ast.args[i],ArrayCell(ast.name+"_"+x[1],[IntegerLit(0)])),o)

    def visitBreakStmt(self, ast, o):
        return self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    
    def visitContinueStmt(self, ast, o):
        return self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
    
    def visitReturnStmt(self, ast, o):
        if ast.expr:
            code,typ = self.visit(ast.expr,Access(o.frame,o.sym,False,True))
            if type(typ) is IntegerType and type(o.frame.returnType) is FloatType:
                code += self.emit.emitI2F(o.frame) + self.emit.emitRETURN(FloatType(),o.frame)
            else:
                code += self.emit.emitRETURN(typ, o.frame)
            self.emit.printout(code)
    
    def visitUnExpr(self, ast, o):
        code, typ = self.visit(ast.val,o)
        if type(typ) is MType: typ = typ.rettype
        if ast.op == "!": return code + self.emit.emitNOT(typ, o.frame), typ
        else: return code + self.emit.emitNEGOP(typ, o.frame), typ
        
    def visitBinExpr(self, ast, o):
        ret,op = None,None
        left, lefttyp = self.visit(ast.left,o)
        right, righttyp = self.visit(ast.right,o)
        if type(lefttyp) is MType: lefttyp = lefttyp.rettype
        if type(righttyp) is MType: righttyp = righttyp.rettype
        
        if isinstance(lefttyp, FloatType) or isinstance(righttyp, FloatType):
            if type(lefttyp) is IntegerType:
                left = left+self.emit.emitI2F(o.frame)
            elif type(righttyp) is IntegerType:
                right = right+self.emit.emitI2F(o.frame)
            ret = FloatType()
        else:
            ret = lefttyp
        
        if ast.op in ['+','-']:
            op = self.emit.emitADDOP(ast.op,ret,o.frame)
        elif ast.op in ['*','/']:
            op = self.emit.emitMULOP(ast.op,ret,o.frame)
        elif ast.op in ['%']:
            op = self.emit.emitMOD(o.frame)
        elif ast.op in ['&&']:
            op = self.emit.emitANDOP(o.frame)
        elif ast.op in ['||']:
            op = self.emit.emitOROP(o.frame)
        elif ast.op in ['::']:
            op = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame)
        else:
            op = self.emit.emitREOP(ast.op,ret,o.frame)
            ret = BooleanType()
        return left+right+op,ret
    
    def visitArrayCell(self, ast, o):
        code = ""
        arr = ast.name
        idx_list = ast.cell
        o, expr = (o[0], o[1]) if isinstance(o, tuple) else (o, None)
        code, arr_type = self.visit(Id(arr), Access(o.frame, o.sym, False, True))
        for i in range(len(idx_list) - 1):
            idx_code, idx_type = self.visit(idx_list[i], Access(o.frame, o.sym, False, True))
            code += idx_code
            code += self.emit.emitALOAD(arr_type, o.frame)
        # last element  
        idx_code, idx_type = self.visit(idx_list[-1], Access(o.frame, o.sym, False, True))
        code += idx_code + self.visit(expr, Access(o.frame, o.sym, False, True))[0] + self.emit.emitASTORE(arr_type.typ, o.frame) \
                if o.isLeft \
                else idx_code + self.emit.emitALOAD(arr_type.typ, o.frame) 
        return code, arr_type.typ
    
    def visitFuncCall(self, ast, o):
        astt = o
        frame = astt.frame
        nenv = astt.sym
        sym = None
        #print("ct",ast.name,[ sym.name if not type(sym) is list else sym for sym in o.sym])
        
        for symbol in o.sym:
            if isinstance(symbol,SubBody): continue
            if isinstance(symbol,list): # local
                sym = list(filter(lambda x: x.name==ast.name,symbol))
                if sym != []: 
                    sym = sym[0]
                    break
                else: sym = None
            elif symbol.name == ast.name:
                sym = symbol
                break
        cname = sym.value.value
        inputtyp = None
        ctype = sym.mtype
        if type(ctype) is MType:
            inputtyp = ctype.partype
        in_ = ("", list())
        for i,x in enumerate(ast.args):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if inputtyp:
                paramtyp = inputtyp[i] if type(inputtyp[i]) is not tuple else inputtyp[i][0]
                if type(paramtyp) is FloatType and type(typ1) is IntegerType:
                    str1 = str1 + self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1] + [typ1])
        ccode = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.name, MType(ctype.partype[0],ctype.rettype) if type(ctype.partype) is tuple else ctype, frame)
        for i,x in enumerate(sym.mtype.partype):
            if(type(x) is tuple and x[3]):
                right,righttyp = self.visit(ArrayCell(ast.name+"_"+x[1],[IntegerLit(0)]),Access(o.frame, o.sym, False))
                left,lefttyp = self.visit(ast.args[i],Access(o.frame, o.sym, True))
                ccode += right+left
        return ccode, ctype

    def visitArrayLit(self, ast, o):
        code, ele_typ = "", None
        o.frame.push()
        for i in range(len(ast.explist)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            ele_code, ele_typ = self.visit(ast.explist[i],o)
            code += ele_code
            code += self.emit.emitASTORE(ele_typ,o.frame)
        o.frame.pop()
        
        # ArrayType(List[Int],typ)
        dims = [len(ast.explist)]
        first_elem = ast.explist[0]
        while(type(first_elem) is ArrayType):
            sub_explist = first_elem.explist
            dims += [len(sub_explist)]
            first_elem = sub_explist[0]
        
        code = self.emit.emitARRAYLITERAL(ArrayType(dims,ele_typ),o.frame) + code
        return code, ArrayType(dims,ele_typ)
    
    def visitId(self,ast,o):
        sym = None
        #print("ct",ast.name,[ sym.name if not type(sym) is SubBody and not type(sym) is list else sym for sym in o.sym])
        for symbol in o.sym:
            if isinstance(symbol,list): # local
                sym = list(filter(lambda x: x.name==ast.name,symbol))
                if sym != []: 
                    sym = sym[0]
                    break
                else: sym = None
            elif isinstance(symbol,SubBody): # func params
                sym = list(filter(lambda x: hasattr(x,"name") and x.name==ast.name,symbol.sym))
                if sym != []: 
                    sym = sym[0]
                    break
                else: sym = None
            elif hasattr(symbol,"name") and symbol.name == ast.name:
                sym = symbol
                break

        if sym:
            if o.isLeft:
                if type(sym.value) is Index:
                    return self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,o.frame), sym.mtype
                elif type(sym.value) is CName:
                    return self.emit.emitPUTSTATIC(sym.value.value+"."+sym.name,sym.mtype,o.frame), sym.mtype
            else:
                if type(sym.value) is Index:
                    return self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,o.frame), sym.mtype
                elif type(sym.value) is CName:
                    return self.emit.emitGETSTATIC(sym.value.value+"."+sym.name,sym.mtype,o.frame), sym.mtype

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()

    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()

    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST('"' + str(ast.val) + '"', StringType(), o.frame), StringType()
    
    def visitBooleanLit(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.val), BooleanType(), o.frame), BooleanType()