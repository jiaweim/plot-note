# Figure 数据结构

2022-04-14, 18:21
***

## 简介

plotly Python 包可用于创建、操作和渲染 Figure，其中渲染过程在后台使用 Plotly.js JavaScript 库实现。plotly.py 使用 python dict 或 `plotly.graph_objecs.Figure` 类表示 Figure，序列化为 JSON 文本格式后传递给 plotly.js 进行渲染。

```ad-note
推荐从 plotly 的高级 API `plotly.express` 开始学习 plotly，该 API 包含简洁易用的绘图函数，这些函数均返回 `plotly.graph_objects.Figure` 对象。这篇内容主要介绍表示这些对象所用的数据结构，适合希望了解更多自定义功能的用户。
```

可以使用 `print(fig)` 查看 `plotly.graph_objects.Figure` 对象（包括 px 函数返回的对象）的底层数据结构，在 JupyterLab 中还可以使用 `fig.show("json")` 查看。`Figure` 还支持 `fig.to_dict()` 和 `fig.to_json()` 方法。

使用 `print()` 输出 figure 中，`layout.template` 由于太长一般以省略号 `...` 表示。

```python
import plotly.express as px  
  
fig = px.line(x=["a", "b", "c"], y=[1, 3, 2], title="sample figure")  
print(fig)  
fig.show()
```

```
Figure({
    'data': [{'hovertemplate': 'x=%{x}<br>y=%{y}<extra></extra>',
              'legendgroup': '',
              'line': {'color': '#636efa', 'dash': 'solid'},
              'marker': {'symbol': 'circle'},
              'mode': 'lines',
              'name': '',
              'orientation': 'v',
              'showlegend': False,
              'type': 'scatter',
              'x': array(['a', 'b', 'c'], dtype=object),
              'xaxis': 'x',
              'y': array([1, 3, 2], dtype=int64),
              'yaxis': 'y'}],
    'layout': {'legend': {'tracegroupgap': 0},
               'template': '...',
               'title': {'text': 'sample figure'},
               'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x'}},
               'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'y'}}}
})
```

![[figure-structure-1.png]]

## 属性 Tree

plotly.js 支持符合其 schema 的输入，下面介绍该 schema 的总体架构，在 [Figure 参考](https://plotly.com/python/reference/index/)中有 schema 的详尽说明（Figure 参考是用 [JSON 格式的 schema](https://raw.githubusercontent.com/plotly/plotly.js/master/dist/plot-schema.json) 生成）。

Figure 被表示为 Tree：

- Tree 的命名 node 称为属性（attribute）
- Tree 的 root node 包含三个顶层属性：data, layout 和 frames

在 Figure 参考中，通过完整路径来引用属性，路径分隔符用点号 `.`。例如，`"layout.width"` 是 Figure 根节点下 `layout` 属性值下 key 为 `width` 的属性。如果父节点是 list 而非 dict，则在引用属性时插入方括号，例如 `"layout.annotations[].text"`。

顶层 "data" 属性定义了一个名为 "traces" 的类型化对象 list，trace 的 schema 取决于其类型，它们的属性在 Figure 参考中的路径样式如 `"data[type=scatter].name"`。

`plotly.graph_objects` 模块包含自动生成的 Python 类，用于表示 Figure schema 中的非叶属性，并提供了 Python API。`plotly.graph_objects.Figure` 对象的属性设置方法有两种：

1. 直接使用 Python 对象属性设置，如 `fig.layout.title.font.family="Open Sans"`
2. 使用 update 方法和下划线 magic，例如 `fig.update_layout(title_font_family="Open Sans")`

在创建 figure 时，不需要设置所有属性。因为在渲染时，plotly.js 对没有指定的属性自动使用默认值，属性默认值可参考 [Figure 参考](https://plotly.com/python/reference/index/)。以 `layout.xaxis.range` 为例，如果没有显式指定，plotly.js 会直接根据与该 axis 关联 trace 的 x 值范围确定。plotly.js 会忽略未知属性或格式不对的属性值。另外还要注意，如果存在 `layout.template` key，plotly 会首先根据 template 提供的内容渲染默认值，当 template 缺失对应默认值时，plotly 才会继续根据数据推断默认值。设置 `layout.template="none"` 可以禁用内置模板。

## 顶层 data 属性

`data` 是 figure 的三个顶层属性之一，其值必须是 list of dicts，称为 traces。

- trace 类型有 40 多种，包括 `scatter`, `bar`, `pie`, `surface`, `choropleth` 等，每个 trace 必须有 `type` 属性，该属性确定了有哪些其它可用属性。
- trace 绘制在 [subplot](https://plotly.com/python/subplots/) 上，trace 和 subplot 的类型要兼容。
- 所有 traces 可能只有一个 legend，pie 和 funnelarea 例外。
- 部分 trace 类型支持连续颜色，带有一个关联的 colorbar，该 colorbar 可以使用 trace 的属性设置，也可以在使用 coloraxis 属性时在 layout 中设置。

## 顶层 layout 属性

`layout` 的属性值为 dict 类型，包含 figure 的非数据部分的设置，如：

- 尺寸和边距
- Figure 范围的默认值：模板、字体、颜色、hover标签和 modebar
- 标题和 legend
- colorscale 以及对应的 colorbar
- 可以绘制多个 traces 的 subplots：
	- `xaxis`, `yaxis`, `xaxis2`, `yaxis3` 等
	- `scene`, `scene2`, `scene3` 等
	- `ternary`, `ternary2`, `ternary3`, `polar`, `polar2`, `polar3`, `geo`, `geo2`, `geo3`, `mapbox`, `mapbox2`, `mabox3`, `smith`, `smith2`
- 可放在 3D 笛卡尔 subplots 的非数据 marks：
    -   `annotations`: [textual annotations with or without arrows](https://plotly.com/python/text-and-annotations/)
    -   `shapes`: [lines, rectangles, ellipses or open or closed paths](https://plotly.com/python/shapes/)
    -   `images`: [background or decorative images](https://plotly.com/python/images/)
- 控制可以在坐标系中放什么，以及什么交互可以触发 plotly.js 函数：
	- `updatemenus`: [single buttons, toggles](https://plotly.com/python/custom-buttons/) and [dropdown menus](https://plotly.com/python/dropdowns/)
	- `sliders`: [slider controls](https://plotly.com/python/sliders/)

## 顶层 frames 属性




## 参考

- https://plotly.com/python/figure-structure/