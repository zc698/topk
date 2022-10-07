Java三种IO的区别

BIO （Blocking I/O）：同步阻塞 I/O 模式。

NIO （New I/O）：同步非阻塞模式。

AIO （Asynchronous I/O）：异步非阻塞 I/O 模型。

同步阻塞模式：这种模式下，我们的工作模式是先来到厨房，开始烧水，并坐在水壶面前一直等着水烧开。

同步非阻塞模式：这种模式下，我们的工作模式是先来到厨房，开始烧水，但是我们不一直坐在水壶前面等，而是回到客厅看电视，然后每隔几分钟到厨房看一下水有没有烧开。

异步非阻塞 I/O 模型：这种模式下，我们的工作模式是先来到厨房，开始烧水，我们不一直坐在水壶前面等，也不隔一段时间去看一下，而是在客厅看电视，水壶上面有个开关，水烧开之后他会通知我。

阻塞 VS 非阻塞：人是否坐在水壶前面一直等。

同步 VS 异步：水壶是不是在水烧开之后主动通知人。

适用场景

BIO 方式适用于连接数目比较小且固定的架构，这种方式对服务器资源要求比较高，并发局限于应用中，JDK1.4 以前的唯一选择，但程序直观简单易理解。

NIO 方式适用于连接数目多且连接比较短（轻操作）的架构，比如聊天服务器，并发局限于应用中，编程比较复杂，JDK1.4 开始支持。

AIO 方式适用于连接数目多且连接比较长（重操作）的架构，比如相册服务器，充分调用 OS 参与并发操作，编程比较复杂，JDK7 开始支持。