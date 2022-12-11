class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.block = [-1]*n
        

    def allocate(self, size: int, mID: int) -> int:
        # print(self.block)
        i,j,count,flag = 0,0,0,0
        
        for i in range(self.n):
            if self.block[i] == -1:
                count+=1
                if count == size:
                    flag = 1
                    break
            else:
                count=0
                j= i+1
        if flag:
            for i in range(j,j+size):
                self.block[i] = mID
            return j
        return -1

    def free(self, mID: int) -> int:
        count  = 0
        for i in range(self.n):
            if self.block[i] == mID:
                self.block[i] = -1
                count+=1
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)