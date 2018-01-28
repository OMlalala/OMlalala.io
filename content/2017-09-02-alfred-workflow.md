Title: "Alfred workflow 初阶探索"
Date: 2017-09-04 21:02:37 +0800
Tags: Alfred, workflow
Slug: 2017-09-02-alfred-workflow


[TOC]


### 背景
最近通过广度优先搜索，收集投资领域的牛人资料。

参照 [@heshenxian1](https://github.com/heshenxian1) 整理的 牛人智库清单：[wisdom-sage](https://www.zotero.org/groups/1568450/openmindclub/items/collectionKey/ZABJPABM)

希望输出自己的 投资牛人清单：[OMlalala > Library](https://www.zotero.org/groups/1654579/omlalala/items)

![](http://omjtq6wcu.bkt.clouddn.com/1.jpg)

### 流程
收集牛人的资料时，以自传、他人写的传记、著作、给股东的信等资料为主，故需要查询下述网站
  - wiki
  - google
  - valuewalk 个人主页
  - google 学术
  - amazon 美国（著作原版）
  - amazon 中国（著作简体字版）
  - 博客来（著作繁体字版）

### 痛点
- 流程：每查找一个投资者，都需要手动打开上述网站，搜索投资者名称，流程固定且重复。
- 目标：希望通过 Alfred 能够自己设置 workflow
- 效果：输入一个投资者名称，能够自动打开以上网页应用的搜索结果

### 探索
- 阳老师对 Alfred 工作流的介绍：[Mac入门笔记（2）：桌面管理 - 阳志平的网志](http://www.yangzhiping.com/tech/mac2.html)
- 官方文档：[Workflows - Alfred Help and Support](https://www.alfredapp.com/help/workflows/)

### 结果
- Alfred workflow 下载地址： [Github](https://github.com/OMlalala/Alfred-workflow) or
[Alfred Forum](https://www.alfredforum.com/topic/10665-web-search-search-investors-information/)

### 演示
- 输入 en + 投资者英文名字，返回 wiki, google, amazon us 等链接

  ![](http://omjtq6wcu.bkt.clouddn.com/2.jpg)

  ![](http://omjtq6wcu.bkt.clouddn.com/3.jpg)

  ![](http://omjtq6wcu.bkt.clouddn.com/4.jpg)

- 输入 cn + 投资者英文名字，返回 amazon cn 链接

  ![](http://omjtq6wcu.bkt.clouddn.com/5.jpg)

  ![](http://omjtq6wcu.bkt.clouddn.com/6.jpg)

  ![](http://omjtq6wcu.bkt.clouddn.com/7.jpg)

### Changelog
20170904 Init
