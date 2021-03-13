#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  code21.py
# 21.�ϲ�������������
# ��������������ϲ�Ϊһ���µ� ���� �������ء���������ͨ��ƴ�Ӹ�����������������нڵ���ɵġ� 
#  ���룺l1 = [1,2,4], l2 = [1,3,4]
#  �����[1,1,2,3,4,4]
# ˼·��list1[0] + merge(list1[1:],list2) list1[0] < list2[0];list2[0] + merge(list1,list2[1:]) otherwise
#��������ͷ��ֵ��С��һ���ڵ���ʣ��Ԫ�ص�merge��������ϲ�
#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/merge-two-sorted-lists

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#ʱ�临�Ӷȣ�O(n + m) n��m��ʾ��������ĳ���
#�ռ临�Ӷȣ�O(n + m) n��m��ʾ��������ĳ���
