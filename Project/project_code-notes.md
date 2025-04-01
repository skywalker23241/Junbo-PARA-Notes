# Project_code-notes

***2025.03.24 这是我的第一条笔记，github存储，come on!***

---

## 关于VScode 拉取Github仓库

### 方法：

* **打开 VS Code**
* **打开命令面板** （`Ctrl + Shift + P` 或 `Cmd + Shift + P` 在 macOS 上）
* **输入 `Git: Clone` 并选择该选项**
* **输入 GitHub 仓库的 URL** （可以在 GitHub 仓库页面点击 "Code" 按钮获取）
* **选择本地存储路径**
* **等待克隆完成后，选择“打开克隆的仓库”**
* **确保 Git 已安装** ：可以使用 `git --version` 检查 Git 是否已安装。
* 如果未安装，请前往 [Git 官方网站](https://git-scm.com/) 下载并安装。
* **配置 Git 账号** （首次使用时）：
  * git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"

### 参考文档：

* [Using Git source control in VS Code在 VS Code 中使用 Git 源代码管理](https://code.visualstudio.com/docs/sourcecontrol/overview)
* [Git学习
  ](https://git-scm.com/doc#top)

---

## 关于本地文件连接到服务器

### **关于FileZilla**

FileZilla 是一款**免费、开源**的  **FTP（File Transfer Protocol）客户端和服务器软件** ，用于在计算机和服务器之间传输文件。它支持多种协议，包括  **FTP、FTPS（FTP Secure）和 SFTP（SSH File Transfer Protocol）** ，适用于 Windows、macOS 和 Linux 等操作系统。

### **FileZilla 的主要功能**

1. **支持多种协议** ：FTP、FTPS、SFTP，确保数据传输的安全性。
2. **友好的用户界面** ：采用类似 Windows 资源管理器的双窗口模式（本地文件和远程服务器文件）。
3. **断点续传** ：支持大文件的续传功能，不用担心传输中断。
4. **多线程传输** ：可以同时上传/下载多个文件，提高效率。
5. **站点管理器** ：可以保存多个 FTP 服务器的登录信息，方便快速连接。
6. **拖拽支持** ：可以直接从本地文件夹拖拽文件到服务器窗口，实现快速上传/下载。
7. **代理支持** ：支持 HTTP/FTP/SOCKS 代理，适用于特殊网络环境。

### **FileZilla 的用途**

* **网站管理** ：开发者和站长可以用它上传/下载网站文件，管理服务器内容。
* **远程备份** ：通过 SFTP 安全地将重要文件备份到远程服务器。
* **文件共享** ：与团队成员共享大文件，尤其是在远程工作环境中。

### **FileZilla 下载**

* **官网** ：[FileZilla官网](https://filezilla-project.org)
* 可以选择 **FileZilla Client（客户端）** 或  **FileZilla Server（服务器）** ：
  * **客户端** ：用于连接 FTP 服务器进行文件传输。
  * **服务器** ：用于搭建自己的 FTP 服务器，让别人连接和传输文件。

### **Shareus 网站 内容同步到服务器**

* Host: shareus.com
* Username: chenggong@shareus.com
* Password: ABC20258899&*

---

## 关于Wiz-Progressbar代码

Html：

```html
<div class="fixed inset-x-0 top-0 z-50 h-0.5 transition-opacity duration-500 opacity-100">
    <span id="progress-bar" style="transform: translateX(-100%);" class="absolute top-0 h-0.5 w-full bg-primary-blue shadow-md shadow-primary-blue/30 transition-transform duration-150"></span>
  </div>
```

span

```css
html:not([data-lt-script-installed]):not(.__lt-dummy-1):not(.__lt-dummy-2):not(.__lt-dummy-3):not(.__lt-dummy-4):not(.__lt-dummy-5):not(.__lt-dummy-6):not(.__lt-dummy-wxyz1234) lt-message .lt-message-container__progressbar {
  width: 100% !important;
  height: 4px !important;
  background: #239aff !important;
  position: absolute !important;
  top: 0 !important;
  animation: lt-message-progress 20s linear forwards !important;
  transform-origin: 0% 50% !important;
}
```

---

## 关于选择网站域名挺有意思的一篇reddit帖子

* [原帖](https://www.reddit.com/r/SEO/comments/1jirc25/did_i_choose_a_bad_domain_name/)

---

## 关于网站切换为暗色主题

TRAE：

```css
:root {
          --bg-color: #ffffff;
          --text-color: #333333;
          --primary-color: #2196f3;
        }

        [data-theme="dark"] {
          --bg-color: #1a1a1a;
          --text-color: #e0e0e0;
          --primary-color: #1976d2;
        }
        .theme-toggle {
          position: fixed;
          top: 20px;
          right: 20px;
          padding: 10px 15px;
          background: var(--primary-color);
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          z-index: 10000;
        }

        .theme-toggle:hover {
          opacity: 0.9;
        }
```

```javascript
const themeToggle = document.getElementById('themeToggle');
        const savedTheme = localStorage.getItem('theme') || 'light';

        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggle.textContent = savedTheme === 'dark' ? '切换亮色主题' : '切换暗色主题';

        themeToggle.addEventListener('click', () => {
          const currentTheme = document.documentElement.getAttribute('data-theme');
          const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  
          document.documentElement.setAttribute('data-theme', newTheme);
          localStorage.setItem('theme', newTheme);
          themeToggle.textContent = newTheme === 'dark' ? '切换亮色主题' : '切换暗色主题';
        });
```

```html
 <button class="theme-toggle" id="themeToggle">切换暗色主题</button>
```

感觉做这个还要考虑移动设备的兼容。

在页面顶端时，按钮显示在作者栏的最右边，当文章慢慢往下划，出现回到顶部的图标后，按钮渐现出现在回到顶部图标的上方。

（未完待續......）

---

## 关于键盘上的Grave键

在键盘上，****grave** 键指的是位于数字键 1 左侧的键，通常标有 `或“~”符号。 在英文中，这个符号被称为“重音符号”（grave accent），常用于表示某些字母的重音，例如法语单词中的“è”。** **在编程中，这个键用于输入反引号`，在某些编程语言中具有特殊意义。**

---

## 关于EMMET快速编码

### **Emmet 速查表（Cheat Sheet）** 🚀

#### **📌 1. HTML 快速编码**

| 语法                              | 结果                                                |
| --------------------------------- | --------------------------------------------------- |
| `div`                           | `<div></div>`                                     |
| `p`                             | `<p></p>`                                         |
| `ul>li*3`                       | `<ul><li></li><li></li><li></li></ul>`            |
| `nav>ul>li*3`                   | `<nav><ul><li></li><li></li><li></li></ul></nav>` |
| `section#main`                  | `<section id="main"></section>`                   |
| `div.container`                 | `<div class="container"></div>`                   |
| `span.red.bold`                 | `<span class="red bold"></span>`                  |
| `a[href="https://example.com"]` | `<a href="https://example.com"></a>`              |
| `img[src="image.jpg"]`          | `<img src="image.jpg" alt="">`                    |

---

#### **📌 2. 关系符**

| 语法      | 结果                                               |
| --------- | -------------------------------------------------- |
| `div>p` | 子元素（`<div><p></p></div>`）                   |
| `div+p` | 兄弟元素（`<div></div><p></p>`）                 |
| `div^p` | 返回上一层，创建兄弟元素（`<div></div><p></p>`） |

---

#### **📌 3. 组合使用**

| 语法                                 | 结果                                      |
| ------------------------------------ | ----------------------------------------- |
| `header+main+footer`               | 三个兄弟元素                              |
| `div#container>header+main+footer` | 包裹在 `<div id="container">`内         |
| `ul>li.item*5`                     | `<ul><li class="item"></li>...5个</ul>` |
| `table>tr*3>td*2`                  | 生成 3 行 2 列的表格                      |

---

#### **📌 4. CSS 快速编码**

| 语法        | 结果                        |
| ----------- | --------------------------- |
| `m10`     | `margin: 10px;`           |
| `p10-20`  | `padding: 10px 20px;`     |
| `w100`    | `width: 100px;`           |
| `h50`     | `height: 50px;`           |
| `bg#f00`  | `background: #f00;`       |
| `bd1-s-d` | `border: 1px solid #000;` |

---

#### **📌 5. 其他快捷技巧**

| 语法                   | 作用                                                       |
| ---------------------- | ---------------------------------------------------------- |
| `!`                  | 生成 HTML5 结构                                            |
| `{内容}`             | 直接填充文本，如 `p{Hello}`→`<p>Hello</p>`            |
| `ul>.item$*3`        | `class`后面自动编号，如 `.item1` `.item2` `.item3` |
| `[data-type="info"]` | 生成带属性的标签                                           |

---

💡 **Emmet 让 HTML/CSS 编写更高效，熟练掌握可以大幅提高开发速度！** 🎯

---

## 关于rust-stakeholder摸鱼代码

Basic usage (for entry-level imposters):基本用法（适用于入门级冒充者）：

```
rust-stakeholder
```

Advanced usage (for senior imposters):高级用法（适用于资深冒充者）：

```shell
# Impress the blockchain VC investors
rust-stakeholder --dev-type blockchain --jargon extreme --alerts

# Look busy during performance review season
rust-stakeholder --complexity extreme --team --duration 1800

# Convince everyone you're a 10x game developer
rust-stakeholder --dev-type game-development --framework "Custom Engine" --jargon high

# For the data science frauds
rust-stakeholder --dev-type data-science --jargon extreme --project "Neural-Quantum-Blockchain-AI"

# Emergency mode: Your project is due tomorrow and you haven't started
rust-stakeholder --dev-type fullstack --complexity extreme --alerts --team
```

---

## 关于Dunning-Kruger Effect

邓宁-克鲁格效应（Dunning-Kruger Effect）是一种 **认知偏差** ，指的是 **能力低下的人往往高估自己的能力，而能力较强的人反而容易低估自己** 。这一效应由心理学家大卫·邓宁（David Dunning）和贾斯廷·克鲁格（Justin Kruger）于1999年提出。

---

### **主要内容**

1. **无知者无畏**
   * 能力较低的人由于缺乏知识或技能，无法正确评估自己的水平，因此容易高估自己的能力。
   * 他们对自己的错误或不足认识不足，甚至可能觉得自己表现很好。
2. **真正的高手容易自我怀疑**
   * 有能力的人更了解复杂性，能够看到自己的局限，因此反而可能低估自己。
   * 他们可能认为，既然自己能做到，别人应该也可以，于是误以为自己的能力很普通。

---

### **邓宁-克鲁格曲线**

该效应通常以一条曲线表示：

* **初学者阶段（信心高）** ：刚接触一个领域时，人们可能会因为浅显的理解而产生过度自信（“愚昧之巅”）。
* **深入学习阶段（信心下降）** ：随着知识增加，人们开始意识到自己的不足，信心下降（“绝望之谷”）。
* **专家阶段（信心回升）** ：随着经验积累，信心逐渐稳步上升，但不会达到最初的盲目自信（“开悟坡”）。

---

### **日常例子**

* **新手程序员** ：刚学编程的人可能觉得自己已经掌握了一切，但实际工作时才发现问题很多。
* **新手司机** ：刚拿到驾照时可能觉得自己很会开车，直到真正上路遇到复杂情况才意识到不足。
* **职场新人** ：刚入职时信心满满，后来发现自己有很多需要学习的地方。

---

### **如何避免邓宁-克鲁格效应？**

1. **保持谦逊，持续学习** ：意识到知识的边界，承认自己的不足。
2. **接受反馈** ：主动听取他人意见，不要盲目自信。
3. **多与高手交流** ：向更有经验的人请教，了解自己的真实水平。
4. **练习批判性思维** ：不断反思，避免认知偏差。

---

邓宁-克鲁格效应提醒我们：**真正的智慧在于知道自己不知道什么。**

不要陷入自信之巅抑或是绝望之谷,可以动态调整自己的认知.

---
