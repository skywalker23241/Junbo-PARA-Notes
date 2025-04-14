画面：在整个视频的演示过程中，时不时插入一些和主题相关的动画或者视频素材，来增强视频的画面感。配音：现在的配音有点过于“机械”了，没有感情，可以尝试真人配音，或者寻找更好的ai配音软件。品牌logo：官号的可以，个人号可以制作独特的品牌logo或者片头片尾。虚拟头像，人物：沿用之前说的小人黑板，感觉还可以，把画面打在绿幕上，具体操作可以放大让小人站在下面。背景音乐：找比较热的背景音乐，我个人觉得激昂一点的比较好。

2024.12.30可以在文章顶部加一个类似于进度条的小东西，便于读者查看自己读到哪里了。增加一个切换暗色模式的按钮或者自动切换。如果可以的话，可以加一个评论区，加一些评论，增加用户可信度。2025.1.6有没有可能如果竞争对手使用太多关于AI的内容导致流量下降，然后间接导致我们的流量上升？建立反向链接：找更加权威的机构建立反向链接。加入一个填写邮件地址订阅的功能，有利于留住客户。然后一周发两到三封邮件这样一方面推广自己的产品，另一方面可以带动网站博客以及其他的流量。主页下面的权威反向链接失效的需要更换。站点导航里面的resource里面包含更多的网页链接。统一样式，每一个部分的样式一致，就像是一个类型的主题。给每一个作者添加社交媒体帐号信息，增加信度。页尾的推特图标可以改成X (√)加一个多少人已经阅读，最近一次阅读是什么时候的提示框，增加文章的信度。给文章内包含的代码添加一个代码复制文本框。

软件免费和付费之间的界限不明确，有点模棱两可。

文章界面UI的优化，可以变的更像杂志一点，比如首字母大写什么的。

给子列表添加一个缩进效果：

软件界面也有点过时的，ui各方面，可以采用更加现代的ui，圆润一点的，参考一下别人的。

/* 为子列表添加缩进 /.guide-ul .sub-list {padding-left: 70px; / 调整值来控制缩进的程度 */}

.guide-ul .sub-list li {margin-bottom: 20px; /* 可选，添加子列表项之间的间距 */}

给step伪元素的css代码添加以下样式，优化由于浏览器渲染造成的显示异常：

.step::after {

content: "";

width: 0;

height: 0;

border-top: 1emsolid#ffffff;  /* 使用相对单位 */

border-right: 1emsolid#ffffff;

border-bottom: 1emsolid#ffffff;

border-left: 1emsolidtransparent;

position: absolute;

top: 50%;

right: 0;  /* 相对单位也可以调整 */

transform: translateY(-50%);

}

关于产品定价问题，过高？分开定价？全部统一价格？移除部分不需要的捆绑包？旧的产品是否还需要单独拎出来售卖？outlook部分是否要删除？

可以把软件页面访问我们的网站改成阅读产品说明。然后把对应的url也改一下。

做一个office激活的软件？

关于二级目录缩进：可以更改一下样式来实现。

##### 转载

A friend of mine submitted his during an update last March. Site got tanked from 5k visits to almost zero. Then a week later i heard a well known seo pro advising not to submit sitemaps or make major changes during an update. Till then we were clueless on what happened.

我的一个朋友在上次更新时提交了他的内容。网站从 5k 访问量跌至几乎为零。然后一周后，我听到一位知名 SEO 专家建议在更新期间不要提交网站地图或进行重大更改。在此之前，我们对此事毫无头绪。

Goggle crawls sites and looks for errors way more deeply during updates than normal crawls. That's why.

谷歌在更新期间比正常爬取更深入地爬取网站并查找错误。这就是原因。

And anyway google isn't find of small business and Individual bloggers now.

无论如何，谷歌现在并不喜欢小型企业和个人博主。

I agree to some degree. After the march 2024 debacle, i lost a lot of traffic. I was publishing daily before that so Google probably thought i was an ai. Anyway in response i stopped writing at all. For about 8 months. Surprisingly my traffic has stabilized. These days I just publish maybe once every 3 months. It seems regular publishing is now a negative for google

我在某种程度上同意。 2024 年 3 月的灾难之后，我失去了很多流量。在此之前我每天都在发布内容，所以谷歌可能认为我是一个人工智能。不管怎样，作为回应，我完全停止了写作。大约8个月。令人惊讶的是我的流量已经稳定了。现在我大概每三个月发布一次。看来定期发布现在对谷歌来说是负面的

### 网站和文章界面优化：

1. 进度条 ：在文章顶部添加进度条，帮助读者查看阅读进度。
2. 暗色模式 ：增加切换按钮或自动切换到暗色模式，提升用户体验。
3. 评论区 ：增加评论区和一些示范评论，提高用户互动和可信度。
4. 文章设计 ：优化文章UI，例如首字母大写、杂志式的排版，提升视觉效果。
5. 阅读人数提示框 ：显示阅读人数和最后阅读时间，增加文章的信任感。
6. 代码复制功能 ：在文章中提供代码复制框，方便用户使用。
7. 子列表缩进 ：为子列表添加缩进效果，改善文章结构。

### SEO和内容优化：

1. 反向链接 ：通过和权威机构建立反向链接来提升SEO排名。
2. 邮件订阅 ：增加邮件订阅功能，每周发送2-3封邮件，既能推广产品，又能带动流量。
3. 站点导航 ：在资源中增加更多网页链接，提高内容的广度。
4. 统一样式 ：确保每个部分的样式一致，类似于统一的主题。(这个部分可以优化下，既每个不同主题的文章使用不同的设计，比如apple类文章用比较圆润的UI，Windows可以用方一点的。)
5. 作者社交媒体信息 ：在每个作者的简介中加入社交媒体账号信息，增强DA。
6. 推特图标 ：将页尾的推特图标改成X（简洁化设计）。
7. 反向链接失效问题 ：主页下方的反向链接失效需要及时更新。
8. 产品页面链接优化 ：将“访问我们的网站”改为“阅读产品说明”，并修改相应URL。

### 产品与定价：

1. 定价策略 ：对产品定价进行优化，考虑是否分开定价，是否需要移除不必要的捆绑包，或者统一价格。
2. 软件产品优化 ：考虑是否删除Outlook部分，是否将旧产品单独销售。

### 软件功能和UI：

1. UI现代化 ：软件界面需要更新，采用更加现代、圆润的设计风格。(10年了，ui还没有更新。。。)
2. 功能优化 ：针对浏览器渲染问题优化CSS样式，解决显示异常。
3. Office激活软件 ：考虑开发一个用于Office激活的工具。
4. 关于视频： 给网页内插入的视频添加导航到YouTube的链接。

### 影响力和传播：

1.文章分享： 添加社交媒体分享。(考虑到其他因素，这个还是不是很现实的:D )

2.视频/软件分享： 添加软件分享评分。

3. 关于0点击搜索：用户可能通过serp直接找到了问题的解决办法，要提高产品的投资转化率，可以试着在title里面加入品牌名称或者其他有辨识度的东西。

iPhone screen black when unlocking

https://www.isumsoft.com/ios-issues/iphone-black-screen-after-unlock.html

AEO，VSO 优化结果显示。让答案可以让用户尽量在serp看见

教程类文章：QA，Steps。

讨论类文章：议论文，热点。

产品类文章：Q 产品。

虽然没有了点击率，但是可以提升品牌知名度。语音助手通常会直接读取Google 特色摘要（Featured Snippet）的内容。

重复的网站对于排名的影响，有？

the public ranking db doesnt use data from GSC/.Analytics AFAIK

大多数审计工具提出的问题都是无用的。我会问他接下来 3 个月、6 个月等有什么计划。他希望将网站带到哪里，他打算针对哪些关键词进行工作，以及他打算如何实现这一点。

可以考虑把文章标题从面包屑导航移除。![1741232828572](assets/1741232828572-20250313152752-2l9h2x7.png)

添加阅读时间预计

面包屑更新动画样式：

```html
<nav aria-label="Breadcrumb" class="breadcrumbcontainer">
	<ul class="crumb">
	  <li class="home"><a href="https://www.isumsoft.com/"><em>Home</em></a></li>
	  <li class="subpage"><a href="../windows-tips/"><em>Windows tips</em></a></li>
	  <li class="currentpage"><span aria-current="page">How to Disable Windows 11 Round Corners</span></li>
	</ul>
</nav> 
```

```css
/* 整体面包屑容器样式 */
.breadcrumbcontainer {
  background-color: #ffffff; /* 背景色 */
  overflow: hidden; /* 防止溢出 */
  position: relative;
}

/* 面包屑列表样式 */
.crumb {
  border-radius: 5px;
  list-style: none; /* 移除默认列表样式 */
  display: flex; /* 横向排列 */
  align-items: center; /* 垂直居中 */
  color: #fff;
  padding: 10px 0;
  max-width: 1200px;
  box-sizing: border-box;
  margin: 0 auto 50px;
  transition: max-width 0.5s ease; /* 宽度动画 */
}

/* 每个导航项 */
.crumb li {
  position: relative;
  margin: 0 5px 0 0; /* 保持间距 */
  padding: 0;
  transition: transform 0.3s ease, opacity 0.3s ease; /* 平滑移动和淡入 */
  opacity: 0; /* 默认隐藏 */
  transform: translateX(-100%); /* 默认向左偏移 */
  overflow: hidden; /* 确保圆角效果不会被溢出的内容覆盖 */
}

/* 第一个项始终可见 */
.crumb li:first-child {
  opacity: 1; /* Home 始终可见 */
  transform: translateX(0); /* 无偏移 */
}

/* 展开状态（由 JS 控制） */
.crumb.expanded li:nth-child(2) {
  transition-delay: 0s; /* 每次悬停重新计算延迟 */
  opacity: 1;
  transform: translateX(0);
}

.crumb.expanded li:nth-child(3) {
  transition-delay: 0.3s; /* 第三级延迟 0.3 秒 */
  opacity: 1;
  transform: translateX(0);
}

.crumb.expanded {
  max-width: 1200px; /* 展开到完整宽度 */
}

/* 链接和文本的公共样式 */
.crumb li a,
.crumb li span {
  display: inline-block; /* 内联块元素 */
  background: #143d8d; /* 背景色（红色） */
  color: #fff; /* 白色文本 */
  padding: 8px 30px 8px 25px; /* 右侧内边距稍大以适应箭头 */
  position: relative;
  clip-path: polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%);
  z-index: 1;
}

/* 伪元素创建右侧白色箭头尖（挖空效果） */
.crumb li:not(:last-child) a::after,
.crumb li:not(:last-child) span::after {
  content: '';
  position: absolute;
  top: 0;
  right: -20px;
  width: 20px;
  height: 100%;
  background: #ffffff;
  clip-path: polygon(0 0, 100% 50%, 0 100%);
  z-index: 2;
}

/* 伪元素创建左侧挖空效果 */
.crumb li:not(:first-child) a::before,
.crumb li:not(:first-child) span::before {
  content: '';
  display: block;
  border-top: 20px solid #143d8d; /* 与背景色匹配 */
  border-bottom: 20px solid #143d8d; /* 与背景色匹配 */
  border-left: 20px solid #ffffff; /* 白色三角形 */
  position: absolute;
  left: 0px;
  top: 0;
  z-index: 2;
}

/* 第一个项的特殊样式 */
.crumb li:first-child {
  padding-left: 20px; /* 保持与右侧对齐 */
}

.crumb li:first-child a::before,
.crumb li:first-child span::before {
  display: none; /* 隐藏第一个项的左侧挖空 */
}

/* 一级：Home */
.home a {
  font-size: 14px;
}

.home a:hover {
  background: #143d8d; /* 悬停时稍深的蓝色 */
}

/* 二级：Subpage */
.subpage a {
  font-size: 14px;
}

.subpage a:hover {
  background: #143d8d;
}

/* 当前页：Currentpage */
.currentpage span {
  font-size: 14px;
  font-weight: bold; /* 当前页加粗 */
  cursor: default;
}
```

```js
// 面包屑导航弹出动画效果 //
const breadcrumbContainer = document.querySelector('.breadcrumbcontainer');
const crumb = document.querySelector('.crumb');
const homeItem = crumb.querySelector('.home'); // 获取 Home 标签
const items = crumb.querySelectorAll('li');
let timeoutId = null;
let fadeOutTimeoutId = null; // 新增的定时器用于延迟渐隐

// 复位所有项的状态
function resetItems() {
    items.forEach((item, index) => {
        if (index > 0) {
            item.style.transition = 'none';
            item.style.opacity = '0';
            item.style.transform = 'translateX(-20px)';
        }
    });

    // 让浏览器重新计算渲染（强制回流）
    void breadcrumbContainer.offsetWidth;

    // 重新添加过渡效果
    items.forEach((item, index) => {
        if (index > 0) {
            item.style.transition = `opacity 0.5s ease ${index * 0.3}s, transform 0.5s ease ${index * 0.3}s`;
        }
    });
}

// 鼠标进入 Home 标签时触发延迟展开
homeItem.addEventListener('mouseenter', () => {
    clearTimeout(timeoutId);

    // 如果已经展开，直接返回
    if (crumb.classList.contains('expanded')) return;

    timeoutId = setTimeout(() => {
        crumb.classList.add('expanded');

        // 重新设置动画
        items.forEach((item, index) => {
            if (index > 0) {
                item.style.opacity = '1';
                item.style.transform = 'translateX(0)';
            }
        });
    }, 500); // 0.5秒延迟后开始动画
});

// 鼠标离开 Home 标签时延迟 2 秒开始渐隐效果
homeItem.addEventListener('mouseleave', () => {
    clearTimeout(timeoutId);
    clearTimeout(fadeOutTimeoutId); // 清除可能的渐隐定时器

    // 只有在已经展开时，才开始渐隐动画
    if (crumb.classList.contains('expanded')) {
        crumb.classList.remove('expanded');

        // 设置延迟 2 秒后才开始渐隐效果
        fadeOutTimeoutId = setTimeout(() => {
            items.forEach((item, index) => {
                if (index > 0) {
                    item.style.transition = 'opacity 0.5s ease';  // 设置渐隐动画
                    item.style.opacity = '0'; // 使导航项透明
                }
            });
        }, 2000); // 延迟 2 秒后执行渐隐效果
    }

    // 重新复位项的状态，以便下次进入时重新触发弹出效果
    setTimeout(() => {
        resetItems();
    }, 2600); // 延迟 2.6 秒确保渐隐效果完成后重置状态
});

// 初始化
resetItems();
```

这个面包屑的样式保存到codepen了。

---

###### Tue Apr 8 09:03:33 CST 2025

## 关于viewport的设置问题:(不是很大问题,但是也可以优化)

从 `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=1" />`
改为 `<meta name="viewport" content="width=device-width, initial-scale=1">`或者 `<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">`
理由:
有视障或老年用户需要超过 5 倍放大

    有研究指出，一些用户可能需要放大 到 10 倍以上 才能清晰阅读；

    你这段代码限制最大放大 5 倍，对他们来说不够。

移动设备行为差异

    有些浏览器（如早期的 iOS Safari）对 maximum-scale 参数很敏感，可能会误解它是开发者故意“锁死缩放”，从而完全禁用缩放，即使你设置了 user-scalable=1；

    这在 iOS 和某些老安卓设备上尤其常见。

不符合 WCAG 2.1 标准

    WCAG 建议支持用户无障碍缩放到至少 200%（即2倍）；

    虽然你这里是5倍，已经合格，但只要人为设置了缩放上限，总是存在争议。

---

###### Tue Apr 8 09:11:03 CST 2025

## ~~关于文章首图不设置懒加载~~

~~我看了下文章的第一张可见图片应该就是作者的头像了,所以作者头像的懒加载是没有必要的,可以考虑把作者头像的懒加载去掉.
或者说把文章里面第一张出现的图片做一个没有懒加载的处理.~~
没事了,hero图没有设置懒加载.

---

## 关于结构化数据

```html
  <!-- 这里是结构化数据 -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "4 Ways to Disable Windows 11 Round Corner Window",
    "description": "Learn four methods to disable the round corners of windows in Windows 11.",
    "step": [
      {
        "@type": "HowToStep",
        "name": "Use Registry Editor",
        "text": "Open Registry Editor and navigate to HKEY_CURRENT_USER..."
      },
      {
        "@type": "HowToStep",
        "name": "Use Group Policy Editor",
        "text": "Open the Group Policy Editor by typing gpedit.msc..."
      }
      // 可以继续添加更多步骤
    ]
  }
  </script>
```


---



考虑将相关文章的链接添加到文章内部.

---
