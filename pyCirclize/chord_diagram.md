# 弦图（Chord Diagram）

@since 2026-09-11⭐
@author Jiawei Mao
***
## 1. 矩阵数据

与 [`circlize`](https://jokergoo.github.io/circlize_book/book/the-chorddiagram-function.html) 类似，`pyCirclize` 可以通过矩阵数据来绘制弦图。

### 1.1 示例 1（3 x 6 矩阵）

本示例使用了与 `circlize` 官方文档中相同的矩阵数据。

```python
from pycirclize import Circos
import pandas as pd

# 创建一个 (3 x 6) 矩阵 dataframe 
row_names = ["S1", "S2", "S3"] # row 索引
col_names = ["E1", "E2", "E3", "E4", "E5", "E6"] # col 名词
# 矩阵数据表示 row 与 col 之间的连接强度、流量或频数
matrix_data = [
    [4, 14, 13, 17, 5, 2],
    [7, 1, 6, 8, 12, 15],
    [9, 10, 3, 16, 11, 18],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# 根据矩阵自动创建扇区和连线
# 每一行、每一列都视为一个扇区，共 3+6=9 个扇区
# 扇区弧长与该行/列的加和成正比
# 矩阵中的每个数值对应一条连线，连线宽度与数值成正比
circos = Circos.chord_diagram(
    matrix_df, # 输入矩阵，行和列自动成为扇区
    start=-265, # 整个圆环的起始角度（-265°等价于 95°）
    end=95, # 终止角度，start 和 end 跨越 360°，因此是完整圆环
    space=5, # 相邻扇区间隔 5°
    r_lim=(93, 100), # 弦图环的半径范围
    cmap="tab10", # 颜色映射表，用于给 9 个扇区自动分配颜色
    label_kws=dict(r=94, size=12, color="white"), # 扇区标签样式，位置半径 94，字号 12，白色文字
    link_kws=dict(ec="black", lw=0.5), # 连线样式：黑色边框，线宽 0.5
)

print(matrix_df)
fig = circos.plotfig()
```

```
    E1  E2  E3  E4  E5  E6
S1   4  14  13  17   5   2
S2   7   1   6   8  12  15
S3   9  10   3  16  11  18
```

<img src="./images/image-20260911100839053.png" alt="image-20260911100839053" width="500" />

### 1.2 示例 2（10 x 10 矩阵）

本示例使用了由 Circos Table Viewer 随机生成的 10 x 10 矩阵数据。

```python
from pycirclize import Circos
import pandas as pd

# 准备矩阵数据
# 行名和列名都是 A-J，共 10 个标签
row_names = list("ABCDEFGHIJ")
col_names = row_names
# 矩阵数据非负，表示节点之间的连接强度
# A→B 的值是 115，B→A 的值是 108，说明连接是有向的（不对称）。
matrix_data = [
    [51, 115, 60, 17, 120, 126, 115, 179, 127, 114],
    [108, 138, 165, 170, 85, 221, 75, 107, 203, 79],
    [108, 54, 72, 123, 84, 117, 106, 114, 50, 27],
    [62, 134, 28, 185, 199, 179, 74, 94, 116, 108],
    [211, 114, 49, 55, 202, 97, 10, 52, 99, 111],
    [87, 6, 101, 117, 124, 171, 110, 14, 175, 164],
    [167, 99, 109, 143, 98, 42, 95, 163, 134, 78],
    [88, 83, 136, 71, 122, 20, 38, 264, 225, 115],
    [145, 82, 87, 123, 121, 55, 80, 32, 50, 12],
    [122, 109, 84, 94, 133, 75, 71, 115, 60, 210],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# 
circos = Circos.chord_diagram(
    matrix_df,
    space=3,
    r_lim=(93, 100),
    cmap="tab10",
    ticks_interval=500,
    label_kws=dict(r=94, size=12, color="white"),
)

print(matrix_df)
fig = circos.plotfig()
```

```
     A    B    C    D    E    F    G    H    I    J
A   51  115   60   17  120  126  115  179  127  114
B  108  138  165  170   85  221   75  107  203   79
C  108   54   72  123   84  117  106  114   50   27
D   62  134   28  185  199  179   74   94  116  108
E  211  114   49   55  202   97   10   52   99  111
F   87    6  101  117  124  171  110   14  175  164
G  167   99  109  143   98   42   95  163  134   78
H   88   83  136   71  122   20   38  264  225  115
I  145   82   87  123  121   55   80   32   50   12
J  122  109   84   94  133   75   71  115   60  210
```

<img src="./images/image-20260911101654045.png" alt="image-20260911101654045" width="500" />

### 1.3 示例 3（10 x 2 矩阵）

本示例使用了由 Circos Table Viewer 随机生成的 10 x 2 矩阵数据。

```python
from pycirclize import Circos
import pandas as pd

# Create matrix data (10 x 2)
row_names = list("ABCDEFGHIJ")
col_names = list("KL")
matrix_data = [
    [83, 79],
    [90, 118],
    [165, 81],
    [121, 77],
    [187, 197],
    [177, 8],
    [141, 127],
    [29, 27],
    [95, 82],
    [107, 39],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# Define link_kws handler function to customize each link property
def link_kws_handler(from_label: str, to_label: str):
    if from_label in ("C", "G"):
        # Set alpha, zorder values higher than other links for highlighting
        return dict(alpha=0.5, zorder=1.0)
    else:
        return dict(alpha=0.1, zorder=0)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrix_df,
    space=2,
    cmap="Set3",
    label_kws=dict(size=12),
    link_kws=dict(direction=1, ec="black", lw=0.5),
    link_kws_handler=link_kws_handler,
)

print(matrix_df)
fig = circos.plotfig()
```

```
     K    L
A   83   79
B   90  118
C  165   81
D  121   77
E  187  197
F  177    8
G  141  127
H   29   27
I   95   82
J  107   39
```

<img src="./images/image-20260911103123195.png" alt="image-20260911103123195" width="500" />

## 2. From-To Table 数据

`pyCirclize` 也可以根据“来源-目标”（From-To）格式的表格数据来绘制弦图。

### 2.1 示例 1

```py
from pycirclize import Circos
from pycirclize.parser import Matrix
import pandas as pd

# Create from-to table dataframe & convert to matrix
fromto_table_df = pd.DataFrame(
    [
        ["A", "B", 10],
        ["A", "C", 5],
        ["A", "D", 15],
        ["B", "D", 8],
        ["C", "D", 6],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrix = Matrix.parse_fromto_table(fromto_table_df)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrix,
    space=3,
    cmap=dict(A="royalblue", B="orange", C="green", D="red"),
    label_kws=dict(size=12),
)

print(fromto_table_df.to_string(index=False))
fig = circos.plotfig()
```

```
from to  value
   A  B     10
   A  C      5
   A  D     15
   B  D      8
   C  D      6
```

<img src="./images/image-20260911103542334.png" alt="image-20260911103542334" width="500" />

### 2.2 示例 2

```python
from pycirclize import Circos
from pycirclize.parser import Matrix
import pandas as pd

# Create from-to table dataframe & convert to matrix
fromto_table_df = pd.DataFrame(
    [
        ["A", "B", 10],
        ["A", "C", 5],
        ["A", "D", 15],
        ["A", "E", 20],
        ["A", "F", 3],
        ["B", "A", 3],
        ["B", "G", 15],
        ["F", "D", 13],
        ["F", "E", 2],
        ["E", "A", 20],
        ["E", "D", 6],
    ],
    columns=["from", "to", "value"], # Column name is optional
)
matrix = Matrix.parse_fromto_table(fromto_table_df)

# Initialize Circos instance for chord diagram plot
circos = Circos.chord_diagram(
    matrix,
    space=3,
    cmap="viridis",
    ticks_interval=5,
    label_kws=dict(size=12, r=110),
    link_kws=dict(direction=1, ec="black", lw=0.5),
)

print(fromto_table_df.to_string(index=False))
fig = circos.plotfig()
```

```
from to  value
   A  B     10
   A  C      5
   A  D     15
   A  E     20
   A  F      3
   B  A      3
   B  G     15
   F  D     13
   F  E      2
   E  A     20
   E  D      6
```

<img src="./images/image-20260911103647157.png" alt="image-20260911103647157" width="500" />

