class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        for s in strs:
            sorteds = ''.join(sorted(s))
            if (sorteds in hmap):
                hmap[sorteds].append(s)
            else:
                hmap[sorteds] = [s]
        l = []
        for k in hmap:
            l.append(hmap[k])
        return l