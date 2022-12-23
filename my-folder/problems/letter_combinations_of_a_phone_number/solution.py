class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        
        hp = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        sol = []
        l = len(digits)
        def backtrack(num,l,path):
            if l==0:
                sol.append(path)
                return
            f = num//(10**(l-1))
            r = num%(10**(l-1))
            for x in hp[f]:
                    backtrack(r,l-1,path+x)
        backtrack(int(digits),l,"")
        return sol
        