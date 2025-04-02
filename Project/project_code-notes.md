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

## 关于obsidian笔记软件

Obsidian 是一款基于 Markdown 的笔记和知识管理软件，其主要目标是帮助用户构建自己的“第二大脑”。它通过本地存储文本文件和强大的双向链接功能，让零散的笔记能够以网络化、非线性方式互相连接，从而构建出一个灵活且可持续扩展的知识体系。

---

### 一、软件简介

* **基于 Markdown** ：Obsidian 以纯文本的 Markdown 文件作为存储格式，这不仅保证了数据的可移植性，也使得笔记内容不受平台限制，可以随时用其他编辑器查看或编辑。
* **本地存储** ：所有笔记都存储在用户本地的“vault”（仓库）中，确保了数据隐私与安全，同时也支持离线工作。
* **双向链接和图谱视图** ：用户可以通过双向链接将笔记互相连接，并利用内置的图谱视图直观地展示知识间的关联。
* **丰富的插件生态** ：通过内置的插件市场，Obsidian 可以根据不同需求扩展出各种功能，如任务管理、日历视图、Kanban 看板等。
* **跨平台支持** ：该软件支持 Windows、macOS、Linux 以及移动端系统（Android 和 iOS），满足多设备办公需求。
* **免费模式** ：个人用户可以免费使用所有核心功能，额外的同步和发布服务为付费选项。

---

### 二、主要优点

1. **本地离线与数据安全**

   * 笔记以标准化的 Markdown 文件存储在本地，数据完全掌握在用户自己手中，且支持离线使用，不依赖网络环境。
2. **强大的双向链接与图谱功能**

   * 通过双向链接，用户可以轻松将相关笔记连接在一起，利用图谱视图直观了解知识网络的结构，这对于构建长期、复杂的知识库尤为重要。
3. **丰富的插件与高度可定制性**

   * Obsidian 拥有超过 500 个插件供用户自由挑选，能够根据个人习惯和需求进行界面、功能、快捷键等多方面定制，使得软件功能非常灵活。
4. **Markdown 编辑体验**

   * 支持原生 Markdown 语法，使得书写和编辑过程简洁高效，同时也方便与其他工具之间的内容交换。
5. **免费与付费模式分明**

   * 个人使用完全免费，适合那些不希望将笔记托管在云端的用户；而需要高级同步、发布等服务的用户可以选择付费服务，灵活满足不同需求。

---

### 三、主要缺点

1. **插件繁多导致上手难度增加**

   * 对于不愿意花时间“折腾”的用户来说，众多插件可能让人无从下手。初学者在配置和选择合适的插件时可能会遇到困扰。
2. **块引用功能不够完善**

   * 相较于 Roam Research 等大纲笔记工具，Obsidian 在块引用（对笔记中部分内容进行引用）方面存在一些不足，可能会影响对某些细粒度笔记需求的实现。
3. **协作和多设备同步的局限性**

   * 虽然 Obsidian 提供了同步服务，但其主要设计思路是以个人知识库为主，团队协作和细粒度权限控制方面不如一些专为协作设计的软件（例如 Notion 或 OneNote）。
4. **依赖 Markdown 语法**

   * 对于习惯所见即所得编辑器的用户，纯 Markdown 的编辑体验可能需要一定的适应期，且部分排版和格式化效果不如传统富文本编辑器直观。

---

### 四、总结与适用场景

Obsidian 非常适合那些追求深度知识管理和个人成长的用户，尤其是以下几类人群：

* **学术研究者与写作者** ：通过双向链接和图谱视图，可以将零散的思考、文献笔记和创意进行有效整合，形成系统性的知识体系。
* **技术人员与开发者** ：原生 Markdown 编辑体验和高度可定制的插件生态使其成为记录代码、文档和项目思路的得力工具。
* **个人知识管理爱好者** ：追求构建“第二大脑”、不断迭代个人知识库的用户可以利用其丰富的扩展功能，持续优化自己的思维流程。

不过，对于那些需要实时协作、直观富文本编辑或对界面要求极高的用户，可能需要评估其他工具，或者将 Obsidian 与其他软件联合使用，以弥补其不足。

---

### 五、发展与生态

自 2020 年发布以来，Obsidian 的用户社区迅速壮大，插件生态日益丰富。开发者和用户不断为其贡献新插件，增强了软件的多样性和功能性。此外，开发团队还不断更新软件版本，推出如 Canvas 插件等新功能，为用户带来更好的使用体验。

---

总体来说，Obsidian 以其本地存储、双向链接、丰富插件和高度定制性在笔记软件中独树一帜，是构建个人知识管理系统的理想选择，但其学习曲线和协作局限也需要用户根据自身需求权衡取舍。(gpt-o3-mini)

---

## 关于Github上传文件的大小数量限制

GitHub 对上传文件的大小和数量有明确的限制，以下是详细信息：

**文件大小限制：**

* **通过浏览器上传：** 单个文件不得超过 **25 MB**。
* **通过 Git 推送：** 单个文件不得超过 **100 MB**。 如果尝试推送超过此大小的文件，GitHub 会阻止该操作。
* **使用 Git Large File Storage (Git LFS)：** 对于超过 100 MB 的大文件，建议使用 **Git LFS**。 Git LFS 允许将大文件存储在 Git 仓库之外，并在仓库中保留文件的引用。

**提交差异限制：**

* **单次提交的文件数量：** 单次提交中可包含的最大文件数量为 5,000 个。
* **差异显示限制：** 在拉取请求中，总差异不得超过 20,000 行或 1 MB 的原始差异数据。 任何单个文件的差异不得超过 20,000 行或 500 KB 的原始差异数据。

**仓库存储建议：**

* **仓库总大小：** 建议仓库保持较小，理想情况下小于 1 GB，强烈建议小于 5 GB。 较小的仓库克隆速度更快，使用和维护更容易。

请注意，超过上述限制可能会影响仓库的性能和可用性。

---

## 关于使用Git LFS的一些小技巧代码

Git LFS（Large File Storage）是一个 Git 扩展，用于管理和存储大型文件，尤其是在 Git 仓库中。当你使用 Git 管理大型文件（如视频、音频文件、大型数据集等）时，Git 会变得非常缓慢且占用大量磁盘空间，Git LFS 通过将这些文件替换为指向外部存储的指针来解决这个问题。下面是一些常见的 Git LFS 使用步骤和代码总结。

### 1. 安装 Git LFS

首先，你需要安装 Git LFS。可以使用以下命令：

```bash
# 在 Mac 上
brew install git-lfs

# 在 Linux 上
sudo apt-get install git-lfs

# 在 Windows 上
choco install git-lfs
```

安装完成后，初始化 Git LFS：

```bash
git lfs install
```

### 2. 跟踪大文件

通过 `git lfs track` 命令来指定哪些类型的文件需要使用 Git LFS 来管理。你可以通过文件扩展名来指定，或者直接指定特定的文件路径。

例如，跟踪所有 `.psd` 文件：

```bash
git lfs track "*.psd"
```

跟踪指定文件：

```bash
git lfs track "assets/images/large_image.png"
```

这会在你的 Git 仓库根目录中创建一个 `.gitattributes` 文件，记录文件类型的跟踪信息。

### 3. 提交和推送文件

Git LFS 会把这些文件替换为指向文件存储的指针，而实际的文件会存储在外部 LFS 存储库中。你可以像平常一样使用 Git 提交和推送文件。

```bash
git add .gitattributes
git add <large_files>
git commit -m "Add large files tracked by Git LFS"
git push origin main
```

### 4. 拉取 LFS 文件

当你从 Git 仓库克隆或者拉取最新的代码时，Git LFS 会自动拉取实际的文件。你只需要使用标准的 Git 命令：

```bash
git pull
```

Git LFS 会自动处理 LFS 文件的下载。

### 5. 查看 LFS 文件状态

你可以使用 `git lfs ls-files` 来查看已经被 Git LFS 跟踪的文件。

```bash
git lfs ls-files
```

### 6. 删除 LFS 文件

如果你需要从 Git LFS 中删除文件，可以使用以下命令：

```bash
git lfs untrack "*.psd"
```

这会从 `.gitattributes` 文件中删除相关的 LFS 跟踪规则。

### 7. 删除 LFS 文件并清理存储

如果你想彻底删除 LFS 文件（例如，清理未使用的 LFS 文件），可以使用：

```bash
git lfs prune
```

### 小贴士

* Git LFS 文件的推送和拉取与普通 Git 操作一样，但文件会存储在 Git LFS 的专用服务器上，可能需要额外的存储费用。
* 注意 Git LFS 存储的文件大小限制，很多 Git 托管平台（如 GitHub、GitLab）都有每月的存储配额和带宽限制。

这些是使用 Git LFS 的一些基本步骤和常见命令。通过合理使用 Git LFS，可以有效地管理大型文件并保持 Git 仓库的性能。

---

## 关于一些网站隐藏自己的html文件名后缀


一些网站文章的 URL 会隐藏 `.html` 标签，主要是出于以下几个原因：

### 1. **美观与可读性**

* 一个 URL 结构清晰、简洁，能提升用户体验。例如：

  ```
  example.com/article/how-to-code
  ```

  比起：

  ```
  example.com/article/how-to-code.html
  ```

  更加直观、简洁。

### 2. **SEO 友好**

* 现代搜索引擎并不需要 `.html` 这种扩展名来理解网页内容，简洁的 URL 更易于索引和排名。
* URL 末尾的 `.html` 可能让用户误以为该网站是静态的，而搜索引擎通常更青睐结构清晰、可扩展的 URL 设计。

### 3. **技术实现上的灵活性**

* 通过隐藏 `.html`，网站可以在不改变 URL 的情况下切换技术，比如从静态 HTML 迁移到 PHP、Node.js、React 等。
* 例如：

  ```
  example.com/article/how-to-code
  ```

  可能最初是 `how-to-code.html`，但以后可以改为 `how-to-code.php` 或 `how-to-code/index.html`，不会影响外部链接。

### 4. **更容易进行 URL 重写和重定向**

* 服务器可以通过 **URL Rewrite（URL 重写）** 规则，将 `/article/how-to-code` 解析到 `how-to-code.html`，对用户透明。
* 这在 Apache（.htaccess）、Nginx、IIS 等服务器配置中很常见，例如：
  ```apache
  RewriteEngine On
  RewriteRule ^article/([a-zA-Z0-9-]+)$ article/$1.html [L]
  ```

### 5. **安全性考虑**

* 虽然隐藏 `.html` 本身不会直接提高安全性，但它可以减少暴露底层技术的机会，防止黑客利用已知漏洞攻击特定的文件类型（如 `.php` 或 `.aspx`）。

### 6. **移动端与 API 兼容**

* 如果 URL 没有 `.html`，同一个路径可以根据不同的请求类型（HTML 页面、JSON API 等）返回不同的内容。例如：

  ```
  example.com/article/how-to-code
  ```

  * Web 端请求 → 返回 HTML 页面
  * API 请求 → 返回 JSON 数据

### **总结**

隐藏 `.html` 主要是为了 **提升用户体验、SEO 友好性、灵活性和安全性** 。很多现代网站通过 **URL 重写技术** 来实现这一点，同时确保用户和搜索引擎可以正常访问内容。

---
