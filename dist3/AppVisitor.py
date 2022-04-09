# Generated from ./antlr4/App.g4 by ANTLR 4.9.2
from antlr4 import *
from utils.AppParseTreeVisitor import AppParseTreeVisitor
from utils.Programm import Programm
if __name__ is not None and "." in __name__:
    from .AppParser import AppParser
else:
    from AppParser import AppParser

# This class defines a complete generic visitor for a parse tree produced by AppParser.

class AppVisitor(AppParseTreeVisitor):

    # Visit a parse tree produced by AppParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:AppParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#instruction.
    def visitInstruction(self, ctx:AppParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#signSequence.
    def visitSignSequence(self, ctx:AppParser.SignSequenceContext):
        return self.visitChildren(ctx)


    def visitSimpleVariableType(self, ctx:AppParser.SimpleVariableTypeContext):
        return ctx.getText()


    def visitComplexVariableType(self, ctx:AppParser.ComplexVariableTypeContext):
        return ctx.getText()


    # Visit a parse tree produced by AppParser#variable.
    def visitVariable(self, ctx:AppParser.VariableContext):
        return self.visitChildren(ctx)


    def visitVariableName(self, ctx:AppParser.VariableNameContext):
        return ctx.getText()


    # Visit a parse tree produced by AppParser#functionName.
    def visitFunctionName(self, ctx:AppParser.FunctionNameContext):
        return self.visitChildren(ctx)


    def visitInteger(self, ctx:AppParser.IntegerContext):
        value = ctx.getText()
        return int(value)


    def visitArithmeticalExpression(self, ctx:AppParser.ArithmeticalExpressionContext):
        NR_OF_CHILDREN = self.getNrOfChildren(ctx)
        if NR_OF_CHILDREN == 1:
            return self.visitChildren(ctx)
        else:
            print("Arithmetic expr, nr of children: {}".format(NR_OF_CHILDREN))
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)

            op = ctx.op.text
            operation =  {
            '+': lambda: l + r,
            '-': lambda: l - r,
            '*': lambda: l * r,
            '/': lambda: l / r,
            }
            return operation.get(op, lambda: None)()


    def visitDeclaration(self, ctx:AppParser.DeclarationContext):
        NR_OF_CHILDREN = self.getNrOfChildren(ctx)
        print("Nr of children: ", NR_OF_CHILDREN)

        if NR_OF_CHILDREN is None or NR_OF_CHILDREN < 6:
            return

        name = self.visitChild(ctx,4)
        type = self.visitChild(ctx,2)
        # print("Type: {}  Name: {}".format(type, name))
        
        if NR_OF_CHILDREN >= 6 and NR_OF_CHILDREN <= 7: # definition without value
            Programm.declareNewVariable(name, Programm.strToType(type))
        
        elif NR_OF_CHILDREN >= 10 and NR_OF_CHILDREN <=11: # definition with value - simple type
            value = self.visitChild(ctx,8)
            Programm.defineNewVariable(name, Programm.strToType(type), value)

        else: 
            # definition with value of complex type
            value1 = self.visitChild(ctx,8)
            value2 = None
            if self.visitChild(ctx,10) is not None:
                value2 = self.visitChild(ctx,10)
            
            elif self.visitChild(ctx,11) is not None:
                value2 = self.visitChild(ctx,11)
            
            else:
                value2 = self.visitChild(ctx,12)
            Programm.defineNewVariable(name, Programm.strToType(type), value1, value2)

        return "declaration"


    def visitDefinition(self, ctx:AppParser.DefinitionContext):
        NR_OF_CHILDREN = self.getNrOfChildren(ctx)
        # print("Nr of children: ", NR_OF_CHILDREN)

        if NR_OF_CHILDREN is None or NR_OF_CHILDREN < 8:
            return
        
        name = self.visitChild(ctx,2)
        value = self.visitChild(ctx,6)

        if NR_OF_CHILDREN < 10: # simple type
            Programm.defineExistingVariable(name, value)

        else: # complex type
            value2 = None
            if self.visitChild(ctx,8) is not None:
                value2 = self.visitChild(ctx,8)
            
            elif self.visitChild(ctx,9) is not None:
                value2 = self.visitChild(ctx,9)
            
            else:
                value2 = self.visitChild(ctx,10)

            Programm.defineExistingVariable(name, value, value2)

        return "definition"

    # Visit a parse tree produced by AppParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:AppParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#condition.
    def visitCondition(self, ctx:AppParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#parallelExpression.
    def visitParallelExpression(self, ctx:AppParser.ParallelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#loop.
    def visitLoop(self, ctx:AppParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#function.
    def visitFunction(self, ctx:AppParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#functionBody.
    def visitFunctionBody(self, ctx:AppParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#functionArgs.
    def visitFunctionArgs(self, ctx:AppParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AppParser#whiteSpace.
    def visitWhiteSpace(self, ctx:AppParser.WhiteSpaceContext):
        return self.visitChildren(ctx)



del AppParser