# Histogram


2026-07-20⭐
@author Jiawei Mao
***

## 简介

![histogram](images/2020-04-01-11-17-21.png)

以图形方式展示 1D 数值型数据的分布。适合用来显示连续间隔或时间段内数据分布。

输入 1D 数值型数据，以指定宽度将变量划分为多个 bins，每个 bin 的高度表示该范围内数据的个数。直方图的面积等于数据的总量。

**特点**：可以在同一坐标轴展示多个变量的分布情况。

直方图有助于估计数值集中位置、上下极值以及是否存在差异、异常值，也可以粗略显示概率分布，其结构如下所示：

<img src="images/2020-04-01-11-19-48.png" alt="histogram" style="zoom:50%;" />

每一个长条高度表示落在该区间内数据的个数。

## bin size

每个 bin 中数据的个数以 bar 的高度表示，所以不同的 bin 宽度，对结果展示影响很大。

## 工具

- [d3](https://observablehq.com/@d3/bar-chart)
- [R](https://www.r-graph-gallery.com/83-histogram-with-colored-tail)
- [seaborn](https://python-graph-gallery.com/histogram/)
- [Data to Viz](https://www.data-to-viz.com/caveat/bin_size.html)
