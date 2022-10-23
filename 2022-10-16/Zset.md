#Zset

zadd myset 1 one:添加一个值

zadd myset 2 two 3 three :添加多个值

排序实现：  
zdd salary 2500 xiaoming  
zdd salary 5000 zhangsan  
zdd salary 100 zxc  

ZRANGEBYSCORE salary -inf +inf:从小到大排序  

ZRANGEBYSCORE salary -inf +inf withscores:显示所有用户并且附带成绩  

ZRANGEBYSCORE salary -inf 2500 withscores:显示小于2500所有用户和成绩升序排序  

 



zrm  

zadd myset 1 hello
zadd myset 2 world 3 zxc
zcount myset 1 3:获取指定区间的成员数量
(interger) 3

案例思路：set 排序 存储班级成绩表，工资排序表。