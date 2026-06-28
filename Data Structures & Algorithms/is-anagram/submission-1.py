class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList = {}
        tList = {}
        for i in range(len(s)):
            sList[s[i]] = sList.get(s[i], 0) + 1
            tList[t[i]] = tList.get(t[i], 0) + 1
        return sList == tList


        