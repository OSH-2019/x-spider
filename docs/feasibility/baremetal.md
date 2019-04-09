## 裸机编程

考虑到许多物联网设备没有操作系统，或者只有为某些程序定制的操作系统，Rain不能运行在这些设备上，所以我们想把Rain改成裸机程序，使它的运行不依赖于操作系统。

由于Rain是用Rust写的，而Rust语言写的程序编译后可以直接在裸机运行，因此适用于裸机编程。我们也将用Rust语言进行修改。

### 层次与可移植性

裸机编程的一个重要的问题是要具有良好的可移植性。裸机程序与硬件直接相关，而不同硬件的设计区别很大。每个供应商，甚至是单个制造商的每个系列都提供不同的外围设备和功能，与这些外围设备交互的方式也会有所不同。如果把硬件部分的代码和软件程序都写在一起，那么换到另一个硬件设备上时，需要改动整个源码，工作量巨大。因此，裸机编程必须是分层的。层次通常如下图：(crate是Rust的编译单元)

![img](https://rust-embedded.github.io/book/assets/rust_layers.svg)

其中非常重要的一层是**HAL（Hardware Abstraction layer，硬件抽象层）**。嵌入式设备的HAL是一组特征（trait），定义了HAL实现、驱动程序和应用程序(或固件)之间的实现契约。这些契约包括功能(例如，如果一个trait是为某个特定类型实现的，那么HAL实现提供了一个特定的功能)和方法(例如，如果你能构造一个实现trait的类型，那么你就能保证在trait中指定的方法是可用的)。这些traits包括：

- GPIO (input and output pins)
- Serial communication
- I2C
- SPI
- Timers/Countdowns
- Analog Digital Conversion

其余的中间层也都是对下层的不同程度的抽象，向上层提供接口。这些层次写起来工作量比较大，而GitHub上已有写好的部分，我们会利用这些已有的代码加入到Rain中。在GitHub上有一个叫做[rust-embedded](https://github.com/rust-embedded)的仓库，由一个团队开发和维护，致力于推广Rust在嵌入式设备上的应用。这个仓库中有裸机编程需要用到的多个层次，包括Peripheral Access Crate，HAL implementation crates，Architecture support crates，Board support crates，Driver crates等。树莓派3B+配备的是 ARM Cortex-A53 处理器，这个仓库中有支持ARM架构、Cortex-A的crates，也有支持树莓派多种外设的驱动crates。所以在层次方面，我们只需要选取合适的已有的crates，组成软硬件之间的中间层，然后在Rain中添加和修改代码，使用中间层提供的接口，实现原本需要操作系统来完成的功能。

### no_std & libcore

在裸金属环境中，没有操作系统提供的软件，无法加载标准库。该程序及其使用的crates只能使用硬件(裸金属)运行。为了防止程序加载标准库，可以使用no_std。

#![no_std]是一个crates属性，指示crates将链接到core-crate而不是std-crate。

标准库中与平台无关的部分可以通过libcore获得。libcore crate是std crate的一个与平台无关的子集，它对程序将运行的系统不做任何假设。因此，它为浮点数、字符串和片等语言原语提供api，以及公开原子操作和SIMD指令等处理器特性的API。然而，它缺乏用于任何涉及平台的API。libcore还排除了一些在嵌入式环境中不常用的东西，如用于动态内存分配的内存分配器，如果需要这些额外的功能，要去找提供这些功能的crates。

Rain原本是运行在操作系统上的，因此使用的是Rust标准库，在裸机上必须换用内核库。但是Rain用到的与平台相关的调用，不能用内核库实现，需要借助上面提到过的HAL自行实现。

### 函数的循环和panic

Rain的main函数会返回到操作系统，而裸机上没有操作系统，所以main函数中必须有一个无限循环，循环一直进行，直到进入其它函数或者发生错误触发panic。

### 调度

没有了操作系统，就没有了线程和线程的调度。但是要让Rain可以在嵌入式设备上使用，必须要实现多任务处理，以为设备本身要进行某种任务，只在空闲时间运行Rain。调度一般有两种方式：抢占式和非抢占式。这里应采用抢占式调度方法，只在设备不执行本身的任务时运行Rain，当设备要执行任务时，立即保存和中断Rain的执行。为了模拟多任务处理的情境，在实验时，给树莓派一个任务，比如接一个温度传感器，每隔一段时间，测量一次气温通过互联网发送给电脑，同时让Rain运行在树莓派后台，编写这两个任务之间的调度程序。

### 如何调试

Rain原本用于部署在Linux系统上，通过命令行进行交互，用户可以通过Rain在命令行中输出的信息看到Rain的运行状态。但是在嵌入式设备上，没有显示器，更没有命令行，所以要用USB转串口线把树莓派连接到电脑上，用串口通信来调试树莓派，如下图，用树莓派的GPIO引脚连接转换器。用OpenOCD（Open On-Chip Debugger）和GDB工具在Linux主机上调试树莓派，可以对内核代码设置断点，逐句调试等。

Rain的源码中关于命令行输入输出的部分需要删除或修改。![img](https://github.com/rust-embedded/rust-raspi3-OS-tutorials/raw/master/doc/wiring_jtag.png)