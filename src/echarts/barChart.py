from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import RenderType

bar = Bar(init_opts=opts.InitOpts(renderer=RenderType.SVG))
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.render()
