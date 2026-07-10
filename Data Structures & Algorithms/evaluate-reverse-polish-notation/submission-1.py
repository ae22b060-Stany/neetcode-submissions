class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0 
        #operator_stack = []
        operand_stack = []
        for token in tokens:

            if token == '+':
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                inte = (op1 + op2)
                operand_stack.append(inte)
            elif token == '-':
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                inte =  (op1 - op2)
                operand_stack.append(inte)
            elif token == '/':
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                inte =  (int(op1 / op2))
                operand_stack.append(inte)
            elif token == '*':
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                inte = (int(op1 * op2))
                operand_stack.append(inte)
            else:
                operand_stack.append(int(token))
        return operand_stack.pop()

            