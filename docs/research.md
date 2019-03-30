# 这是题目

## 小组成员
队长：詹佑翊

队员：曹宇昂 万琪 琚泽谦 张衎

## 项目简介

## 项目背景

## 立项依据

## 前瞻性及重要性

## 相关工作

### MapReduce
MapReduce是Hadoop框架中的一个编程模型或模式，用于访问存储在Hadoop文件系统(HDFS)中的大数据。

使用MapReduce，不是将数据发送到应用程序或逻辑所在的位置，而是在数据已经所在的服务器上执行逻辑，以加快处理速度。

#### MapReduce是如何工作的:
MapReduce的核心是两个功能:Map和Reduce。 Map函数将磁盘中的输入作为<key，值>对，处理它们，并生成另一组中间<key，值>对作为输出。Reduce函数还将输入作为<key，值>对，并生成<key，值>对作为输出。
输入数据首先被分割成更小的块。然后将每个块分配给一个mapper进行处理。这期间均经历以下过程：

+ Combine：一个可选过程。combiner是一个在每个mapper服务器上单独运行的reducer。它将每个mapper上的数据进一步简化为简化形式，然后再传递给下游。这使得洗牌和排序更容易，因为要处理的数据更少。

+ Partition：将mapper生成的<key、值>对转换为另一组<key、值>对以提供给reducer的过程。它决定如何将数据呈现给reducer，并将其分配给特定的reducer。

+ Reduce：在所有mapper完成处理之后，框架在对结果进行排序再传递给reducer。当映射程序还在进行中时，reducer不能启动。所有具有相同key的映射输出值都分配给一个单一的reducer，然后该reducer聚合该key的值。MapReduce是Hadoop框架中的一个编程模型或模式，用于访问存储在Hadoop文件系统(HDFS)中的大数据。

![MapReduce](./files/MapReduce.jpg "MapReduce")

### Apache Spark
它具有以下特点：
+ 执行速度极快：首先它支持将计算任务的中间结果放在内存中而不是HDFS上，这样可以加快速度，根据评测最高可以提升100倍。
+ 支持多种运行模式：除了可以独立在集群上执行任务以外，Spark还支持将任务执行在EC2或Apache Hadoop的YARN上，也可以从HDFS、Cassandra、HBase、Hive等。各种数据存储系统中读取数据。
+ 更多更通用的计算模型：I-ladoop只提供了较为底层的MapReduce模型，编程人员往往需要大量编码来解决简单的任务。而spark则提供了SQL接口、APachespark流模型接口、MLib机器学习接口以及GraphX图形计算接口等多种接口，可以方便应用于多种场合，提高开发人员的开发效率。


### Apache Storm
Apache storm是一个开源的、实时的计算平台，最初由社交分析公司Backtype的NathanMarz编写，后来被Twitter收购，并作为开源软件发布。从整体架构上看，Apache Storm和Hadoop非常类似。Apache Storm从架构基础本身就实现了实时计算和数据处理保序的功能，而且从概念上看，Apache Storm秉承了许多Hadoop的概念、术语和操作方法。
Apache Storm作为实时处理系统中的一个典型案例，其特点和优势如下。
+ 高可扩展性：Apache Storm可以每秒处理海量消息请求，同时该系统也极易扩展，
只需增加机器并提高计算拓扑的并行程度即可。根据官方数据，在包含10个节点的Apache Storm集群中可以每秒处理一百万个消息请求，由此可以看出Apache Storm的实时处理性能优越。
+ 高容错性：如果在消息处理过程中出现了异常，Apache Storm的消息源会重新发送相关元组数据，确保请求被重新处理。
+ 易于管理：Apache Storm使用Zookeeper来协调集群内的节点配置并扩展集群规模。
+ 消息可靠性：Apache Storm能够确保所有到达计算拓扑的消息都能被处理。


### Pregel
Pregel在概念模型上遵循BSP模型。整个计算过程由若干顺序运行的超级步（Super Step）组成，系统从一个“超级步”迈向下一个“超级步”，直到达到算法的终止条件  

Pregel在编程模型上遵循以图节点为中心的模式，在超级步S中。每一个图节点能够汇总从超级步S-1中其它节点传递过来的消息，改变图节点自身的状态。并向其它节点发送消息。这些消息经过同步后。会在超级步S+1中被其它节点接收并做出处理。用户仅仅须要自己定义一个针对图节点的计算函数F(vertex)，用来实现上述的图节点计算功能。至于其它的任务，比方任务分配、任务管理、系统容错等都交由Pregel系统来实现。典型的Pregel计算由图信息输入、图初始化操作，以及由全局同步点分割开的连续运行的超级步组成，最后可将计算结果进行输出。

每一个节点有两种状态：活跃与不活跃，刚开始计算的时候，每一个节点都处于活跃状态，随着计算的进行，某些节点完毕计算任务转为不活跃状态，假设处于不活跃状态的节点接收到新的消息，则再次转为活跃，假设图中全部的节点都处于不活跃状态，则计算任务完毕，Pregel输出计算结果。
![Pregel](./files/Pregel.png "Pregel")

### Baidu Bigflow
Baidu Bigflow是百度的一套计算框架，它致力于提供一套简单易用的接口来描述用户的计算任务，并使同一套代码可以运行在不同的执行引擎之上。用户基本可以不去关心Bigflow的计算真正运行在哪里，可以像写一个单机的程序一样写出自己的逻辑， Bigflow会将这些计算分发到相应的执行引擎之上执行。

## 参考文献
https://www.talend.com/resources/what-is-mapreduce/

https://stanford.edu/~rezab/classes/cme323/S15/notes/lec8.pdf

https://baidu.github.io/bigflow/zh/index.html

卢誉声.分布式实时处理系统：原理、架构与实现[M].机械工业出版社:北京,2016.6:2-14.