"""
232.��ջʵ�ֶ���
�����ʹ������ջʵ�������ȳ����С�����Ӧ��֧��һ�����֧�ֵ����в�����push��pop��peek��empty����

ʵ�� MyQueue �ࣺ

void push(int x) ��Ԫ�� x �Ƶ����е�ĩβ
int pop() �Ӷ��еĿ�ͷ�Ƴ�������Ԫ��
int peek() ���ض��п�ͷ��Ԫ��
boolean empty() �������Ϊ�գ����� true �����򣬷��� false

���룺
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
�����
[null, null, null, 1, 1, false]

���ͣ�
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/implement-queue-using-stacks
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������


˼·��
ʹ������ջ��������ջ���������˳��ߵ�������ѡ�����ջ����Ԫ����������ŵ������ջ�����ٴӡ����ջ������Ԫ�ص�ʱ������Ը���������ʵ�����Ƚ��ȳ���
"""

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty(),

"""
ʱ�临�Ӷȣ�push() ʱ�临�Ӷ��� O(1)��peek()/pop() ��̯ʱ�临�Ӷ��� O(1)�������������ʱ�临�Ӷ��� O(N)��
�ռ临�Ӷȣ�O(N)����Ϊ�ܵ�ռ����N ��Ԫ�صĿռ䡣
"""






