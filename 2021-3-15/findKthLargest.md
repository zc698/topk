215.数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2

输出: 5

来源：力扣（LeetCode）

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：升序排序后，目标元素的索引是len - k。

    class Solution:
		def findKthLargest(self, nums:List[int],k:int) -> int:
			size = len(nums)
			nums.sort()
			return nums[size - k]

时间复杂度：O(NlogN),这里 N 是数组的长度，算法的性能消耗主要在排序，默认使用快速排序，因此时间复杂度为O(NlogN)。

空间复杂度：O(1),这里是原地排序，没有借助额外的辅助空间。

思路2：

借助 partition 操作定位到最终排定以后索引为 len - k 的那个元素（特别注意：随机化切分元素）


    from typing import List
	import random
	class Solution:
		def findKthLargest(self,nums:List[int],k:int) -> int:
			size = len(nums)
			target =size - k
			left = 0
			right = size - 1
			while True:
				index = self.__partition(nums,left,right)
				if index == target:
					return nums[index]
				elif index < target:
					left = index + 1
				else:
					right = index - 1
		def __partition(self,nums,left,right):
			# 随机化切分元素
        	# randint 是包括左右区间的
			random_index = random.randint(left,right)
			nums[random_index], nums[left] = nums[left],nums[random_index]
			pivot = nums[left]
			j = left
			for i in range(left + 1,right + 1):
				if nums[i] < pivot:
					j += 1
					nums[i],nums[j] = nums[j],nums[i]
			nums[left],nums[j] = nums[j],nums[left]
			return j

时间复杂度：O(N),N指数组的长度。

空间复杂度：O(1),原地排序，没有借助额外的辅助空间。
