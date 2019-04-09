
# 将rain部署到raspbian

## 项目介绍

本项目旨在将[Rain](https://github.com/substantic/rain)（一个开源的Rust语言编写的分布式计算框架）从Linux系统移植到raspbian系统上，使树莓派成为分布式计算节点，能够接收、执行和返回服务器分发的计算任务；缩减和优化Rain代码，使其更加轻量、快速，并且能够长期在树莓派的后台运行，不影响其他运行在树莓派上的程序，以此实现对以树莓派为代表的物联网设备的闲置算力的有效利用。如果时间允许，还将尝试对Rain进行裸机编程的改造，提高Rain的运行速度，同时使Rain适用于更多物联网设备。

目前，经过初步的尝试，分布式的计算框架rain已经可以被移植到raspbian上并且正常运行。我们小组打算在目前工作上更进一步，在现有框架上进行易用性，高效性与普适性等方面的改造。目前我们计划的工作如下。我们对每个具体工作进行了可行性调研，并根据具体实施难度与实际意义选择其中一部分尝试实现。

+ 尝试将rain部署在安卓设备上。
+ 将rain部署于树莓派裸机上。
+ 改进rain的调度算法
+ 对rain的通讯方式进行改造

## 将rain部署于raspbian

### rain的主要特点
rain是一个分布式计算框架。在表层上，其主要由两个部分组成：一个叫rain的一体化静态链接二进制文件，和一个用于调用rain服务的仅限python的库。

在底层上，rain的二进制文件包含了server，executor与governor三个主要组成部分。其中：

+ server是服务器节点，用于与其他计算节点通信，管理其余计算节点，并进行任务分配与调度，收集计算结果。
+ governor是计算节点的调控管理者，用于与服务器节点通信，接收服务器节点分配的任务与数据，生成executor执行这些任务，并将结果返回给服务器节点。
+ executor是在计算节点由governor生成的用于执行计算任务的部分。rain中内置了部分简单的executor用于简单测试功能（如将两个字符串合并），也支持使用python的通用executor，还提供了rust与c的库，以方便用户编写自己的专用executor。

由于rain将服务器功能与计算节点功能融合进了一个二进制文件中，则目标机器是服务器还是计算节点取决于如何执行rain。执行

    rain start --simple

会将server与governor都部署于本地机器上。执行

     rain start -S --governor-host-file=my_hosts

会将server部署于本地，从my_hosts文件中读取计算节点信息，并使用ssh连接计算节点。执行

    rain governor <SERVER-ADDRESS>

会在本机上启动一个计算节点。它将尝试与server通信，从而接收数据与计算任务。

由于rain本身一体化的设置与便于使用的特性，对其进行直接移植的便利性大大增强。只需将rain编译为能在arm架构树莓派上运行的一个一体化二进制文件就能实现大部分工作。

### rust的主要特点
Rust是一种系统编程语言，专注于三个目标：安全性、速度和并发性。Rust同样类似于C，是一种静态的强类型系统编程语言，但解决了c广为诟病的安全性问题。

rust还具有以下特点，方便了rain的移植工作：

+ rustup
  官方提供了一个管理 Rust 版本和相关工具的命令行工具rustup，它方便地为我们提供版本稳定且统一的rust开发工具。

+ cargo
  Cargo 是 Rust 的构建系统和包管理器。使用cargo来管理 Rust 项目十分容易，它替代了make在大型c项目的作用，同时又不需要编写繁复的类似makefile文件来进行代码构建与项目生成。
  
  cargo利用工程目录下的Cargo.toml文件信息来构建项目。Cargo.toml 包含了各类杂项信息如作者，时间，版本等，同时也包含项目构建所必需的信息，如所需的库和依赖。

  在Cargo.toml 中指定所需的库时需要显式地指定库的版本。当搭建项目时发现本地缺乏库或版本不一致时，cargo会自动从官方地址下载获取对应所需的库，而不需手动添加。这使得项目的编译搭建与项目的移植变得容易。同时使用 Cargo 的一个额外的优点是，不管你使用什么操作系统，其命令都是一样的，为跨平台的工作带来便利。

+ 多平台支持
  rust编译支持众多[平台](https://forge.rust-lang.org/platform-support.html)，其中不乏树莓派。rust为跨平台编译也提供了工具链。构建项目时使用target=armv7-unknown-linux-gnueabihf，并配合树莓派官方交叉编译工具链，便可以方便地构建raspbian上运行所需要的格式。

由于rain主要是由rust搭建而成，以上特点使得rain的移植更为便利。

### 搭建与部署过程简述

由于rain项目的搭建除了需要Cargo.toml中指定的依赖外还需要SQLite3，则rain迁移到树莓派主要分为以下两步：
+ SQLite3在arm架构下的交叉编译与库生成
+ rain的交叉编译与生成

#### SQLite3
从官方获取 sqlite3源码，使用以下指令配置交叉编译信息

    ./configure --host=arm-linux --prefix=$INSTALL_PATH CC=arm-linux-gnueabihf-

并使用make编译，然后使用make install安装到指定路径。

将安装路径中lib文件夹中的库文件libsqlite3.a，libsqlite3.so等复制到交叉编译工具链目录下的lib文件夹中，即完成了适合树莓派使用的SQLite3库的编译与安装。

#### rain
利用git获取rain源码，直接使用cargo构建项目

    cargo build --release target=armv7-unknown-linux-gnueabihf

此时cargo会自动下载交叉编译所需额外工具，然后开始编译。若未将sqlite3相关库文件添加，则会在编译时出现以下错误

    ld: can not find lsqlite3

若正确地添加了适用于树莓派的sqlite3库，则编译将顺利进行，二进制文件被至于target文件夹中。

#### 尝试部署运行
将生成的二进制文件置于树莓派中运行。

rain能顺利运行。则rain可以较容易地被部署于树莓派上，并利用树莓派作为计算节点参与计算贡献算力。
