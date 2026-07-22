class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        new_dict = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))
        return [x for i, x in enumerate(new_dict) if i < k]