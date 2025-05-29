# 如何构建自己的第二大脑来减轻大脑的负担?

想写这篇文章也是受到红迪网上一篇博客的影响, 有关使用GOOGLE drive和Chat来构建自己的第二大脑

谢天谢地保存了这篇[帖子](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jqzpi9/finally_i_found_a_way_to_keep_chatgpt_remember/)哈哈哈.

然后后面就想一下自己要怎么构建了, 我的想法是: 通过不断的提示来让chat记住之前的话并及时优化自己的prompt.

那两篇博客提到的方法就是连接至google drive, 归档自己所有聊天,之后每次聊天的时候让gpt检索里面的信息然后回答. 但是我觉得这个方法有点不太实际, Google的东西能光明正大给你openai用?不是长久之计.

还有一点就是今天看到chat更新的一个记忆库就是网上的很多东西,而且可以连接到github, 在想可不可以把自己的笔记存储在repo里面让chat读取然后回答. 现在先去测试一下吧, 别是高级用户才能使用哈哈哈.

记录一下刚刚和gpt交流的结果,如果想看原文的话可以看这段[对话](https://chatgpt.com/share/6800ef0f-62c8-800b-ae67-d4584d5d3b72), 大致的结果是如下:

gpt把自己类比成一位图书管理员,只是擅长总结归纳我们的文本,而无法逐字逐句的复述什么之类的,但是我将我的para日志的[repo](https://github.com/skywalker23241/Junbo-PARA-Notes/blob/main/Project/project_log.md)连接到chat后,它其实是可以读取部分数据的,但是可能受模型功能限制,还无法读取全部的内容,可能也是因为我的日志比较长,而且记录的很多都是碎碎念哈哈哈,它只是简单的总结了一下最近发生的事情就草草了之了~ 有点敷衍我.

这里我就是把github的仓库类比成一个红迪网上面的这篇[帖子](https://syncreticsage.wordpress.com/2025/04/03/memory-loophole-creating-a-second-brain-for-chatgpt-discussion-w-chatgpt/)里面说的Gdrive吧, 但是我还没归档我和chat的所有聊天到一个repo然后让他读取之类的.只是那我最近的日志试了试,效果还是不太行,而且随着时间的积累,chat会越来越多,这个存储量也是一个问题, 这里我想到另一个办法, 就是在chat中也使用自己的para笔记的方法来尽量减少存储的大小,这样是不是就能让chat记忆更多的东西.

总结一下吧, 除了前面老哥说的那种[方法](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jqzpi9/finally_i_found_a_way_to_keep_chatgpt_remember/)我觉得有点不切实际,如果一直让ai自己去优化我们和他的记忆显然是不实际的,还有就是Gdrive/Gsheet的存储方式....... out!

然后就是我自己想到的方法, 连接自己在github上面的知识库或者是对话库来达到相似的效果, 目前的情况就是还行, 起码可以总结里面的内容, 但这个库是需要我们自己去维护的, 使用前面提到的[para的方法](https://fortelabs.com/blog/para/?utm_source=pocket_saves)来减小这个库数据的量,不断归档分类, 然后只是让chat处理我们log里面的数据,来作为我们的"第二大脑", so, that's my plan.

然后就是怎么实现了.

1. 归档自己的聊天 to github repo with para;
2. 连接自己的gpt and github.
3. 让chat读取其中归档的聊天并持续更新
4. loop
5. 优化repo里面的数据来减少存储
6. done!

目前还不知道能不能实现哈哈哈,先这样吧. 算了吧, 感觉chat记忆的部分有token限制哈哈哈......

目前chat免费的我觉得那种个性化的聊天也只是在一段对话中生效,当他提醒你过一段时间再试之后就基本上是那种普通的对话了,我觉得应该是没有把你个性化的数据接入的回答,感觉很一般.

所以这个项目肯定是要依赖chat的高级模型的,而且axize的那个合租肯定是满足不了的

先这样吧......

感觉这个文章可以重新开始写了, 技术更新的太快了, 现在的MCP给了很多可以实现这个想法的机会, 未完待续...... (5.27日整理笔记)
