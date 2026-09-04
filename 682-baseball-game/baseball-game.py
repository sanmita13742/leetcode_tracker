class Solution:
    def calPoints(self, operations: List[str]) -> int:
        draw = []
        other = set('DC+')
        total = 0
        for op in operations:
            if op not in other:
                draw.append(int(op))
                total+= int(op)
                #print('digit add:', draw)
            elif op == '+':
                total+= int(draw[-1]+ draw[-2])
                draw.append(draw[-1]+ draw[-2])
                
                #print(' add:', draw)
            elif op == 'D':
                total+= int(draw[-1]*2)
                draw.append(draw[-1]*2)
                
                #print('d :', draw)
            elif op == 'C':
                total -= draw[-1]
                draw.pop()
                #print('c :', draw)
        return total








