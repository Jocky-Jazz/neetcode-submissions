class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(map(lambda p, s:(p, (target-p)/s), position, speed))
        cars.sort(key = lambda x: x[0], reverse = True)
        times = [c[1] for c in cars]
        stack = []
        for n in times:
            if (not stack or stack[-1] < n):
                stack.append(n)
        return len(stack)


