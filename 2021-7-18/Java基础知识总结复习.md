# 1.Java运行原理 #

  HelloWorld.java文件通过Javac编译为HelloWorld.class，再通过Java执行并运行结果。

# 2.Java注释 #
  1.单行注释：//
  2.多行注释：/*...*/
  3.文档注释：/**..*/

# 3.标识符命名 #
标识符定义：Java 语言中，对于变量，常量，函数，语句块也有名字，我们统统称之为 Java 标识符.  

标识符作用：标识符是用来给类、对象、方法、变量、接口和自定义数据类型命名
的。  

标识符命名规则：Java 标识符由数字，字母和下划线（_），美元符号（$）组成。
在 Java 中是区分大小写的，而且还要求首位不能是数字。最重要的是，Java 关键字
不能当作 Java 标识符。  

# 4.数据类型 #
1.基本数据类型：  
数值型：  
（1）整数类型：byte，short，int，long  
（2）浮点类型：float，double  
字符型：char  
布尔型：boolean  
2.引用数据类型:  
类class，接口interface，数组  

# 5.数组 
数组：数组是 java 中最常见的一种数据结构，可用于存储多个数据。  
数组的定义：type [] arrayName;或者 type arrayName[];  
实例：int []arr;int arr[];  
数组的初始化：  
1.静态初始化：  
格式 arrayName=new type[]{element1,element2,element3.....}  
实例：int  arr1[]=new int[]{1,2,3};  
2.动态初始化：  
格式 arrayName=new type[length];  
实例：int arr2[]=new int[3];//默认为3个0  

# 6.面向对象 
定义：以基于对象的思维去分析和解决问题，万物皆对象；  
特性：封装，继承，多态  

# 7.方法 
方法重载：方法名称相同，但是参数的类型或者参数的个数不同。  
static 方法：方法属于类本身； 调用方式：1，类名.方法；2，对象.方法  
普通方法： 方法属于类的对象；调用方式：1，对象.方法





