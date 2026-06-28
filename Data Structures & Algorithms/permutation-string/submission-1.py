class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = s1Map.get(s1[i], 0) + 1
        window = s2[0:len(s1)]
        windowMap = {}
        for i in range(len(window)):
            windowMap[window[i]] = windowMap.get(window[i], 0) + 1
        if windowMap == s1Map:
            return True
        for i in range(len(s2)- len(s1)):
            windowMap[s2[i+len(s1)]] = windowMap.get(s2[i+len(s1)], 0) + 1
            windowMap[s2[i]] -= 1
            if windowMap[s2[i]] == 0:
                del windowMap[s2[i]]
            if windowMap == s1Map:
                return True
        return False
                            
        