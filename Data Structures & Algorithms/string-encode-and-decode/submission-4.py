class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        lenstr=""
        len=-1
        string=""
        f=0
        l=[]
        print(s)
        for c in s:
            if (f==0 and c=='#'):
                f = (f+1)%2
                len=int(lenstr)
                lenstr=""
                if (len==0):
                    l.append("")
                    f = 0
            elif (f==0):
                lenstr += c
            else:           
                string += c
                len -= 1
                if (len == 0):
                    l.append(string)
                    string=""
                    f = 0
        return l