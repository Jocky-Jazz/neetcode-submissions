class TimeMap:

    def __init__(self):
        self.myList = dict()
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myList[(key, timestamp)] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        timeList = self.timestamps[key]
        l, u, mid = 0, len(timeList), 0
        while (u > l):
            mid = l + ((u-l)>>1)
            if (timestamp<timeList[mid]):
                u = mid
            else:
                l = mid+1
        return self.myList[(key, timeList[l-1])] if l>0 else ""
