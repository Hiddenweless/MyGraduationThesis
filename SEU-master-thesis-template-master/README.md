# 东南大学硕士毕业论文 Latex 模板

本仓库是基于levitate-qian的 [SEUThesisLatexTemplate-Levitate](https://levitate.lanzoub.com/iRmnq2j8wcnc) 修改而来。详细文档查看[LaTeX札记（七）：硕士学位论文相关](https://levitate-qian.github.io/2024/12/28/latex-note-07/)

## 模板修改次序

TouchFishPioneer -->  Reanon

TouchFishPioneer  +  Reanon  -->  levitate-qian  -->  本模板

TouchFishPioneer: [SEU-master-thesis](https://github.com/TouchFishPioneer/SEU-master-thesis)

Reanon: [SEUThesisLatexTemplate](https://github.com/Reanon/SEUThesisLatexTemplate)

levitate-qian: [SEUThesisLatexTemplate-Levitate](https://levitate.lanzoub.com/iRmnq2j8wcnc)

## 本模板修改内容

- 在Windows下，使用AutoFakeBold来表示加粗宋体。

- 将图、表列表中的内容修改为图1-1、表1-1的形式，原模板中的列表只有1-1，没有“图”、“表”字样。

- 将原模板适用于双面打印的形式修改为单面，去掉了一些空白页。

## 使用攻略

### Overleaf及Mac

详见Reanon: [SEUThesisLatexTemplate](https://github.com/Reanon/SEUThesisLatexTemplate) 或 docs/README-src.md或docs/README.pdf

### Windows

参考CSDN[Latex和Vscode安装和配置](https://blog.csdn.net/bulletstart/article/details/142502912)或[VScode配置LaTex编辑](https://blog.csdn.net/weixin_55988068/article/details/138716818)

需执行脚本`make.bat`

## 代码细节

- 在main.tex中，学硕使用第一行，专硕注释掉第一行

- 如需去掉多余的空白页，取消main.tex第70行的注释

- 参考文献格式：作者只有三名或更少时，显示所有作者。中文作者第四名及以后使用`等`代替，英文作者第四名及以后使用`et al`代替，英文作者名全部大写。

- 更多细节查看`main.pdf`第一章第一节的注意事项

