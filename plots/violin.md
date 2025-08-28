# Violin

2020-04-16, 15:47
****

## 简介

小提琴图（Violin plot）对一个或多组数值变量的可视化。它类似于箱线图（boxplot），但在两侧增加了一个旋转的核密度图，是箱线图和密度分布（Density Plot）的组合。所以小提琴图可以方便的查看多组数据的分布和概率密度。

其结构如下所示：

<img src="images/2020-03-31-11-13-31.png" alt="violin" width="350" />

说明：

- 中间白色原点为中位数
- 中间的黑色粗线为四分位间距
- 细黑线上下对应最大和最小值。

小提琴图相对箱线图提供了更多信息。当数据量很大，无法显示单个数据点时，使用小提琴尤其合适。数据集较小时，使用包含数据点的 boxplot 也可以。



## 参考

- [https://en.wikipedia.org/wiki/Violin_plot](https://en.wikipedia.org/wiki/Violin_plot)
