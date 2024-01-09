from Visitor import Visitor
from StaticError import *
##
from Visitor import *
from AST import *
##


''' 
    o = [Scope(N),Scope(N-1),Scope(0),EnvScope]
    Scope(i) = [Symbol1,Symbol2,...,SymbolN]
    Symbol:
        name: str
        typ: Type
        param: [Symbol]: Name
        out: bool
        inherit: bool
'''
class Symbol:
    def __init__(self, name, typ, param=None, out=None, inherit=None):
        self.name = name
        self.typ = typ
        self.param = param
        self.out = out
        self.inherit = inherit
    
    def __str__(self):
        return "Symbol" + "("+ str(self.name) + ", " + str(self.typ) + (", " + str(self.param) if self.param != None else "") + (", " + str(self.out) if self.out else "") + (", " + str(self.inherit) if self.inherit else "") + ")"
    
class Utils:
    def infer(env, name, typ):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
    
    def isFunc(sym):
        return sym.param != None

    def printO(o,signal=""):
        print(signal)
        print("[",end="\n")
        for symbol_list in o:
            print("\t[",end="")
            for symbol in symbol_list:
                print(symbol,end=" ")
            print("]",end="\n")
        print("]")
        
class GetEnv(Visitor):
    # First Visit: Only get function decls - Do not throw any exceptions
    def __init__(self,ast):
        self.ast = ast
    def visitProgram(self,ast,o): 
        global_scope = [[Symbol("readInteger",IntegerType(),[]),
                        Symbol("readFloat",FloatType(),[]),
                        Symbol("readBoolean",BooleanType(),[]),
                        Symbol("readString",StringType(),[]),
                        Symbol("preventDefault",VoidType(),[]),
                        Symbol("printInteger",VoidType(),[Symbol("<Param>",IntegerType(),)]),
                        Symbol("printString",VoidType(),[Symbol("<Param>",StringType(),)]),
                        Symbol("writeFloat",VoidType(),[Symbol("<Param>",FloatType(),)]),
                        Symbol("printBoolean",VoidType(),[Symbol("<Param>",BooleanType(),)]),
                        Symbol("super",VoidType(),[])
                        ]]
        for decl in ast.decls:
            self.visit(decl, global_scope)
        return global_scope
    
    def visitVarDecl(self, ast, o): pass

    def visitParamDecl(self, ast, o):
        o[0] += [Symbol(ast.name,ast.typ,None,ast.out,ast.inherit)]
    
    def visitFuncDecl(self, ast, o):
        o_1 = [[Symbol(ast.name,ast.return_type,[])]] + o
        for i in ast.params:
            self.visit(i, o_1)
        # Collect all values
        lst_param = []
        for i in range(1,len(ast.params)+1):
            lst_param += [Symbol(o_1[0][i].name,o_1[0][i].typ,None,o_1[0][i].out,o_1[0][i].inherit)] 
        
        o[0] += [Symbol(ast.name,ast.return_type,lst_param,None,ast.inherit)]
    
class StaticChecker(Visitor):
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast, None)
        
    def visitIntegerType(self, ast, o):
        return IntegerType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBooleanType(self, ast, o):
        return BooleanType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast, o):
        return ArrayType(ast.dimensions, ast.typ)
    
    def visitAutoType(self, ast, o):
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
        
    def visitBinExpr(self, ast, o):
        op = ast.op
        left = self.visit(ast.left,o)
        right = self.visit(ast.right,o)
        lefttyp = type(left)
        righttyp = type(right)
        
        # Inference: Left or Right is Auto
        if lefttyp is AutoType and righttyp is not AutoType:
            lefttyp = type(Utils.infer(o,ast.left.name,right))
        if lefttyp is not AutoType and righttyp is AutoType:
            righttyp = type(Utils.infer(o,ast.right.name,left))

        if op in ['+','-','*','/']:
            if not (lefttyp is IntegerType or lefttyp is FloatType) or not (righttyp is IntegerType or righttyp is FloatType):
                raise TypeMismatchInExpression(ast)
            if lefttyp is IntegerType and righttyp is IntegerType:
                return IntegerType() # if op != '/' else FloatType()
            if lefttyp is FloatType or righttyp is FloatType:
                return FloatType()
            
        if op in ['%']:
            if lefttyp is IntegerType and righttyp is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)

        if op in ['&&','||']:
            if lefttyp is BooleanType and righttyp is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['::']:
            if lefttyp is StringType and righttyp is StringType:
                return StringType()

            raise TypeMismatchInExpression(ast)

        if op in ['<', '>', '<=', '>=']:
            if not (lefttyp is IntegerType or lefttyp is FloatType) and not (righttyp is IntegerType or righttyp is FloatType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        
        if op in ['!=','==']:
            if not (lefttyp is IntegerType or lefttyp is BooleanType) and not (righttyp is IntegerType or righttyp is BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        
    def visitUnExpr(self, ast, o):
        op = ast.op
        val = self.visit(ast.val, o)
        valtyp = type(val)
        
        if op in ['-']:
            if valtyp is IntegerType:
                return IntegerType()
            if valtyp is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['!']:
            if valtyp is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast, o):
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.name == symbol.name and not Utils.isFunc(symbol):
                    return symbol.typ
        raise Undeclared(Identifier(),ast.name)
        
    def visitArrayCell(self, ast, o):
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.name == symbol.name:
                    name_type = symbol.typ
                    # The name should be in ArrayType
                    if type(name_type) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    # ArrayCell should point to unbreakable subscript
                    ''' if len(name_type.dimensions) != len(ast.cell):
                        raise TypeMismatchInExpression(ast) '''
                    # All cell vals must be of IntegerType
                    for item in ast.cell:
                        ityp = self.visit(item,o)
                        if type(ityp) is not IntegerType:
                            # need to infer - Yes
                            if type(ityp) is AutoType: # function
                                Utils.infer(o,item.name,IntegerType())
                            # error: for the id or array_cell?
                            else: raise TypeMismatchInExpression(item)
                    if len(name_type.dimensions) == len(ast.cell):
                        
                        return name_type.typ
                    elif len(name_type.dimensions) < len(ast.cell):
                        raise TypeMismatchInExpression(ast)
                    else:
                        return ArrayType(name_type.dimensions[len(ast.cell):],name_type.typ)
        raise Undeclared(Identifier(),ast.name)
    
    def visitIntegerLit(self, ast, o):
        return IntegerType()
    
    def visitFloatLit(self, ast, o):
        return FloatType()
    
    def visitStringLit(self, ast, o):
        return StringType()
    
    def visitBooleanLit(self, ast, o):
        return BooleanType()
    
    def visitArrayLit(self, ast, o):
        explist = ast.explist
        if explist == []: return ArrayType([0],AutoType())
        
        utyp = None
        for exp in explist:
            exptyp = self.visit(exp,o)
            # 1st assignment
            if utyp is None: 
                utyp = exptyp
            # 2nd++
            else:
                # inference
                if type(utyp) is AutoType:
                    utyp = exptyp
                elif type(exptyp) is AutoType:
                    Utils.infer(o,exp.name,utyp)
                elif type(exptyp) is ArrayType or type(utyp) is ArrayType:
                    if not hasattr(exptyp,"dimensions") or not hasattr(utyp,"dimensions") or exptyp.dimensions != utyp.dimensions:
                        raise IllegalArrayLiteral(ast)
                elif type(utyp) != type(exptyp):
                    raise IllegalArrayLiteral(ast)
        fin_dim = [len(ast.explist)]+utyp.dimensions if type(utyp) is ArrayType else [len(ast.explist)]
        fin_typ = utyp.typ if type(utyp) is ArrayType else utyp
        return ArrayType(fin_dim,fin_typ)
    
    def visitFuncCall(self, ast, o):
        # Check if function exists
        # o[-1]: functions that of global scope
        flag = False
        
        # Check funcname compatibility - Only throw error if it is VoidType
        for symbol in o[-2]+o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                if type(symbol.typ) is VoidType:
                    raise TypeMismatchInExpression(ast)
                break
        # super() is not a normal funcall
        # if ast.name == "super": raise TypeMismatchInExpression(ast.args)
        if not flag: raise Undeclared(Function(),ast.name)
        
        # Check param compatibility
        for symbol in o[-2] + o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                lst_param = symbol.param
                args = ast.args
                # length check
                if len(args) > len(lst_param):
                    #raise TypeMismatchInExpression(args[len(lst_param)])
                    raise TypeMismatchInExpression(ast)
                elif len(args) < len(lst_param):
                    #raise TypeMismatchInExpression(lst_param[len(args)+1].name)
                    raise TypeMismatchInExpression(ast)
                # argument and param
                else:
                    for i in range(0, len(lst_param)):
                        ptyp = lst_param[i].typ # LHS
                        atyp = self.visit(ast.args[i], o) # RHS
                        
                        # OUT PARAM -> arg must be ID
                        if lst_param[i].out and not hasattr(ast.args[i],"name"):
                            raise TypeMismatchInExpression(ast)
                        # TYPE INFERRED: RHS -> LHS: Auto
                        if type(atyp) is not AutoType and type(ptyp) is AutoType:
                            symbol.param[i].typ = atyp
                            continue
                        if type(atyp) is AutoType and type(ptyp) is not AutoType:
                            ast.args[i].typ = ptyp
                            continue
                        # TYPE COERCION: RHS:Integer -> LHS:Float
                        if type(atyp) is IntegerType and type(ptyp) is FloatType:
                            continue
                        # TYPE MISMATCH
                        if type(atyp) is not type(ptyp):
                            raise TypeMismatchInExpression(ast)
                return symbol.typ    
            
    def visitAssignStmt(self, ast, o):
        rtype = self.visit(ast.rhs,o)
        ltype = self.visit(ast.lhs,o)
        # if lhs is VoidType/ArrayType
        if type(ltype) is VoidType or type(ltype) is ArrayType:
            raise TypeMismatchInStatement(ast)
        
        # Right infer
        if type(ltype) is AutoType:
            ltype = Utils.infer(o, ast.lhs.name, rtype)
            return ltype
        
        # Left infer
        if type(rtype) is AutoType:
            rtype = Utils.infer(o, ast.rhs.name, ltype)
            return rtype
        
        # NO MORE Inference - Check if types are equal
        ## TYPE COERCION: Int->Float
        if type(ltype) is type(rtype) or (type(rtype) is IntegerType and type(ltype) is FloatType):
            return rtype
        ## TYPE MISMATCH
        if type(ltype) is not type(rtype):
            raise TypeMismatchInStatement(ast)

    def visitIfStmt(self, ast, o):
        ctype = self.visit(ast.cond,o)
        if type(ctype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o1 = [[]] + o
        if ast.tstmt:
            self.visit(ast.tstmt,o1)
        o2 = [[]] + o
        if ast.fstmt:
            self.visit(ast.fstmt,o2)
            
    def visitForStmt(self, ast, o):
        itype = self.visit(ast.init,o)
        ctype = self.visit(ast.cond,o)
        utype = self.visit(ast.upd,o)
        if type(ctype) is not BooleanType or type(itype) is not IntegerType or type(utype) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        o1 = [[Symbol("<Loop>",VoidType)]] + o
        self.visit(ast.stmt,o1)
        
    def visitWhileStmt(self, ast, o):
        ctype = self.visit(ast.cond,o)
        if type(ctype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o1 = [[Symbol("<Loop>",VoidType)]] + o
        self.visit(ast.stmt,o1)
        
    def visitDoWhileStmt(self, ast, o):
        ctype = self.visit(ast.cond,o)
        if type(ctype) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o1 = [[Symbol("<Loop>",VoidType)]] + o
        self.visit(ast.stmt,o1)
        
    def visitBreakStmt(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitContinueStmt(self, ast, o):
        flag = False
        for symbol_list in o:
            for symbol in symbol_list: # visit all outer blocks
                if symbol.name == "<Loop>": 
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitReturnStmt(self, ast, o):
        rtype = self.visit(ast.expr,o) if ast.expr else VoidType() # RHS
        ftype, inner = None, False # LHS
        for i in range(1,len(o)):
            if len(o[i])>0 and Utils.isFunc(o[i][0]):
                ftype = o[i][0].typ
                # RHS -> LHS
                if type(ftype) is AutoType:
                        o[i][0].typ = rtype
                # RHS != LHS
                elif type(ftype) is not type(rtype):
                    raise TypeMismatchInStatement(ast)
                break
        
        
    def visitCallStmt(self, ast, o):
        # Check if function exists
        flag = False
        # Check func compatibility
        for symbol in o[-2] + o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                # Inference
                ''' if type(symbol.typ) is AutoType:
                    symbol.typ = VoidType() '''
                # update: callstmt can be another type
                ''' if type(symbol.typ) is not VoidType:
                    raise TypeMismatchInStatement(ast) '''
                break
        if not flag: raise Undeclared(Function(),ast.name)
                
        # Check param compatibility
        for symbol in o[-2] + o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                lst_param = symbol.param
                args = ast.args
                # length check
                if len(args) > len(lst_param):
                    #raise TypeMismatchInExpression(args[len(lst_param)])
                    raise TypeMismatchInStatement(ast)
                elif len(args) < len(lst_param):
                    #raise TypeMismatchInStatement(lst_param[len(args)+1].name)
                    raise TypeMismatchInStatement(ast)
                # argument and param
                else:
                    for i in range(0, len(lst_param)):
                        ptyp = lst_param[i].typ # LHS
                        atyp = self.visit(ast.args[i], o) # RHS
                        
                        # OUT PARAM -> arg must be ID
                        if lst_param[i].out and not hasattr(ast.args[i],"name"):
                            raise TypeMismatchInStatement(ast)
                        # TYPE INFERRED: RHS -> LHS: Auto
                        if type(atyp) is not AutoType and type(ptyp) is AutoType:
                            symbol.param[i].typ = atyp
                            continue
                        if type(atyp) is AutoType and type(ptyp) is not AutoType:
                            ast.args[i].typ = ptyp
                            continue
                        # TYPE COERCION: RHS:Integer -> LHS:Float
                        if type(atyp) is IntegerType and type(ptyp) is FloatType:
                            continue
                        # TYPE MISMATCH
                        if type(atyp) is not type(ptyp):
                            raise TypeMismatchInStatement(ast)
                return symbol.typ
                        
    def visitBlockStmt(self, ast, o):
        o1 = [[]] + o
        
        # check if this block is DIRECTLY from a function
        flag_func = False
        for symbol in o1[1]:
            if Utils.isFunc(symbol): flag_func = True
        
        if not flag_func:
            for stmt_decl in ast.body:
                self.visit(stmt_decl,o1)
        else:
            # o1: [[block],[func_name,func_param1,...],...]
            func_scope = o1[1] # no need to check further
            first_stmt = True
            ret = False
            
            parent_name = o1[1][0].inherit
            
            # Parameter Inheritance
            if parent_name:
                for symbol in o[-2] + o[-1]:
                    if symbol.name == parent_name: # find the right parent
                        for i in range(len(symbol.param)):
                            # Get inherited vars for local scope
                            if symbol.param[i].inherit:
                                #func_scope: [func_name,func_p1,func_p2,...]
                                if len(func_scope) > 1:
                                    for fparam in func_scope[1:]: #remove function
                                        if fparam.name == symbol.param[i].name:
                                            raise Invalid(Parameter(),fparam.name)
                                o1[0] += [Symbol(symbol.param[i].name,symbol.param[i].typ)]
                        if ast.body == [] and len(symbol.param) > 0: raise InvalidStatementInFunction(o1[1][0].name)
            # Activation
            for stmt_decl in ast.body:
                # find redecl func at global scope
                if hasattr(stmt_decl,"name"): #VarDecl
                    for func_component in func_scope[1:]: # FuncDecl is of outer scope
                        if stmt_decl.name == func_component.name:
                            raise Redeclared(Variable(),stmt_decl.name)
                if not parent_name:
                    if hasattr(stmt_decl,"name") and (stmt_decl.name == "super" or stmt_decl.name == "preventDefault"):
                        raise InvalidStatementInFunction(stmt_decl.name)
                    if ret is True and type(stmt_decl) is ReturnStmt: continue
                    self.visit(stmt_decl,o1)
                    if type(stmt_decl) is ReturnStmt:
                        ret = True
                    first_stmt = False
                elif not first_stmt:
                    if ret is True and type(stmt_decl) is ReturnStmt: continue
                    self.visit(stmt_decl,o1)
                    if type(stmt_decl) is ReturnStmt:
                        ret = True
                else:
                    first_stmt = False
                    # find parent function in o[-2] + o[-1]
                    found = False # find function
                    prevent = False # check for preventDefault
                    
                    for symbol in o[-2] + o[-1]:
                        if found: break
                        if symbol.name == parent_name: # find the right parent
                            found = True     
                            # parent is an empty function
                            if len(symbol.param)==0:
                                # auto inheritance
                                if not hasattr(stmt_decl,"name"): self.visit(stmt_decl,o1)
                                # prevent inheritance
                                elif stmt_decl.name == "preventDefault" and len(stmt_decl.args)==0: prevent = True
                            # parent is a non-empty function
                            else:
                                # not vardecl
                                if not hasattr(stmt_decl,"name"): raise InvalidStatementInFunction(o1[1][0].name)
                                # super()
                                elif stmt_decl.name == "super": # inference and inheritance
                                    # arg and param inference
                                    l = len(symbol.param)
                                    if len(stmt_decl.args) > l: raise TypeMismatchInExpression(stmt_decl.args[l])
                                    elif len(stmt_decl.args) < l: raise TypeMismatchInExpression(None)
                                # preventDefault        
                                elif stmt_decl.name == "preventDefault" and len(stmt_decl.args)==0: prevent = True
                                else: raise InvalidStatementInFunction(o1[1][0].name)
                            if not prevent:
                                for i in range(len(symbol.param)):
                                    arg_typ = self.visit(stmt_decl.args[i],o)
                                    p_typ = symbol.param[i].typ
                                    # Arg-Param Inference
                                    if type(p_typ) is FloatType and type(arg_typ) is IntegerType: 
                                        continue
                                    if type(p_typ) is AutoType: 
                                        symbol.param[i].typ = arg_typ
                                        continue
                                    if type(arg_typ) is AutoType: 
                                        stmt_decl.args[i].typ = arg_typ
                                        continue
                                    if type(p_typ) is not type(arg_typ):
                                        raise TypeMismatchInExpression(stmt_decl.args[i])
                    if not found: raise Undeclared(Function(),parent_name)
        
    def visitParamDecl(self, ast, o):
        # Check if existed - at the same scope
        for symbol in o[0]:
            if symbol.name == ast.name: raise Redeclared(Parameter(),ast.name)
        o[0] += [Symbol(ast.name,ast.typ,None,ast.out,ast.inherit)]
    
    def visitFuncDecl(self, ast, o):
        # Check if existed (func+inherit) - at the same scope
        found = False
        for symbol in o[-1]+o[-1][:10]: # Func
            if symbol.name == ast.name: 
                if not found: found = True
                else: raise Redeclared(Function(),ast.name)
        for symbol in o[0]: # Var
            if symbol.name == ast.name: 
                raise Redeclared(Function(),ast.name)
        if ast.inherit:
            found = False
            for symbol in o[-1]: # global scope
                if symbol.name == ast.inherit: found = True
            if not found: raise Undeclared(Function(),ast.inherit)
        # Visit all params and body block stmt
        # [[body],[func_scope],...]
        o_1 = [[Symbol(ast.name,ast.return_type,[], None, ast.inherit)]] + o
        for i in ast.params:
            self.visit(i, o_1)
        # Body visit
        self.visit(ast.body,o_1)
        # Collect all values
        lst_param = []
        ## only lists of params: each must have NAME to check re-declaration !!
        for i in range(1,len(ast.params)+1):
            lst_param += [Symbol(o_1[0][i].name,o_1[0][i].typ,None,o_1[0][i].out,o_1[0][i].inherit)] 
        ## Function Inference
        o[0] += [Symbol(ast.name,o_1[0][0].typ,lst_param,None,ast.inherit)]

    def visitVarDecl(self, ast, o):
        
        # Check if existed - at the same scope
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(),ast.name)
        for symbol in o[-2] + o[-1][:10]: # round 2 + built-in funcs
            if symbol.name == ast.name and Utils.isFunc(symbol):
                raise Redeclared(Variable(),ast.name)
        # Auto Type and Without Init
        if not ast.init and type(ast.typ) is AutoType:
            raise Invalid(Variable(), ast.name) 
        # With Init - Inference
        if not ast.init: o[0] += [Symbol(ast.name,ast.typ)]
        else:
            inittyp = self.visit(ast.init, o)
            # Implicit Conversion
            if type(inittyp) is IntegerType and type(ast.typ) is FloatType:
                Utils.infer(o,ast.name,FloatType())
                o[0] += [Symbol(ast.name,FloatType())]
            elif type(inittyp) is FloatType and type(ast.typ) is IntegerType:
                raise TypeMismatchInVarDecl(ast.init)
            elif type(inittyp) is ArrayType and type(ast.typ) is ArrayType:
                ast.typ.dimensions = list(map(lambda x: int(x),ast.typ.dimensions))
                inittyp.dimensions = list(map(lambda x: int(x),inittyp.dimensions))
                if inittyp.dimensions != ast.typ.dimensions:
                    raise TypeMismatchInVarDecl(ast)
                if type(inittyp.typ) is not type(ast.typ.typ) and not (type(inittyp.typ) is AutoType):
                    if not (type(inittyp.typ) is IntegerType and type(ast.typ.typ) is FloatType): raise TypeMismatchInVarDecl(ast)
                if hasattr(ast.init,"explist"): # ArrayLit
                    for exp in ast.init.explist:
                        if hasattr(exp,"name"): 
                            typ = self.visit(exp,o)
                            if type(typ) is AutoType:
                                Utils.infer(o,exp.name,ast.typ.typ)
                o[0] += [Symbol(ast.name,ast.typ)]
            elif type(inittyp) is ArrayType and type(ast.typ) is AutoType:
                Utils.infer(o,ast.name,inittyp)
                o[0] += [Symbol(ast.name,inittyp)]
            elif type(inittyp) is AutoType and type(ast.typ) is not AutoType:
                Utils.infer(o,ast.init.name,ast.typ)
                o[0] += [Symbol(ast.name,ast.typ)]
            
            ## Mismatch
            elif type(inittyp) is not AutoType and type(ast.typ) is not AutoType and type(inittyp) is not type(ast.typ):
                raise TypeMismatchInVarDecl(ast.init)
            ### Or else...
            else:
                #Utils.infer(o,ast.name,inittyp)
                o[0] += [Symbol(ast.name,inittyp)]

    def visitProgram(self, ast, o):
        # Preliminary, no need to check for errors
        global_scope = GetEnv(ast).visit(ast, o)
        
        # Round 2 - Detailed Visit
        env = [[]] + global_scope
        for decl in ast.decls:
            self.visit(decl,env)
            ''' # update detail to global scope
            for local_f in env[-2]:
                for global_f in env[-1]:
                    if local_f.name == global_f.name and type(loca):
                        global_f = local_f '''
                        
        # Finally, check for Entry Point
        flag = False
        for decl in global_scope[0]:
            if decl.name == "main" and type(decl.typ) is VoidType and len(decl.param)==0:
                flag = True
                break
        if not flag:
            raise NoEntryPoint()