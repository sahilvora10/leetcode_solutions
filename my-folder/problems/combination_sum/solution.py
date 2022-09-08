class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def combination_sum(i,s,arr):
            if i == n:
                if s == 0:
                    solution.append(list(arr))
                return
            if candidates[i] <= s:
                arr.append(candidates[i])
                # print("here", candidates[i]," ",s)
                combination_sum(i,s-candidates[i],arr)
                arr.remove(candidates[i])
            combination_sum(i+1,s,arr)
        solution = []
        combination_sum(0,target,[])
        return solution
            
            
        