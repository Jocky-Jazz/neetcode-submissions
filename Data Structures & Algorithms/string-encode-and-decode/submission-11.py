class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        lenstr=""
        length=-1
        string=""
        f=0
        l=[]
        cursor = 0
        while (cursor < len(s)):
            if (f==0 and s[cursor]=='#'):
                f = 1
                length=int(lenstr)
                lenstr=""
                if (length==0):
                    l.append("")
                    f = 0
            elif (f==0):
                lenstr += s[cursor]
            else:           
                l.append(s[cursor:cursor+length])
                f = 0
                cursor += length-1
            cursor += 1
        return l