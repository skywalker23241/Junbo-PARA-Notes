## 2025-3-13

星期：星期四

天气：晴

---

今天的心情：

平静（上午），稍微有点躁动（下午）

---

今天的主要事件：

1. 完成了isumsoft站内代码块复制的添加：
   * 更新了一个复制按钮代码框样式，js中添加了复制代码框中的code代码
   * 给一些包含代码块的文章添加了复制代码框，优化了文章图片
   * 还有一些之前的文章图片格式有点不对需要重新抓图或者改变大小
2. 想给站内文章图片添加一个放大预览的效果：
   * 刚刚在看思源笔记的博客 [https://ld246.com/article/1546941897596](https://ld246.com/article/1546941897596) 的时候看到的，效果还不错，就是图片鼠标悬停时指针变成放大镜，然后点击展开预览，鼠标变成缩小镜，点击空白区域或者esc还原，对用户看不清楚的图片还是蛮好的。
   * ```css
     .vditor-reset__preview {
     cursor: zoom-in;
     display: inline-block;
     position: relative;
     }
     ```
   * 他这个应该是插件的功能了，看下可以考虑给我们的网站也整一个嘛，蛮不错的功能。
3. 

---

反思与总结：

---

明天的计划：

---

结束语：

“明天是全新的一天，充满了无限可能，让我全力以赴，迎接每一个挑战，加油！”

## 2025-3-14

星期：_____五_____

心情指数（1-10）：_____8_____

天气：_____🌤_____

今天的主要事件：

1. 给网站面包屑导航换新，以前的太老套了。
2. 动画效果还是算了吧，对手机端听不友好的，然后还有bug
3. ---
4. ---

今天的感受：

* 对事件的想法和感受：
  --------------------

  ---
* 让我感到快乐的事情：
  --------------------

  ---
* 需要改进的地方或烦恼：
  ----------------------

  ---

明天的目标：

感谢的事情：

其他备注：

---

## 2025-3-18

10点49分 也是把精简版系统安装上来了，还有很多软件需要安装，到时候再看吧。

10点55分

> 在OBS中强制使用SDR动态范围的设置意味着强制将你的画面输出设为标准动态范围（Standard Dynamic Range, SDR）模式，而不是高动态范围（HDR）模式。
>
> 动态范围（Dynamic Range）指的是画面中最亮和最暗部分的差异。HDR可以显示更多的亮度层次和颜色细节，而SDR的动态范围较窄，亮度和对比度相对较低。
>
> 通常，HDR的视频内容需要支持HDR的显示设备（如支持HDR10的电视或显示器）才能正常观看。如果你的设备或者流媒体平台不支持HDR，或者你不希望以HDR输出视频，那么强制使用SDR可以确保画面正常显示，避免因设备不兼容而导致显示问题。
>
> 简单来说，强制使用SDR动态范围是为了确保你的直播或录制视频在不支持HDR的设备上也能正常播放，避免出现颜色失真或画面过于暗淡的问题。

11点49分 差不多都弄好了。

13点35分 休息个屁哈哈哈。

13点52分 这个网线是不是我制作的时候有点问题哈哈哈。

14点02分 现在是大家都没网了。

> 您不应依赖一个冗长而详细的提示来获得完美的解决方案，而应使用 Copilot 进行迭代 - UI 专为迭代而构建，让您完全控制流程，确保最终结果更好。

14点30分 当你只有一个输入法的时候就没那么多事了哈哈哈。

14点44分 win11就在虚拟机装吧。

15点44分 然而这个虚拟机还是那么卡哈哈哈，要用再用吧。

15点54分 vscode里面的svn不能用了。

16点33分 换一个虚拟机平台吧。

## 2025-3-19

```regex
jquery-1.7.1.min.js,user-guides.html,purchase-personal.html,purchase-professional.html,purchase-ultimate.html,technical-faq.html,order-faq.html,against-scam.html,user-guide-for-plus.html,404.shtml,404.html,demo.html,index.html,purchase.html,review.html,upgrade.html,user-guide.html,charlotte-bayley.html,cynthia-huff.html,david-brown.html,isabella-shinn.html,lucas-watson.html,ralph-adolphs.html,roy-uleri.html,faq.html,reference.html,contact.html,privacy.html,sitemap.html,downloads.html,products.html,store.html
```

把这些排除了剩下的就都是文章了。

激活windows11的一个小方法：

Win + R 打开run，输入

```run
powershell
```

然后输入

```regex
irm massgrave.dev/get | iex
```

在打开的窗口输入 1

等待一会即可成功激活。

可以在programdata里面自定义windows的样式，里面蛮多东西都还不错。

以下代码用于统计一个父目录下所有子项中文件的个数，可以包含引号里面的目录。

```powershell
(Get-ChildItem -Path "android", "backup-recovery", "bitlocker", "computer-tweaks", "gpu", "internet", "ios-issues", "iphone-tips", "mac-tips", "office", "pdf", "product-key", "rar-zip", "sql-server", "surface", "unlock-iphone", "windows-password", "windows-tips" -Recurse -File | Measure-Object).Count
```

实例：统计isumsoft文章总数：

1477 然后删去每个子目录的index（16个其中produc-tkey和sql-server没有index）得 1461

更新了样式，把shareus的抄过来了哈哈哈。

这个显示键盘的样式确实好看，但是得自己调。

这个AltDrag也不错，基本上可以平替linux上的那个吧。

桌面图标也是他这个更酷一点哈哈哈！开干！

```regex
./android, ./backup-recovery, ./bitlocker, ./computer-tweaks, ./gpu, ./internet, ./ios-issues, ./iphone-tips, ./mac-tips, ./office, ./pdf, ./product-key, ./rar-zip, ./sql-server, ./surface, ./unlock-iphone, ./windows-password, ./windows-tips
```

这个可以匹配所有文章文件夹。

这个石山代码真的！！！

## 2025-3-20

已经是在h1里面了，就没必要再加 `<strong>`了，除非你是要突出显示，从预览来看，也不是很突出。

更新下首页的热点文章和最新文章，很多都是去年的了。

## 2025-3-21

如何用火狐浏览器取代Chrome？

社交媒体的运行方式：先由软件/网站制作组发布以后投入广告宣传»部分基础用户»基础用户承认产品做的不错互相推荐»制作组再次激励基础用户创作其他板块/分区内容为网站提供关键词»搜索引擎为网站带来新用户，从而形成良性循环。

哪个天才想的把所有文章时间改成一样的。。。

测试一下把站点文件移动到同一磁盘能不能工作。

## 2025-3-24

更新了阅读内容进度条有关截屏显示异常的代码，虽然方法笨了点，但总归还是有点用的。

得找一个方法把以前的图换一下，感觉之前截图的都有点小问题。

把GIMP下载回来了，待会先看看怎么添加边框，问问ai吧。

开通了一个github仓库用来储存笔记吧，现在感觉好多笔记软件啊。

## 2025-03-25

isumsoft的google的页面还是没有更新；可能和这次三月份核心更新有关，待会检查一下shareus的什么时候提交更新的。

把keep的笔记整理到github吧，然后国内就用语雀和思源，国外就用github了。

keep可以滚了哈哈，Gdrive和坚果云也差不多了哈哈哈
