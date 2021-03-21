5.������Ӵ�
����һ���ַ��� s���ҵ� s ����Ļ����Ӵ���
���룺s = "babad"
�����"bab"
���ͣ�"aba" ͬ���Ƿ�������Ĵ𰸡�

#˼·��
��1��������״̬
dp[i][j] ��ʾ�Ӵ� s[i..j] �Ƿ�Ϊ�����Ӵ��������Ӵ� s[i..j] ����Ϊ����ұ����䣬����ȡ�� s[i] �� s[j]��
��2����˼��״̬ת�Ʒ���
dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
�߽������ǣ����ʽ [i + 1, j - 1] ���������䣬�������ϸ�С�� 2���� j - 1 - (i + 1) + 1 < 2 ������� j - i < 3��
�� s[i] == s[j] ������ j - i < 3 ��ǰ���£�ֱ�ӿ����½��ۣ�dp[i][j] = true�������ִ��״̬ת�ơ�
��3�������ǳ�ʼ��
��ʼ����ʱ�򣬵����ַ�һ���ǻ��Ĵ�����˰ѶԽ����ȳ�ʼ��Ϊ true���� dp[i][i] = true ��
��4�����������
ֻҪһ�õ� dp[i][j] = true���ͼ�¼�Ӵ��ĳ��Ⱥ���ʼλ�ã�û�б�Ҫ��ȡ��������Ϊ��ȡ�ַ���ҲҪ�������ܣ���¼��ʱ�Ļ����Ӵ��ġ���ʼλ�á��͡����ĳ��ȡ����ɡ�


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start = 0
        max_len = 1
        dp = [[(False) for _ in range(n) ] for _ in range(n)]
        for i in range (n):
            dp[i][i] = True
        for j in range(1,n):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i +1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
        
        
ʱ�临�Ӷȣ�O(N^2)
�ռ临�Ӷȣ�O(N^2)
