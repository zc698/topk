# String 类能不能被继承？为什么？ #

不能，因为String类被final修饰符修饰了

final修饰符的限定  
final修饰符修饰类，此类为终极类，不能再被继承  
final类修饰变量，则此变量一经赋值，就不能被改变  
final修饰基本变量，不能修改值  
final修饰引用对象，不能修改指向其他对象  

被final修饰变量的初始化问题  
当修饰变量为成员变量时，必须要在构造函数或者直接new  
当修饰变量为静态变量时，必须要在static块或者直接new

参考文档：  
[https://www.wolai.com/river1235r/uBSAqypbJbctKpkRQ2RXZc](https://www.wolai.com/river1235r/uBSAqypbJbctKpkRQ2RXZc)