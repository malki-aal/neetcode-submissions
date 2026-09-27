class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = []
        for ops in operations:
            if ops == "+":
                op.append(op[-1]+op[-2])
            elif ops == "C":
                op.pop()
            elif ops == "D":
                op.append(2*op[-1])
            else:
                op.append(int(ops))
        return sum(op)        