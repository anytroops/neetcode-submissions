class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        perm = []
        def back(o, c):
            if o == n and c == n:
                ret.append("".join(perm))
                return
            if o < n:
                perm.append("(")
                back(o + 1, c)
                perm.pop()
            if c < o:
                perm.append(")")
                back(o, c + 1)
                perm.pop()
        back(0,0)
        return ret

        