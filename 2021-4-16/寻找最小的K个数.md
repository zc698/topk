# 寻找最小的K个数 #

0、  咱们先简单的理解，要求一个序列中最小的k个数，按照惯有的思维方式，很简单，先对这个序列从小到大排序，然后输出前面的最小的k个数即可。

1、   至于选取什么的排序方法，我想你可能会第一时间想到快速排序，我们知道，快速排序平均所费时间为n*logn，然后再遍历序列中前k个元素输出，即可，总的时间复杂度为O（n*logn+k）=O（n*logn）。  
2、   咱们再进一步想想，题目并没有要求要查找的k个数，甚至后n-k个数是有序的，既然如此，咱们又何必对所有的n个数都进行排序列?
       这时，咱们想到了用选择或交换排序，即遍历n个数，先把最先遍历到得k个数存入大小为k的数组之中，对这k个数，利用选择或交换排序，找到k个数中的最大数kmax（kmax设为k个元素的数组中最大元素），用时O（k）（你应该知道，插入或选择排序查找操作需要O（k）的时间），后再继续遍历后n-k个数，x与kmax比较：如果x<kmax，则x代替kmax，并再次重新找出k个元素的数组中最大元素kmax‘（多谢kk791159796 提醒修正）；如果x>kmax，则不更新数组。这样，每次更新或不更新数组的所用的时间为O（k）或O（0），整趟下来，总的时间复杂度平均下来为：n*O（k）=O（n*k）。  
3、   当然，更好的办法是维护k个元素的最大堆，原理与上述第2个方案一致，即用容量为k的最大堆存储最先遍历到的k个数，并假设它们即是最小的k个数，建堆费时O（k）后，有k1<k2<...<kmax（kmax设为大顶堆中最大元素）。继续遍历数列，每次遍历一个元素x，与堆顶元素比较，x<kmax，更新堆（用时logk），否则不更新堆。这样下来，总费时O（k+（n-k）*logk）=O（n*logk）。此方法得益于在堆中，查找等各项操作时间复杂度均为logk（不然，就如上述思路2所述：直接用数组也可以找出前k个小的元素，用时O（n*k））。  
4、 按编程之美第141页上解法二的所述，类似快速排序的划分方法，N个数存储在数组S中，再从数组中随机选取一个数X（随机选取枢纽元，可做到线性期望时间O（N）的复杂度，在第二节论述），把数组划分为Sa和Sb俩部分，Sa<=X<=Sb，如果要查找的k个元素小于Sa的元素个数，则返回Sa中较小的k个元素，否则返回Sa中所有元素+Sb中小的k-|Sa|个元素。像上述过程一样，这个运用类似快速排序的partition的快速选择SELECT算法寻找最小的k个元素，在最坏情况下亦能做到O（N）的复杂度。不过值得一提的是，这个快速选择SELECT算法是选取数组中“中位数的中位数”作为枢纽元，而非随机选取枢纽元。  
5、   RANDOMIZED-SELECT，每次都是随机选取数列中的一个元素作为主元，在O（n）的时间内找到第k小的元素，然后遍历输出前面的k个小的元素。 如果能的话，那么总的时间复杂度为线性期望时间：O（n+k）=O（n）（当k比较小时）。