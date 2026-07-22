class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i, k = 0, 0
        days = [0 for _ in temperatures]
        while(i < len(days)):
            k = i+1
            while(k < len(days)):
                if (temperatures[i] < temperatures[k]):
                    days[i] = k-i
                    break
                k += 1
            i += 1
        return days