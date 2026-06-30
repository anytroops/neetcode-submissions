class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        perm = []
        def back(i, sum):
            if sum == target:
                ret.append(perm.copy())
                return
            if sum > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                perm.append(candidates[j])
                back(j + 1, sum + candidates[j])
                perm.pop()
        back(0,0)
        return ret
        