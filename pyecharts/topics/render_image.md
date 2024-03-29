# 渲染图片

2022-04-25, 19:20
***

## 简介

pyecharts 提供了 selenium, phantomjs 和 pyppeteer 三种渲染图片方式。

## make_snapshot

make_snapshot 用于 pyecharts 直接生成图片。

```py
from pyecharts.render import make_snapshot
```

```py
def make_snapshot(
    # 渲染引擎，可选 selenium 或者 phantomjs
    engine: Any,

    # 传入 HTML 文件路径
    file_name: str,

    # 输出图片路径
    output_name: str,

    # 延迟时间，避免图还没渲染完成就生成了图片，造成图片不完整
    delay: float = 2,

    # 像素比例，用于调节图片质量
    pixel_ratio: int = 2,

    # 渲染完图片是否删除原 HTML 文件
    is_remove_html: bool = False,

    # 浏览器类型，目前仅支持 Chrome, Safari，使用 snapshot-selenium 时有效
    browser: str = "Chrome",
    **kwargs,
)
```

## snapshot-selenium

安装：

```sh
pip install snapshot-selenium
```

