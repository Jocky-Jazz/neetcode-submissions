class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box1=[]
        box2=[]
        box3=[]
        cols = [[] for i in range(9)]
        for j, r in enumerate(board):
            row = [x for x in r if not (x=='.')]
            if (not (len(row)==len(set(row)))):
                return False
            for i, n in enumerate(r):
                if (n=='.'):
                    continue
                cols[i].append(n)
                if (i//3==0):
                    box1.append(n)
                elif (i//3==1):
                    box2.append(n)
                elif (i//3==2):
                    box3.append(n)
            if (j==2 and not ( (len(box1)==len(set(box1))) and (len(box2)==len(set(box2))) and (len(box3)==len(set(box3))) ) ):
                return False
                box1=[]
                box2=[]
                box3=[]
        for c in cols:
            if not ( (len(c)==len(set(c))) ):
                return False
        return True