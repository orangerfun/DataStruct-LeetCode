class Solution:
    def permute(self, nums):
        path = []
        result = []
        isused = [False for _ in range(len(nums))]
        self.digui(path, result, isused, nums)
        return result
    
    def digui(self, path, result, isused, nums):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if isused[i] == True:
                continue
            else:
                path.append(nums[i])
                isused[i] = True

            self.digui(path, result, isused, nums)
            path.pop()
            isused[i] = False

nums = [1,2,3,4]
solution = Solution()
print(solution.permute(nums))