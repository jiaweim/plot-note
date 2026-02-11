# UpSet

## 简介

UpSet 可以看作韦恩图的升级版，用于查看集合的交集：

- 集合数不超过 3：韦恩图更合适
- 更多集合：UpSet 更合适

如下图所示：

<img src="./images/upsetr.png" alt="A simple UpSet Example" width="600" />

UpSet 使用矩阵可视化集合交集。

**应用场景**

UpSet 适合 3-30 个集合数。如果少于 4 组集合，韦恩图更合适。

UpSet 非常适合分析许多数据的分布和属性。

## UpSet 基础

UpSet 将集合的交集绘制为矩阵，如下图所示：

- 每列对应一个集合，顶部的条形图显示集合大小
- 每行对应一个可能的交集：

<img src="./images/concept_1_matrix.svg" alt="Explaining the matrix approach in UpSet." width="300" />

下图通过韦恩图来解释 UpSet：

- 第一行为空，表示不属于任何集合的元素
- 绿色的第三行只属于集合 B 的元素（不属于 A 或 C）
- 橙色的第五行表示集合 A 和 B 包含但 C 不包含的元素
- 最后的紫色 A, B, C 的交集

<img src="./images/concept_2_intersections.svg" alt="Explaining the intersections in UpSet" width="400" />

还可以在矩阵旁边使用条形图绘制交集的大小（cardinality），如下所示：

<img src="./images/concept_3_cardinality.svg" alt="Plotting intersection sizes with bars in UpSet." width="400" />

这样更容易比较交集的大小。

矩阵也非常有用，例如，可以按各种方式排序。通常按从大到小排序，如下图所示。

<img src="./images/concept_4_sorting.svg" alt="Sorting by cardinality in UpSet" width="300" />

UpSet 可以按水平或垂直方向排列。垂直布局更适合可滚动的交互式图，而水平布局更适合论文的 figure。

<img src="./images/concept_5_horizontal.svg" alt="Horizontal layout in UpSet" width="300" />

## 解读 UpSet plot

UpSet 通常很容易阅读。但有一个**注意事项**：当数据集大小相差很大时，在解读时应谨慎（慎读😁）。如下图：

<img src="./images/unequal_set_size.png" alt="UpSet and unequal set sizes." width="600" />

这里查看电影类型，看起来 "Drama" 和 "Comedy" 的交集最大。虽然这种算法没错，但情景剧（Drama）和喜剧（Comedy）似乎不搭。这是因为 Drama 和 Comedy 这两个集合较大导致的。相比 Children 和 Documentary，这两个集合过于大。所以解读 UpSet plot，一定**不能省略集合大小**。

上例显示了另一个指标：假设集合成员是随机的，则交集偏离预期大小的程度。可以看到，如果数据集随机的，comedy-drama 交集比实际要小很多。

## UpSet vs. Venn Diagrams

维恩图不适合可视化超过 3 组集合的交集。下图是发表在 Nature 的 six-set venn diagram，用于可视化植物物种共享的基因，展示香蕉的基因组与其它 5 种植物基因组之间的关系。

![The six set banana venn diagram.](./images/banana.png)

这个图看起来很有意思，但不是很有用。很难从中提取有用信息。

用 UpSet 显示相同数据：

![UpSet showing the banana data.](./images/upsetr-banana.png)

由于数字很小，这个图看起来有点费劲。把后面几个很小的删掉：

![UpSet showing the bana data with small intersections removed. ](./images/upsetr-banana_clipped.png)

这样看起来容易多了，绝大多数基因所有植物共享，如下图：

![UpSet showing the banana data with highlight on largest intersection, which includes all sets.](./images/upset_genome_top.png)

同样，前三个物种（Oryza_sativa, Sorghum_bicolor, Brachypodium_distachyon）似乎高度相关，因为它们为交集中的前三。相比之前，第 6 个物种（Phoenix dactylifera）似乎与其它物种差异最大。

## 高级特性

## UpSet 实现



## FAQ

### 如何创建高分辨率的 UpSet plot

有三种选择：

- 如何更喜欢使用基于网页的交互式版本，可以将交互式 UpSet plot 打印为 PDF，然后使用 AI 等矢量编辑软件编辑 PDF
- 可以使用 R 或 Python 创建可导出的 figure
- 使用 Upset 的 R-Shiny 版本创建 static figure

### 显示交集属性

大多数实现支持可视化属性。

### 导出特定交集的元素

目前只有 UpSet 2 的交互式版本支持：https://upset.app/upset/#upset2

## 参考

- https://upset.app/
- UpSet 原文献：*Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot, Hanspeter Pfister. UpSet: Visualization of Intersecting Sets IEEE Transactions on Visualization and Computer Graphics (InfoVis), 20(12): 1983--1992, doi:10.1109/TVCG.2014.2346248, 2014.*
- UpSetR 包：*Jake R. Conway, Alexander Lex, Nils Gehlenborg. UpSetR: An R Package For The Visualization Of Intersecting Sets And Their Properties Bioinformatics, 33(18): 2938-2940, doi:10.1093/bioinformatics/btx364, 2017.*
- UpSet Python 包：https://upsetplot.readthedocs.io/en/stable/index.html