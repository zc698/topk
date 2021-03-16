"""
189.旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
使用额外的数组来将每个元素放至正确的位置。用n表示数组的长度，我们遍历原数组，将原数组下标为i的元素放至新数组下标为(i+k) mod n 的位置，最后将新数组拷贝至原数组即可。
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
		n = len(nums)
        newArr1 = [0] * n
        for i in range(n):
            newArr1[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = newArr1[i]
            
            
"""
时间复杂度：O(n),n为数组长度。
空间复杂度：O(n)
"""

"""
方法二：
对于[1,2,3,4,5,6,7][1,2,3,4,5,6,7]，
根据k=k\%nk=k%n，将数组分为两段：

第一段，对应数组下标范围[0,n-k-1][0,n−k−1]段，即[1,2,3,4][1,2,3,4]
第二段，对应数组下标范围[n-k,n-1][n−k,n−1]，即[5,6,7][5,6,7]
分为三步：

反转第一段，[4,3,2,1,5,6,7]
反转第二段，[4,3,2,1,7,6,5]
反转整体，[5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:   
        n=len(nums)
        k=k%n
        def swap(l,r):
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        swap(0,n-k-1)
        swap(n-k,n-1)
        swap(0,n-1)

时间复杂度：O(n),n为数组长度。
空间复杂度：O(1)
"""





