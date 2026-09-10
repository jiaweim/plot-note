# Circos

## 简介

Circos 是一款用于环形布局展示数据的软件包。因此 Circos 非常适合用于展示探索对象或位置之间的相互关系。目前，Circos 图表已出现在数千篇科学出版物中。尽管它最初是为基因组数据的可视化而设计的，但同样能够基于任何领域的数据生成图表。

## 背景

Circos 支持多种不同的图表类型，例如直方图、散点图和热图等。每个 Circos 图表可以包含多个轨道（tracks），每个轨道内又可嵌套不同的子图，这使得它非常适合用于高维数据的可视化。

### 1. 安装与配置

#### 1.1 UNIX vs WINDOWS

运行 Circos 需要安装 Perl。Perl 是一种解释型语言，这意味着您无需对 Circos 进行编译即可运行它。Circos 的代码由 Perl 可执行文件读取，该文件会负责代码的解释、编译与运行。安装 Circos 非常简单，只需解压压缩包即可1。

Circos 的设计理念对 UNIX 用户来说非常熟悉：没有图形用户界面，采用纯文本配置文件和命令行工具。如果您是 Windows 用户，起初可能会觉得有些不习惯。本节中关于安装、配置和 Perl 模块的教程，将详细讨论 Circos 在 UNIX 和 Windows 系统上使用的差异1。

运行 Circos 不需要您精通 Perl 语言，但您需要熟悉以下基本概念：

- 目录与文件的概念
- 在命令行提示符下切换/导航目录
- 在命令行提示符下创建和删除目录
- 绝对路径与相对路径的概念（例如：`/path/file.txt` 与 `../file.txt` 或 `file.txt` 的区别）1

在 UNIX 系统中，您将完全通过命令行和文本编辑器进行操作。如果您是 Windows 用户，且不熟悉 DOS 命令行，建议先阅读以下教程：

- Windows 命令行教程
- 15分钟掌握 Windows 命令行提示符1

## 参考

- https://circos.ca/guide/
- https://circos.ca/tutorials/tutorials/
- https://training.galaxyproject.org/training-material/topics/visualisation/tutorials/circos/tutorial.html