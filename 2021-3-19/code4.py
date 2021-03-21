4. Ѱ�����������������λ��
����������С�ֱ�Ϊ m �� n �����򣨴�С�������� nums1 �� nums2�������ҳ���������������������� ��λ�� ��
���룺nums1 = [1,3], nums2 = [2]
�����2.00000
���ͣ��ϲ����� = [1,2,3] ����λ�� 2

#˼·������һ��������numst����nums1��nums2����ϲ���������numst�У�������numst��������,Ȼ�������λ���Ķ����������������ȡֵ��
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numst = nums1 + nums2
        numst.sort()
        n = len(numst)
        if n % 2 == 0:
            return ((numst[n // 2 - 1] + numst[n // 2 ])/2)
        else:
            return numst[n // 2]
            
            
ʱ�临�Ӷȣ�O(m + n)
�ռ临�Ӷȣ�O(m + n)

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
       
            
            - ��Ҫ˼·��Ҫ�ҵ��� k (k>1) С��Ԫ�أ���ô��ȡ pivot1 = nums1[k/2-1] �� pivot2 = nums2[k/2-1] ���бȽ�
            - ����� "/" ��ʾ����
            - nums1 ��С�ڵ��� pivot1 ��Ԫ���� nums1[0 .. k/2-2] ���� k/2-1 ��
            - nums2 ��С�ڵ��� pivot2 ��Ԫ���� nums2[0 .. k/2-2] ���� k/2-1 ��
            - ȡ pivot = min(pivot1, pivot2)������������С�ڵ��� pivot ��Ԫ�ع��Ʋ��ᳬ�� (k/2-1) + (k/2-1) <= k-2 ��
            - ���� pivot �������Ҳֻ���ǵ� k-1 С��Ԫ��
            - ��� pivot = pivot1����ô nums1[0 .. k/2-1] ���������ǵ� k С��Ԫ�ء�����ЩԪ��ȫ�� "ɾ��"��ʣ�µ���Ϊ�µ� nums1 ����
            - ��� pivot = pivot2����ô nums2[0 .. k/2-1] ���������ǵ� k С��Ԫ�ء�����ЩԪ��ȫ�� "ɾ��"��ʣ�µ���Ϊ�µ� nums2 ����
            - �������� "ɾ��" ��һЩԪ�أ���ЩԪ�ض��ȵ� k С��Ԫ��ҪС���������Ҫ�޸� k ��ֵ����ȥɾ�������ĸ���
            
            
            index1, index2 = 0, 0
            while True:
                # �������
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # �������
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


���ߣ�LeetCode-Solution
���ӣ�https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
��Դ�����ۣ�LeetCode��
����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������
ʱ�临�Ӷȣ�O(log(m + n))
�ռ临�Ӷȣ�O(1)
"""
