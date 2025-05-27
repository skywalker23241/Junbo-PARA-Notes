本地部署AI启动代码:

python GPT.py

ollama run deepseek-r1:1.5b(弃用)

复制代码框样式：

```html
<div class="code-container">
	<button class="copy-btn" onclick="copyToClipboard(this)">Copy</button>
	<pre><code>代码</code></pre>
</div>
```

键盘按键样式：

```html
<txt-button>button name here</txt-button>
```

step样式代码：

```html
<span class="step">Step ?</span>
```

内部链接代码：

```html
<a href="input your url here">input your display txt here.</a>
```

提示框代码：

```html

<div class="notice-div">
    <p>Boxname: </p>
	    <ul>
	      <li>input your text here.</li>
	    </ul>
</div>
```

导言部分虚线框：

```html
<div class="bor-dashed">
	<p><strong><em></em></strong></p>
</div>
```

目录样式代码：

```html
<ul class="guide-ul">
	<li></li>
	<li></li>
	<li></li>
</ul>
```

表格代码：

```html
<table border="1" width="700" align="center" style="border-color: black; text-align: center;">
<tr>
	<th>Method</th>
	<th>Speed</th>
	<th>Best for</th>
	<th>Description</th>
</tr>
<tr>
	<td>**Local Reinstall**</td>
	<td>**Faster**</td>
	<td>System is working fine, only needs a reset</td>
	<td>Uses existing system files without downloading</td>
</tr>
<tr>
	<td>**Cloud Download**</td>
	<td>**Slower** (depends on internet speed)</td>
	<td>Corrupt system files or wanting the latest version</td>
	<td>Downloads a fresh system image from Microsoft's servers</td>
</tr>
</table>
```

正则：

(Step \d+)[:.]

`<span class="step">Step $1</span>`

贪婪的捕获组：(.*?)

...

cloner产品div：

```html
<div>
		<div class="product-div">
		<img loading="lazy" src="../images/boxshot/cloner.png" alt="iSumsoft Cloner" width="140" height="185">
		<div class="function-div">
		<p class="points">iSumsoft Cloner</p>
		<h2>Clone/Backup Windows OS or hard drive to save you from data loss</h2>
		<ul>
			<li class="points">Clone Windows from one hard drive to another and remain the destination drive bootable.</li>
			<li class="points">Fully backup and restore Windows or data partitions without losing any data.</li>
			<li class="points">Clone one hard drive to another, leaving all data and partitions intact.</li>
			<li>Clone Windows, partitions, or entire hard drives without logging into Windows.</li>
			<li>Clone bootable USB flash drive to another USB drive.</li>
		</ul>
			<div class="download-button">
				<a class="download-link win-link" href="https://www.isumsoft.com/download/isumsoft-cloner.exe">FREE DOWNLOAD</a>
			</div>
		</div>  
		</div>
	  </div>
```

网站内部视频iframe代码：

```html
<iframe width="800" height="450" src="video-url" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

\w 匹配任意字母,数字或下划线,相当于[a-zA-Z0-9].
