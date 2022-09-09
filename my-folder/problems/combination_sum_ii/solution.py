class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def combtwo(index,target,ds):
            if target == 0:
                solution.append(list(ds))
                # print(ds)
                return
            for i in range(index,n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                combtwo(i+1,target-candidates[i],ds)
                ds.remove(candidates[i])
            
        solution = []
        candidates.sort()
        print(candidates)
        combtwo(0,target,[])
        return solution
            
            
                
    
        