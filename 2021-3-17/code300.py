"""
300.�����������
����һ���������� nums ���ҵ�������ϸ���������еĳ��ȡ�

���������������������������У�ɾ������ɾ���������е�Ԫ�ض����ı�����Ԫ�ص�˳�����磬[3,6,2,7] ������ [0,3,1,6,2,2,7] �������С�

ʾ��1��
���룺nums = [10,9,2,5,3,7,101,18]
�����4
���ͣ�������������� [2,3,7,101]����˳���Ϊ 4 ��
���ߣ�LeetCode-Solution
���ӣ�https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
��Դ�����ۣ�LeetCode��
����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������


"""



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
        
"""
ʱ�临�Ӷȣ�O(n^2),����nΪ����nums�ĳ��ȡ�
�ռ临�Ӷ�:O(n)����Ҫ����ʹ�ó���Ϊn��dp���顣
"""

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


ʱ�临�Ӷȣ�O(nlogn)������nums �ĳ���Ϊn�����������������е�Ԫ��ȥ����d���飬������d����ʱ��Ҫ����O(logn) �Ķ���������������ʱ�临�Ӷ�Ϊ O(nlogn)��
�ռ临�Ӷȣ�O(n)����Ҫ����ʹ�ó���Ϊn ��d ���顣
"""
