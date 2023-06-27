class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                prevprev = int(record[-2])
                prev = int(record[-1])
                record.append(str(prev + prevprev))
            elif op == 'D':
                prev = int(record[-1])
                record.append(str(prev * 2))
            elif op == 'C':
                record.pop()
            else:
                record.append(op)
        record = [int(i) for i in record]
        return sum(record)