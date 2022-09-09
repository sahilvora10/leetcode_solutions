class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def subsetwo(index,ds):
            if index == n:
                # print(ds)
                solution[tuple(ds)] = 1
                return
            ds.append(nums[index])
            subsetwo(index+1,ds)
            ds.remove(nums[index])
            subsetwo(index+1,ds)
            # for i in range(index,n):
            #     if i>index and nums[i] == nums[i-1]:
                    # continue
                # ds.append(nums[i])
                # subsetwo(i+1,ds)
                # ds.remove(nums[i])
                # subsetwo(i+1,ds)
        solution = {}
        nums.sort()
        subsetwo(0,[])
        # print(solution)
        x = [list(k) for k in solution.keys()]
        # print(x)
        return x
                
        