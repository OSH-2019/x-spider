# 可行性报告

[项目简介](项目简介)

[项目背景](项目背景)

- [RESTful框架](RESTful框架)
- [cap'n Proto](cap'n Proto)

[技术路线](技术路线)

[参考资料](参考资料)

## 项目简介

本项目主要是去完成Rain作者自己提出来的一个优化方向：为客户机应用程序创建一个REST API，简化新语言中的API创建，并将其与仪表板/状态查询API统一。原来作者提供的机器通信部分使用的是capnp API，显得有点笨手笨脚，作者想要实现REST API规范，可以为用户提供更大的方便。

## 项目背景

**RESTful 框架**

REST这个词，是Roy Thomas Fielding在他2000年的博士论文中提出的。REST即Representational State Transfer的缩写，翻译是"表现层状态转化"。直接看中文翻译很难理解，不急，慢慢看REST的相关介绍。

Fielding是一个非常重要的人，他是HTTP协议（1.0版和1.1版）的主要设计者、Apache服务器软件的作者之一、Apache基金会的第一任主席。所以，他的这篇论文一经发表，就引起了关注，并且立即对互联网开发产生了深远的影响。

他这样介绍论文的写作目的：

"本文研究计算机科学两大前沿----软件和网络----的交叉点。长期以来，软件研究主要关注软件设计的分类、设计方法的演化，很少客观地评估不同的设计选择对系统行为的影响。而相反地，网络研究主要关注系统之间通信行为的细节、如何改进特定通信机制的表现，常常忽视了一个事实，那就是改变应用程序的互动风格比改变互动协议，对整体表现有更大的影响。**我这篇文章的写作目的，就是想在符合架构原理的前提下，理解和评估以网络为基础的应用软件的架构设计，得到一个功能强、性能好、适宜通信的架构。**"

那么，在Fielding眼里，什么样的通信架构算的上是**功能强、性能好、适宜通信**呢？

那么我们直接来看看REST框架有什么特点：

- 为所有资源定义ID
- 将所有资源链接在一起
- 使用标准方法
- 资源多重表述
- 无状态通信

下面我们来一个一个看一下这些特点。

**为所有资源定义ID**

所谓"资源"，就是网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的实在。你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。所谓"上网"，就是与互联网上一系列的"资源"互动，调用它的URI。

很显然，为所有资源定义ID在创建工程时会带来更多工作量，但是有了统一的定位符之后，带来的好处是不言而喻的。

在这里我还想提一点，起初我看到这个介绍的时候，脑子里第一想法是，难道其他通信不是这样设计的吗？后来我去调查了一下SOAP，在客户端和服务器间通信时，它是将所需要的信息全部打包在一个XML文件里，一并传送，只实现到客户端和服务器的对应关系，并不是所有资源都有一个ID。比如，在客户机上看服务器端上的文件，并不能实现对所有服务器端上的资源访问（有权限的先不考虑）。

顺带一提，URI的规范性也很重要，为了避免URI的重复，以及URI尽可能有意义(名字能包含它的信息)，REST有一套规范的命名方式。

**将所有资源链接在一起**

字面意思解读，使用URI可以指向被标志的事物，所有资源都链接在一起了。

**使用标准方法**

那么，我们现在有了一个访问资源的方式，下一步自然想的是，我该怎么进行对资源的操作呢？

我想到的基本操作是：增删改查(类似于数据库的基本操作方式)。REST框架提出的要求是，对资源的操作提供一套标准的基本方法，用户需要的其他复杂的操作在这些基本方法上面构成（由用户自己设计）。这样的好处自然就是规范化带来的好处，适用性广，方便，可阅读性强。一般来说，现在客户端借用的方法其实也就是http协议给出的基本方法，例如get, post, put, push等等。

**资源多重表述**

理想情况下，所有资源如果有统一的表述方式，那么所有的信息传输问题都会变的简单许多，不需要考虑跨平台，语言不同，处理器架构不同等一系列的问题。不幸的是，这不会在现实情况中发生。那么，假如我的资源有HTML和XML两种表述方式，就意味着我的资源能被可以处理这两种表述方式的服务器接收。如果我的资源拥有更多的资源表述方式，就意味着这个资源可以被更多机器利用。资源多重表述，可以使得资源的流通性更强，更加广泛。

**无状态通信**

无状态通信，即服务器端不能保持除了单次请求之外的，任何与其通信的客户端的通信状态。比如，我们点击一个网页链接，服务器端把所需要的数据全部发送过来，然后就与我的本地电脑断开链接，服务器端的变化不会影响已经在我PC上的网页的内容变化。这样的好处就是节省服务器端内存，若要保持有状态通信，服务器端需要分配一些内存来记录我的个人电脑上的状态，若有很多客户端同时访问，这自然会严重影响到服务器端的内存。

总结：这五点内容是REST风格最主要的五点。REST只是一种风格，按这种风格实现的RPC（Remote Procedure Call）就是REST。

**cap'n Proto**

自称是比proto buffer协议快上infinity times的数据交互格式。(这只是从编码的过程考虑)

下面附上官方给出的比较图片：

![infinity_times_faster](./images/infinity_times_faster.png)





实际上这只是官方给的一个噱头。因为这个比较标准并不公平(官方后面也有澄清)。这个比较只是测试了编码/解码的过程的时间，而capnp是不需要编码，解码过程的，自然快上无限倍了。(笑)

官方对于capnp的描述是：The Cap’n Proto encoding is appropriate both as a data interchange format and an in-memory representation, so once your structure is built, you can simply write the bytes straight out to disk!

百度翻译如下：cap'n协议编码既适用于数据交换格式，也适用于内存表示，因此一旦构建了结构，您就可以直接将字节写入磁盘！

这是不是很神奇？

具体细节，个人能力有限，无法弄明白到底是怎么实现的。不过，我们这引出了几个需要思考的问题，如果不需要编码，capnp文件格式是不是只针对特定平台使用的呢？

官方给出解释：

NO! The encoding is defined byte-for-byte independent of any platform. However, it is designed to be efficiently manipulated on common modern CPUs. Data is arranged like a compiler would arrange a struct – with fixed widths, fixed offsets, and proper alignment. Variable-sized elements are embedded as pointers. Pointers are offset-based rather than absolute so that messages are position-independent. Integers use little-endian byte order because most CPUs are little-endian, and even big-endian CPUs usually have instructions for reading little-endian data.

简单来说，就是编码是按字节定义的，支持现在的大部分CPU。

## 技术路线

本项目目标是，把capnp文件部分改写使其符合REST风格，源码里面.capnp文件部分总共代码也就1000行。当然，不仅仅只改动.capnp文件，还需要把dashboard/status query部分的代码也一并修改。所以，接下去的工作，就是把涉及到dashboard/status query部分的代码也找出来，然后按照REST风格的要求对所有源码逐一检查和修改。

可行性分析：要保证在修改API的情况下，不修改核心源码而仍正常使用有点困难。为解决核心源码函数调用改动的部分，有两个方法：1.不修改核心源码，把现有.capnp文件作为中间层，再写一个符合RESTful的底层方法函数 2.同时修改核心源码的调用函数部分和.capnp文件。

## 参考资料

1.http://www.ruanyifeng.com/blog/2011/09/restful.html 阮一峰：理解RESTful架构

2.<https://www.infoq.cn/article/rest-introduction> Stefan Tilkov：深入浅出REST

3.https://capnproto.org/index.html Cap'n Proto