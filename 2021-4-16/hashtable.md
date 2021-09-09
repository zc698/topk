# 哈希表是什么？ #

散列表（Hash table，也叫哈希表），是根据键（Key）而直接访问在内存存储位置的数据结构。也就是说，它通过计算一个关于键值的函数，将所需查询的数据映射到表中一个位置来访问记录，这加快了查找速度。这个映射函数称做散列函数，存放记录的数组称做散列表。

# hash表中为了防止冲突过多常用素数，为什么？ #

首先来说假如关键字是随机分布的，那么无所谓一定要模质数。但在实际中往往关键字有某种规律，例如大量的等差数列，那么公差和模数不互质的时候发生碰撞的概率会变大，而用质数就可以很大程度上回避这个问题。

# Hash 表常见操作的时间复杂度是多少？遇到 Hash 冲突是如何解决 #

一般：O(1)，最差：O(N)

参考文档：
[https://blog.csdn.net/Beyond_2016/article/details/81286360](https://blog.csdn.net/Beyond_2016/article/details/81286360)
