# 论文正文审阅文本包

- 生成时间：2026-04-25 15:22:01
- 论文目录：`/Users/wtl/Desktop/我的毕业论文 /SEU-master-thesis-template-master`
- 说明：本文件汇总正文写作相关源文件，排除图片、PDF、编译中间文件和个人附属页。
- 用途：可交给其他模型检查行文逻辑、术语一致性、章节衔接、图表引用和学术表达。

## 文件清单

- `main.tex`
- `chapters/abstract.tex`
- `chapters/chapter1.tex`
- `chapters/chapter2.tex`
- `chapters/chapter3.tex`
- `chapters/chapter4.tex`
- `chapters/chapter5.tex`
- `chapters/chapter6.tex`
- `chapters/appendix.tex`
- `reference.bib`

---

## main.tex

```latex
% !TEX program = xelatex
% \documentclass[algorithmlist,figurelist,tablelist,nomlist]{template/seumasterthesis} %学硕使用这一行
\documentclass[algorithmlist,figurelist,tablelist,engineer,fontset=fandol,nocolorlinks]{template/seumasterthesis}
\setCJKmainfont{Noto Serif CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{multirow} % 处理跨行表格数据
\usepackage{array}
\usepackage{longtable}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{float}
\usepackage[section]{placeins}
\usepackage{lipsum}
\usepackage{pifont}  % 引入 pifont 宏包
\usepackage{enumitem}
\usepackage{etoolbox}
\usetikzlibrary{positioning,calc,arrows.meta,fit,backgrounds,shapes.multipart}
\pgfplotsset{compat=1.18}
\preto{\subsection}{\FloatBarrier}

\definecolor{pgBlue}{HTML}{5B8FF9}
\definecolor{pgTeal}{HTML}{5AD8A6}
\definecolor{pgOrange}{HTML}{F6BD16}
\definecolor{pgPurple}{HTML}{9270CA}
\definecolor{pgGreen}{HTML}{7BCFA6}
\definecolor{pgDark}{HTML}{2F3A4A}
\definecolor{pgSkyBg}{HTML}{EAF3FF}
\definecolor{pgMintBg}{HTML}{E8F8F1}
\definecolor{pgAmberBg}{HTML}{FFF3D9}
\definecolor{pgLavenderBg}{HTML}{F1ECFF}
\definecolor{pgGreenBg}{HTML}{EEF8F1}

\tikzset{
    roadmaptitle/.style={draw=pgBlue!70!black, fill=pgBlue!16, rounded corners=10pt, line width=1pt, minimum height=1.1cm, align=center, text=pgDark, font=\bfseries\large},
    roadmapleft/.style={draw=pgOrange!78!black, fill=pgAmberBg, rounded corners=10pt, line width=1pt},
    roadmapright/.style={draw=pgTeal!72!black, fill=pgMintBg, rounded corners=10pt, line width=1pt},
    roadmapcard/.style={draw=black!72, fill=white, rounded corners=8pt, line width=0.9pt, minimum width=4.1cm, minimum height=1.1cm, text width=4.0cm, align=center},
    roadmaparrow/.style={-{Latex[length=3mm,width=2.2mm]}, line width=1.1pt, draw=pgBlue!78!black},
    feedbackarrow/.style={-{Latex[length=3mm,width=2.2mm]}, line width=1pt, draw=pgOrange!88!black, dashed},
    flowboxblue/.style={draw=pgBlue!72!black, fill=pgSkyBg, rounded corners=8pt, line width=0.95pt, align=center},
    flowboxorange/.style={draw=pgOrange!82!black, fill=pgAmberBg, rounded corners=8pt, line width=0.95pt, align=center},
    flowboxteal/.style={draw=pgTeal!72!black, fill=pgMintBg, rounded corners=8pt, line width=0.95pt, align=center},
    flowboxpurple/.style={draw=pgPurple!72!black, fill=pgLavenderBg, rounded corners=8pt, line width=0.95pt, align=center},
    flowboxgreen/.style={draw=pgGreen!68!black, fill=pgGreenBg, rounded corners=8pt, line width=0.95pt, align=center},
    flowlink/.style={-{Latex[length=3mm,width=2.2mm]}, line width=1.05pt, draw=pgBlue!80!black}
}

\pgfplotscreateplotcyclelist{plangraph}{
    {draw=pgBlue, fill=pgBlue!60},
    {draw=pgTeal!90!black, fill=pgTeal!65},
    {draw=pgOrange!92!black, fill=pgOrange!72},
    {draw=pgPurple, fill=pgPurple!52},
    {draw=pgGreen!85!black, fill=pgGreen!55}
}

\pgfplotsset{
    cycle list name=plangraph,
    every axis/.append style={
        axis line style={draw=black!60},
        tick style={draw=black!55},
        grid style={draw=black!12},
        major grid style={draw=black!12},
        label style={text=black!85},
        tick label style={text=black!80}
    }
}
% Mac系统取消以下两行代码的注释，
% \usepackage{fontspec} % 加载 fontspec 宏包
% \usepackage{xeCJK}    % 加载 xeCJK 宏包以支持中文
\renewcommand{\thefootnote}{\ding{\numexpr171+\value{footnote}}}
\begin{document}

%% ----------------------------------------------------------------------------
%%                                 Meta Data
%% ----------------------------------------------------------------------------
\categorynumber{TN92} %《中国图书资料分类法》分类法
\UDC{004.8}              %《国际十进分类法UDC》的类号
\secretlevel{公开}        % 学位论文密级分为"公开"、"内部"、"秘密"和"机密"四种
\studentid{请填写学号}      % 学号要完整，前面的零不能省略

%% ----------------------------------------------------------------------------
%%                           Thesis Title and Spine
%% ----------------------------------------------------------------------------
\title
    {基于规划反馈的图推理多智能体协同求解方法研究}        % 论文中文标题
    {}         % 论文中文副标题，没有可以空着
    {Research on Planning-Feedback-Based Multi-Agent Collaborative Solving Methods for Graph Reasoning}  % 论文英文标题
    {}            % 论文英文副标题，没有可以空着

\spine
	% 书脊标题与副标题
    {基于规划反馈的图推理多智能体协同求解方法研究} 
    {}                                                               

%% ----------------------------------------------------------------------------
%%                             Author and Advidor
%% ----------------------------------------------------------------------------
\author
    {王腾龙}                        % 作者中文姓名
    {WANG Teng-long}                  % 作者英文姓名，首字母大写，姓名分开，双字用「-」连接

\advisor
    {林丽}                % 导师中文姓名
    {LIN Li}        % 导师英文姓名
    {}                     % 导师职称
%% ----------------------------------------------------------------------------
%%                              Thesis Defence
%% ----------------------------------------------------------------------------
\engthesistype{应用研究}            % 工程硕士论文类型
\degreetype                        % 学位类型
    {电子信息硕士}
    {Master of Electronic Information}
\major{人工智能}                 % 一级学科名
\submajor{图推理与智能计算}             % 二级学科名
\defenddate{2026年5月}          % 答辩日期 \today
\authorizedate{}                  % 授予学位日期，这个档案袋不需要填
\committeechair{}               % 答辩委员会主席姓名
\reviewer{}{}                % 两位论文评阅人姓名
\department                        % 学院名称
    {苏州联合研究生院}
    {Suzhou Joint Graduate School}
% \seuthesisthanks                % 资助信息，没有可以不写
%     {本文的部分工作受国家自然基金 No. zxgg666 的支持与帮助，在此表示感谢。}

%garbagecoder: \let 是 TeX 的赋值命令，它会让 \cleardoublepage 变成 \clearpage，原模板限制奇偶页适用于双面打印，此命令用于去掉多余的空白页
% \let\cleardoublepage\clearpage 

%% ----------------------------------------------------------------------------
%%                                  Cover
%% ----------------------------------------------------------------------------
% ⚠️ 可以在编写论文的时候注释掉封面，加快编译速度
% % \makebigcover  % 生成A3大封面
\makecover     % 生成小封面
	 
%% ----------------------------------------------------------------------------
%%                          Abstract and Contents
%% ----------------------------------------------------------------------------
\input{chapters/abstract}
\cleardoublepage
\addcontentsline{toc}{chapter}{目　　录}
\tableofcontents          % 生成目录
\listofothers             % 生成图、表等目录，没有可以不写
 
%% ----------------------------------------------------------------------------
%%                                Main Body
%% ----------------------------------------------------------------------------
\mainmatter                    % 开始正文
\input{chapters/chapter1}      % 第一章：
\input{chapters/chapter2}      % 第二章：
\input{chapters/chapter3}      % 第三章：
\input{chapters/chapter4}      % 第四章：
\input{chapters/chapter5}      % 第五章：
\input{chapters/chapter6}      % 第六章：

%% ----------------------------------------------------------------------------
%%            Acknowledgement, Appendix, Bibliography and Resume
%% ----------------------------------------------------------------------------
\input{chapters/acknowledgement}    % 致谢
\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{\bibname}
\bibliographystyle{gbt7714-numerical}
\bibliography{reference}            % 生成参考文献

%% 下面一句只是用于提示 TexPad 参考文献位置，正式生成时一定要删除
% \bibliography{reference.bib} % 告诉编译器参考文献所在文件

\input{chapters/appendix}           % 附录
\input{chapters/resume}             % 作者简介
\input{chapters/Committees_list}    % 毕业/学位论文答辩委员会名单
\end{document}
```

---

## chapters/abstract.tex

```latex
%% ----------------------------------------------------------------------------
%%                              Chinese Abstract
%% ----------------------------------------------------------------------------
\begin{abstract}{图推理, 大语言模型, 规划反馈, 多智能体}
图推理是图数据分析与智能决策中的关键问题，在路径规划、网络分析、组合优化和知识推断等场景中具有重要应用价值。近年来，大语言模型在自然语言理解、复杂推理和程序生成方面取得了显著进展，为图推理任务的自动化求解提供了新的可能。然而，图推理具有显著的拓扑依赖与强约束特征，一方面，现有方法通常将图数据序列化为文本后进行端到端推理，容易在长序列输入和复杂约束下出现拓扑关系遗漏、结构理解偏差与答案幻觉；另一方面，一些依赖历史任务样本、经验代码库或专门微调的程序生成方法虽然能够提升局部任务表现，但往往伴随较高的数据构建与维护成本，在知识更新和跨任务泛化上仍存在边界。这些问题共同限制了大语言模型在复杂图任务中的可靠性与泛化能力。

针对上述问题，本文提出一种基于规划反馈的图推理多智能体协同求解框架 PlanGraph，将求解过程组织为规划生成、规划引导检索与检索质量评估、验证推理三个阶段。首先，问题智能体与规划智能体协同工作，将自然语言图任务转化为结构化伪代码规划，显式表达任务目标、核心算法步骤与约束条件；其次，检索智能体依据规划结果从图算法文档知识库中检索相关 API 与实现知识，并结合检索质量评估在必要时进行知识片段精炼或补充检索，以提高外部知识与求解步骤之间的匹配精度；最后，编码智能体基于规划与检索结果生成可执行程序，并结合执行测试、错误反馈、推理修复和有界重生成机制形成验证闭环，使规划在前向方向上约束知识调用与程序生成，反馈在反向方向上修正实现偏差与约束遗漏，从而提升程序化图推理的稳定性、正确性与可解释性。

本文在 GraphArena、NLGraph、GraphWiz、LLM4DyG 和 GraphInstruct 五个公开图推理基准测试集上对所提方法进行了系统评估。实验结果表明，PlanGraph 在多个数据集上取得了优于现有方法的性能，平均准确率达到 97.69\%，并在经典图算法、组合优化和指令式图推理任务中表现出较强的鲁棒性。消融实验进一步验证了规划模块、检索模块和验证模块对整体性能提升的关键作用。研究结果说明，将显式规划、外部知识检索与程序验证通过反馈闭环有机结合，能够有效缓解大语言模型在图推理任务中的幻觉与不稳定问题，为大语言模型与图算法工具协同求解复杂结构化问题提供了一种具有工程可行性和可解释性的解决思路。
\end{abstract}

%% ----------------------------------------------------------------------------
%%                              English Abstract
%% ----------------------------------------------------------------------------
\begin{englishabstract}{graph reasoning, large language models, planning feedback, multi-agent systems}
Graph reasoning is a core problem in graph analytics and intelligent decision-making, with wide applications in path planning, network analysis, combinatorial optimization, and knowledge inference. Recent advances in large language models (LLMs) have opened a new avenue for automating graph reasoning tasks through natural language understanding, complex reasoning, and code generation. However, graph reasoning is characterized by strong topological dependencies and strict structural constraints. Existing approaches typically serialize graphs into text for end-to-end reasoning, or directly prompt LLMs to generate graph-solving programs, which makes task understanding, algorithm selection, knowledge usage, and correctness verification entangled in a single generation process. In addition, some program-generation methods rely on historical task samples, empirical code repositories, or task-specific fine-tuning, which introduces considerable data construction and maintenance costs and limits knowledge updating and cross-task generalization. These issues lead to incomplete structural understanding, inaccurate algorithm selection, unstable code execution, and hallucinated answers in complex graph reasoning tasks.

To address these challenges, this thesis proposes PlanGraph, a planning-feedback-based multi-agent framework for graph reasoning, which decomposes the solving process into three stages: planning generation, plan-guided retrieval with retrieval-quality assessment, and verified reasoning. First, a question agent and a planning agent collaboratively transform a natural language graph task into structured pseudocode that explicitly represents the task goal, key algorithmic steps, and constraints. Next, a retrieval agent uses the generated plan to retrieve relevant API documentation and graph algorithm knowledge from an external knowledge base, and further conducts quality assessment, snippet refinement, or supplementary retrieval when necessary, improving the alignment between retrieved knowledge and the intended solution procedure. Finally, a coding agent generates executable programs based on the plan and retrieved knowledge, while an execution-verification loop refines the solution through testing, error feedback, reasoning-based repair, and bounded regeneration. In this process, planning serves as a forward constraint on retrieval and code generation, while feedback acts as a backward correction signal for implementation errors and missing constraints, thereby improving stability, correctness, and interpretability.

Extensive experiments are conducted on five public graph reasoning benchmarks, namely GraphArena, NLGraph, GraphWiz, LLM4DyG, and GraphInstruct. The results show that PlanGraph outperforms existing methods on multiple datasets and achieves an average accuracy of 97.69\%. The framework also demonstrates strong robustness on classical graph algorithm tasks, combinatorial optimization problems, and instruction-following graph reasoning tasks. Ablation studies further verify the critical contributions of the planning module, the retrieval module, and the verification module. These findings indicate that tightly integrating explicit planning, external knowledge retrieval, and program verification through a feedback loop can effectively mitigate hallucinations and instability in LLM-based graph reasoning, providing an interpretable and practical solution for solving complex structured problems with LLMs and graph algorithm tools.
\end{englishabstract}
```

---

## chapters/chapter1.tex

```latex
\chapter{绪论}
\label{chp:introduction}

\section{研究背景与意义}

图结构能够自然描述实体之间的复杂关系，广泛存在于交通网络、社交网络、生物分子网络、知识图谱以及软件依赖分析等场景中。围绕图结构开展推理与计算，是图论、数据挖掘和人工智能领域的核心问题之一。最短路径、连通性判定、匹配、最大团、最小顶点覆盖以及旅行商问题等典型任务，既具有明确的理论基础，也在工程应用中具有重要价值\cite{cormen2009clrs,diestel2017graph,korte2018combinatorial}。

近年来，大语言模型在自然语言理解、复杂推理和程序生成方面表现出强大能力。Transformer 架构、少样本学习、指令微调以及开源基础模型的发展，为语言模型从文本建模走向通用任务求解提供了重要基础\cite{vaswani2017attention,brown2020language,ouyang2022instructgpt,touvron2023llama,bubeck2023sparks}。通过链式思维提示、自一致性采样、树状思维等技术，语言模型在数学推理、代码生成和工具调用任务中取得了显著进展\cite{wei2022chain,wang2023selfconsistency,yao2023tree,besta2024graph,gao2023pal}。这些进展使得研究者开始尝试将大语言模型应用于图推理任务，希望利用其自然语言理解能力完成从任务描述到算法求解的自动映射。

% [figure omitted: image content removed]
\caption{图推理任务整体示意图}
\label{fig:intro_task_overview}

图\ref{fig:intro_task_overview}给出了本文所研究图推理任务的基本流程：系统首先接收自然语言形式的任务描述，再围绕给定图结构执行最短路径、最大团、旅行商等不同类型的图推理任务，最终生成目标答案。与传统纯文本问答不同，这类任务的关键在于如何把自然语言目标准确映射到可执行的图算法流程上。

然而，图推理与一般文本推理存在本质差异。图结构强调节点、边及其拓扑关系，输入信息通常由离散的结构对象组成，而非自然语言中的线性语义序列。为了适配语言模型，大多数现有方法需要将图序列化为文本，再让模型直接进行端到端推理或生成代码。随着图规模增大、边属性变复杂以及约束条件增多，这种串行化表示会显著增加模型理解负担，导致拓扑关系遗漏、约束违反和答案幻觉等问题。

针对这一挑战，本文聚焦的问题并不是泛泛意义上的图推理任务较难，而是大语言模型在图推理求解中普遍面临的流程耦合问题：任务理解、算法选择、知识调用、代码实现和正确性验证常被压缩在一次生成过程中，任何一个中间环节出现偏差，都可能造成最终答案错误或程序不可执行。对于图推理这类同时依赖结构理解、算法步骤和约束满足的任务而言，这种耦合会进一步放大错误传播风险。

因此，本文围绕如何提升大语言模型在图推理任务中的可靠性与泛化能力开展研究。本文认为，仅依赖更长的推理链或更强的基础模型，并不足以从根本上解决图任务中的稳定性问题；更关键的是在任务描述与程序执行之间引入显式的中间组织机制，使规划在前向方向上约束知识调用与代码生成，使反馈在反向方向上修正实现偏差与约束遗漏。基于这一判断，本文选择以规划前向约束与反馈反向修正为核心思路，构建面向图推理的多智能体协同求解框架。

\section{国内外研究现状}

为了更清晰地界定本文的研究问题与方法设计依据，本节对与本文密切相关的研究工作进行归纳和总结，主要从以下三个方面展开：大语言模型推理增强方法、图推理任务上的大模型研究进展，以及现有方法在图任务求解中的主要局限。最后，本文将在此基础上对现有工作的启发与不足进行分析，进一步说明本文选择规划反馈协同求解路线的原因。

\subsection{大语言模型推理方法研究}

大语言模型的推理能力增强，最初主要依赖提示工程与解码策略优化。Chain-of-Thought 通过显式生成中间步骤，提高了模型在算术和逻辑问题上的表现\cite{wei2022chain}；Scratchpad、过程验证器与 Program of Thoughts 等工作进一步说明，把中间计算、程序执行和结果验证显式化，有助于降低复杂推理中的隐性错误\cite{nye2021scratchpads,cobbe2021verifiers,chen2023pot}。Self-Consistency 则通过对多条推理路径进行投票聚合，降低单一路径错误带来的影响\cite{wang2023selfconsistency}。在此基础上，Least-to-Most Prompting 将复杂问题拆解为更小的子问题逐步求解\cite{zhou2023least}，Tree-of-Thoughts 与 Graph-of-Thoughts 进一步引入了分支探索与结构化搜索思想\cite{yao2023tree,besta2024graph}。此外，Zero-Shot CoT、Selection-Inference、ReAct、Self-Refine、Reflexion、CRITIC、语言智能体树搜索以及过程验证类工作，又分别从零样本推理、选择--推断分离、推理--行动耦合、自反馈迭代修正、工具交互式纠错、搜索式行动规划和过程监督等角度扩展了推理增强范式\cite{kojima2022zeroshot,creswell2023selection,yao2023react,madaan2023selfrefine,shinn2023reflexion,critic2023,zhou2024lats,lightman2023processreward}。这些方法为复杂任务中的分步思考提供了重要启发。

除了基于文本提示增强推理能力，研究者还尝试将语言模型与外部工具、执行环境和程序系统进行结合。PAL 将问题求解过程转化为程序生成与执行，使模型把复杂计算委托给解释器完成\cite{gao2023pal}；Toolformer 和 ToolLLM 则强调模型对外部 API 的主动调用能力\cite{schick2023toolformer,qin2023toolllm}。进一步地，Gorilla 与 AlphaCode 等工作分别从大规模 API 对齐和复杂程序生成角度说明，语言模型可以借助外部环境获得更强的任务求解能力\cite{gorilla2023,liang2022alphacode}。这类方法表明，语言模型并不需要独立完成所有细节计算，而是可以通过规划、调用工具和读取外部知识来完成更复杂的任务。

从技术路线演进看，大语言模型推理增强大致经历了从提示增强、工具增强到过程控制与系统化协同三个阶段。早期方法主要致力于通过提示设计和解码策略让模型显式展开中间思路；随后研究开始强调把精确计算、外部知识检索和 API 调用交给程序环境完成；再往后，越来越多工作开始关注推理过程本身的可追踪、可回退与可验证性，使规划、行动、反馈和修复逐步被组织为统一的求解链路\cite{wei2022chain,wang2023selfconsistency,gao2023pal,schick2023toolformer,qin2023toolllm,yao2023react,critic2023}。这说明，复杂任务能力的提升并不只是让模型思考得更长，更重要的是让模型在不同阶段承担合适职责，并与外部能力形成稳定分工。

然而，上述推理增强研究大多围绕自然语言问答、数学推理和通用代码生成任务展开，其输入通常仍是线性文本，目标也多是生成答案、程序或行动序列。对于图推理任务，仅依赖一般性的思维链扩展，往往难以保证节点关系、边属性和约束条件在中间步骤中被完整保留；仅依赖工具调用，也难以保证算法步骤与知识检索、程序实现之间始终保持一致。因此，这些研究虽然为图任务中的分阶段求解提供了重要方法论基础，但仍需要进一步引入面向图结构的中间表示与过程验证机制，才能真正适应高约束图推理场景\cite{besta2024graph,gao2023pal,yao2023react,lightman2023processreward}。

\subsection{图推理任务上的大语言模型研究}

针对图推理问题，近两年出现了一批专门的评测基准。NLGraph 关注自然语言条件下的经典图算法任务\cite{chen2024nlgraph}，GraphWiz 面向指令式图算法推理\cite{gong2024graphwiz}，GraphArena、GraphInstruct 与 LLM4DyG 则分别从经典图问题、指令跟随场景和动态图场景评估模型能力\cite{tang2025grapharena,graphinstruct2024,llm4dyg2024}。与此同时，相关方法研究也开始从图理解对齐、图序列化表达和组合优化思维生成等角度系统推动该方向发展\cite{fatemi2024talk,zhang2023graphmeetsllms,jin2024llmgraphs,gundam2024,graphthought2025,pseudocode2025}。这些基准与方法研究普遍表明，尽管大模型在小规模样例和规则明确的问题上能够取得一定效果，但在结构复杂、约束严格或需要组合优化的场景下，其性能仍显著受限。

现有图推理增强方法大致可分为三类。第一类方法强调图结构感知，通过任务改写、结构提示或针对图任务进行指令微调，以提升模型对图拓扑的理解\cite{tang2024graphgpt,pan2024graphllm}。第二类方法强调程序化求解，将图任务翻译为 Python 代码，并借助 NetworkX 等图计算库完成求解\cite{hagberg2008networkx,zhang2025gcoder}。第三类方法尝试采用多智能体架构，由不同角色分别完成规划、检索、代码生成、评审与修复等步骤，以提升系统整体稳定性\cite{li2024graphteam}。

从评测设计看，不同基准测试集对模型能力的侧重点存在明显差异。NLGraph 更强调自然语言描述与经典图算法之间的映射关系，关注模型能否从文本中恢复任务语义并选择合适算法；GraphWiz 和 GraphInstruct 更强调指令跟随、执行步骤一致性与输出格式规范性；GraphArena 更突出任务覆盖面与组合优化难度；LLM4DyG 则进一步把时间演化和动态图约束纳入评测范围\cite{chen2024nlgraph,gong2024graphwiz,tang2025grapharena,graphinstruct2024,llm4dyg2024}。此外，围绕图推理泛化、复杂图理解、大规模图数据编码和强化学习式图推理的最新研究，也进一步强调了评测任务必须同时覆盖推理正确性、代码执行能力和跨结构泛化能力\cite{zhang2024memorization,yuan2025gracore,wu2025grapheval36k,guo2025g1}。这表明，图推理并不是单一能力测试，而是由输入解析、图构建、算法匹配、程序执行和结果验证等多个子能力共同决定的复合任务。

从方法发展脉络看，现有研究实际上已经逐步形成了结构感知增强—程序化求解—多智能体协作三条主线。结构感知类方法试图缩小语言模型与图结构之间的表征鸿沟，程序化方法强调借助成熟图计算库获得稳定可执行结果，多智能体方法则进一步把任务理解、规划组织、知识获取和错误修复拆分为多个角色协同完成\cite{tang2024graphgpt,pan2024graphllm,zhang2025gcoder,li2024graphteam}。这些探索说明，研究重点正在从如何让模型看懂图进一步转向如何让系统稳定求解图任务。但在中间规划表示、知识调用一致性和验证闭环方面，现有路线仍存在不足，这也直接引出了下一小节需要重点讨论的问题。

\subsection{现有方法的不足}

尽管已有研究取得了积极进展，但从图推理任务的实际求解链路看，现有方法仍然没有很好地回答一个核心问题：如何在任务理解、知识调用与程序执行之间建立稳定且可验证的中间组织机制。综合前述研究可以看到，当前方法的不足主要集中在两条相互关联的技术路线上。

第一类不足来自端到端图推理过程本身。模型往往需要在一次生成中同时完成任务理解、图结构还原、算法匹配、知识调用和结果组织。面对长序列化图输入、复杂属性约束和组合优化目标时，拓扑关系遗漏、约束违反与答案幻觉更容易出现。即使引入外部文档或 API，如果检索查询仍然直接由原始问题生成，也很难保证返回知识与实际算法步骤始终保持一致。

第二类不足来自对历史经验数据和专门适配过程的依赖。一些程序生成或经验增强方法通过任务--代码对、样例库检索或专门微调来提高图任务表现，这类路径在特定任务上往往有效，但通常伴随较高的数据构建、维护和更新成本；当任务类型变化、图规模扩大或基准测试集发生迁移时，其泛化能力和可持续适配性仍然存在明显边界。

因此，有必要构建一种更加稳健的图推理框架，在保留大语言模型通用理解能力的同时，将规划、知识使用与执行验证显式拆分，以提升求解过程的可靠性与泛化性能。

\section{研究内容与研究目标}

围绕上述问题，本文提出一种基于规划反馈的图推理多智能体协同求解框架 PlanGraph。本文所关注的研究对象，不是一般意义上的文本推理增强，而是如何让大语言模型在图推理任务中形成可规划、可验证、可修正的求解过程。结合前一节的分析，本文认为改进空间主要体现在两个方面：其一，通过显式规划对复杂图任务进行结构化拆解，减轻模型在一次生成中同时处理任务理解、算法匹配与约束满足的负担；其二，以规划结果而非原始问题作为知识调用的中间语义，使检索目标更贴近当前求解步骤，并在必要时触发知识片段精炼或补充检索。基于这一定位，PlanGraph 不直接从原始自然语言问题生成最终程序或答案，而是将整个求解过程拆分为规划生成、规划引导检索与检索质量评估、验证推理三个阶段。

在规划生成阶段，系统首先从原始问题中抽取任务目标、输入图信息和输出要求，并由规划智能体将问题转换为结构化伪代码。该伪代码不追求完整实现细节，而是强调算法意图、求解顺序与关键约束，用于刻画后续程序生成所需的核心操作序列。在知识检索阶段，系统不再基于原始问题文本直接检索外部知识，而是使用规划阶段生成的伪代码作为查询依据，从图算法文档知识库中检索相关的 API 说明、输入输出约束和使用示例。这种方式能够使检索目标更贴近实际算法步骤，从而减少无关信息的干扰。在验证推理阶段，编码智能体结合规划结果和检索知识生成可执行代码；随后系统通过小样本图上的单元测试验证程序基本正确性，并在出现错误时调用推理智能体进行迭代修复。当多轮修复仍失败时，系统触发重新生成机制，形成局部修复--重生成双层闭环。由此，规划在前向方向上约束检索与代码生成，执行反馈在反向方向上修正实现偏差、知识不匹配与约束遗漏，最终输出可靠答案。

结合前述分析，本文进一步将研究问题凝练为两个相互关联的核心挑战。其一，如何把复杂的自然语言图推理任务稳定映射为可执行求解过程。图任务往往同时包含问题语义、图结构信息和约束条件，若缺乏合适的中间表示，模型容易在理解正确但实现偏差与实现正确但约束遗漏之间出现错位。其二，如何在规划约束下实现面向当前任务的高质量外部知识调用与运行可靠性提升。对图任务而言，检索结果是否与当前算法步骤一致，直接决定后续代码生成质量；而一次性程序生成又难以覆盖复杂边界条件，因此还需要借助执行反馈与迭代修复机制共同提高最终正确率。

围绕上述关键问题，本文的总体研究目标是：构建一种能够兼顾可解释性、稳定性与泛化性的图推理框架，使大语言模型在复杂图任务上不仅能够给出答案，而且能够形成可追踪、可验证、可修正的求解过程。具体而言，本文期望达到以下目标：

（1）在方法层面，建立规划生成—知识检索—验证推理的分阶段求解范式，并通过反馈回流机制降低端到端推理负担；

（2）在系统层面，形成面向多智能体协同的中间工件传递与黑板调度机制，保证模块之间的信息一致性与过程可追踪性；

（3）在实验层面，在多个公开基准测试集上验证所提方法在精确匹配率、稳定性与鲁棒性方面的综合表现。

在上述研究内容与研究目标基础上，本文进一步形成如下技术路线。整体求解过程可概括为问题解析—显式规划—知识检索—程序生成—执行验证—答案组织六个阶段。如图\ref{fig:research_roadmap}所示，本文整体研究思路可以归纳为两条互相衔接的主线：一条主线关注任务理解与规划建模，通过问题智能体和规划智能体把自然语言图任务转化为稳定的中间伪代码表示；另一条主线关注知识增强与程序化求解，通过检索、编码和验证闭环把规划结果落实为可执行且可复核的求解过程。

% [figure omitted: image content removed]
\caption{研究技术路线图}
\label{fig:research_roadmap}

首先，系统对输入任务进行结构化解析，显式抽取任务类型、图要素与约束信息；其次，规划模块把求解过程表示为算法级伪代码，为后续检索与编码提供统一中间语义；随后，检索模块依据规划步骤从外部文档知识中筛选候选 API 与算法说明，并结合检索质量评估决定是否需要进一步进行知识片段精炼或补充检索；在此基础上，编码模块生成可执行程序，并由验证模块通过测试反馈驱动修复或重生成；最终，系统根据任务要求输出可复核答案。与直接生成最终答案的路径相比，上述技术路线的关键优势在于：一方面将复杂任务拆解为多个可独立检查的阶段，便于定位错误来源；另一方面通过执行反馈形成闭环，使系统能够在失败后进行有依据的修正，而不是无方向地重复生成。

围绕上述研究目标与技术路线，本文的主要贡献可概括为以下三个方面：

（1）在方法设计方面，本文提出了基于规划反馈的图推理协同求解方法。该方法在自然语言任务和程序生成之间引入显式规划层，并利用执行反馈对程序实现、知识调用和规划结果进行反向修正，从而将复杂图推理组织为可解释、可检查、可迭代的闭环过程。

（2）在系统实现方面，本文构建了面向图推理任务的多智能体协同求解系统。系统以黑板调度为组织核心，围绕规划、检索、编码、验证与修复等阶段管理中间工件和运行状态，使规划结果、检索知识与执行反馈能够在统一流程中稳定传递。

（3）在实验验证方面，本文基于多个公开图推理基准测试集对所提方法进行了系统评估，并结合分层分析、机制验证、消融实验与鲁棒性测试，对规划反馈协同求解框架在图推理任务中的有效性进行了较为全面的分析。

\section{论文组织结构}

全文结构安排如下。

（1）第\ref{chp:introduction}章为绪论，主要介绍研究背景与意义、国内外研究现状，以及本文的研究内容、研究目标和技术路线。

（2）第\ref{chp:related_tech}章梳理与本文相关的理论基础和关键技术，包括图推理任务基础、大语言模型推理增强、工具增强与程序生成、多智能体协作以及图计算库与知识库构建等内容。

（3）第\ref{chp:method}章重点介绍基于规划反馈的图推理协同求解方法，围绕研究问题定义、面向图推理的规划生成方法、规划引导的知识检索与程序生成方法、基于执行反馈的验证推理方法以及方法分析与任务族适配展开。

（4）第\ref{chp:system}章介绍基于黑板调度的多智能体图推理协同系统，重点说明系统问题定义、系统架构与协同调度机制、中间工件管理与反馈恢复机制，以及系统复现配置与任务扩展机制。

（5）第\ref{chp:experiment}章给出实验验证与结果分析，围绕实验设计与设置、总体实验结果与稳定性分析、分层结果分析、机制验证与补充实验，以及模块贡献与典型结果分析等内容，系统验证所提方法的有效性。

（6）第\ref{chp:conclusion}章对全文工作进行总结，概括本文的主要结论，并对后续可能的改进方向和研究展望进行讨论。

此外，附录部分仅保留各基准测试集的详细实验结果，用于对正文中的总体统计结论进行逐任务补充说明与结果复核。
```

---

## chapters/chapter2.tex

```latex
\chapter{相关理论与关键技术}
\label{chp:related_tech}

\section{图推理任务基础}

本节从图表示、典型图算法与任务特性出发，说明图推理问题与一般文本推理任务在输入形式、约束结构和求解目标上的差异，为后续方法设计提供基础定义。

\subsection{图与图算法}

设图记为 $G=(V,E)$，其中 $V$ 表示节点集合，$E$ 表示边集合。根据边是否具有方向和权重，可进一步区分为有向图、无向图、带权图、多重图以及动态图等形式\cite{diestel2017graph}。在众多图计算任务中，最短路径、连通分量、拓扑排序、最大流、匹配以及团搜索等问题具有较高代表性。

传统图算法在上述任务上已经形成了较为成熟的理论体系。例如，Dijkstra 和 Bellman-Ford 可用于最短路径计算，DFS 与 BFS 可用于遍历和连通性判断，Ford-Fulkerson 与 Edmonds-Karp 可用于流优化，回溯搜索与动态规划常用于处理旅行商等组合优化问题\cite{cormen2009clrs,korte2018combinatorial}。从更广义的图学习视角看，DeepWalk、node2vec、GCN、GraphSAGE、GAT、GIN 和 GraphGPS 等模型推动了图表示学习从随机游走表征、消息传递网络逐步发展到图 Transformer 架构\cite{perozzi2014deepwalk,grover2016node2vec,kipf2017gcn,hamilton2017graphsage,velickovic2018gat,xu2019gin,rampasek2022graphgps}。与此同时，SNAP、OGB、Benchmarking Graph Neural Networks 和 GraphGym 等工作则为图数据组织、模型设计空间和评测流程提供了系统基础\cite{leskovec2016snap,hu2020ogb,dwivedi2023benchmarking,you2020graphgym}。这些算法与基准共同说明，图任务具有清晰的结构对象、成熟的计算过程和稳定的评测方式，因此非常适合作为大语言模型外部求解的可靠支撑。

\subsection{图推理任务的特点}

与一般文本推理相比，图推理任务同时具有强结构依赖、强约束驱动和强程序化特征。许多问题的答案并不来自局部语义片段，而是来自节点与边在全局拓扑中的相对位置；同时，大量任务还要求结果必须满足路径连通、回路闭合、容量限制、覆盖约束或最优性等严格条件。这意味着图推理不是只要叙述自洽即可，而是必须计算正确且满足约束。

另一方面，图任务又具有鲜明的可执行性。最短路径、连通分量、拓扑排序、最大流、匹配和最小生成树等问题都存在成熟算法，很多组合优化问题也存在清晰的搜索框架。因此，相比把所有求解压力压在语言模型一次性生成答案上，更合理的思路是让模型承担任务理解、规划组织与知识调用，再将精确计算交给外部程序环境完成。

然而，图任务并不天然适合当前主流大语言模型的输入方式。语言模型擅长处理线性序列，但图结构本质上是离散关系对象的集合，需要在文本中额外编码节点、边、权重和约束。当图规模增大或约束变复杂时，文本化表示很容易失去局部相邻关系与全局拓扑的直观性，这也是图推理性能不稳定的重要原因。

% [figure omitted: image content removed]
\caption{图推理任务从自然语言输入到最终输出的困难传递链}
\label{fig:graph_reasoning_challenge}

图\ref{fig:graph_reasoning_challenge}从输入到输出概括了图推理的典型难点传播路径。可以看到，一旦图结构在输入阶段被不充分地表达，后续任务识别、算法匹配和程序实现都会受到连锁影响。因此，构建更稳定的中间规划表示，不仅是为了提升模型的推理质量，更是为了阻断错误在系统中的层层放大。

\subsection{图表示与序列化困难}

图结构序列化是大语言模型进入图推理场景时最早遇到的技术障碍。常见序列化方式包括边列表、邻接表、自然语言描述和半结构化 JSON 样式表示。边列表便于完整列出关系，但当图中同时存在方向、权重和时间信息时，阅读成本会迅速升高；邻接表更接近图的局部结构，却不利于表达全局约束；自然语言描述更贴近用户提问方式，却容易混杂背景叙述和算法需求；半结构化表示较利于程序处理，但会牺牲部分自然语言语义线索。

更关键的是，序列化并不是一个单纯的格式转换过程，它会直接改变模型的注意力分配方式。在线性上下文中，相距较远的边信息即便在原图中高度相关，也可能因为跨越多个文本片段而难以被模型联合建模。对人类而言，图像化拓扑结构通常可以一眼看出关键连通关系；但对语言模型而言，同样的结构必须通过多轮文本匹配才能恢复。正因为如此，很多图推理基准测试集虽然规模不算大，却依然对模型构成明显挑战。

\begin{table}[htbp]
\centering
\caption{常见图表示方式及其适用特点}
\label{tab:graph_representation}
\begin{tabular}{m{2.8cm}m{4.1cm}m{4.4cm}}
\toprule
表示方式 & 优点 & 局限性 \\
\midrule
边列表表示 & 结构直接、适合精确列出节点关系 & 全局拓扑不直观，长图时阅读负担大 \\
邻接表表示 & 便于表达局部邻接关系 & 不利于表达全局路径和复杂约束 \\
自然语言描述 & 用户友好，适合嵌入任务背景 & 语义噪声较多，算法意图不够集中 \\
半结构化表示 & 易于程序解析和转换 & 对语言模型不够自然，可读性相对较弱 \\
\bottomrule
\end{tabular}
\end{table}

表\ref{tab:graph_representation}说明，不同表示方式各有优势，但没有一种方式可以同时兼顾自然表达、结构完整和实现友好。因此，很多高性能图推理系统并不会只依赖输入表示本身，而是会在读取输入后先构造结构化中间表示，再进入规划与程序生成阶段。

\section{大语言模型推理增强技术}

本节围绕分步推理、结构化搜索与推理过程控制等方向，归纳大语言模型在复杂任务中的能力增强路径，并分析其对图推理场景的可借鉴性。

\subsection{链式与分解式推理}

Chain-of-Thought 提示通过要求模型先生成中间推理步骤，再给出最终答案，从而提升复杂问题求解能力\cite{wei2022chain}。Self-Consistency 在此基础上采样多条思维链并进行投票，降低单次生成的偶然误差\cite{wang2023selfconsistency}。Least-to-Most Prompting 则强调先求解简单子问题，再逐步组合为完整解答\cite{zhou2023least}。进一步地，Zero-Shot CoT 与 Selection-Inference 说明，即便在缺少显式示例或需要保持中间步骤可解释的情况下，合理的推理分解也能改善模型表现\cite{kojima2022zeroshot,creswell2023selection}。这些方法共同说明，对于复杂任务而言，分步思考是提升模型稳定性的有效手段。

然而，上述方法更多是针对自然语言或数值推理场景设计。在图推理中，模型不仅要生成中间思路，还需要将这些思路映射为图结构上的算法操作。如果缺乏明确的算法级规划表示，中间推理仍可能停留在模糊的自然语言层面，难以直接指导程序实现。

\subsection{搜索式与结构化推理}

Tree-of-Thoughts 将问题求解建模为搜索过程，通过对多条候选思路进行扩展、评估和回溯，提高复杂任务中的探索能力\cite{yao2023tree}。Graph-of-Thoughts 进一步将思路组织为图结构，以支持更灵活的状态复用和关系建模\cite{besta2024graph}。ReAct 则把推理过程与外部行动交织到同一循环中，而 Self-Refine、CRITIC 和过程验证工作进一步强调中间步骤在生成后仍可被检查、纠偏和修复\cite{yao2023react,madaan2023selfrefine,critic2023,lightman2023processreward}。这些方法揭示了一个重要方向，即大语言模型的推理过程可以显式结构化，而不仅仅是生成一串文本。

对图推理任务而言，这一启示尤为重要。因为图任务本身就具有天然的结构性，如果中间规划同样以结构化方式表达，则更容易与后续图算法选择、知识检索和代码实现过程耦合。

\subsection{推理增强方法的阶段性演进}

若从技术路线演进角度观察，大语言模型推理增强方法大致经历了三个阶段。第一阶段主要依赖提示工程，通过示例、角色设定和思维链等方式引导模型输出更合理的中间步骤。第二阶段开始强调将复杂计算委托给外部程序或 API，从而缓解语言模型在精确计算上的局限\cite{schick2023toolformer,qin2023toolllm,gorilla2023}。第三阶段则进一步引入多智能体和过程控制思想，希望在生成前后增加规划、检索、审阅、验证与修复等环节，构建更加稳定的系统化求解流程；CAMEL、MetaGPT、AgentVerse、AutoGen、Language Agents as Optimizable Graphs、Generative Agents 与 Voyager 等工作都体现了这种从单模型生成走向系统协作与持续执行的趋势\cite{camel2023,metagpt2023,agentverse2023,wu2023autogen,zhuge2024languageagents,park2023generativeagents,wang2023voyager,zhou2023promptbreeder}。

图推理任务非常适合成为这一演进路线的应用场景，因为它天然具有结构化输入、明确算法和可执行求解过程。与其要求单个模型在一次生成中同时完成问题理解、算法选择和程序实现，不如将这些功能拆分到多个阶段，利用中间结构和外部工具提升整体稳定性。对本文所关注的问题而言，这一路径也为后续方法设计提供了直接启发。

% [figure omitted: image content removed]
\caption{大语言模型推理增强方法的阶段性演进}
\label{fig:reasoning_evolution}

图\ref{fig:reasoning_evolution}用较为概括的方式展示了相关技术路线的演化脉络。对本文而言，这一演进并不是背景性的叙述，而是后续方法设计的重要背景。相较于仅通过提示词增强单次回答质量，面向图推理的求解系统更需要把外部知识、执行环境和验证闭环纳入统一框架加以考虑。

\section{工具增强与程序生成技术}

由于图推理任务具有可执行、可验证的显著特征，工具调用与程序生成成为连接语言理解与算法求解的重要桥梁。本节重点讨论相关技术在图任务中的适配方式。

\subsection{程序辅助求解}

PAL 证明了在许多数学和符号推理任务上，让模型生成程序并交给解释器执行，往往比直接生成答案更可靠\cite{gao2023pal}。在更广的程序生成研究中，AlphaCode 展示了大模型在复杂编程任务上的潜力\cite{liang2022alphacode}。类似地，GraphCoder 等工作也尝试将图问题转化为调用 NetworkX 的程序，从而借助成熟图算法库完成求解\cite{zhang2025gcoder,hagberg2008networkx}。

程序辅助求解的核心优势在于将高精度计算从语言模型中剥离出来。模型只需负责理解问题与组织算法，而具体求值过程可以由外部程序完成。对于图推理这类结构约束强、精确计算要求高的任务，这一思路具有明显优势。

\subsection{工具调用与外部知识使用}

Toolformer、ToolLLM 等工作强调模型可以学习何时调用外部工具、使用什么接口以及如何整合工具返回结果\cite{schick2023toolformer,qin2023toolllm}。Gorilla 与 CRITIC 则进一步表明，模型不仅需要掌握调用能力，还需要在工具交互过程中完成 API 对齐、结果校验和错误纠正\cite{gorilla2023,critic2023}。在图推理场景下，外部工具不仅包括图计算函数，还包括图算法文档、函数说明和示例代码等知识源。

但需要注意的是，工具可用并不等于工具能被正确调用。如果模型对任务的算法意图理解不足，或者对 API 语义把握不准，依然可能选择错误函数、误用参数或忽略关键约束。因此，在调用工具之前建立一层规划表示，对于工具的精准使用具有重要意义。

\subsection{图任务中程序生成的适配性分析}

程序生成之所以在图推理任务上具有明显潜力，是因为很多图问题本质上都存在标准化算法流程。例如最短路径问题对应路径搜索算法，最大流问题对应流网络算法，匹配问题对应二分图匹配算法，而团搜索和旅行商问题则可以通过枚举、搜索或优化方法求解。一旦系统能够正确识别任务类型，就有可能借助成熟算法库获得高精度结果。

但图任务中的程序生成也面临比一般代码生成更严格的要求。首先，图构建方式必须正确，错误的方向、边权或时间属性会直接破坏后续求解。其次，许多基准测试集对输出格式极为严格，哪怕节点顺序、集合格式或空格细节不一致，也可能被判为错误。最后，组合优化任务不仅要求程序可运行，还要求解满足可行性和最优性双重约束。近期一些图任务工作也尝试通过思维生成或伪代码注入来缩小语言理解与图算法执行之间的落差\cite{graphthought2025,pseudocode2025}。因此，图任务中的程序生成更适合与规划和验证机制结合，而不是依赖一次性生成。

\subsection{图推理基准测试集的研究推动作用}

公开基准测试集在图推理研究中扮演了非常重要的角色。一方面，它们把原本零散的图算法问答、指令执行和动态图查询任务组织为可重复比较的标准测试集，使研究者能够更客观地评价模型性能。另一方面，不同基准测试集的设计重点并不相同，这恰好促使方法研究从单一任务优化转向跨任务泛化能力的讨论。例如，GraphArena 更强调经典算法与组合优化混合场景，NLGraph 更强调自然语言问题理解，GraphWiz 和 GraphInstruct 更接近指令式执行，而 LLM4DyG 又把时序动态性引入评价体系。

在本文研究中，讨论基准测试集的意义并不仅是罗列数据集名称，更重要的是理解这些数据集分别在考察什么能力。只有识别出它们在输入复杂度、约束严苛程度和输出规范性上的差异，才能解释为什么某些方法在一个基准测试集上表现突出，却在另一个基准测试集上出现明显回落。这也是本文在后续实验章节中同时关注总体表现、任务类别和扰动鲁棒性的原因。

为了更直观地刻画相关方法的演进脉络，图\ref{fig:llm_graph_reasoning_taxonomy}从两个维度对代表性工作进行了归纳：横轴表示方法所面向的任务属性，由通用任务逐步过渡到图任务；纵轴表示方法的系统组织程度，由单次生成/弱闭环逐步过渡到系统化协同/强闭环。在左下象限，CoT、Self-Consistency、ToT、GoT 与 CRITIC 等方法更接近通用推理增强范式，强调单模型上的思维链扩展、路径搜索或自我修正\cite{wei2022chain,wang2023selfconsistency,yao2023tree,besta2024graph,critic2023}。在右下象限，NLGraph、GraphWiz、GraphGPT、GraphInstruct、GraphLLM、GCoder 与 LLM4DyG 等工作则更加聚焦图任务本身，重点解决图结构表示、图算法调用和动态图推理等问题\cite{chen2024nlgraph,gong2024graphwiz,tang2024graphgpt,graphinstruct2024,pan2024graphllm,zhang2025gcoder,llm4dyg2024}。

% [figure omitted: image content removed]
\caption{图推理相关方法的二维谱系示意图}
\label{fig:llm_graph_reasoning_taxonomy}

进一步看，右上象限的方法更强调工具使用、多智能体协同和闭环控制，例如 Toolformer、ToolLLM、Gorilla、GraphTeam、GraphAgent-Reasoner、CAMEL、MetaGPT、AgentVerse 与 MA-GTS 等，体现出方法研究正从提升单次回答质量逐步转向构建可组织、可回退、可协作的系统\cite{schick2023toolformer,qin2023toolllm,gorilla2023,li2024graphteam,hu2024graphagentreasoner,camel2023,metagpt2023,agentverse2023,yuan2025magts}。与此同时，DPTS、HyperTree Planning、Graph-enhanced Plan Reasoning、ARise、Decision Pivots 与 ReAct 等工作位于图中上半区域，说明近年来越来越多研究开始通过显式搜索、层次规划、图式计划表示和风险感知推理来增强复杂任务求解过程的稳定性\cite{ding2025dpts,gui2025hypertree,lin2024plangraph,zhang2025arise,cho2025decisionpivots,yao2023react}。整体来看，这一二维谱系图反映出相关研究正在沿着从通用推理到图任务适配、从单次生成到系统化协同两条主线持续演化，而本文工作同时面向图任务适配与系统化协同闭环，因而与上述两条研究趋势相对应。

\subsection{图推理任务谱系与能力分解}

为了更系统地理解图推理问题的研究范围，本文进一步将常见任务划分为五类：结构查询类、路径搜索类、排序与可达性类、网络流与匹配类以及组合优化类。结构查询类任务通常关注邻居、度数、连通分量和局部关系判断，更依赖图构建的准确性；路径搜索类任务关注最短路径、可达性与遍历顺序，要求系统稳定处理边权、方向和路径格式；排序与可达性类任务强调全局先后约束，例如拓扑排序和有向无环图判定；网络流与匹配类任务要求对容量、配对约束和全局最优性同时建模；组合优化类任务如最大团、最小点覆盖和旅行商问题，则进一步提高了搜索复杂度和验证难度。

\begin{table}[htbp]
\centering
\caption{图推理任务谱系及其核心能力要求}
\label{tab:task_taxonomy}
\begin{tabular}{m{2.6cm}m{4.3cm}m{5.1cm}}
\toprule
任务类别 & 代表任务 & 对系统的核心能力要求 \\
\midrule
结构查询类 & 邻居查询、度数计算、连通分量 & 正确构图、局部关系读取、格式化输出 \\
路径搜索类 & 最短路径、DFS/BFS、可达性判断 & 边权处理、方向判断、路径序列生成 \\
排序与可达性类 & 拓扑排序、环检测、前驱查询 & 全局依赖建模、顺序约束识别 \\
网络流与匹配类 & 最大流、二分图匹配、最小割 & 容量约束、全局最优、API 细节正确使用 \\
组合优化类 & 最大团、最小点覆盖、旅行商问题 & 约束满足、搜索策略、验证与最优性检查 \\
\bottomrule
\end{tabular}
\end{table}

表\ref{tab:task_taxonomy}所呈现的任务谱系说明，图推理并不是一个单一难点，而是由图表示、约束识别、算法匹配、程序实现、结果验证多个能力共同决定的复合问题。对大语言模型而言，不同任务类别暴露出的短板也并不相同。例如，结构查询类任务更容易受到输入解析错误影响，而组合优化类任务更容易在搜索空间控制和最优性验证阶段失效。正因为这种差异性存在，本文在方法设计上没有将所有图任务统一视为自然语言问答，而是选择通过规划与验证机制显式刻画任务间的结构差异。

\section{多智能体协作技术}

多智能体系统通常将复杂任务拆分给多个功能角色，例如规划者、执行者、检索者、审阅者和修复者等。不同角色在提示词、上下文和目标函数上各有侧重，可以缓解单一智能体既要理解问题、又要生成程序、还要验证结果的压力。除 GraphTeam 外，CAMEL、MetaGPT、AgentVerse、Generative Agents 与 Voyager 等工作也从角色扮演协作、软件式协同框架、群体模拟和持续探索等角度展示了多智能体系统的潜力\cite{li2024graphteam,camel2023,metagpt2023,agentverse2023,park2023generativeagents,wang2023voyager}。

不过，现有多智能体方法中仍存在两个值得改进的问题。其一，角色拆分往往停留在讨论式协作层面，缺乏统一的中间规划表示；其二，知识检索与执行验证往往只是附属模块，没有真正围绕结构化求解过程展开。对于本文所研究的图推理场景而言，这说明仅有角色划分仍然不够，还需要进一步引入规划先行和验证闭环的一体化组织方式。

\subsection{多智能体系统的设计原则}

结合现有研究可以看出，面向图推理的多智能体系统至少需要满足四类设计要求。首先，角色边界要足够清晰，否则问题解析、规划、编码和验证之间容易互相覆盖，系统看似分工，实际却难以定位错误来源。其次，中间表示应尽可能稳定，也就是让智能体通过结构化工件协作，而不是完全依赖自由文本讨论。再次，系统必须为外部知识和外部工具预留标准化接入口，这样才能在不推翻整体架构的前提下替换知识库、执行环境和图算法库。最后，闭环验证是不可缺少的环节，多智能体系统不应只追求生成更多答案，而应追求更快发现错误并修正错误。

这几项原则本质上体现了从语言生成系统向可控推理系统的转变。对于图推理任务而言，这种转变尤其重要，因为很多失败并非来自语义理解完全错误，而是来自中间流程缺少稳定约束，导致错误 API 被调用、关键条件被遗漏或格式结果不一致。

从功能分工看，问题解析、规划组织、知识检索、程序实现与结果验证可以分别由不同角色承担。问题智能体负责降低输入复杂度，规划智能体负责生成可传递的中间目标，检索智能体负责补足外部算法知识，编码智能体负责把规划转化为程序，而验证或推理角色则结合执行反馈对候选程序进行局部分析与修正。这种按角色划分局部目标的方式，有助于降低一次性端到端生成的风险，也为后续章节讨论规划反馈闭环提供了协作基础。

\section{图计算支撑与相关工作比较}

NetworkX 是 Python 生态中使用广泛的图计算库，支持丰富的图结构表示与算法接口，包括路径搜索、中心性分析、匹配、生成树、团搜索、流计算等\cite{hagberg2008networkx}。对于语言模型生成程序而言，NetworkX 具备以下优势。

一方面，NetworkX 的 API 语义相对清晰，文档覆盖也较为完整，适合作为外部知识库的重要来源；另一方面，它覆盖了大量经典图算法，使得不同基准测试集上的求解过程可以尽量统一到同一套工具生态内。同时，Python 风格调用对大语言模型而言较自然，便于从伪代码规划过渡到可执行程序。在大多数公开图推理基准测试集中，NetworkX 已经能够覆盖基础图构建、路径计算、连通性分析、匹配、流和部分组合搜索任务，因此十分适合作为本文系统实现的底座。

本文将文档知识组织为外部知识库，每条知识包含函数名、适用任务、输入参数、返回形式及示例说明。与一般 RAG 系统类似，知识库的核心作用不是直接替代模型推理，而是在模型已形成规划后，为其提供可靠的实现参照；Dense Passage Retrieval、RAG、RETRO、Atlas、Self-RAG 以及相关综述说明，外部检索、向量索引和生成后自我评估机制在复杂知识密集型任务中具有显著价值\cite{karpukhin2020dpr,lewis2020rag,borgeaud2022retro,izacard2022atlas,johnson2019faiss,asai2024selfrag,gao2024ragsurvey}。

\subsection{图计算库与知识库的支撑作用}

需要强调的是，知识库并不是为了让系统记住题目答案，而是为了让系统在已经形成初步规划后，能够更稳定地选择实现方式。换言之，知识库更多承担实现支撑层的作用，而不是经验记忆层的作用。

这种定位有两方面意义。其一，它降低了方法对大量人工整理题解的依赖，使系统更容易维护和扩展。其二，它提升了方法在新任务场景中的迁移能力。只要新的任务仍能映射到已有图算法接口或可新增相应文档条目，整个框架就能在保持总体架构不变的情况下继续工作。

从求解机制角度看，图计算库与外部知识库分别承担可执行求解底座和实现选择参照两类功能。前者保证图任务能够被统一映射到稳定的程序接口上，后者保证模型在面对多种候选实现时能够获得更可靠的 API 语义、参数约束与示例支持。两者结合后，图推理系统不再只是依赖语言模型内部参数进行模糊匹配，而是可以在结构化规划与外部执行之间建立更稳定的过渡层。也正因为这一过渡层存在，后续方法章节才能进一步讨论如何把规划结果转化为检索条件、代码实现与验证反馈。

\subsection{相关工作比较与归纳}

为更清晰地总结现有图推理方法之间的差异，表\ref{tab:related_compare}从推理方式、是否使用外部知识、是否执行程序以及是否具备验证闭环四个维度进行了对比。

\begin{table}[htbp]
\centering
\caption{相关图推理方法对比}
\label{tab:related_compare}
\begin{tabular}{m{2.8cm}m{3.0cm}m{1.9cm}m{1.9cm}m{1.9cm}}
\toprule
方法类别 & 代表思路 & 外部知识 & 程序执行 & 验证闭环 \\
\midrule
直接提示推理 & CoT、ToT 等 & 否 & 否 & 否 \\
结构感知提示 & GraphGPT、GraphLLM & 可选 & 否 & 否 \\
程序生成方法 & PAL、GCoder & 可选 & 是 & 弱 \\
多智能体方法 & GraphTeam 等 & 可选 & 可选 & 部分具备 \\
\bottomrule
\end{tabular}
\end{table}

由表\ref{tab:related_compare}可见，现有方法之间的差异并不只体现在是否使用图结构这一单一维度上，而更多体现在是否引入外部知识、是否真正执行程序，以及是否形成可回退的验证闭环。直接提示推理与结构感知提示方法更关注输入表达和单次生成质量，程序生成方法开始借助外部执行提升精确性，多智能体方法则尝试通过角色协作增强复杂任务处理能力，但在统一规划表示、检索支撑和反馈修复的协同组织上仍有进一步整合空间。基于这一观察，后续方法章节将围绕显式规划、知识检索、程序执行与反馈推理的协同机制展开。

\enlargethispage{4\baselineskip}

\section{本章小结}

本章从图推理任务特性、大语言模型推理增强、工具调用、多智能体协作以及图计算支撑与相关工作比较五个方面，梳理了本文工作的理论基础。综合现有研究可以看出，图推理问题天然适合采用结构化规划 + 外部知识 + 程序执行的混合求解范式，而多角色协作与验证闭环则为复杂任务中的稳定求解提供了进一步支撑。下一章将对所提方法进行详细说明。
```

---

## chapters/chapter3.tex

```latex
\chapter{基于规划反馈的图推理协同求解方法}
\label{chp:method}

图推理任务要求模型在自然语言描述、图结构表示、算法约束和答案格式之间建立稳定映射。与一般问答任务相比，图推理的中间过程更长，约束更显式，且最终答案通常可以通过程序执行或规则检查进行验证。如果直接令大语言模型一次性生成答案，模型需要同时完成任务理解、算法选择、代码或推理步骤组织以及结果格式化，容易出现任务类型误判、图约束遗漏、API 使用错误和答案格式不一致等问题。

针对上述问题，本文提出一种基于规划反馈的图推理协同求解方法。该方法将图推理过程拆解为结构化解析、规划生成、规划引导检索、程序化执行验证和反馈修复等阶段。规划结果作为前向约束，指导后续知识检索和候选程序生成；执行验证结果作为反向反馈，修正程序实现，并在必要时触发检索补充或规划重写。通过这种规划约束生成、反馈修正的闭环机制，系统能够把复杂图推理任务转化为可分解、可检查、可迭代的协同求解过程。

本章侧重介绍方法层面的设计，即规划反馈范式如何定义、规划如何生成并作用于检索和程序生成、执行反馈如何被抽象为可用于修复的信号，以及该方法为什么能够降低图推理中的错误传播。为避免与系统实现章节重复，本章主要讨论求解语义和方法机制；调度策略、共享黑板、工件版本管理和运行配置等工程细节将在第\ref{chp:system}章进一步说明。

\section{研究问题定义}

本节对本文所研究的图推理问题进行统一界定，并说明为何需要采用规划反馈范式组织求解过程。具体而言，本节将从任务形式化描述、规划反馈闭环以及方法整体流程三个方面给出问题定义，从而为后续规划生成、知识检索、程序实现和反馈修复等方法展开提供一致的问题背景。

给定自然语言问题 $Q$ 以及与之关联的图数据，图推理任务的目标是输出满足题目语义和格式要求的答案 $A$。其中，图数据可以显式出现在题目文本中，也可以作为结构化输入提供。本文将图表示为
\begin{equation}
G=(V,E,\mathcal{X}),
\end{equation}
其中 $V$ 表示节点集合，$E$ 表示边集合，$\mathcal{X}$ 表示与节点、边或全局图相关的附加属性，例如边权、方向、容量、时间戳、标签和约束参数等。对于动态图任务，$\mathcal{X}$ 还可包含事件序列或时间窗口；对于组合优化任务，$\mathcal{X}$ 则可能包含必须访问、互斥、容量或目标函数等约束。

为了统一不同基准测试集中的任务形式，本文将自然语言问题解析为结构化任务描述
\begin{equation}
T=(\tau,\mathcal{C},\mathcal{O},\mathcal{F}),
\end{equation}
其中 $\tau$ 表示任务类型，如最短路径、最大流、匹配、旅行商、拓扑排序或动态图查询；$\mathcal{C}$ 表示任务约束集合，如起点终点、是否带权、是否有向、是否必须回路、是否要求最优性等；$\mathcal{O}$ 表示目标函数或判定目标；$\mathcal{F}$ 表示输出格式要求。于是图推理任务可以写作
\begin{equation}
A=\mathrm{Solve}(Q,G,T),
\end{equation}
即系统需要在理解 $Q$ 与 $G$ 的基础上，依据任务描述 $T$ 生成最终答案。

这一形式化定义强调了图推理的两个特征。第一，图推理并不是单纯的文本理解任务，答案必须满足图结构和算法约束。例如，路径类任务不仅要给出一串节点，还要保证相邻节点之间存在边；旅行商问题不仅要覆盖全部节点，还要返回闭合回路并满足代价最小化目标。第二，图推理也不是单纯的程序执行任务，因为原始输入中的任务目标、约束和输出要求往往以自然语言形式出现，必须先经过语义解析才能映射到具体算法。

因此，本文不将大语言模型直接视为最终答案生成器，而是将其作为多个智能体的语义推理能力来源。各智能体围绕结构化任务表示、规划、知识和执行反馈展开协同，使求解过程从不可观测的一次生成转化为可检查的多阶段推理。

本文所称规划反馈，包含两个方向的约束关系：一是由规划到下游生成的前向约束，二是由执行反馈到上游语义的反向修正。给定结构化任务描述 $T$，规划智能体生成算法级规划
\begin{equation}
P=\{p_1,p_2,\ldots,p_n\},
\end{equation}
其中每个 $p_i$ 对应一个明确的求解动作，例如图构建、候选算法选择、约束检查、结果计算和答案格式化。规划 $P$ 不直接等同于程序代码，而是承担中间语义的作用：它将自然语言问题压缩为可执行求解路线，并为检索和编码提供稳定条件。

在前向方向上，规划用于约束知识检索和程序生成。检索智能体根据 $P$ 召回与当前算法步骤相关的外部知识，编码智能体再基于 $P$ 与检索知识 $K$ 生成候选程序 $C$。这一过程可表示为
\begin{equation}
K=\mathrm{SearchAgent}(P),\quad C=\mathrm{CodingAgent}(P,K).
\end{equation}
与直接使用原始问题文本检索相比，规划查询更接近算法实现语义，能够降低题目叙述噪声对检索结果的干扰；与直接生成程序相比，规划又为代码结构提供了约束，减少模型在控制流、算法选择和约束检查上的随意性。

在反向方向上，执行验证将候选程序的运行状态转化为反馈信号。若程序在测试样例或目标输入上出现语法错误、运行异常、约束违反或格式错误，系统会形成反馈 $F_t$，并据此更新候选程序、检索知识或规划结果：
\begin{equation}
(P_{t+1},K_{t+1},C_{t+1})=\mathrm{Revise}(P_t,K_t,C_t,F_t).
\end{equation}
在大多数情况下，反馈首先用于局部修复候选程序；当错误显示知识条目不匹配时，系统触发补充检索；当错误表明规划遗漏关键约束或任务类型判断错误时，系统才回退到规划阶段。可以看到，反馈并不是简单的报错后重试，而是先对当前求解状态进行归因，再选择修正路径。

这种范式使图推理过程具有更强的可解释性。若最终答案错误，系统能够检查规划是否覆盖任务约束、检索知识是否与规划步骤匹配、候选程序是否通过约束验证，从而将错误定位到相对明确的阶段。相比端到端生成，规划反馈机制不是依赖单次生成质量，而是通过中间表示和外部反馈逐步压缩错误空间。

本文方法的整体流程如图\ref{fig:framework_overview}所示。系统首先由问题智能体对输入问题进行结构化解析，得到任务类型、图结构信息、约束集合和输出格式；随后由规划智能体生成算法级伪代码规划；检索智能体根据规划召回外部图算法知识；编码智能体结合规划与知识生成候选程序；最后由执行验证和反馈推理过程对候选程序进行测试、修复、重生成和答案格式化。

% [figure omitted: image content removed]
\caption{基于规划反馈的图推理协同求解框架}
\label{fig:framework_overview}

图\ref{fig:framework_overview}中的关键不在于简单串联多个智能体，而在于每个阶段都产生可被后续阶段消费的中间语义。问题智能体输出的结构化任务表示降低了原始文本噪声；规划智能体输出的伪代码规划明确了求解路线；检索智能体输出的知识集合补充了 API 和算法细节；编码智能体输出的候选程序将规划转化为可执行对象；执行验证过程输出的反馈信号则为修复和回退提供依据。

从输入输出角度看，本文方法并不是一个仅接收问题文本并直接输出答案的黑盒。系统输入包括原始问题描述、图结构信息和答案格式约束；系统输出除了最终答案，还包括结构化任务表示、规划、检索知识、候选程序和执行反馈等中间结果。这些中间结果在方法分析中具有重要意义：一方面，它们能够解释每个阶段对最终求解的贡献；另一方面，它们使错误归因和后续实验分析成为可能。

综合而言，本章后续内容围绕三条主线展开。第一，规划如何从自然语言任务中生成，并如何评价其质量；第二，规划如何引导知识检索与程序生成，使外部知识和代码实现围绕同一求解语义展开；第三，执行反馈如何驱动候选程序修复，并在必要时影响检索与规划。三条主线分别对应前向规划约束、知识增强实现和反向反馈修正，共同构成本文方法区别于直接推理和普通检索增强生成方法的核心。

\section{面向图推理的规划生成方法}

规划生成是本文方法的核心起点。对于图推理任务而言，规划并不是一般意义上的思维链描述，而是从自然语言问题到可执行程序之间的中间求解语义。本节从任务结构化解析、伪代码规划生成、规划表示设计以及规划质量评价四个方面说明规划生成方法。

\subsection{任务结构化解析}

问题智能体负责从原始输入中抽取任务目标、图结构和答案格式约束，其过程可形式化为
\begin{equation}
(T,G) \leftarrow \mathrm{QuestionAgent}(Q).
\end{equation}
其中，$T$ 为结构化任务描述，$G$ 为图数据表示。对于输入中已经显式给出边列表或邻接矩阵的样例，问题智能体主要负责规范化节点、边、权重和方向；对于输入中以自然语言描述图关系的样例，问题智能体还需要将文本中的关系转换为可计算的图结构。

任务结构化解析包含四类信息。第一类是图结构属性，包括图是否有向、是否带权、是否含容量或时间属性、是否存在多重边等。第二类是任务目标，如求最短路径、判断连通性、寻找最大流、计算匹配、寻找团结构或求解组合优化目标。第三类是约束条件，如起点和终点、必须访问的节点、是否要求闭合回路、是否允许重复节点、是否只考虑某个时间窗口等。第四类是输出格式，如返回数值、路径序列、布尔值、节点集合或自然语言解释。

结构化解析的作用并不是提前解决问题，而是为规划生成提供稳定输入。如果任务类型或约束在这一阶段没有被显式表示，后续规划很可能沿着错误方向展开。例如，在旅行商问题中，若解析阶段没有识别回到起点这一约束，规划阶段可能只生成一条覆盖所有节点的路径，而不是闭合回路；在最大流问题中，若容量字段未被识别，程序生成阶段可能将边权误用为普通距离。由此可见，解析阶段对约束的保真度直接影响规划质量。

\subsection{伪代码规划生成}

规划智能体基于结构化任务描述生成算法级伪代码规划：
\begin{equation}
P \leftarrow \mathrm{PlanningAgent}(T).
\end{equation}
其中 $P=\{p_1,p_2,\ldots,p_n\}$ 表示一系列求解步骤，每个步骤对应一个清晰的算法动作。本文采用伪代码而不是自然语言长段解释，主要是为了让规划同时服务于知识检索、程序生成和执行验证。伪代码不要求完全符合某种编程语言语法，但需要明确输入、计算、约束检查和输出之间的关系。

以带权最短路径任务为例，规划通常包含构建带权图、读取源点和目标点、调用最短路径算法、计算路径总代价、按要求格式化输出等步骤。对于旅行商问题，规划则包含构建带权无向图、固定起点或选择起点、枚举或搜索满足哈密顿回路约束的候选路径、计算每条回路总代价、返回最小代价路径等步骤。不同任务的规划内容不同，但都遵循图构建—算法执行—约束验证—结果整理的基本结构。

为了避免规划成为不可执行的自由文本，本文在生成阶段引入三类约束。首先，规划需要显式指明任务族和核心算法方向，避免后续检索在过宽范围内搜索。其次，规划需要单独列出关键约束，而不是把约束隐含在泛化描述中。最后，规划步骤需要保持合理顺序，尤其要避免先进行结果格式化、再补充图构建或约束检查这类顺序错误。通过这些约束，规划能够承担前向骨架的作用，为下游检索、编码和验证提供稳定语义。

\subsection{规划表示设计}

本文对规划表示提出三个设计要求。第一，原子性。每条规划步骤应尽量只表达一个核心动作，避免一条语句中混合构图、算法调用和输出整理等多个目标。原子化步骤有利于后续将规划映射为检索查询、程序片段和验证检查点。第二，约束显式性。对于起点固定、必须回路、容量限制、时间过滤、节点不重复等关键约束，规划需要以独立步骤或标签形式给出。第三，工具无关性。规划本身不绑定某个具体库函数名，而是描述算法语义；具体 API 选择交由检索和编码阶段完成。

在该表示下，规划既不是纯自然语言解释，也不是完整代码，而是介于任务语义与程序实现之间的中间层。它足够抽象，可以适配不同图计算工具；又足够具体，可以直接约束检索和编码。相比自由思维链，规划表示减少了冗余叙述和不稳定推理；相比直接代码，它又保留了更清晰的任务级语义。

规划阶段仍可能出现错误。根据实验观察，典型失败模式包括任务类型误判、关键约束遗漏、步骤粒度过粗、步骤顺序不合理和算法方向偏差。任务类型误判会导致检索和编码整体偏离目标；约束遗漏会使程序即使运行成功也无法满足题意；粒度过粗会让编码智能体缺少足够实现依据；步骤顺序不合理则容易造成程序控制流混乱。本文并不假设规划天然正确，而是通过执行反馈对规划产生间接监督。当错误反馈反复指向同一类约束缺失时，系统可回退到规划阶段进行修正。

\subsection{规划质量评价指标}

为了避免规划质量只停留在主观判断层面，本文进一步定义一组可操作的规划评价指标。设规划结果为 $P=\{p_1,\ldots,p_n\}$，任务真实约束集合为 $\mathcal{C}$，从规划中抽取到的约束集合为 $\mathcal{C}_P$。首先，约束覆盖率定义为
\begin{equation}
\mathrm{Cov}(P)=\frac{|\mathcal{C}_P\cap\mathcal{C}|}{|\mathcal{C}|},
\end{equation}
用于衡量规划是否显式包含题目中的关键约束。覆盖率越高，说明规划越能保留任务边界条件。

其次，步骤一致性用于衡量规划内部是否存在逻辑冲突，记为 $\mathrm{Con}(P)$。例如，若规划前一步声明构建无向图，后一步却按有向图处理边；或者前一步要求寻找最短路径，后一步却按最大流进行输出，则说明规划内部存在不一致。该指标可结合规则检查和轻量语义匹配获得。

再次，可执行性评分用于评估规划是否能够稳定映射为程序骨架，记为 $\mathrm{Exe}(P)$。本文将规划中的动作词映射为标准操作集合，如构图、算法调用、候选枚举、约束校验、结果格式化等。若规划缺少核心动作，或动作顺序与数据依赖关系冲突，则可执行性评分下降。综合三项指标，规划质量总分可表示为
\begin{equation}
\mathrm{Score}(P)=\alpha\,\mathrm{Cov}(P)+\beta\,\mathrm{Con}(P)+\gamma\,\mathrm{Exe}(P),
\end{equation}
其中 $\alpha+\beta+\gamma=1$。

该评分具有两方面作用。在离线分析中，它帮助解释不同样例的失败来源。例如，某些样例并非编码能力不足，而是规划覆盖率偏低，导致后续链路从一开始就缺少关键约束。在运行过程中，它也可以作为回退触发信号：当 $\mathrm{Score}(P)$ 低于阈值时，方法流程优先请求规划重写，而不是直接进入代码生成。这样，规划质量评价成为连接方法设计和反馈修正的重要桥梁。

\section{规划引导的知识检索与程序生成方法}

规划生成之后，系统需要将求解语义落到可执行实现上。对于图推理任务而言，外部知识的作用不仅是补充背景事实，更重要的是提供稳定的图算法接口、参数含义和返回格式说明。本节介绍如何构建图算法知识库，如何利用规划引导检索，以及如何将规划和知识共同映射为候选程序。

\subsection{图算法知识库构建}

为降低模型仅依赖参数记忆导致的实现不稳定，本文构建了面向图计算的外部知识库。知识库条目主要来自图算法库文档、常见任务说明和接口示例。每个知识条目可表示为
\begin{equation}
k_i=\{name_i, desc_i, input_i, output_i, example_i, tag_i, strip_i\},
\end{equation}
其中 $name_i$ 表示函数或算法名称，$desc_i$ 表示功能描述，$input_i$ 和 $output_i$ 分别表示参数与返回值说明，$example_i$ 表示简要调用示例，$tag_i$ 表示任务类型、图属性和适用约束标签，$strip_i$ 表示从原始条目中拆分出的细粒度知识片段。这里的知识片段主要围绕适用图类型、关键参数含义、返回结果结构、约束检查要点等信息组织，使检索阶段不必将整段文档原样送入编码阶段，而可以按规划步骤重新组合更紧凑的实现依据。

知识库覆盖的内容包括最短路径、连通性、最小生成树、最大流、匹配、拓扑排序、团与独立集、旅行商问题以及部分动态图处理方法。对于成熟算法，知识条目强调 API 的输入格式和返回结构；对于组合优化任务，知识条目还会补充可行性检查和目标函数计算方式。知识条目经过向量化后存入检索索引，并保留标签字段用于后续重排序。

需要说明的是，知识库并不替代规划。知识库主要提供实现依据和工具选择线索，规划则负责确定当前任务的求解思路。如果直接用原始问题检索知识，返回内容可能受到自然语言表述中冗余信息的干扰；如果只有规划而缺少知识支撑，编码阶段又可能出现 API 误用。因此，本文将规划和知识库设计为互补关系。

\subsection{规划引导检索与查询构造}

与直接使用问题文本进行检索不同，本文以规划 $P$ 作为核心查询依据，并结合结构化任务描述中的图属性和约束标签构造检索查询。检索过程可表示为
\begin{equation}
K=\mathrm{SearchAgent}(P,T),
\end{equation}
其中 $K=\{k_1,k_2,\ldots,k_m\}$ 为返回的知识集合。

规划引导检索的第一步是从规划中抽取任务类型、关键动作和约束条件。例如，构建带权无向图并计算从源点到终点的最短路径会被拆解为 weighted graph、shortest path、source target、path length 等检索要素；旅行商规划中的枚举哈密顿回路并最小化总代价则会转化为 traveling salesman、Hamiltonian cycle、cycle cost、minimum route 等检索要素。第二步是结合图属性补充查询标签，如 directed、weighted、capacity、temporal 等。第三步是将上述要素组合为更接近文档表达的检索文本。

这种查询构造策略的本质是语义压缩。自然语言问题中可能包含故事背景、变量解释和输出说明，但真正决定 API 选择的是任务类型、图属性和算法动作。通过规划压缩，检索器更容易命中与实现相关的知识条目。第五章中的检索质量实验将进一步验证，不同查询表达方式在 Hit@k 和 MRR 指标上存在明显差异，规划查询能够显著改善知识命中效果。

\subsection{知识重排序、质量评估与纠偏筛选}

检索得到候选知识后，系统还需要结合规划进行重排序和筛选。设候选知识条目为 $k_i$，其语义向量相似度为 $s_{\mathrm{sem}}(P,k_i)$，标签匹配得分为 $s_{\mathrm{tag}}(T,k_i)$，约束一致性得分为 $s_{\mathrm{cons}}(P,k_i)$，则综合得分可表示为
\begin{equation}
s(P,T,k_i)=\lambda_1 s_{\mathrm{sem}}(P,k_i)+\lambda_2 s_{\mathrm{tag}}(T,k_i)+\lambda_3 s_{\mathrm{cons}}(P,k_i),
\end{equation}
其中 $\lambda_1+\lambda_2+\lambda_3=1$。

语义相似度用于衡量知识条目与规划文本的整体相关性；标签匹配用于判断知识条目是否适用于当前图属性和任务族；约束一致性则用于排除可能导致实现偏差的条目。例如，若任务明确要求有向图上的最短路径，则无向图专用或忽略方向的说明应被降权；若任务涉及容量约束，则普通边权路径算法不能被误作为最大流算法；若任务要求返回节点集合，则只返回数值目标的接口说明需要额外补充格式化逻辑。

仅有重排序还不够。对于图推理任务，如果检索结果与规划步骤只存在表面语义相似，而未覆盖关键约束或返回结构，编码阶段仍可能在 API 选择和参数组织上出现偏差。为此，本文进一步引入检索质量评估机制，对候选知识集合是否足以支撑当前规划进行显式判断。为避免与前述排序权重混淆，质量评估阶段使用 $\mu$ 表示各评价项权重。设规划共有 $|P|$ 个关键步骤，其中被候选知识覆盖的步骤比例为 $\mathrm{Cov}_{\mathrm{step}}(K,P)$，关键约束覆盖比例为 $\mathrm{Cov}_{\mathrm{cons}}(K,P)$，候选知识之间的冗余度为 $\mathrm{Red}(K)$，则检索质量得分定义为
\begin{equation}
\mathrm{RQ}(K|P,T)=\mu_1 \max_{k_i \in K} s(P,T,k_i)+\mu_2 \mathrm{Cov}_{\mathrm{step}}(K,P)+\mu_3 \mathrm{Cov}_{\mathrm{cons}}(K,P)-\mu_4 \mathrm{Red}(K),
\end{equation}
其中 $\mu_1+\mu_2+\mu_3+\mu_4=1$。该得分不仅衡量最高相关条目的质量，还同时考虑规划步骤是否被充分支撑、约束信息是否完整以及候选上下文是否存在明显噪声。

在此基础上，系统按照检索质量得分选择不同纠偏动作。若 $\mathrm{RQ}(K|P,T)\ge \tau_h$，说明当前知识集合已具备较高支撑性，系统直接进入编码阶段；若 $\tau_l \le \mathrm{RQ}(K|P,T)<\tau_h$，系统对候选知识进行片段级精炼，仅保留与当前规划步骤、图属性和关键约束直接相关的知识片段；若 $\mathrm{RQ}(K|P,T)<\tau_l$，则系统触发补充检索，依据缺失的规划步骤或约束标签重写查询，再执行一次面向局部失败点的定向召回。其决策过程可写为
\begin{equation}
\mathcal{A}_{\mathrm{ret}}=
\begin{cases}
\text{DirectCode}, & \mathrm{RQ}(K|P,T)\ge \tau_h,\\
\text{RefineStrip}(K), & \tau_l \le \mathrm{RQ}(K|P,T)<\tau_h,\\
\text{RewriteQuery}(P,T)\rightarrow \text{SearchAgent}, & \mathrm{RQ}(K|P,T)<\tau_l.
\end{cases}
\end{equation}

这种机制借鉴了纠错式检索增强的思想，但并不依赖开放域网页搜索，而是结合图算法知识库和规划反馈框架完成受控补检索。其作用在于避免系统在低质量检索结果上直接进入代码生成，从而减少无效上下文对候选程序的污染，并降低后续修复轮数。

\begin{table}[htbp]
\centering
\small
\caption{检索质量评估下的分级纠偏策略}
\label{tab:retrieval_correction}
\begin{tabular}{m{2.2cm}m{3.3cm}m{4.2cm}m{3.2cm}}
\toprule
质量状态 & 判定依据 & 触发动作 & 主要作用 \\
\midrule
高置信度 & $\mathrm{RQ}(K|P,T)\ge \tau_h$ & 直接进入编码，仅保留高分条目 & 减少额外调用，保持编码上下文紧凑 \\
中置信度 & $\tau_l \le \mathrm{RQ}(K|P,T)<\tau_h$ & 片段级精炼，按规划步骤重组知识片段 & 降低冗余上下文，强化步骤与知识的一致性 \\
低置信度 & $\mathrm{RQ}(K|P,T)<\tau_l$ & 根据缺失步骤和约束标签重写查询，执行补充检索 & 避免在低质量知识上盲目编码，减少后续修复成本 \\
\bottomrule
\end{tabular}
\end{table}

通过重排序、质量评估与纠偏筛选，编码智能体接收到的知识集合更紧凑，也更贴近规划意图。该过程并不是为了召回尽可能多的知识，而是为了减少与当前求解无关甚至相互冲突的上下文。对于大语言模型生成代码而言，过多不相关知识可能反而造成上下文噪声，导致 API 混用或算法选择摇摆。因此，知识筛选不只是检索阶段的附加步骤，而是连接规划约束、知识利用和后续编码效率的重要中间机制。

\subsection{规划到程序的映射机制}

在本文方法中，程序生成并不是从原始问题直接到代码的跳跃，而是由规划和知识共同约束。编码智能体根据规划 $P$ 和筛选后的知识集合 $K$ 生成候选程序
\begin{equation}
C_0 \leftarrow \mathrm{CodingAgent}(P,K).
\end{equation}
候选程序通常采用 Python 实现，并优先调用成熟图计算库完成核心算法。编码阶段需要满足两个要求：一是忠实执行规划步骤，二是尽量使用检索知识中提供的接口和参数说明，减少模型凭经验随意实现造成的错误。

为了提高映射稳定性，本文将规划到程序的转换显式建模为两阶段过程。第一阶段是从线性规划到操作图。系统将伪代码步骤 $p_i$ 映射为操作节点 $o_i$，并建立依赖边 $e_{ij}$ 表示数据依赖和执行顺序，形成
\begin{equation}
\mathcal{G}_P=(\mathcal{O},\mathcal{E}).
\end{equation}
其中，$\mathcal{O}$ 包含构图、算法调用、候选枚举、约束检查和结果整理等节点类型。操作图能够显式表示哪些步骤必须先执行，哪些步骤可以作为独立检查点，从而降低代码组织混乱的风险。

第二阶段是从操作图到程序骨架。系统为不同类型的操作节点分配相应模板片段，例如图初始化、边权读取、算法调用、异常处理、可行性检查和输出封装，再按照依赖关系组织为候选程序。这样，即使模型在局部实现细节上出现偏差，整体程序结构仍受规划约束，不容易出现严重顺序错误。

此外，本文引入约束绑定机制，将规划中的关键约束绑定到程序中的检查点。例如，哈密顿路径或旅行商任务会在结果检查阶段插入节点覆盖完整、节点不重复、路径闭合和代价与边权一致等检查；最大流任务会绑定容量字段和源汇点约束；动态图任务会绑定时间过滤逻辑。通过约束绑定，规划中的语义不再停留在文字层面，而是转化为程序中的可验证条件。

\section{基于执行反馈的验证推理方法}

规划和检索能够降低生成难度，但并不能保证候选程序一次正确。图推理任务的一个重要优势是许多约束可以被程序化检查，因此本文在程序生成后引入执行反馈机制。本节说明验证样例如何构造，错误反馈如何表示，以及反馈如何驱动局部修复、补充检索和有界重生成。

\subsection{候选程序生成与执行验证}

候选程序 $C_0$ 生成后，系统首先在验证样例上执行程序，而不是立即接受其输出。验证样例可以来自题目中的小规模图，也可以由系统根据任务类型构造。执行验证关注四类问题：语法或导入错误、运行时异常、图算法 API 使用错误以及任务约束违反。若程序无法运行，说明候选实现尚未达到基本可执行要求；若程序可运行但违反约束，则说明其算法或格式化逻辑仍需修正。

执行验证过程可表示为
\begin{equation}
F_t=\mathrm{ExecuteVerify}(C_t,\mathcal{D}_{val},P),
\end{equation}
其中 $\mathcal{D}_{val}$ 表示验证样例集合，$P$ 用于提供约束检查依据，$F_t$ 表示第 $t$ 轮反馈。与普通单元测试不同，这里的验证不仅检查代码是否报错，也检查程序是否实现了规划意图。例如，路径类任务需要检查相邻节点是否存在边、总代价是否与边权一致；组合优化任务需要检查可行性和目标方向；动态图任务需要检查时间窗口是否被正确应用。

当程序通过验证后，系统再将其作用于目标图数据 $G$，获得计算结果 $R$，并根据题目要求生成最终答案：
\begin{equation}
A \leftarrow \mathrm{FormatAnswer}(R,\mathcal{F}).
\end{equation}
格式化阶段将程序输出转换为基准测试集要求的答案形式，例如节点序列、数值、布尔判断、节点集合或自然语言说明。若格式化结果不符合输出约束，系统也会将其视为反馈的一部分，而不是简单地认为推理已经完成。

\subsection{验证样例构造与错误反馈表示}

验证样例的质量直接影响反馈有效性。若验证样例过于简单，程序可能通过测试却在目标图上违反关键约束；若验证样例过于复杂，又会增加执行成本并降低错误定位效率。本文采用小规模、强约束、可判定的构造原则：样例规模保持较小，以便快速执行；样例必须覆盖当前任务的关键图属性和输出约束；样例答案或约束检查结果应可由规则稳定判定。

对于路径类任务，验证样例重点检查路径合法性、起终点一致性和代价计算；对于最大流任务，样例需要包含容量字段、源汇点和流量守恒检查；对于匹配任务，样例需要检查每个节点是否最多被匹配一次；对于旅行商问题，样例需要检查回路闭合、节点覆盖和总代价；对于动态图任务，样例需要包含时间过滤前后答案不同的情况。通过这些设计，验证样例能够更准确地暴露规划与程序之间的偏差。

当候选程序执行失败时，系统将原始报错、触发样例、约束违反位置和关联规划步骤整理为统一反馈。反馈可表示为
\begin{equation}
F_t=(etype_t,msg_t,case_t,loc_t,rel_t),
\end{equation}
其中 $etype_t$ 表示错误类型，$msg_t$ 表示错误摘要，$case_t$ 表示触发错误的验证样例，$loc_t$ 表示程序或输出中的错误位置，$rel_t$ 表示与错误最相关的规划步骤或约束。标准化反馈的作用在于减少推理智能体重新阅读全部上下文的负担，使其能够聚焦于当前失败原因。

\subsection{局部修复与有界重生成}

获得反馈后，系统优先执行局部修复：
\begin{equation}
C_{t+1}\leftarrow \mathrm{ReasoningAgent}(C_t,F_t,P,K).
\end{equation}
局部修复适用于错误范围较小且规划方向仍可信的情况，例如语法错误、变量名不一致、导入缺失、返回格式错误或单个 API 参数使用错误。由于修复过程仍以原规划和检索知识为约束，它通常能够在保留已有正确结构的基础上调整局部实现。

若反馈显示当前知识不足或 API 选择不匹配，系统会触发补充检索，利用错误类型和关联规划步骤构造二次查询。例如，当最大流任务出现容量字段读取错误时，二次查询会强调 capacity 参数、source、sink 和返回值结构；当最短路径任务出现权重字段误用时，二次查询会强调 weight 参数和路径长度计算。补充检索的目标不是重新开始整个求解，而是为当前失败位置提供更准确的实现知识。

若局部修复达到上限仍无法通过验证，或错误表明当前候选程序结构与规划严重不一致，系统将进行有界重生成：
\begin{equation}
C'_0\leftarrow \mathrm{CodingAgent}(P,K,F_{1:t}).
\end{equation}
有界重生成不同于完全重新推理，它仍然保留当前规划、检索知识和历史反馈，只重新生成候选程序。这样既避免了无限修补低质量代码，又防止每次失败都从原始问题开始，导致已经正确的规划信息被丢弃。

\subsection{反馈驱动的协同求解流程}

综合上述过程，算法\ref{alg:plangraph}给出了本文方法的完整推理流程。该算法体现了规划反馈的基本思想：先通过规划确定求解路线，再通过检索补充实现知识，随后在执行验证中不断根据反馈修复候选程序。当错误反馈表明下游实现问题时，系统进行局部修复；当错误反馈指向知识缺失或规划遗漏时，系统才回退到相应上游阶段。其中，$\mathrm{SearchAndCorrect}$ 表示检索智能体先根据规划构造查询并召回候选知识，再进行质量评估；若质量低于阈值，则执行知识片段精炼、查询重写或补充检索。

\begin{algorithm}[htbp]
\caption{基于规划反馈的图推理协同求解流程}
\label{alg:plangraph}
\begin{algorithmic}[1]
\Require 自然语言图推理问题 $Q$
\Ensure 最终答案 $A$
\State $(T,G) \gets \mathrm{QuestionAgent}(Q)$
\State $P \gets \mathrm{PlanningAgent}(T)$
\State $K \gets \mathrm{SearchAndCorrect}(P,T)$
\State $C \gets \mathrm{CodingAgent}(P,K)$
\For{$t=1$ to $T_{\max}$}
    \State $F_t \gets \mathrm{ExecuteVerify}(C,\mathcal{D}_{val},P)$
    \If{$F_t$ 表示验证通过}
        \State $R \gets \mathrm{Run}(C,G)$
        \State $A \gets \mathrm{FormatAnswer}(R,\mathcal{F})$
        \State \Return $A$
    \ElsIf{$F_t$ 指向局部实现错误}
        \State $C \gets \mathrm{ReasoningAgent}(C,F_t,P,K)$
    \ElsIf{$F_t$ 指向知识不匹配}
        \State $K \gets \mathrm{SearchAndCorrect}(P,T,F_t)$
        \State $C \gets \mathrm{ReasoningAgent}(C,F_t,P,K)$
    \ElsIf{$F_t$ 指向规划遗漏}
        \State $P \gets \mathrm{PlanningAgent}(T,F_t)$
        \State $K \gets \mathrm{SearchAndCorrect}(P,T)$
        \State $C \gets \mathrm{CodingAgent}(P,K)$
    \EndIf
    \If{局部修复达到上限}
        \State $C \gets \mathrm{CodingAgent}(P,K,F_{1:t})$
    \EndIf
\EndFor
\State \Return 基于当前最优候选的格式化答案或失败标记
\end{algorithmic}
\end{algorithm}

图\ref{fig:artifact_feedback}进一步展示了规划反馈闭环中的关键中间语义及其修正路径。与图\ref{fig:framework_overview}强调整体阶段划分不同，该图突出的是方法层面的前向约束和反向反馈：规划如何同时约束检索与编码，验证反馈又如何根据错误归因分别作用于候选程序、知识检索和规划语义；第\ref{chp:system}章将从实现角度说明这些中间结果如何通过共享黑板进行管理。

% [figure omitted: image content removed]
\caption{规划反馈闭环中的中间语义与修正路径}
\label{fig:artifact_feedback}

通过算法流程和反馈链路可以看出，本文方法不是将多个智能体简单串联，而是让每个智能体围绕可共享的中间语义进行协作。规划智能体提供求解骨架，检索智能体补充实现知识，编码智能体产生可执行候选，推理智能体根据执行反馈进行修复。由于反馈被绑定到规划步骤和候选程序位置，系统能够在较小范围内完成纠偏，从而提高复杂图推理任务的稳定性。

\section{方法分析与任务族适配}

前述小节从生成、检索和验证三个角度说明了本文方法的具体流程。本节进一步分析该方法的有效性来源，并讨论规划模板库如何支持不同图推理任务族。相比第四章的系统扩展机制，本节关注的是方法层面的任务适配，即不同任务为什么可以共享规划反馈框架。

\subsection{搜索空间压缩与误差隔离分析}

端到端生成方法需要在任务理解—算法选择—程序实现—格式输出的联合空间中一次性搜索，候选空间可近似表示为
\begin{equation}
\Omega_{\mathrm{e2e}}=\Omega_T\times\Omega_A\times\Omega_C\times\Omega_F,
\end{equation}
其中 $\Omega_T$ 表示任务理解空间，$\Omega_A$ 表示算法选择空间，$\Omega_C$ 表示程序实现空间，$\Omega_F$ 表示格式化输出空间。由于这些空间相互耦合，任一阶段的偏差都可能直接污染最终答案。

本文方法将联合搜索分解为条件搜索。系统先根据 $Q$ 和 $G$ 获得结构化任务 $T$，再生成规划 $P$，随后在 $P$ 的约束下检索知识和生成程序。该过程可理解为
\begin{equation}
\Omega_{\mathrm{pf}}=\Omega_T \times \Omega_{P|T} \times \Omega_{K|P,T} \times \Omega_{C|P,K} \times \Omega_{F|C},
\end{equation}
其中每个阶段的候选空间都受到前一阶段中间语义的约束。虽然分阶段机制会引入额外调用成本，但它降低了模型在无约束联合空间中随机探索的概率，尤其适合图推理中约束明确、算法结构稳定的任务。

从误差传播角度看，端到端方法的错误通常难以定位。最终答案错误时，很难判断问题出在任务理解、算法选择、实现细节还是输出格式。本文方法通过规划、知识、候选程序和反馈等中间语义将错误局部化：规划错误主要表现为约束覆盖不足或步骤冲突；检索错误主要表现为知识条目不匹配；编码错误主要表现为运行异常或约束断言失败；格式错误则主要表现为最终输出不符合评测要求。由于错误类型在结构上可区分，系统可以采用不同修正策略，而不必每次都完全重启推理。

此外，执行反馈提供了外部可观测信号，使系统不完全依赖模型自我判断。程序是否可运行、路径是否合法、代价是否一致、节点是否重复、容量约束是否满足，这些都可以通过规则或测试样例验证。对图推理任务而言，这种可验证性是天然优势。本文方法正是利用这一优势，将大语言模型的生成能力和程序执行的可检验性结合起来。

从多智能体协同角度看，搜索空间压缩还意味着角色职责被显式划分。问题智能体主要负责从输入中恢复任务语义，规划智能体负责组织求解路线，检索智能体负责提供实现知识，编码与推理智能体负责把规划落到程序并根据反馈修正。若这些职责全部压缩到一次生成中，模型需要在同一上下文里同时维护多个目标，容易因局部生成偏差破坏整体一致性。分阶段协同使每个智能体只面对相对明确的子问题，也使后续阶段能够检查前一阶段的输出是否满足自身输入要求。

这种分解并不意味着各阶段彼此独立。相反，规划反馈方法的关键在于阶段之间存在条件依赖和反向校正。规划质量会影响检索查询，检索结果会影响程序实现，程序执行反馈又会反过来暴露规划或检索中的缺陷。正因为这些依赖关系被显式表示，系统才能在错误发生后选择局部修复、补充检索或重新规划，而不是无差别地重新生成全部内容。

\subsection{规划模板库设计}

为了提高规划生成在不同数据集上的一致性，本文构建了轻量级规划模板库。模板库并不是固定答案集合，而是面向任务族的动作骨架集合，用于约束规划输出的最低结构完整性。按照任务目标，本文将常见图推理任务划分为路径类、连通与可达类、匹配与流类、组合优化类和动态图类。

路径类任务的模板通常包括图构建、起终点解析、路径算法调用、路径合法性检查和代价计算。连通与可达类任务强调图构建、连通分量或遍历算法、目标节点可达性判断和布尔输出。匹配与流类任务强调容量或配对约束、核心算法调用、可行性检查和目标值输出。组合优化类任务通常需要候选解生成、约束过滤、目标函数计算和最优解选择。动态图类任务则额外包含时间窗口过滤、事件序列更新和时序约束检查。

模板库采用软约束策略。规划智能体可以根据具体题目扩展步骤，但若缺失任务族的关键动作，系统会触发质量告警或要求重写规划。这样既保留了大语言模型处理复杂自然语言的灵活性，又避免规划输出过于随意。对于长尾任务或表述复杂的样例，模板库能够提供稳定骨架，降低规划遗漏关键环节的概率。

模板库还支持组合式使用。若任务同时具备多个属性，例如动态图上的最短路径或带容量约束的路径选择，系统可以将主任务模板与属性子模板叠加，形成复合规划。这种设计避免了为每个细分任务单独编写完整模板，也使方法具有更好的迁移性。

从论文方法角度看，模板库的作用不是把图推理任务写成固定规则系统，而是为大语言模型的生成过程提供结构先验。传统规则系统要求研究者手动覆盖大量任务变体，维护成本较高；完全自由生成则缺少稳定边界，容易遗漏关键约束。本文采用的模板库位于二者之间：它只规定每类任务必须包含的最小动作集合，不限制模型根据题目细节添加额外步骤。因此，模板库既能约束规划的下限，又不会完全牺牲大语言模型处理开放表达的能力。

\subsection{任务族适配策略}

任务族适配的核心是将不同图推理任务映射到统一的规划反馈框架中。对于一个新任务，系统首先识别其任务族和关键约束，再选择或组合规划模板，随后根据规划中的算法动作构造检索查询，并在执行验证阶段生成对应检查规则。适配过程关注的是任务语义，而不是具体基准测试集名称。

需要区分的是，本节讨论的是方法层面的任务适配，即如何从任务语义出发生成规划、检索条件和验证检查点；第\ref{chp:system}章的任务适配器则讨论这些语义条件在系统中如何被配置、注册和调度。前者回答新任务为什么能够进入规划反馈范式，后者回答新任务如何在系统实现中接入。

以最短路径任务为例，系统需要识别图是否带权、是否有向、起点和终点是什么、输出是否需要路径本身还是路径长度。规划模板确定后，检索阶段主要召回最短路径相关 API，验证阶段检查路径连续性和代价一致性。对于最大流任务，适配重点转向容量字段、源汇点、流量守恒和最大流值。对于旅行商问题，适配重点则变为节点覆盖、回路闭合和总代价最小化。

这种适配策略体现了本文方法的泛化方式：不同任务并不共享同一段固定提示词，而是共享解析、规划、检索、执行和反馈这一求解范式，并在任务族层面调整规划模板和验证规则。这样做可以减少对单一数据集格式的依赖，使方法能够在 GraphArena、NLGraph、GraphWiz、GraphInstruct 和 LLM4DyG 等不同基准测试集上保持较一致的流程。

在接入新任务族时，适配过程通常包括三步。第一步是确定任务族标签和关键约束，例如将问题归入路径、流、匹配、组合优化或动态图查询，并抽取起终点、容量、时间窗口、覆盖约束等条件。第二步是为该任务族补充最小规划动作，如构图、候选生成、约束过滤、目标计算和格式化输出。第三步是定义验证检查点，使执行反馈能够判断候选程序是否真正满足任务语义。只要这三步能够完成，新任务就可以纳入统一规划反馈流程，而无需改变方法本身。

\subsection{方法边界讨论}

规划反馈方法的优势主要来自结构化分解和执行验证，但它并不适用于所有情形。对于极简单的图查询，例如只需读取节点度数或判断一条边是否存在的任务，分阶段规划、检索和验证可能带来不必要的调用开销。此时，直接程序生成或简单规则解析已经能够稳定解决问题，完整规划反馈流程的收益相对有限。

对于知识库覆盖不足的长尾算法，规划反馈方法也可能受到限制。规划能够指出需要解决的问题，但若外部知识库缺少对应 API、算法说明或实现示例，检索阶段就无法为编码提供充分支持。此时系统仍可依赖模型内部知识生成程序，但稳定性会下降。因此，知识库覆盖范围和条目质量会影响该方法在长尾任务上的表现。

执行反馈的有效性还取决于任务是否具有可验证条件。最短路径、最大流、匹配、旅行商等任务通常具备明确的可行性或最优性检查，因此适合采用程序执行反馈；而某些需要复杂数学证明、开放式解释或难以自动判定正确性的任务，反馈信号可能不够充分。在这类任务中，系统需要额外引入人工标注、符号验证或更强的判定器。

从时间复杂度和调用成本看，规划反馈方法相比端到端生成引入了额外阶段。设规划、检索、编码和验证的平均开销分别为 $c_p$、$c_r$、$c_c$ 和 $c_v$，平均修复轮数为 $\bar{t}$，则单个样例的近似开销可表示为
\begin{equation}
C_{\mathrm{pf}}\approx c_p+c_r+c_c+\bar{t}(c_v+c_{\mathrm{fix}}),
\end{equation}
其中 $c_{\mathrm{fix}}$ 表示单轮修复开销。该开销高于一次性生成，但换来了更强的错误可观测性和可恢复性。因此，本文在第五章同时报告准确率、稳定性和效率指标，以展示方法收益与计算代价之间的关系。

综合来看，规划反馈方法更适合结构约束明确、可程序化验证、且算法实现存在一定复杂度的图推理任务。对于这类任务，规划能够降低求解路线的不确定性，检索能够补充实现知识，执行反馈能够抑制错误累积；对于过于简单或难以验证的任务，则需要根据成本和收益判断是否启用完整流程。这一分析也为第五章的实验设置提供了依据：实验不仅应观察最终准确率，还应结合检索质量、修复轮数、运行开销和错误类型判断规划反馈机制是否真正发挥作用。

\section{本章小结}

本章提出并详细说明了基于规划反馈的图推理协同求解方法。该方法首先将自然语言图推理任务解析为结构化任务表示，再生成算法级伪代码规划；随后利用规划引导外部知识检索和候选程序生成；最后通过执行验证形成反馈，驱动局部修复、补充检索或规划重写。与端到端直接生成相比，所提方法通过中间语义降低联合搜索难度，并通过执行反馈抑制错误传播。

本章重点讨论的是方法层面的求解范式和关键机制。下一章将进一步介绍基于黑板调度的多智能体图推理协同系统，说明上述方法如何在系统中完成调度、工件管理、异常恢复和任务扩展。
```

---

## chapters/chapter4.tex

```latex
\chapter{基于黑板调度的多智能体图推理协同系统}
\label{chp:system}

上一章从方法原理角度说明了 PlanGraph 如何将图推理任务分解为规划、检索和验证推理等阶段。本章进一步转向系统实现层面的讨论，重点回答该方法在真实运行中如何被组织为一个可调度、可恢复、可追踪和可复现的多智能体协同系统。与第三章关注求解过程为什么这样设计不同，本章关注系统如何稳定地执行这一求解过程，因此叙述重点不再重复各模块的算法功能，而是围绕主控调度、共享黑板、中间工件、执行控制、缓存复现与任务适配等运行机制展开。

对于图推理任务而言，系统实现并不是方法之外的附属环节。原因在于，图任务通常同时包含结构解析、约束识别、算法选择、代码执行和格式输出等多个阶段，其中任一阶段的不稳定都可能导致最终答案错误。如果系统仅依赖多个智能体自由对话，即使单个智能体具备较强语言生成能力，整体流程仍容易出现角色边界模糊、上下文覆盖、错误难以定位以及失败后无序重试等问题。因此，PlanGraph 在实现时采用主控调度器 + 角色智能体 + 共享黑板 + 工件存储的组织方式，将多智能体协作从自由对话转化为围绕状态和工件展开的受控协同。

本章结构安排如下：首先从系统问题定义出发，说明该方法在工程实现中需要满足的稳定性、可恢复性与可复现性要求；随后介绍系统架构与协同调度机制，说明系统如何组织多智能体角色、推进状态转移并记录运行事件；接着介绍中间工件管理与反馈恢复机制，说明系统如何保存中间状态、利用执行反馈并完成异常恢复；最后介绍系统复现配置与任务扩展机制，说明系统如何控制运行开销、支撑实验复现并适配新的图推理任务。通过这些内容，本章为第五章实验结果提供系统层面的实现基础。

\section{系统问题定义}

从系统实现视角看，本文需要解决的核心问题不是单个智能体是否能够完成局部生成，而是如何让多个角色在统一控制下稳定完成一条可回放、可恢复、可复现的图推理求解链路。具体而言，系统需要同时满足三个要求：其一，能够围绕结构化任务表示、规划、检索知识、候选程序和验证反馈等中间结果形成稳定的数据流，避免角色在多轮协作中反复覆盖前序结论；其二，能够在程序执行失败、知识不匹配或约束遗漏时，根据失败来源选择局部修复、补充检索或上游回退，而不是进行无方向的重复生成；其三，能够保留足够的运行记录和显式配置，使实验分析与结果复核建立在真实可追踪的系统证据上。

基于上述要求，PlanGraph 将系统实现建模为一个以主控调度器为中心、以共享黑板和工件链为支撑的多智能体协同系统。该系统接收自然语言问题与图结构输入，输出最终答案以及对应的中间工件、运行日志和恢复轨迹；其核心目标不是追求最自由的角色交互，而是在角色分工明确的前提下，将第三章提出的规划反馈方法落实为受控执行过程。围绕这一系统问题，后续各节将分别从架构与调度、工件与恢复、复现与扩展三个方面展开说明，从而为第五章实验结果提供实现基础。

\section{系统架构与协同调度机制}

本节围绕 PlanGraph 的系统组织方式展开，重点说明系统如何从总体架构、主控调度和黑板事件三个层面支撑多智能体协同。与第三章中按方法模块展开的叙述不同，本节关注运行期的控制关系：系统如何接收任务、如何推进阶段、如何记录事件，以及如何在失败时选择下一步动作。

\subsection{系统总体架构}

多智能体系统的一种直接实现方式是让不同角色通过自然语言彼此对话，由模型自行决定何时规划、何时检索、何时修复。然而，在图推理场景中，这种方式存在明显风险：一方面，角色之间可能重复承担同一职责，例如规划智能体和编码智能体都试图重新解释任务；另一方面，当程序执行失败时，系统难以判断应当回到规划阶段、检索阶段还是编码阶段。为避免这类控制流不稳定问题，PlanGraph 将全局流程交由主控调度器统一管理，各角色智能体只负责本阶段的局部任务。

图\ref{fig:system_architecture}给出了 PlanGraph 的系统总体架构。自上而下，系统可划分为输入与任务建模层、主控调度层、多智能体执行层以及共享状态与支撑资源层。输入与任务建模层负责接收自然语言问题和图结构信息；主控调度层负责推进阶段、检查状态并决定失败后的恢复动作；多智能体执行层包含问题智能体、规划智能体、检索智能体、编码智能体和推理智能体；共享状态与支撑资源层则提供黑板、工件存储、知识库、执行器和缓存等基础设施。与第三章中的方法流程图相比，本图更强调运行期控制关系，即调度器如何组织各角色协同、如何保存阶段状态，以及系统如何在失败后进入受控恢复路径。

% [figure omitted: image content removed]
\caption{PlanGraph 系统总体架构}
\label{fig:system_architecture}

在具体实现中，调度器并不直接参与具体内容生成，而是维护当前样例所处的运行状态、可用工件和剩余恢复预算。每个角色智能体在被调用时只读取与本阶段有关的工件，例如规划智能体读取结构化任务表示，检索智能体读取规划和任务标签，编码智能体读取规划与知识条目，推理智能体读取候选程序和验证反馈。完成阶段任务后，智能体将结果写入工件存储，并向共享黑板写入事件。这样做的好处是，角色之间不需要直接互相调用，也不需要维护复杂的私有上下文，系统协同关系由调度器和黑板统一承载。

\subsection{主控调度与状态转移}

为了使调度过程可解释，PlanGraph 将样例求解过程抽象为若干状态及其转移关系。表\ref{tab:scheduler_states}侧重描述调度器如何决定下一步，即当前阶段接收什么输入、产出什么结果以及失败后回到哪里。可以看到，系统并不是在失败后无条件重启，而是根据失败发生的位置和错误类型选择不同恢复动作。例如，规划阶段失败通常触发重新规划，检索阶段结果不足时触发补充检索，代码验证失败时则优先进入局部修复；只有当局部修复达到上限或错误类型显示当前候选不可继续利用时，系统才会触发重生成或上游回退。

\begin{table}[htbp]
\centering
\small
\caption{主控调度器的核心状态转移}
\label{tab:scheduler_states}
\renewcommand{\arraystretch}{1.12}
\begin{tabular}{m{1.7cm}m{2.5cm}m{2.8cm}m{3.6cm}}
\toprule
调度状态 & 主要输入 & 正常输出 & 失败后的转移策略 \\
\midrule
\texttt{PARSE} & 原始问题、图描述 & 任务表示 & 重新解析；失败退出 \\
\texttt{PLAN} & 任务表示 & 规划、约束标签 & 重新规划；回到解析 \\
\texttt{RETRIEVE} & 规划、任务标签 & 知识条目、质量评分 & 片段精炼；补充检索 \\
\texttt{CODE} & 规划、检索知识 & 候选程序 & 局部修复；重生成 \\
\texttt{VERIFY} & 候选程序、验证样例 & 验证结果、错误类型 & 修复；二次检索；重生成 \\
\texttt{REPAIR} & 错误反馈、候选程序 & 修复程序 & 再次验证；预算耗尽后回退 \\
\texttt{OUTPUT} & 通过验证的程序结果 & 最终答案 & 格式修复；失败退出 \\
\bottomrule
\end{tabular}
\end{table}

这种状态化调度使多智能体协作具有明确的边界感。问题智能体不需要知道编码阶段如何调用 NetworkX，编码智能体也不需要重新决定任务属于哪一类图问题；它们只需要按照调度器提供的输入完成当前阶段输出。换言之，PlanGraph 的协同并不是依靠智能体之间的自由讨论，而是依靠统一状态、统一事件和统一工件形成稳定的执行链路。这也是本文第四章将系统称为基于黑板调度的原因。

\subsection{共享黑板与事件记录}

共享黑板在该过程中承担事件总线的作用。与表\ref{tab:scheduler_states}的状态转移视角不同，表\ref{tab:blackboard_events}侧重说明系统留下什么运行记录。系统内部使用 \texttt{STAGE\_STARTED}、\texttt{TASK\_PARSED}、\texttt{PLAN\_READY} 等事件编码进行同步，这些事件并不存放所有长文本内容，而是记录阶段摘要、工件索引和关键状态，使调度器能够根据事件顺序重建样例的求解轨迹。

\begin{table}[htbp]
\centering
\small
\caption{共享黑板中的核心事件类型}
\label{tab:blackboard_events}
\begin{tabular}{m{2.5cm}m{2.2cm}m{3.0cm}m{3.2cm}}
\toprule
消息类型 & 触发时机 & 核心字段 & 主要用途 \\
\midrule
阶段启动事件 & 阶段开始 & 阶段名 & 记录调度轨迹并触发日志写入 \\
任务解析完成 & 解析完成 & 任务类型 & 为规划和检索提供任务语义 \\
规划结果就绪 & 规划完成 & 工件编号、版本号 & 触发检索与编码阶段 \\
检索结果就绪 & 检索完成 & 检索原因、候选条数 & 向编码或修复提供知识依据 \\
候选代码就绪 & 代码生成完成 & 工件编号、版本号 & 触发受控执行与验证 \\
代码失败事件 & 验证失败 & 错误码、恢复动作 & 指导调度器选择恢复路径 \\
局部修复完成 & 修复完成 & 修复轮数 & 触发再次验证 \\
结果输出完成 & 结果生成完成 & 成功标志 & 结束样例求解并写入最终日志 \\
\bottomrule
\end{tabular}
\end{table}

需要强调的是，黑板事件不是额外的形式化包装，而是系统稳定运行的必要条件。若缺少事件记录，调度器只能根据当前上下文判断下一步动作，容易在多轮修复后丢失失败来源；而通过事件链，系统可以明确知道当前候选程序来自哪一次规划、依赖哪一次检索、失败于哪一次验证。这种可追踪性不仅有助于调试系统，也为第五章中关于首次通过率、修复收敛率和失败类型的分析提供了数据基础。

\section{中间工件管理与反馈恢复机制}

在完成总体架构和调度机制说明后，本节进一步讨论系统在运行过程中如何保存中间状态、利用执行反馈并完成异常恢复。若说上一节关注系统如何推进，本节则关注系统如何在推进过程中记住、诊断和修复。这部分机制是 PlanGraph 区别于普通多智能体流水线的重要基础。

\subsection{中间工件链与版本化管理}

在多阶段图推理系统中，状态管理的核心问题不是是否保存中间结果，而是以什么粒度保存、如何关联、失败后如何利用。若所有中间内容都只保留在一次 prompt 上下文中，系统虽然实现简单，但会面临三个问题：其一，上下文不断增长后容易引入无关噪声；其二，后续智能体可能覆盖前序结论，导致无法判断错误来源；其三，实验复现时难以恢复某次失败前后的具体输入输出。为解决这些问题，PlanGraph 将中间结果从临时文本上下文中剥离出来，作为具有版本和依赖关系的工件进行管理。

对每个样例，系统将求解过程组织为一条显式工件链：
\begin{equation}
\begin{aligned}
\mathcal{A}=\{&\texttt{raw\_problem},\texttt{task\_spec},\texttt{plan},\texttt{retrieval},\texttt{candidate\_code},\\
&\texttt{verification},\texttt{repair},\texttt{final\_answer}\}.
\end{aligned}
\end{equation}
其中，\texttt{raw\_problem} 保存原始输入，\texttt{task\_spec} 保存结构化任务表示，\texttt{plan} 保存规划结果，\texttt{retrieval} 保存候选知识集合，\texttt{candidate\_code} 保存候选程序，\texttt{verification} 保存执行验证结果，\texttt{repair} 保存修复动作与修改摘要，\texttt{final\_answer} 保存最终格式化答案。工件链的设计使得系统可以在不重新读取全部上下文的情况下，定位任一阶段的输入和输出。

每个工件都附带统一元信息，用于描述来源、版本和依赖关系。表\ref{tab:artifact_fields}给出了核心字段。与一般日志不同，工件不是简单的文本记录，而是可被后续阶段继续读取和消费的结构化对象。例如，检索模块读取的不是自然语言长文本，而是规划工件中的任务动作、约束标签和算法族；修复模块读取的也不是完整历史对话，而是候选程序工件和验证反馈工件。对于检索工件，系统还会额外记录检索质量评分；当评分低于阈值时，调度器可触发知识片段精炼或查询重写后的补充检索，并将更新结果继续写入共享黑板供后续编码与恢复阶段使用。

\begin{table}[htbp]
\centering
\small
\caption{中间工件的核心字段}
\label{tab:artifact_fields}
\begin{tabular}{m{2.8cm}m{7.5cm}}
\toprule
字段 & 含义 \\
\midrule
\texttt{id} & 工件唯一标识，例如 \texttt{plan:1:ad03bd12} \\
\texttt{kind} & 工件类别，如 \texttt{task\_spec}、\texttt{plan}、\texttt{retrieval} \\
\texttt{version} & 同类工件的版本号，用于标识迭代过程 \\
\texttt{source\_module} & 生成该工件的模块，例如问题解析模块或规划模块 \\
\texttt{timestamp} & 工件写入时间，用于记录阶段顺序与复现实验 \\
\texttt{parent\_version} & 上游依赖版本，用于恢复依赖链和定位失败来源 \\
\texttt{payload} & 工件主体内容，如结构化任务、规划伪代码或验证结果 \\
\texttt{summary} & 对长代码、长列表和复杂对象的压缩摘要 \\
\bottomrule
\end{tabular}
\end{table}

工件链的价值可以通过旅行商问题样例加以说明。对于一个要求从固定起点出发、访问全部节点并返回起点的带权无向图任务，问题解析阶段生成的 \texttt{task\_spec} 会记录图类型、边权信息、起点约束、回路约束和输出形式；规划阶段生成的 \texttt{plan} 会记录构建带权图—固定起点—枚举候选回路—计算总代价—选择最优闭环的求解意图；检索阶段生成的 \texttt{retrieval:1} 保存与旅行商问题、哈密顿回路和路径代价计算相关的知识条目；编码阶段生成的 \texttt{candidate\_code:1} 则依赖 \texttt{plan:1} 和 \texttt{retrieval:1}。如果验证阶段发现候选程序没有正确处理回到起点的约束，系统不会覆盖原有工件，而是生成 \texttt{verification:1} 和后续的 \texttt{repair:1}。这样，失败原因、修复动作和新程序版本之间形成明确依赖关系。

这种版本化管理在系统恢复中尤其重要。对于图推理任务，错误可能来自不同阶段：规划缺少约束会导致后续程序方向错误；检索召回了不匹配的 API 会导致函数调用错误；编码阶段遗漏边权会导致答案数值错误；格式化阶段不符合基准测试集输出规范也会造成最终判错。若系统只保留最后一次生成内容，就很难判断该回到哪个阶段修复。通过工件依赖链，调度器可以根据失败工件定位上游来源：若验证失败但规划和检索均合理，则优先局部修复代码；若错误与知识使用有关，则触发二次检索；若规划本身缺少关键约束，则回退到规划阶段。

当然，完整保存所有中间内容也会带来运行开销。因此，PlanGraph 在工件管理中采用完整工件 + 摘要索引的折中策略。对于短文本对象，如任务标签、约束列表和错误码，系统完整保存；对于较长对象，如候选代码、检索条目列表和模型输出，系统保存完整内容的同时生成摘要，供黑板事件快速引用。当历史工件过多时，调度器优先保留最近轮次的完整版本，对更早版本只保留摘要、错误类型和关键依赖关系。这样既保证失败回放所需的信息不丢失，又避免将全部历史内容反复注入模型上下文。

从学位论文写作角度看，黑板式状态记忆还承担了连接方法设计与实验分析的作用。第三章说明了规划、检索和验证如何构成求解方法，而本节说明这些中间阶段在系统中如何被记录、管理和追踪。第五章中对稳定性、修复收敛和失败类型的分析，正是以这些运行时工件为基础。因此，工件管理不是单纯的工程实现细节，而是 PlanGraph 可解释性和可复现性的关键支撑。

\subsection{检索执行反馈推理闭环}

第三章已经从方法角度说明了规划引导检索和执行验证的作用，本节进一步说明系统如何在运行期组织二者之间的闭环关系。对于图推理任务，首次检索通常只能覆盖规划预期中的知识需求，而程序执行后暴露出的错误往往包含更具体的实现信息，例如字段缺失、API 参数不匹配、路径约束未满足或输出格式错误。若系统不能把这些失败信息重新纳入检索与修复过程，检索模块就会退化为编码前的一次性辅助工具，无法真正参与失败恢复。

为此，PlanGraph 将检索输入组织为多层查询集合：
\begin{equation}
\mathcal{Q}_{\mathrm{retr}}=\{Q_0,Q_1,Q_2,Q_3,Q_4\}.
\end{equation}
其中，$Q_0$ 为原始问题文本，$Q_1$ 为结构化任务表示，$Q_2$ 为规划伪代码，$Q_3$ 为任务适配器给出的图类型标签与约束标签，$Q_4$ 为执行失败后的错误反馈。实际运行中，首次检索主要依赖 $Q_2$ 与 $Q_3$，即以规划步骤、算法提示和关键约束作为查询主线；当执行阶段暴露出新的错误信息时，系统再将 $Q_4$ 作为补充查询条件，触发面向失败原因的二次检索。

这种设计体现了规划锚定与反馈修正的运行原则。规划锚定意味着二次检索仍然围绕原始求解意图展开，避免系统因某次局部报错而偏离任务目标；反馈修正则意味着错误信息不只用于让模型重写代码，也用于让检索模块找到更贴近失败原因的知识条目。例如，当候选程序在旅行商任务中因图字段组织方式出错而触发 \texttt{API\_OR\_GRAPH\_ERROR} 时，二次检索并不是重新查找旅行商问题的一般介绍，而是更关注图构建、边权字段、路径代价计算等与错误直接相关的知识。

为减少语义相关但任务不匹配的检索噪声，系统在召回后执行面向任务的重排序。设候选知识条目为 $k_i$，综合得分可表示为：
\begin{equation}
\mathrm{Rank}(k_i)=
\lambda_1\mathrm{sim}_{\mathrm{task}}(k_i,T)
+\lambda_2\mathrm{sim}_{\mathrm{cons}}(k_i,\mathcal{C})
+\lambda_3\mathrm{sim}_{\mathrm{alg}}(k_i,P)
+\lambda_4\mathrm{score}_{\mathrm{snip}}(k_i).
\end{equation}
其中，$\mathrm{sim}_{\mathrm{task}}$ 表示任务类型匹配度，$\mathrm{sim}_{\mathrm{cons}}$ 表示约束标签匹配度，$\mathrm{sim}_{\mathrm{alg}}$ 表示算法族匹配度，$\mathrm{score}_{\mathrm{snip}}$ 表示条目片段自身的检索得分。该排序方式使检索模块不只是返回相似文本，而是根据当前规划、任务标签和失败反馈筛出更适合当前样例的知识片段。

执行验证则承担将抽象规划重新压回任务约束的作用。候选程序生成后，系统会通过 \texttt{ExecutionVerifier} 在受控环境中执行程序，并将结果统一整理为包含 \texttt{ok}、\texttt{stdout}、\texttt{error\_type} 和 \texttt{stderr\_head} 等字段的验证工件。这里的验证并不局限于语法检查。对于路径类任务，系统重点检查路径合法性、总代价一致性以及起止条件；对于组合优化任务，系统优先检查解的可行性，再在必要时比较目标值；对于动态图或带时间约束的问题，验证样例会覆盖时间窗口和事件顺序。

以旅行商任务中的一次失败恢复为例，系统首先完成任务解析和规划，随后基于规划召回相关知识并生成候选程序。若首轮验证发现程序读取边信息时出现字段缺失，调度器会将该错误归类为图构建或 API 使用错误，并触发二次检索 + 局部修复的恢复路径：二次检索阶段将错误类型和报错摘要作为补充查询，推理智能体则在保持原始规划不变的前提下修复图构建逻辑；修复后的程序再次进入验证阶段，若路径闭合、节点覆盖和代价计算均满足要求，系统才会进入答案输出阶段。这个过程说明，PlanGraph 的反馈并不是一般意义上的再次自由尝试，而是通过执行器提供的外部信号驱动检索和修复。

从运行机制看，该闭环还有一个重要作用，即限制失败信息的传播范围。若候选程序出现 API 参数错误，系统并不会把整个任务重新交给模型自由生成，而是把错误压缩为结构化反馈，并与原规划、原检索知识共同提供给修复阶段。这样既保留了前序阶段已经确定的求解意图，又允许系统针对真实错误做局部调整。对于图推理任务而言，这种保留稳定部分、修复不稳定部分的策略尤其重要，因为许多失败并非来自任务方向完全错误，而是来自图字段组织、边权读取、约束检查或输出格式等局部实现偏差。

该闭环机制也说明了第四章与第三章的分工。第三章关注规划、检索和验证作为方法模块如何提升求解质量；本节关注这些模块在系统运行时如何被调度器连接成可恢复的执行链路。换言之，系统实现的重点不是重复论证规划为什么有效，而是确保规划、知识和反馈能够以稳定的数据结构流动，并在失败时形成明确的恢复路径。

\subsection{执行控制与异常恢复}

由于 PlanGraph 采用程序化求解，系统可靠性不仅取决于语言模型生成质量，还取决于运行时能否安全执行候选程序、识别失败类型并及时终止错误分支。图推理程序可能包含组合搜索、图遍历、路径枚举或动态更新等操作，若缺少执行控制，错误程序可能出现异常退出、无限搜索、输出格式不规范或资源占用过高等问题。因此，PlanGraph 将执行控制设计为系统可靠性的独立组成部分，而不是简单地把程序交给解释器运行。

在执行阶段，系统对候选程序设置时间限制、标准输出捕获、异常堆栈截断和结果格式检查。时间限制用于防止组合搜索类任务进入不可接受的长尾执行；标准输出捕获用于记录程序产生的中间结果和最终答案；异常堆栈截断用于保留关键错误信息，同时避免过长报错污染后续修复上下文；结果格式检查则用于判断程序输出是否满足基准测试集要求。通过这些控制，验证工件不仅能反映程序是否运行成功，还能反映失败发生在什么位置、是否适合局部修复、是否需要回退到上游阶段。

当前实现中的主要错误类型及恢复路径如表\ref{tab:error_recovery}所示。表中列出的不是底层编程语言异常的简单罗列，而是经过系统归因后的恢复语义。例如，语法错误和导入错误通常说明候选程序局部不可执行，但规划和检索结果未必有问题，因此优先局部修复；图构建或 API 使用错误往往说明检索知识和实际字段组织之间存在偏差，因此需要结合失败反馈进行二次检索；超时错误则通常意味着当前实现路径成本过高，继续局部修补意义有限，应优先放弃当前候选并触发重生成。

\begin{table}[htbp]
\centering
\small
\caption{主要错误类型与恢复路径}
\label{tab:error_recovery}
\begin{tabular}{m{3.0cm}m{3.0cm}m{4.9cm}}
\toprule
错误类型 & 典型含义 & 恢复路径 \\
\midrule
语法或导入错误 & 程序本身不可执行 & 保持当前规划与检索结果，直接进行局部修复 \\
空输出或约束违反 & 程序可运行但结果不满足任务要求 & 局部修复后再次验证 \\
图构建或 API 使用错误 & 图字段组织方式或函数选择存在偏差 & 二次检索后进入局部修复，再次验证 \\
答案错误 & 程序可执行但答案与判定器不一致 & 结合失败反馈补充检索，必要时重生成 \\
超时错误 & 程序超时或搜索开销失控 & 受控终止当前执行，放弃该候选并触发重生成 \\
上游阶段失败与未知异常 & 规划、检索阶段失稳，或预算耗尽 & 有界回退；超过预算后输出结构化失败 \\
\bottomrule
\end{tabular}
\end{table}

异常恢复机制的关键在于有界。如果系统在同一错误上无限修复，虽然表面上体现了反馈能力，实际却会造成运行成本失控和错误方向强化。为避免这种情况，PlanGraph 为规划尝试次数、检索尝试次数、局部修复轮数和重生成轮数分别设置上限。设第 $s$ 个阶段的最大尝试次数为 $B_s$，当前尝试次数为 $b_s$，则调度器只在
\begin{equation}
b_s < B_s
\end{equation}
时允许继续在该阶段内修复；若达到预算上限，则根据错误类型选择上游回退、重生成或输出结构化失败结果。该预算约束使系统能够在稳定性和成本之间取得平衡：既避免一出错就推倒重来的高成本，也避免在错误方向上无限修补。

从系统分析角度看，异常恢复还提供了失败归因能力。每次失败都会同时写入黑板事件和验证工件，记录错误类型、触发阶段、候选程序版本、恢复动作和后续结果。这样，系统不仅能够在当前样例中选择恢复路径，也能够在实验分析中统计哪些任务更容易发生规划遗漏、哪些任务更容易出现 API 使用错误、哪些任务主要受输出格式约束影响。第五章中的误差分析正是建立在这种结构化运行记录之上。

异常恢复机制还体现了系统层面对“正确性”和“可用性”的折中。对于部分组合优化任务，严格验证可能增加执行次数和反馈轮数，但它能够减少表面可运行、实际不满足约束的答案；对于部分简单结构查询任务，系统则可以在首次验证通过后直接输出，避免不必要的修复开销。因此，恢复策略并不是固定地追求更多轮次，而是在错误类型、恢复预算和任务复杂度之间做受控选择。这种选择由调度器执行，而不是由单个智能体临时决定，从而保证不同样例之间的运行策略具有一致性。

需要指出的是，执行控制并不能保证所有失败都能被自动修复。对于规划阶段已经遗漏核心约束、知识库缺乏相关算法条目或任务本身需要复杂长尾搜索的样例，局部修复可能只能缓解部分实现错误。因此，本文将异常恢复定位为提高系统稳定性与可诊断性的机制，而不是保证所有样例必然成功的万能策略。这种边界说明也使系统设计更符合工程实践。

\section{系统配置管理与任务扩展机制}

前两节分别说明了系统的调度方式和反馈恢复机制，本节进一步讨论 PlanGraph 如何在工程层面控制运行开销、管理关键配置，并支持新任务扩展。对于硕士学位论文而言，这部分内容的重点不是展示复杂工程接口，而是说明系统实现如何支撑后续实验比较和方法迁移。

\subsection{运行开销与缓存优化}

多智能体协同和验证反馈会带来额外运行开销。与直接生成答案相比，PlanGraph 需要经历任务解析、规划生成、知识检索、代码生成、执行验证和必要的反馈修复等阶段，因此系统实现必须同时考虑准确性和成本控制。若只追求增加智能体数量或修复轮数，虽然可能在部分样例上提高成功率，但也会显著增加调用成本和执行时延。因此，本节从运行开销来源、缓存优化和配置管理三个方面说明系统如何控制工程代价。

从单样例角度看，PlanGraph 的总时延可分解为：
\begin{equation}
T_{\mathrm{all}}=T_{\mathrm{parse}}+T_{\mathrm{plan}}+T_{\mathrm{retr}}+T_{\mathrm{code}}+T_{\mathrm{exec}}+T_{\mathrm{repair}}.
\end{equation}
其中，$T_{\mathrm{parse}}$、$T_{\mathrm{plan}}$ 和 $T_{\mathrm{code}}$ 主要受模型调用影响，$T_{\mathrm{retr}}$ 主要受知识库检索和重排序影响，$T_{\mathrm{exec}}$ 主要受图规模和算法复杂度影响，$T_{\mathrm{repair}}$ 则是由失败样例触发的额外成本。实践中，长尾开销往往不是来自所有阶段均匀增加，而是来自少数复杂样例的多轮修复和重生成。因此，系统采用局部修复优先、重生成受限、超时终止和缓存复用等策略控制运行成本。

缓存机制主要用于减少重复规划和重复检索。PlanGraph 引入 \texttt{JsonCache} 作为轻量缓存层，缓存键由结构化任务摘要、任务标签、规划版本和检索参数共同决定。对于完全相同或高度相似的任务，系统可以复用已有规划结果；对于规划和任务标签一致的检索请求，系统可以复用候选知识条目集合。需要注意的是，系统并不缓存最终答案作为默认行为，因为最终答案与具体图实例和输出格式强相关，直接复用可能破坏实验公平性。相比之下，规划结果和检索知识具有更强的中间语义属性，更适合作为可复用对象。

缓存优化与黑板机制之间存在自然配合。黑板记录当前样例使用了哪些缓存项，工件存储记录缓存命中的规划或检索版本。当缓存命中时，系统仍会生成新的事件和工件引用，而不是跳过记录过程。这样做保证了即便某一阶段没有重新调用模型或检索器，实验日志中仍然能够完整呈现阶段流转，避免缓存导致复现实验时出现缺失步骤的问题。

在此基础上，仅有缓存机制还不足以约束系统运行。缓存解决的是重复计算开销问题，而配置管理解决的是运行条件一致性问题。为避免不同批次的结果受到隐含参数影响，系统还需要记录关键参数、运行产物和缓存命中情况。

\subsection{运行配置与产物管理}

系统将关键运行参数显式配置化。表\ref{tab:runtime_config}给出了当前实现中最重要的一组默认配置。这些配置不属于实验结果本身，而是主控调度器执行各阶段时使用的边界条件，用于约束检索范围、修复深度、重生成次数和程序执行时间。

\begin{table}[htbp]
\centering
\small
\caption{核心运行配置}
\label{tab:runtime_config}
\begin{tabular}{m{3.0cm}m{2.0cm}m{6.1cm}}
\toprule
配置项 & 默认值 & 作用 \\
\midrule
检索返回条数 & 5 & 每次检索返回的候选知识条数 \\
最大局部修复轮数 & 3 & 单个候选程序允许的最大局部修复轮数 \\
最大重生成轮数 & 1 & 修复失败后允许的最大重生成次数 \\
最大规划尝试次数 & 2 & 规划阶段最大尝试次数 \\
最大检索尝试次数 & 2 & 检索阶段最大尝试次数 \\
单次执行超时阈值 & 15 & 单次程序执行超时阈值（秒） \\
随机种子 & 42 & 随机采样和实验复现使用的固定种子 \\
\bottomrule
\end{tabular}
\end{table}

显式配置化的意义在于约束系统行为。检索返回条数决定编码阶段可见知识范围，最大局部修复轮数决定反馈闭环深度，最大重生成轮数决定系统在失败后的探索边界，执行超时阈值决定复杂搜索的成本上限，随机种子则影响模型采样和任务处理顺序。将这些因素统一配置后，调度器才能在不同任务上保持一致的运行策略。

此外，运行产物目录也采用统一组织方式。每个样例的原始输入、结构化任务、规划结果、检索条目、候选程序、验证反馈和最终答案均写入同一工作目录下的对应子项，缓存目录则独立保存可复用的规划与检索结果。这样的目录组织看似是工程细节，实际影响系统的可追踪性：当某个样例结果异常时，研究者可以直接检查该样例完整链路，而不需要从混合日志中手动恢复上下文；当更换模型版本或知识库版本时，也可以通过目录和配置文件对比不同运行条件下的工件差异。

从论文结构上看，第四章只讨论系统开销来源和成本控制机制，不在此处展开大规模效率对比。原因是运行时间会受到模型接口响应、网络环境、图规模、任务类型和修复轮数等多重因素影响，若在系统实现章中给出过多统计表，反而容易削弱本章对机制设计的论述。第五章将结合具体基准测试集报告平均耗时、验证次数和参数敏感性，从实验角度进一步说明系统开销与性能之间的关系。

\subsection{面向扩展任务的适配策略}

PlanGraph 的目标并不是为某一个基准测试集编写固定流程，而是构建一种可迁移的图推理协同系统。第三章已经从方法层面说明了任务族如何共享规划反馈范式，本节进一步说明系统实现中如何通过适配器承载这些任务语义。因此，系统实现中需要区分稳定主流程和可替换任务知识。稳定主流程包括任务解析、规划、检索、编码、验证、修复和输出等阶段；可替换任务知识则包括图类型标签、任务目标、约束集合、规划模板、知识条目和验证规则。任务适配器的作用，就是将不同图任务的语义映射到统一主流程中。

从抽象形式看，任务适配器可表示为
\begin{equation}
\mathcal{D}_{\mathrm{task}}=\{\tau,\mathcal{G}_{\mathrm{tag}},\mathcal{C},\mathcal{A}_{\mathrm{alg}},\mathcal{P}_{\mathrm{tpl}},\mathcal{V}_{\mathrm{rule}}\},
\end{equation}
其中，$\tau$ 表示任务类型，$\mathcal{G}_{\mathrm{tag}}$ 表示图结构标签，$\mathcal{C}$ 表示关键约束集合，$\mathcal{A}_{\mathrm{alg}}$ 表示候选算法族，$\mathcal{P}_{\mathrm{tpl}}$ 表示规划模板，$\mathcal{V}_{\mathrm{rule}}$ 表示验证规则集合。该形式化表示并不是为了增加额外算法复杂度，而是为了说明任务适配器在系统中的位置：它位于任务理解和主流程调度之间，用于把具体任务语义转化为后续阶段可消费的结构化条件。

具体而言，任务适配器并不直接给出答案，而是描述某类任务的图类型、目标类型、输出形式、关键约束、算法族和验证规则。以旅行商任务为例，适配器会声明该任务通常属于带权无向图，目标类型为组合优化，输出形式为路径，关键约束包括访问每个节点一次、回到起点和最小化总代价；对应算法族可包括旅行商问题、哈密顿回路和组合枚举；验证规则则包括路径是否闭合、是否覆盖全部节点、路径边是否合法以及总代价是否与边权一致。通过这些适配信息，规划模块能够生成更完整的动作序列，检索模块能够构造更聚焦的查询，验证模块也能够执行更有针对性的约束检查。

任务适配器的关键价值在于降低扩展新任务时对主调度器的侵入。若新增一个图任务，系统通常只需要完成四类局部修改：第一，补充任务标签和约束描述，使问题智能体能够识别该任务；第二，补充规划模板，使规划智能体能够生成符合任务族特征的动作序列；第三，补充知识条目，使检索模块能够召回相关 API、算法说明和实现注意事项；第四，注册验证规则，使执行器能够检查关键约束是否满足。主调度器本身不需要因为新增任务而改变状态转移逻辑。

以动态图最短路径任务为例，若任务要求在指定时间窗口内计算可达路径，系统无需改变调度器的 \texttt{PARSE}、\texttt{PLAN}、\texttt{RETRIEVE}、\texttt{CODE} 和 \texttt{VERIFY} 状态，只需要在适配器中增加动态图标签、时间窗口约束、事件过滤模板和对应验证规则。规划阶段会据此生成先筛选时间窗口、再构建有效图、最后执行路径搜索的动作序列；检索阶段会优先召回动态图处理和时间过滤相关知识；验证阶段则检查程序是否在图搜索前正确处理时间条件。由此，系统扩展体现为局部知识和规则的补充，而不是主流程的重写。

这种设计使系统扩展具有配置优先、流程稳定的特点。对于路径类任务，通常只需调整起点、终点、边权和路径合法性约束；对于匹配与流类任务，则需要补充容量、配对关系和可行性检查；对于动态图任务，则需要额外描述时间窗口、事件顺序和状态更新规则。虽然不同任务的知识和验证规则不同，但它们都可以通过同一调度框架进入规划、检索、编码和验证链路。

需要注意的是，适配器机制并不意味着系统可以零成本处理任意图任务。若新任务的算法知识库覆盖不足，或验证规则难以形式化，系统仍可能出现规划粒度不足或验证不充分的问题。因此，PlanGraph 的扩展性主要体现在系统主流程不需要重写，而不是承诺所有任务都能自动达到相同性能。对于学位论文而言，这一点有助于明确方法边界：本文强调的是一种可配置、可验证、可恢复的协同求解框架，而不是覆盖所有图智能问题的通用求解器。

从工程实现角度看，任务适配器还便于后续研究替换系统组件。当知识源从文档库扩展为向量数据库、代码库或专用求解器说明时，只要保持知识条目结构一致，检索模块即可替换底层索引；当验证方式从小样例执行扩展为约束求解或静态分析时，只要保持验证工件结构一致，调度器也不需要改变。由此，PlanGraph 的可扩展性来自主调度流程、任务适配器和验证规则之间的职责分离。

\section{本章小结}

本章从系统实现角度对 PlanGraph 进行了展开。与第三章侧重方法原理不同，本章重点说明了规划、检索、编码和验证等模块在真实运行中如何被组织为稳定的多智能体协同系统。首先，系统通过总体架构和黑板调度机制明确角色边界、状态转移和事件记录；其次，系统通过中间工件管理与反馈恢复机制实现失败归因、过程回放、反馈修复和异常控制；最后，系统通过缓存、显式配置、运行产物管理和任务适配器机制支撑实验复现与任务扩展。

总体而言，PlanGraph 的系统价值不在于简单增加智能体数量，而在于将多智能体协作约束在可观察、可恢复和可复现的运行框架中。上述系统机制共同构成第五章实验验证的基础，也说明本文方法不仅具有概念上的合理性，而且具备落地为稳定图推理系统的工程条件。
```

---

## chapters/chapter5.tex

```latex
\chapter{实验验证与结果分析}
\label{chp:experiment}

\section{实验设计与设置}

本章围绕方法是否有效、机制是否成立、系统代价是否可接受三个层面展开实验验证。考虑到本文提出的是一种基于规划反馈的多智能体图推理协同求解方法，实验设计不仅需要比较总体精确匹配率，还需要从任务类型、知识检索质量、参数预算、工程开销与输入扰动鲁棒性等角度对方法行为进行拆解分析。基于这一思路，本章先说明实验目标、数据集与实现设置，再给出总体结果、分层结果以及若干机制验证与补充实验。

\subsection{实验目标}

为验证所提 PlanGraph 框架的有效性，本文围绕以下四个研究问题展开实验。

\begin{itemize}
    \item PlanGraph 相比现有大语言模型图推理方法，整体性能是否具有优势？
    \item PlanGraph 在不同图推理基准测试集上的表现是否稳定？
    \item PlanGraph 在不同类别图任务上的优势主要体现在哪些方面？
    \item PlanGraph 的性能提升是否来自规划、检索和验证等关键模块的协同作用？
\end{itemize}

\subsection{数据集与任务类型}

本文选取五个具有代表性的图推理基准测试集进行评估，分别为 GraphArena、NLGraph、GraphWiz、LLM4DyG 和 GraphInstruct\cite{tang2025grapharena,chen2024nlgraph,gong2024graphwiz,llm4dyg2024,graphinstruct2024}。这些数据集覆盖了经典图算法、组合优化、指令跟随以及动态图推理等不同场景。

\begin{itemize}
    \item \textbf{GraphArena：} 覆盖基础结构查询、距离计算、组合优化和旅行商等任务，能够综合考察经典图算法与高约束搜索能力。
    \item \textbf{NLGraph：} 强调自然语言条件下的图算法推理，涉及连通性、最大流、环检测、拓扑排序和双边匹配等问题。
    \item \textbf{GraphWiz：} 面向指令式图推理，覆盖二分图判断、最短路径、最大三角和、最大流、哈密顿路径和子图匹配等任务。
    \item \textbf{LLM4DyG：} 聚焦动态图或含时间约束的图推理问题，对模型的时序理解与图结构联动能力提出更高要求。
    \item \textbf{GraphInstruct：} 关注图指令跟随场景，包含邻居查询、前驱节点、深度优先遍历和拓扑排序等基础任务。
\end{itemize}

由于不同基准测试集在任务数量、样本规模、难度划分和答案格式方面存在差异，直接采用原始完整划分进行横向比较可能导致评价口径不一致。为保证不同方法之间的公平比较，本文按照任务可验证、答案格式明确、评价指标一致、基线结果可对齐的原则，从各基准测试集中选取具有代表性的任务样本构建统一评测集合。对于任务覆盖范围较广的数据集，本文保留能够代表典型图结构查询、路径推理、组合优化和指令跟随能力的任务；对于动态图和自然语言图算法任务，则依据公开测试划分和任务定义选取相应样本。后续主实验统一采用精确匹配率（Exact Match, EM）作为总体性能指标。

\subsection{对比方法与实现设置}

为保证实验结论具有可比性与可复核性，本节先说明对比基线构成，再给出实验中采用的实现配置。系统组织方式、运行时控制和异常恢复机制已在第四章中详细展开，本节仅保留与实验复现直接相关的设置。

本文主要将 PlanGraph 与四类代表性结果进行比较：一是通用强基座模型 GPT-4o 的直接推理结果；二是代表性的多智能体图推理方法 GraphTeam\cite{li2024graphteam}；三是代表性的程序生成式图推理方法 GCoder\cite{zhang2025gcoder}；四是各基准测试集已公开报告的最优结果。之所以重点选择 GraphTeam 和 GCoder 作为核心对比对象，是因为二者分别代表了当前图推理任务中最具代表性的两条技术路线：GraphTeam 强调通过多智能体角色分工提升图任务协同求解能力，GCoder 强调通过程序生成与图问题代码化提升可执行求解能力；同时，这两类方法也是相关基准测试集上具有代表性的强基线。通过与它们进行对比，本文能够更清楚地回答 PlanGraph 相对于多智能体协作路线和程序生成路线的增益究竟来自何处，从而同时评估 PlanGraph 相对通用大模型、现有专门方法与当前已知最优性能的增益幅度。

实验中，PlanGraph 使用 GPT-4o 作为基础语言模型，模型调用采用 OpenAI-compatible Chat Completions API，程序执行环境统一为 Python 与 NetworkX。为降低生成随机性带来的结果波动，主实验中温度参数设置为 0.2，最大输出长度设置为 2048 tokens。系统在每个样本上只保留一条最终答案，不采用多答案投票，以避免额外采样带来的结果偏移。

外部知识检索使用固定版本的轻量图算法知识库。该知识库共包含 3349 条知识条目，覆盖最短路径、最大流、最大团、最小点覆盖、最大独立集、旅行商、哈密顿路径、连通性、拓扑排序、二分图判定、图直径、邻居查询、子图匹配和最小割等常见图任务。除参数敏感性实验外，知识库版本、检索器和重排序规则在所有实验中保持一致，以避免外部知识源变化对结果造成干扰。

除非特别说明，本文沿用第四章给出的默认运行配置：检索返回条数设为 5，最大局部修复轮数设为 3，最大重生成轮数设为 1，规划与检索阶段的最大尝试次数分别设为 2，单次候选程序执行超时阈值设为 15 秒，随机种子固定为 42。对于大规模批量实验，为避免单个样例因接口等待而长时间阻塞，单次模型调用超时设置为 30 秒。验证样例主要覆盖图构建正确性、任务约束满足性与输出格式规范性；对于组合优化问题，还额外检查候选解的可行性。上述设置的目的在于尽量固定运行条件，使第五章结果反映方法本身的有效性，而非额外采样策略带来的收益。

为保证实验比较的公平性，本文在所有实验中固定数据划分、样本顺序、模型版本、温度参数、最大输出长度、执行环境、超时阈值和答案判定规则。不同方法之间仅改变被比较模块，例如是否引入规划、是否引入检索以及是否启用反馈修复。对于使用检索的方法，知识库版本、检索器、返回条数和重排序规则保持一致；对于使用代码执行的方法，候选程序均在相同的 Python 环境中运行，并由同一验证器判断输出是否正确。

\subsection{评价指标}

为确保不同基准测试集间结果可比较，本文在主实验中统一采用精确匹配率（Exact Match, EM）作为总体性能指标。设测试集样本数为 $N$，其中模型完全答对的样本数为 $N_c$，则精确匹配率定义为：

\begin{equation}
\mathrm{EM} = \frac{N_c}{N} \times 100\%
\end{equation}

对于代码生成类方法，精确匹配率按 exact match 统计。所有失败样例均保留在统计中，包括运行错误、超时错误、输出不可解析的格式错误以及程序运行成功但答案错误的情形，不进行人工过滤或事后修正。

除总体性能所采用的精确匹配率外，本文在补充实验中还使用了若干任务相关指标。检索质量验证使用 Hit@k 与平均倒数排名（MRR），用于衡量不同查询方式对知识命中与排序质量的影响。其中，若第 $i$ 个查询的正确知识条目排序位置为 $\mathrm{rank}_i$，则：

\begin{equation}
\mathrm{Hit@}k = \frac{1}{N}\sum_{i=1}^{N}\mathbb{I}(\mathrm{rank}_i \le k)\times 100\%
\end{equation}

\begin{equation}
\mathrm{MRR} = \frac{1}{N}\sum_{i=1}^{N}\frac{1}{\mathrm{rank}_i}\times 100\%
\end{equation}

参数敏感性分析除统计总体精确匹配率外，还进一步报告简单样本与困难样本上的分层精确匹配率、执行成功率、平均修复轮数与平均端到端耗时，以刻画参数设置对稳定性、修复成本和工程代价的影响。本文中的难度分层主要依据图规模确定：简单样本对应节点数小于 10 的图实例，中等样本对应节点数为 10 至 20 的图实例，困难样本对应节点数大于 30 的图实例。设可成功完成代码执行并返回可验证结果的样本数为 $N_s$，第 $i$ 个样本触发的修复轮数为 $r_i$，端到端耗时为 $t_i$，则相关指标定义为：

\begin{equation}
\mathrm{ExecSuccess} = \frac{N_s}{N}\times 100\%
\end{equation}

\begin{equation}
\mathrm{AvgRepair} = \frac{1}{N}\sum_{i=1}^{N} r_i
\end{equation}

\begin{equation}
\mathrm{AvgTime} = \frac{1}{N}\sum_{i=1}^{N} t_i
\end{equation}

其中，简单样本与困难样本上的分层精确匹配率与总体精确匹配率形式相同，只是在对应难度子集上分别统计；参数敏感性实验选取两端难度样本进行比较，主要用于观察参数变化在低结构复杂度与高结构复杂度样本上的影响差异。

此外，本文在定性分析中还关注可解释性、稳定性、知识利用能力与约束满足能力。其中，可解释性用于评估系统是否能够清晰呈现规划步骤、错误反馈与修复过程；稳定性用于观察结构相近但表达不同的问题上输出是否一致；知识利用能力用于衡量模型是否能够依据规划调用合适的图算法 API；约束满足能力则用于评估路径、匹配和时间窗口等关键约束的达成情况。这些观察维度虽然不直接纳入统一表格统计，但对理解 PlanGraph 性能来源具有重要意义。

\section{总体实验结果与稳定性分析}

\subsection{总体性能对比}

表~\ref{tab:overall_result}给出了 PlanGraph 在统一评测集合上的总体精确匹配率结果，其中任务数表示本文实际纳入主实验统计的任务类别数量。可以看出，PlanGraph 在五个基准测试集中有四个取得最优结果，平均精确匹配率达到 97.69\%，相比最佳对比基线提升 2.07 个百分点。

\begin{table}[htbp]
\centering
\small
\caption{不同基准测试集上的总体精确匹配率比较（\%）}
\label{tab:overall_result}
\begin{tabular}{lcccccc}
\toprule
数据集 & 任务数 & GPT-4o & GraphTeam & GCoder & PlanGraph & 相对提升 \\
\midrule
GraphArena & 9 & 43.50 & 95.49 & 94.80 & \textbf{97.88} & +2.39 \\
NLGraph & 8 & 51.40 & 97.71 & 96.90 & \textbf{98.72} & +1.01 \\
GraphWiz & 9 & 47.61 & 88.62 & 90.20 & \textbf{97.01} & +6.81 \\
LLM4DyG & 9 & 58.04 & \textbf{96.35} & 93.78 & 96.11 & -0.24 \\
GraphInstruct & 9 & 78.18 & 98.33 & 97.39 & \textbf{98.74} & +0.41 \\
\midrule
平均 & -- & 55.75 & 95.30 & 94.61 & \textbf{97.69} & +2.07 \\
\bottomrule
\end{tabular}
\end{table}

从具体结果看，PlanGraph 在 GraphWiz 上提升最为明显，较 GCoder 提升 6.81 个百分点。这意味着在算法约束较强、路径搜索更复杂的任务中，规划反馈闭环能够较明显地减少直接生成带来的错误。PlanGraph 在 GraphArena 和 NLGraph 上也取得了稳定提升，说明本文方法在经典图算法和自然语言图问题上具备较强泛化能力。

在 LLM4DyG 上，PlanGraph 与最佳方法相差 0.24 个百分点，虽然略低于最优结果，但总体仍保持较高准确率。这一现象表明，动态时序信息对规划与程序实现提出了额外挑战，后续仍存在进一步优化空间。

进一步观察不同基线之间的差异可以发现，GPT-4o 直接推理在所有基准测试集上都明显落后于程序生成式和多智能体方法，说明图推理问题对外部结构化求解能力依赖较强。GraphTeam 与 GCoder 都已经展示出较高性能，而 PlanGraph 仍能在大多数数据集上进一步提升，说明仅有多智能体分工或代码生成能力还不够，规划、检索与验证三者之间的耦合方式同样重要。

\subsection{重复运行稳定性分析}

在总体性能对比基础上，本文进一步观察 PlanGraph 在重复运行中的稳定性，并结合表~\ref{tab:overall_result}中的结果差异说明方法的适用特征。

从提升幅度看，PlanGraph 的收益并非平均分布。在算法约束较强、可行性检查较明确的任务上，规划反馈闭环能够更充分地发挥作用；在任务结构较清晰的场景中，提升幅度相对平稳；而在动态图任务中，结果更接近最佳基线，说明时间依赖关系仍会限制规划表示和程序实现的精细程度。

结合失败样本看，错误主要集中在复杂时间条件、检索重排序偏差、组合搜索边界遗漏和严格输出格式四类情形。这些现象说明，进一步提升性能的关键不在于简单增加生成次数，而在于增强规划粒度、改进知识重排序和提高验证样例覆盖性。

除单次精确匹配率外，本文还观察 PlanGraph 在重复运行中的稳定性。稳定性分析主要关注三项指标：不同运行轮次之间的准确率波动范围、程序首次生成即通过验证的比例，以及进入修复循环后能够在限定轮数内收敛的比例。其结果如表~\ref{tab:stability_observation}所示。

\begin{table}[htbp]
\centering
\caption{重复运行中的稳定性观察}
\label{tab:stability_observation}
\begin{tabular}{lccc}
\toprule
数据集 & 准确率波动范围（百分点） & 首次通过率（\%） & 修复后收敛率（\%） \\
\midrule
GraphArena & $\pm0.7$ & 79.6 & 91.4 \\
NLGraph & \textbf{$\pm0.5$} & \textbf{82.3} & \textbf{93.1} \\
GraphWiz & $\pm0.9$ & 74.8 & 89.7 \\
\bottomrule
\end{tabular}
\end{table}

表~\ref{tab:stability_observation}显示，结构较清晰、标准算法映射较稳定的任务在三个指标上整体更优；约束更复杂的任务首次通过率略低，但经过反馈修复后仍能保持较高收敛水平。这说明 PlanGraph 的价值不仅体现在单次运行的精确匹配率上，也体现在多次运行时对结果波动的抑制能力上。

\section{分层结果分析}

\subsection{不同任务类别分析}

为了进一步分析 PlanGraph 的性能特征，本文将多个基准测试集中的任务按照求解目标划分为图结构分析、最短路径、匹配问题、流优化和哈密顿类问题五个类别，并统计不同方法在各类任务上的平均表现，如图~\ref{fig:category_accuracy_comparison}所示。

% [figure omitted: image content removed]
\caption{不同任务类别上的准确率对比}
\label{fig:category_accuracy_comparison}

由图~\ref{fig:category_accuracy_comparison}可见，PlanGraph 在图结构分析、最短路径、匹配问题和哈密顿类问题上均取得最优效果，尤其在哈密顿类问题上提升明显。这类任务通常需要显式的约束满足与路径构造，若直接由模型生成答案，很容易出现漏点、重复访问或路径代价计算错误；而 PlanGraph 通过规划与程序执行能够较好地规避这些问题。

在流优化任务上，PlanGraph 与最佳结果接近但未完全超过对比方法。本文分析认为，流网络任务往往涉及残量图、容量更新和边界条件等细节，若检索阶段未能覆盖足够精确的实现知识，程序生成质量仍可能受到影响。

不同任务类别间的性能差异，本质上反映了规划表达难度和程序验证难度的不同。对于图结构分析和最短路径问题，规划阶段往往能够非常明确地映射到标准算法步骤，验证阶段也较容易构造测试用例，因此整体准确率较高。对于匹配问题和哈密顿类问题，虽然搜索复杂，但其可行性约束比较清晰，程序化求解优势明显，因此 PlanGraph 相比直接推理方法表现更突出。

相比之下，流优化问题常常涉及隐式状态转移，例如残量网络更新、反向边容量处理以及多轮迭代终止条件等，这些过程在自然语言规划中的表达并不如路径类问题直观。因此，即便模型已经识别出这是最大流问题，在实现层面仍可能因细节遗漏而出现误差。

结合表~\ref{tab:overall_result}与图~\ref{fig:category_accuracy_comparison}可以进一步发现，PlanGraph 的优势具有明显的结构性。一方面，在算法约束更强、执行一致性要求更高的任务集合上，其提升更为集中，也更容易暴露端到端生成的短板。另一方面，在任务类别维度上，路径、匹配和哈密顿类任务的增益最为显著，说明规划和验证机制尤其适合处理需要显式可行性检查的问题。

此外，图~\ref{fig:category_accuracy_comparison}还揭示出一个现象：即便在 GPT-4o 直接推理表现已经不算太差的结构分析任务上，PlanGraph 仍然能够获得一定提升。这说明规划反馈范式的作用并不局限于难任务补救，它同样能够提升中等难度任务中的稳定性。

在总体结果基础上，本文进一步按任务结构维度分析性能差异，以揭示不同约束模式下方法收益的来源。对于以经典图算法为主的任务集合，PlanGraph 表现出较高适配性，说明基于规划反馈的方法能够较稳定地映射到标准算法流程，尤其在最大流、拓扑排序和组合优化类问题上，外部知识检索有助于模型稳定调用已有算法函数。对于强调指令理解与执行一致性的任务集合，PlanGraph 同样保持较高水平，说明所提框架不仅适用于给出图求结果的场景，也适用于按指令完成图操作的场景，其中，问题智能体对输出格式和约束条件的显式抽取是保证这类任务稳定性的关键。相比之下，动态图任务的主要难点在于图结构会随时间发生变化，系统不仅要构建图，还要处理时间窗口、事件顺序和动态约束。虽然 PlanGraph 已经能够借助规划与验证获得较高结果，但规划层对时间逻辑的表达仍相对粗粒度，因此后续仍可考虑进一步引入时序感知规划或动态图专用知识库。

为避免正文分析仅停留在平均准确率层面，本节进一步选取三个具有代表性的基准测试集，将部分逐任务结果放入正文。这样做的目的在于更清楚地展示：PlanGraph 的性能提升并不是均匀地撒在所有任务上，而是在若干关键图任务上表现出特别明显的优势。

\begin{table}[htbp]
\centering
\small
\caption{细粒度任务结果比较（\%）}
\label{tab:fine_grained_main}
\begin{tabular}{lcccc}
\toprule
任务 & GPT-4o & GraphTeam & GCoder & PlanGraph \\
\midrule
\multicolumn{5}{l}{\textit{GraphArena}} \\
MIS & 22.4 & 97.8 & 96.8 & \textbf{98.8} \\
MVC & 19.3 & 98.6 & 97.6 & \textbf{100.0} \\
MCP & 12.5 & 90.5 & 88.7 & \textbf{100.0} \\
TSP & 4.9 & 82.7 & 80.7 & \textbf{86.8} \\
\multicolumn{5}{l}{\textit{NLGraph}} \\
MF & 67.3 & 93.67 & 94.10 & \textbf{97.53} \\
TOPO & 60.5 & 91.20 & 92.80 & \textbf{94.80} \\
HP & 40.7 & \textbf{100.0} & \textbf{100.0} & \textbf{100.0} \\
GNN & 52.1 & 96.80 & \textbf{97.40} & \textbf{97.40} \\
\multicolumn{5}{l}{\textit{GraphWiz}} \\
CYC & 95.0 & \textbf{100.0} & \textbf{100.0} & \textbf{100.0} \\
CONN & 70.3 & 86.5 & 90.2 & \textbf{91.2} \\
BIP & 82.7 & 96.3 & 98.0 & \textbf{100.0} \\
SP & 78.6 & 95.0 & 96.4 & \textbf{98.5} \\
MF & 69.1 & 94.0 & 94.7 & \textbf{95.1} \\
HP & 15.4 & 32.5 & 40.2 & \textbf{99.2} \\
SM & 88.3 & 99.3 & \textbf{99.5} & 98.8 \\
\bottomrule
\end{tabular}
\end{table}

从表~\ref{tab:fine_grained_main}可以看到，PlanGraph 在最大独立集、最小点覆盖、最大团、最大流、最短路径和哈密顿路径等任务上都体现出了显著优势，尤其在 GraphWiz-HP 任务上提升极为明显。这些任务的共同点在于，它们都需要显式约束满足与程序化验证支持。如果仅依赖自然语言直出，模型很容易在路径完整性、最优性或格式要求上出现失误；而当规划与验证机制介入后，系统就能更稳定地把复杂任务压缩到可执行程序层面。

\subsection{NP-hard 与非 NP-hard 任务分析}

为同时考察任务复杂度、图规模、约束强度三个维度，本文在具有统一复杂度标注和规模分桶信息的代表性任务集合上开展分层分析\cite{tang2025grapharena}。在这一设定下，复杂度与图规模两个因素能够被较稳定地拆分出来，从而更清楚地观察规划、检索与验证机制在不同难度区间中的作用差异。

按照该任务集合中的公开任务定义，本文将连通性/可达性/最短距离等任务划为非 NP-hard 组，将最大独立集、最小点覆盖、最大团、最小割、旅行商等任务划为 NP-hard 组。图~\ref{fig:difficulty_scale_trend}展示了任务复杂度与样本难度两个视角下的分层趋势。可以看到，PlanGraph 在非 NP-hard 任务上已接近饱和，提升幅度有限；而在 NP-hard 任务上优势明显扩大，初步说明规划与验证闭环的收益主要体现在高组合复杂度场景。这与前文 TSP、MIS、MVC 等任务的观察一致。

\subsection{样本难度分层分析}

在同一分层设定下，样例还被进一步划分为简单、中等和困难三个难度区间。该划分以图规模为主要依据：简单样本对应节点数小于 10 的图实例，中等样本对应节点数为 10 至 20 的图实例，困难样本对应节点数大于 30 的图实例。图规模并不是图推理难度的唯一来源，但在多数图算法任务中，节点数量增加会显著放大搜索空间、结构关系和约束检查成本，因此适合作为本文观察难度变化的主要分层依据。

% [figure omitted: image content removed]
\caption{难度与规模分层下的性能趋势}
\label{fig:difficulty_scale_trend}

从图~\ref{fig:difficulty_scale_trend}可见，随着样本难度提高，不同方法的性能都出现下降，但 PlanGraph 的下降斜率更缓。尤其在困难样本上，优势进一步扩大，说明规划先行 + 执行验证对大搜索空间下的稳定性提升更明显。

综合复杂度分层与难度分层结果，可以得到更具解释力的结论：PlanGraph 的核心收益主要来自难任务增益，而非简单任务再抬高天花板。具体而言，非 NP-hard 和简单样本上方法间差距较小；当任务进入 NP-hard 或困难样本区间后，规划、检索与验证模块的协同作用开始显著放大。图~\ref{fig:difficulty_scale_trend}中逐步扩大的性能差距进一步支撑了本文方法定位：面向高约束图推理任务，优先追求可执行性与稳定性，而非单轮生成速度。

\section{机制验证与补充实验}

第四章已经从系统实现角度说明了规划、检索与验证之间的协作方式。本节不再重复系统流程，而是通过若干补充实验验证这些机制在实验层面是否确实带来了可观察收益。具体而言，本文依次比较不同检索查询方式的知识命中质量、关键参数组合的变化趋势、系统的工程开销以及输入扰动下的鲁棒性表现，以说明性能提升并非来自偶然调参，而是来自规划、检索与验证三类机制的共同作用。其中，检索质量相关实验也用于验证第三章提出的检索质量评估与纠偏筛选机制是否能够提高知识命中效果和后续编码可用性。

\subsection{检索质量验证}

为了更细致地验证规划模块对检索阶段的影响，本文进一步比较四种查询方式：直接使用原始问题文本进行检索、使用任务类型+关键词进行简化检索、使用规划伪代码进行检索，以及在规划伪代码基础上补充结构约束标签进行检索。实验基于五个基准测试集构造对应查询实例，统计 Hit@1、Hit@3、Hit@5 以及平均倒数排名（MRR）四项指标，结果如表~\ref{tab:retrieval_quality}所示。

\begin{table}[htbp]
\centering
\caption{不同检索查询方式的知识命中效果比较}
\label{tab:retrieval_quality}
\begin{tabular}{lcccc}
\toprule
查询方式 & Hit@1 & Hit@3 & Hit@5 & MRR \\
\midrule
Q1 原始问题文本 & 42.6\% & 61.8\% & 72.9\% & 51.4\% \\
Q2 任务类型 + 关键词 & 68.9\% & 84.7\% & 92.1\% & 76.3\% \\
Q3 规划伪代码 & 76.4\% & 90.8\% & 96.3\% & 83.5\% \\
Q4 规划伪代码 + 结构约束标签 & \textbf{82.1\%} & \textbf{94.2\%} & \textbf{98.0\%} & \textbf{88.4\%} \\
\bottomrule
\end{tabular}
\end{table}

从表~\ref{tab:retrieval_quality}可以看出，四种查询方式呈现出较为清晰的层次关系：直接使用原始问题文本的效果最弱；在显式加入任务语义后，Q2 的命中效果明显提升；进一步将问题压缩为规划伪代码后，Q3 在四项指标上继续改善；当查询中继续补充图类型、目标形式和关键约束等结构化标签时，Q4 的检索排序质量达到最好。这一结果并不是为了再次说明第四章中的检索流程，而是从实验上验证：随着查询表达逐步从自然语言描述转向结构化任务表示，检索模块确实能够更稳定地定位与求解过程相关的知识条目。

进一步看 MRR 指标可以发现，Q3 和 Q4 的提升不仅体现在正确知识是否被召回，还体现在正确知识能否更靠前地出现。这意味着规划步骤和约束标签不仅扩大了相关知识的召回范围，也有效改善了候选结果的排序质量。对于后续代码生成而言，较高的前位排序有助于减少编码阶段对错误 API 或不相关文档的尝试次数，从而降低修复成本，并为后续验证阶段提供更稳定的知识支撑；这也说明，基于检索质量评估的纠偏筛选能够在进入编码前提前过滤一部分低价值知识条目。

\subsection{参数敏感性分析}

为避免参数分析停留在模板求解器层面，本文进一步在完整 LLM 链路下重新运行代表性参数组合实验。实验选取约束明确且具有稳定难度分层的典型组合优化任务，重点比较简单样本与困难样本两个端点。这样设置的目的不是重新覆盖全部难度区间，而是观察检索返回条数和修复轮数变化时，系统在低结构复杂度与高结构复杂度场景中的响应差异。本文选择六组具有代表性的参数组合进行比较，即 $(1,0)$、$(3,1)$、$(5,3)$、$(7,3)$、$(5,4)$ 和 $(9,4)$。其中，$k$ 表示检索模块返回的候选知识条目数，$r$ 表示最大反馈修复轮数；所有样例均通过真实 LLM 代理完成规划、编码与修复，不过滤失败样例，并统一统计整体精确匹配率、难度分层精确匹配率、执行成功率、平均修复轮数与平均端到端耗时。

表~\ref{tab:param_main_result}给出了代表性参数组合的主结果。可以看到，默认配置 $(5,3)$ 并不是该任务上的最优折中点；在本组实验中，$(3,1)$ 取得最高整体准确率 74.17\%，同时平均耗时仅为 15.20 秒，较默认配置减少 3.20 秒。相比之下，$(1,0)$ 虽然成本最低，但在困难样本上下降明显；而进一步增大检索候选数与修复轮数后，准确率收益并未持续提升，反而出现上下文噪声与错误传播带来的波动。

\begin{table}[htbp]
\centering
\caption{不同参数组合下的总体性能比较（\%）}
\label{tab:param_main_result}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccc}
\toprule
$(k,r)$ & 总体 EM & 简单样本 EM & 困难样本 EM & 执行成功率 & 平均修复轮数 & 平均耗时(s) & $\Delta$EM vs $(5,3)$ & $\Delta$耗时(s) \\
\midrule
$(1,0)$ & 70.00 & \textbf{85.00} & 55.00 & 74.20 & \textbf{0.00} & \textbf{13.80} & +1.25 & -4.60 \\
$(3,1)$ & \textbf{74.17} & 82.50 & 63.75 & 80.80 & 0.36 & 15.20 & +5.42 & -3.20 \\
$(5,3)$ & 68.75 & 75.00 & 61.25 & 78.30 & 0.92 & 18.40 & 0.00 & 0.00 \\
$(7,3)$ & 73.75 & 80.00 & \textbf{66.25} & \textbf{81.70} & 0.88 & 17.60 & +5.00 & -0.80 \\
$(5,4)$ & 71.25 & 75.00 & 65.00 & 80.40 & 1.14 & 20.90 & +2.50 & +2.50 \\
$(9,4)$ & 71.25 & 77.50 & 63.75 & 79.20 & 1.20 & 19.70 & +2.50 & +1.30 \\
\bottomrule
\end{tabular}
}
\end{table}

从难度维度看，$r=0$ 时系统在简单样本上仍能保持较高准确率，但困难样本准确率仅为 55.00\%，说明困难实例更依赖反馈修复机制。$(7,3)$ 在困难子集上达到最高的 66.25\%，表明对高约束样本而言，适度增大检索预算并保留有限修复轮数仍然有益；但若继续把参数增大到 $(5,4)$ 或 $(9,4)$，则困难样本上的局部改善不足以抵消整体耗时上升。

综合表~\ref{tab:param_main_result}可以得到较清晰的结论。首先，$(1,0)$ 代表弱检索、无修复设置，此时简单样本仍然可解，但困难样本下降明显。其次，$(3,1)$ 提供了更平衡的知识量与修复深度，在整体准确率和效率上均优于默认设置，说明适中的 $k$ 与较小的 $r$ 对当前任务最为稳健。再次，$(5,3)$ 虽是系统默认配置，但在该任务上并非最优，表明增加上下文和修复轮数并不必然带来更好结果。最后，$(7,3)$、$(5,4)$ 和 $(9,4)$ 说明，当参数继续增大时，困难样本可能获得一定收益，但总体收益趋于饱和，且平均耗时明显上升。

因此，本文认为参数预算的收益具有明显任务依赖性。对于此类约束明确且难度分层清晰的组合优化任务，过大的检索候选数和过多的修复轮数会增加上下文噪声与错误传播风险；相较之下，适中的检索规模与少量反馈修复更有利于在准确率、执行成功率与工程开销之间取得平衡。

\subsection{工程开销分析}

为了说明 PlanGraph 的工程代价，本文统计了其在典型任务上的平均端到端推理耗时、平均代码生成轮数和平均验证次数。这里选取三类代表任务：最短路径、最大流和旅行商问题。需要说明的是，平均耗时会受到 API 响应、返回长度与验证轮次等因素影响，因此表~\ref{tab:efficiency}中的数值主要用于展示本系统在不同任务之间的相对开销差异。

\begin{table}[htbp]
\centering
\caption{不同任务上的平均推理开销}
\label{tab:efficiency}
\begin{tabular}{lccc}
\toprule
任务类型 & 平均耗时（s） & 平均生成轮数 & 平均验证次数 \\
\midrule
最短路径 & \textbf{10.8} & \textbf{1.1} & \textbf{1.3} \\
最大流 & 14.6 & 1.3 & 1.8 \\
旅行商问题 & 24.3 & 1.8 & 2.7 \\
\bottomrule
\end{tabular}
\end{table}

从表~\ref{tab:efficiency}可见，不同任务的工程开销存在明显差异。最短路径问题结构清晰、算法成熟，因此规划、检索和验证都较为顺畅；最大流任务由于涉及容量约束和残量网络，平均验证次数有所增加；旅行商问题则需要显式处理组合搜索与可行性判断，因此耗时和验证次数最高。这与前文的性能分析是一致的，即任务越依赖复杂约束满足，规划反馈框架越能发挥优势，但相应地也会付出更高的推理成本。

然而，这一额外开销并非单纯的系统负担。对于组合优化问题，如果缺乏验证环节，系统虽然可以更快给出答案，但错误率通常会显著升高；而加入验证后，即便存在更多程序执行步骤，整体输出质量和可信度却显著提升。就本文研究目标而言，本文更强调可靠地完成图推理，而非追求最低时延响应，因此这种成本换准确率的设计选择是合理的。

\subsection{鲁棒性分析}

除标准基准测试集外，本文还在输入扰动设置下进一步考察 PlanGraph 的表现，以分析框架对问题表述变化的稳定性。该实验覆盖五个基准测试集，并构造了三种常见扰动：节点顺序随机打乱、边列表描述改写、输出要求从自然语言答案改为结构化列表。在相同求解任务下比较准确率变化，结果如表~\ref{tab:robustness}所示。

\begin{table}[htbp]
\centering
\caption{输入扰动条件下的鲁棒性分析（\%）}
\label{tab:robustness}
\begin{tabular}{lccc}
\toprule
扰动类型 & GPT-4o & GraphTeam & PlanGraph \\
\midrule
节点顺序打乱 & 51.6 & 92.4 & \textbf{96.8} \\
边描述改写 & 48.9 & 91.1 & \textbf{95.7} \\
输出格式切换 & 44.3 & 89.8 & \textbf{94.9} \\
\bottomrule
\end{tabular}
\end{table}

表~\ref{tab:robustness}说明，PlanGraph 在输入扰动下仍然保持较高准确率。本文认为其原因在于：问题智能体首先将自然语言输入规整为结构化表示，减少了不同表述形式对后续规划的影响；同时，程序执行结果在最终答案生成前还会经过格式化处理，因此输出形式变化对系统影响相对有限。相比之下，直接推理方法更容易受到表面措辞差异的干扰。

综合检索质量、参数变化、工程开销与鲁棒性结果可以得到一个更明确的中间结论：PlanGraph 的收益不是单一模块偶然奏效，而是由规划约束、知识匹配和执行反馈共同支撑的。为进一步说明这些模块的必要性，并补充对方法适用边界的理解，下面继续从消融、案例和误差三个层面展开分析。

\section{模块贡献与典型结果分析}

\subsection{模块贡献分析}

本文设计了三种消融变体：（1）\textbf{去除规划模块}：直接根据原始问题生成代码；（2）\textbf{去除检索模块}：不再使用规划引导检索，仅依赖模型内部知识生成程序；（3）\textbf{去除验证模块}：移除程序执行验证与反馈推理闭环，仅保留一次性代码生成。

图~\ref{fig:ablation_result_visual}给出了在三个代表性数据集上的消融结果，展示了不同模块移除后的性能变化。

% [figure omitted: image content removed]
\caption{关键模块消融实验结果}
\label{fig:ablation_result_visual}

从图~\ref{fig:ablation_result_visual}可以看出，去除规划模块后，三个数据集上的性能均出现最明显下降。这说明规划模块在整套框架中起到了核心作用。没有显式伪代码约束时，模型需要直接从自然语言任务描述生成程序，往往难以稳定识别算法意图，也更容易忽略边权、方向或输出格式等细节。

去除验证模块后，系统性能也出现了较大下降，尤其在 GraphWiz 上从 97.01\% 降至 90.72\%。这表明程序执行反馈对于纠正代码错误非常重要。即使规划与检索都较为合理，编码阶段仍可能出现参数名错误、函数选型偏差和边界条件遗漏；若没有执行闭环，这些问题将直接影响最终答案。

检索模块带来的性能提升相对温和，但依然稳定。本文认为，规划模块解决的是任务目标与求解方向的问题，检索模块解决的是实现依据是否充分的问题，验证模块则负责检查结果是否满足要求。三者共同构成了 PlanGraph 的完整求解闭环。

\subsection{消融结果讨论}

从三个消融变体的结果还可以得到一个更细致的观察：规划模块的作用不仅体现在准确率提升上，还体现在为检索模块和验证模块提供稳定的中间锚点。当规划模块被移除后，检索失去高质量查询、验证失去明确的目标约束，整个系统会退化为围绕原始问题反复生成和修补代码的模式，导致错误类型显著增加。

与此同时，检索模块虽然在数值上带来的提升略小于规划模块和验证模块，但它对跨任务泛化尤其重要。因为在一些并非高频出现的图任务中，模型内部知识并不足以保证函数调用准确，而规划引导检索可以为程序生成提供更可信的实现依据。

图~\ref{fig:ablation_result_visual}也从数值变化上直观反映了这一点：去掉规划模块后，三个基准测试集都出现了最明显下降，说明规划模块具有稳定贡献；去掉检索模块和验证模块后，性能虽然下降幅度略小，但仍明显低于完整模型。这说明这两个模块并非可有可无的附加组件，而是会实际影响系统最终性能的组成部分。由此可以看到，第五章前面观察到的总体增益和分层收益，并不是某个单点技巧带来的偶然提升，而是完整求解闭环共同作用的结果。

\subsection{典型案例分析}

为了更全面地展示 PlanGraph 的求解特点，本文除旅行商问题外，进一步选取最短路径和动态图查询两个代表性场景进行补充分析。与第四章不同，本节不再展开系统流程本身，而是关注这些案例能否为实验结果提供更直观的解释。

在最短路径任务中，输入通常包含起点、终点以及带权图结构。对于这类问题，直接推理方法的一个常见错误是把路径可达性判断和最短代价计算混为一谈，或者遗漏边权而仅依据边数判断路径长度。实验中，PlanGraph 在这类样例上的优势主要来自两点：其一，规划结果会显式区分构建带权图、选择最短路径算法和同时输出路径与总代价等关键动作；其二，验证阶段能够及时检查边权是否被正确纳入计算。因此，在标准图算法场景下，规划结果与外部 API 的语义匹配度较高，系统也更容易稳定获得正确结果。

在动态图查询任务中，输入除图结构外还包含时间戳、事件顺序或时间窗口等约束。对于这类问题，直接推理方法容易忽略先过滤时间、再执行图搜索的顺序要求，从而得到看似可执行但并不满足时序条件的答案。实验观察表明，PlanGraph 在这类任务上的优势主要体现在：规划会显式保留先处理时间、再处理图结构的顺序信息，检索能够据此返回更贴近时序场景的知识条目，而验证阶段则可通过边界样例检查程序是否错误地忽略时间条件。

尽管当前框架在这类问题上仍有提升空间，但验证闭环已经能够显著减少程序能运行却忽略时间约束的情况。

为了更直观地说明 PlanGraph 的工作过程，本文选取 GraphArena 中一个旅行商问题样例进行分析。该样例给定一个五节点带权无向图，要求从节点 A 出发，访问所有节点恰好一次并返回起点，同时使路径总代价最小。

% [figure omitted: image content removed]
\caption{案例求解流程图}
\label{fig:tsp_case_pipeline}

常见错误主要包括：（1）未访问全部节点，生成的路径并非哈密顿回路；（2）节点出现重复访问，违反每个节点只访问一次的约束；（3）虽然路径形式正确，但代价计算错误；（4）混淆无向边和有向边，导致路径不可达。

这些错误的根本原因在于，模型很难在一次生成中同时兼顾图构建、约束检查、路径枚举和最优性判定。

其求解意图可以概括为：（1）构建带权无向图；（2）固定起点 A；（3）枚举满足哈密顿回路约束的候选路径；（4）计算每条路径总代价；（5）选择总代价最小的回路并格式化输出。

在此基础上，系统会围绕路径搜索、组合遍历和图构建等关键点补充相应知识，并通过测试样例检查以下条件：是否恰好访问全部节点、是否回到起点、是否按权重正确计算代价、输出格式是否符合要求。

若程序在某次生成中遗漏了返回起点的约束，验证阶段便可在测试中及时发现这一问题，并推动后续修正。最终，系统输出如下最优路径：

\begin{equation}
A \rightarrow B \rightarrow E \rightarrow D \rightarrow C \rightarrow A
\end{equation}

其总代价为 14。该案例说明，通过规划先行和执行验证，PlanGraph 能够将复杂的组合优化问题转化为更稳定的程序求解过程。

本节三个案例共同说明：PlanGraph 的优势并非来自简单增加生成轮数，而是来自中间规划、知识补充和验证约束在具体样例中的协同作用。对于路径类问题，规划有助于明确优化目标；对于组合优化问题，规划有助于显式表达可行性约束；对于动态图问题，规划有助于保留先处理时间再处理拓扑的执行顺序。这些案例为前文的总体结果提供了更具可解释性的实例支撑。

\subsection{误差分析与讨论}

除准确率提升外，误差分析有助于识别方法边界并指导后续改进。本节从错误类型、成因与系统性改进方向展开讨论。

综合实验现象，主要错误可归纳为四类：（1）\textbf{规划粒度不足。} 对某些动态图或特殊约束问题，伪代码计划仍然过于粗糙，无法完全覆盖实现细节；（2）\textbf{检索结果不够精确。} 当多个 API 语义相近时，检索模块可能返回功能类似但约束不同的函数说明；（3）\textbf{测试样例代表性不足。} 若验证样例未覆盖关键边界情况，程序可能在测试中通过，但在目标样例上失效；（4）\textbf{复杂搜索开销较大。} 对于某些 NP-hard 任务，程序虽能保证正确性，但推理和执行成本较高。

\begin{table}[htbp]
\centering
\small
\caption{失败样本的典型错误类型归纳}
\label{tab:error_taxonomy}
\begin{tabular}{m{3cm}m{4.5cm}m{5cm}}
\toprule
错误类型 & 具体表现 & 主要影响阶段 \\
\midrule
任务识别偏差 & 将判定任务误识别为优化任务，或混淆路径搜索与可达性判断 & 规划阶段 \\
约束遗漏 & 忽略固定起点、回路闭合、时间窗口或容量限制 & 规划/编码阶段 \\
API 误用 & 选择语义相近但并不匹配的函数，或参数使用错误 & 检索/编码阶段 \\
边界情况失效 & 在小样例上通过，但在目标图上因特殊结构而失败 & 验证阶段 \\
输出格式错误 & 路径顺序、集合表示或文本格式不符合官方脚本要求 & 答案生成阶段 \\
\bottomrule
\end{tabular}
\end{table}

表~\ref{tab:error_taxonomy}从实验结果角度总结了失败样本的主要来源。可以发现，错误并不只集中在代码实现阶段，而是可能在规划、检索、验证和格式化等多个阶段累积出现。这说明图推理并非单一子模块即可解决的问题，而是一个需要中间表示、知识支持与执行约束共同配合的系统性任务。

结合前文总体结果、案例分析与扰动实验，可以进一步得到两点认识。第一，PlanGraph 的主要瓶颈并不在于模型完全不会做，而更多体现在规划粒度不足、检索重排序不够精确以及验证样例覆盖有限等方面；第二，这些误差恰好说明本文方法的后续优化方向应集中在中间表示和约束检查质量上，而不是简单增加生成次数。

总体来看，PlanGraph 在高约束图任务上已经展现出较强稳定性，但面对动态图、复杂时序逻辑和长尾组合搜索时仍有改进空间。后续可以从时序感知规划、失败反馈驱动的知识重排序以及更具代表性的验证样例构造等方面继续完善，以提升方法在更复杂场景下的适用性。

\section{本章小结}

本章围绕实验设计与设置、总体实验结果与稳定性分析、分层结果分析、机制验证与补充实验，以及模块贡献与典型结果分析，对 PlanGraph 的有效性进行了系统验证。从实验结果来看，所提方法在多数图推理基准测试集上都取得了具有竞争力的表现，尤其在高约束、强组合性的图任务中优势更加明显。进一步的参数、效率、鲁棒性与消融分析也显示，规划、检索和验证模块之间的协同闭环是性能提升的重要来源；案例与误差分析则进一步揭示了方法的适用边界及后续改进方向。整体而言，第五章的实验结论为本文方法的有效性与可解释性提供了较为充分的实证支撑。
```

---

## chapters/chapter6.tex

```latex
\chapter{总结与展望}
\label{chp:conclusion}

\section{论文总结}

图推理任务要求模型同时完成结构理解、约束满足、算法选择和结果表达等多个环节，对大语言模型的综合求解能力提出了较高要求。现有方法虽然已经在部分图任务上展现出一定效果，但仍普遍存在端到端推理链条过长、知识调用缺乏中间组织以及程序生成结果不稳定等问题，导致模型在复杂图任务、强约束任务和动态图任务中容易出现理解偏差、实现错误或格式失配。围绕上述问题，本文提出了一种基于规划反馈的图推理多智能体协同求解框架 PlanGraph，通过在问题理解与程序执行之间引入显式伪代码规划，并利用执行反馈对程序实现、知识调用与规划结果进行反向修正，将规划、检索、编码、验证和修复等环节组织为一个相互衔接的求解闭环。在本文所采用的图推理设定与实验条件下，这一框架能够提升复杂图推理任务中的求解稳定性、可验证性与过程可解释性。

本文围绕所提方法开展了较为系统的研究，主要工作和研究结论如下。

（1）针对大语言模型在图推理任务中的主要困难进行了系统分析。本文从任务特性出发，梳理了图推理问题在结构表示、约束建模、算法映射和程序执行等方面的特殊性，指出图任务并不仅仅是一般文本推理的简单延伸，而是一类同时依赖结构化理解和可执行求解的复杂任务。进一步地，本文总结出当前大语言模型在该类任务中面临的两类关键瓶颈：一类来自端到端直接生成时推理负担过重、外部知识调用缺乏结构化引导、程序生成与调试过程稳定性不足；另一类来自对历史经验样本、样例库检索或专门适配过程的较强依赖，这会带来较高的构建成本，并限制跨任务迁移时的泛化表现。这一分析为后续方法设计提供了明确的问题导向，也说明了仅依赖更大参数规模或更重的经验积累并不足以从根本上解决图推理中的可靠性问题。

（2）设计并实现了基于规划反馈的多智能体图推理框架 PlanGraph。本文围绕图推理任务的求解流程，构建了问题智能体、规划智能体、检索智能体、编码智能体和推理智能体等功能角色，使系统能够按照理解问题、生成规划、调用知识、生成程序、执行验证和反馈修正的顺序逐步完成求解。与传统的端到端答案生成方式相比，该框架将原本隐含在模型内部的一次性推理过程显式拆解为若干相互协同的中间阶段，并使规划在前向方向上约束知识调用与程序生成，执行反馈在反向方向上修正实现偏差和约束遗漏。这种组织方式使各模块具有更清晰的职责边界，也使系统整体更便于分析、调试和扩展。结合第五章的实验结果与案例分析，规划反馈协同机制在复杂图任务中确实有助于减少错误传播。

（3）提出了基于伪代码规划的知识检索机制。为了缓解大语言模型在图算法调用和 API 选择上的不稳定性，本文没有直接使用原始问题文本进行知识检索，而是利用规划阶段生成的伪代码步骤作为中间查询表示，使检索内容更贴近算法流程与实现意图。与直接检索相比，这种方式能够更准确地定位图构建、路径搜索、匹配求解、流网络处理以及约束检查等相关知识；在此基础上，引入检索质量评估与纠偏筛选后，候选知识在进入编码阶段前还可以进一步完成相关性检查与补充检索。第五章的检索实验结果显示，在本文设定下，规划引导检索在知识命中率和排序质量等指标上均优于其他查询方式，中间规划对知识调用质量的改善是比较明确的。

（4）构建了程序执行验证与反馈推理闭环。针对图推理任务中程序表面上能够运行但结果并不满足任务要求的常见问题，本文在程序生成之后引入执行验证环节，通过测试样例、约束检查和格式校验对候选程序进行自动评估；当发现错误时，再将异常信息反馈给推理智能体进行局部修正或重新生成。该机制使系统不仅能够输出程序，还能够对程序是否真正满足任务目标进行二次确认。第五章的消融与案例分析显示，验证与推理模块对整体性能提升具有稳定贡献，尤其在路径搜索、组合优化和强约束图任务中作用更为明显。对图推理这类可程序化求解的问题来说，执行反馈能够为系统提供更可信的纠错依据。

（5）在多个公开图推理基准测试集上对所提方法进行了系统实验评估。本文在 GraphArena、NLGraph、GraphWiz、LLM4DyG 和 GraphInstruct 等数据集上对 PlanGraph 进行了实验验证，并从总体结果、稳定性、任务类别、复杂度分层、参数敏感性、工程开销、鲁棒性、消融实验和案例分析等多个角度展开了分析。根据第五章的实验结果，在本文设定下，PlanGraph 在多数基准测试集上都取得了具有竞争力的表现；尤其在组合优化、路径搜索和结构约束较强的任务中，整体优势更稳定。与此同时，规划、检索与验证三者之间的协同闭环，是性能提升和稳定性增强的重要来源。实验中的失效样例也提示我们，PlanGraph 在动态图场景下仍有进一步优化空间。

综合全文可以看出，对于图推理任务，大语言模型能否实现稳定可靠求解，关键并不只在于生成更长的自然语言推理链，而在于构建符合任务本质的系统化求解流程。本文提出的 PlanGraph 将规划生成、知识调用与执行验证组织为带反馈回流的求解链路，为大语言模型处理图结构任务提供了一条更容易分析、扩展和落地的实现路径。

\section{论文展望}

本文的工作主要建立在公开图推理基准测试集和通用图算法工具之上，已经能够支撑对规划反馈协同求解有效性的判断。后续研究可从以下几个方面进一步展开。

（1）继续增强规划表示对复杂图任务的表达能力。当前 PlanGraph 的规划模块已经能够较好支持经典图算法和部分动态图任务，但对复杂时间依赖、动态图演化过程以及异构节点和边类型之间关系的表达仍然偏粗粒度。下一步更关键的，不是单纯拉长规划文本，而是让它更准确地表示时间顺序、约束来源、状态变化以及多类型关系之间的交互逻辑。

（2）继续扩展外部知识来源，并改进检索选择机制。本文当前使用的知识主要来自图计算文档和相关 API 说明，这已经能够支撑多数实验任务；但面对更复杂、更开放的真实问题时，知识来源仍然偏窄。后续可以把算法教材、经典代码仓库、高质量技术问答以及专用图推理工具文档逐步纳入统一知识库，同时配合重排序、工具选择和多路检索融合策略，提升系统在不同任务下调用外部知识的准确性。

（3）进一步系统化程序验证机制。本文目前采用的小样例执行验证与错误修复机制已经能够发现相当一部分实现问题，但在边界条件覆盖、约束完备性和形式化正确性方面还有明显提升空间。后续如果能够把自动测试生成、约束求解、静态分析等方法引入进来，验证环节就不会只停留在样例检查，而会更接近真正的可信性保障。

（4）推动方法面向真实图应用场景落地。本文的实验主要建立在公开基准测试集基础之上，这足以验证方法本身是否成立，但和真实应用之间还有距离。知识图谱问答、软件依赖分析、社交关系推断、网络运维诊断以及复杂流程优化等任务，都更接近 PlanGraph 未来可能面对的使用场景。把系统放到这些场景里，才能进一步看清它在开放输入、长链约束和多工具协同条件下的真实表现。

（5）探索多模型、多工具协同的混合求解方式。随着大语言模型、图神经网络、外部求解器和程序分析工具持续发展，图推理系统很可能不会长期依赖单一模型完成全部任务。更自然的演化方向是：让语言模型负责任务理解与规划，让专用图模型负责结构表征，让外部求解器承担精确计算与验证。这种分工可能在不显著增加系统复杂度的前提下，提高高约束图任务中的求解可靠性。

总体来看，规划反馈协同求解在图推理任务上还有不少可以继续深入的空间。随着大语言模型能力提升、图工具生态完善以及验证方法逐步成熟，围绕结构化规划、知识调用、程序执行和结果验证的结合方式，仍会是这一方向里最值得继续打磨的部分。
```

---

## chapters/appendix.tex

```latex
\appendix

\chapter{详细实验结果}
\label{appendix:detailed_results}

为与正文中的平均精确匹配率结果相对应，本附录进一步给出各基准测试集的逐任务精确匹配率统计，并结合数据集特点对结果差异进行补充分析。整体组织遵循数据集介绍段—逐任务结果表—结果分析段的结构，以便将正文中的平均结果展开到更细粒度的任务层面，从而更完整地展示 PlanGraph 在不同图推理场景中的表现。

\section{GraphArena 逐任务结果}

GraphArena 是面向图计算与图推理任务的综合基准测试集，覆盖连通性、距离计算、独立集、点覆盖、团、割以及旅行商等多种经典问题，其中既包含基础结构判断任务，也包含约束显式、搜索空间较大的组合优化任务\cite{tang2025grapharena}。这类数据集的特点在于任务跨度较大，能够较好地区分基础图结构识别能力和高约束图求解能力两类水平。表~\ref{tab:appendix_grapharena}给出了各方法在该基准测试集各子任务上的逐项结果。

\begin{table}[H]
\centering
\caption{GraphArena 各任务精确匹配率（\%）}
\label{tab:appendix_grapharena}
\begin{tabular}{lcccc}
\toprule
任务 & GPT-4o & GraphTeam & GCoder & PlanGraph \\
\midrule
CN & 100.0 & 100.0 & 100.0 & 100.0 \\
CC & 100.0 & 100.0 & 100.0 & 100.0 \\
SD & 100.0 & 100.0 & 100.0 & 100.0 \\
GD & 100.0 & 100.0 & 100.0 & 100.0 \\
MIS & 22.4 & 97.8 & 96.8 & 98.8 \\
MVC & 19.3 & 98.6 & 97.6 & 100.0 \\
MCP & 12.5 & 90.5 & 88.7 & 100.0 \\
MCS & 8.4 & 90.8 & 89.4 & 95.3 \\
TSP & 4.9 & 82.7 & 80.7 & 86.8 \\
\bottomrule
\end{tabular}
\end{table}

从表~\ref{tab:appendix_grapharena}可以看出，GraphArena 中的基础结构任务对各强基线均已较为容易，CN、CC、SD 和 GD 等子任务几乎都达到满分；真正拉开差距的是 MIS、MVC、MCP、MCS 和 TSP 等组合优化问题。PlanGraph 在这些高约束任务上仍保持更优结果，说明规划生成、知识检索和执行验证的闭环机制并不是简单提升简单题的天花板，而是更有效地改善了复杂图搜索任务中的可行性控制与错误修复能力。

\section{NLGraph 逐任务结果}

NLGraph 主要考察自然语言条件下的图算法推理能力，其核心难点并不只在于调用某个图算法，而在于先从自然语言描述中恢复图结构、任务目标和求解约束，再完成相应的算法推理\cite{chen2024nlgraph}。因此，该基准测试集对任务语义解析和算法意图识别提出了更高要求。表~\ref{tab:appendix_nlgraph}给出了各方法在 NLGraph 各子任务上的逐项结果。

\begin{table}[H]
\centering
\caption{NLGraph 各任务精确匹配率（\%）}
\label{tab:appendix_nlgraph}
\begin{tabular}{lcccc}
\toprule
任务 & GPT-4o & GraphTeam & GCoder & PlanGraph \\
\midrule
CONN & 92.10 & 100.0 & 100.0 & 100.0 \\
MF & 67.30 & 93.67 & 94.10 & 97.53 \\
CYC & 95.80 & 100.0 & 100.0 & 100.0 \\
TOPO & 60.50 & 91.20 & 92.80 & 94.80 \\
SP & 72.40 & 100.0 & 100.0 & 100.0 \\
BM & 81.30 & 100.0 & 100.0 & 100.0 \\
HP & 40.70 & 100.0 & 100.0 & 100.0 \\
GNN & 52.10 & 96.80 & 97.40 & 97.40 \\
\bottomrule
\end{tabular}
\end{table}

在 NLGraph 上，PlanGraph 对最大流和拓扑排序这类需要算法步骤清晰展开的任务提升更为明显，而在连通性、最短路径、二分匹配和哈密顿路径等已被现有方法较好解决的任务上也至少保持同等水平。结合数据集特点可以看出，PlanGraph 的优势主要体现在把自然语言问题稳定映射到可执行图求解过程这一环节上，即先通过规划抽取任务结构，再利用程序验证约束答案形式，从而降低因语义歧义或步骤遗漏带来的错误。

\section{GraphWiz 逐任务结果}

GraphWiz 是面向指令式图推理场景构建的基准测试集，强调模型在给定图操作指令或求解要求时，能否稳定完成从任务理解到结果生成的全过程\cite{gong2024graphwiz}。与更偏结构问答的数据集相比，GraphWiz 更突出流程化求解和输出一致性，因此较适合观察规划与程序执行机制在复杂任务上的作用。表~\ref{tab:appendix_graphwiz}给出了各方法在该基准测试集各子任务上的逐项结果。

\begin{table}[H]
\centering
\caption{GraphWiz 各任务精确匹配率（\%）}
\label{tab:appendix_graphwiz}
\begin{tabular}{lcccc}
\toprule
任务 & GPT-4o & GraphTeam & GCoder & PlanGraph \\
\midrule
CYC & 95.00 & 100.0 & 100.0 & 100.0 \\
CONN & 70.30 & 86.50 & 90.20 & 91.20 \\
BIP & 82.70 & 96.30 & 98.00 & 100.0 \\
TOPO & 75.20 & 100.0 & 100.0 & 96.50 \\
SP & 78.60 & 95.00 & 96.40 & 98.50 \\
MTS & 71.80 & 94.00 & 95.10 & 93.80 \\
MF & 69.10 & 94.00 & 94.70 & 95.10 \\
HP & 15.40 & 32.50 & 40.20 & 99.20 \\
SM & 88.30 & 99.30 & 99.50 & 98.80 \\
\bottomrule
\end{tabular}
\end{table}

GraphWiz 中最值得关注的是 HP 任务，其对路径约束满足要求极高。PlanGraph 在该任务上远超对比方法，说明显式规划与程序验证对哈密顿路径类问题尤为有效。与此同时，在 CONN、SP 和 MF 等需要稳定图构建与步骤执行的任务上，PlanGraph 也保持了较强竞争力；只有在 TOPO、MTS 和 SM 等少数任务上未取得最优。这说明该方法的主要收益仍集中在约束敏感且容易因一步出错而整体失效的任务类型上。

\section{LLM4DyG 逐任务结果}

LLM4DyG 聚焦动态图与时间约束场景，任务通常要求模型同时处理图结构变化、时间顺序以及事件依赖关系，因此比静态图基准测试集更强调时序建模与动态状态更新\cite{llm4dyg2024}。这类任务能够较好地检验规划反馈方法在复杂状态演化条件下的适用性。表~\ref{tab:appendix_llm4dyg}给出了各方法在 LLM4DyG 各子任务上的逐项结果。

\begin{table}[H]
\centering
\small
\caption{LLM4DyG 各任务精确匹配率（\%）}
\label{tab:appendix_llm4dyg}
\begin{tabular}{lccccc}
\toprule
任务 & GPT-4o & LLM4DyG & GraphTeam & GCoder & PlanGraph \\
\midrule
WL & 58.00 & 47.30 & 96.33 & 94.33 & 98.67 \\
WC & 67.33 & 64.10 & 94.33 & 94.78 & 93.56 \\
WTC & 87.67 & 63.00 & 100.00 & 97.08 & 100.00 \\
NT & 33.33 & 45.90 & 95.33 & 94.74 & 97.47 \\
NP & 44.67 & 20.00 & 100.00 & 94.83 & 100.00 \\
CTC & 77.33 & 66.70 & 99.67 & 100.00 & 99.33 \\
CTP & 57.67 & 59.80 & 87.00 & 100.00 & 92.03 \\
FTP & 46.67 & 80.80 & 81.00 & 74.58 & 84.57 \\
SE & 49.67 & 35.80 & 99.67 & 93.67 & 99.33 \\
\bottomrule
\end{tabular}
\end{table}

可以看到，PlanGraph 在 WL、NT、NP 和 SE 等任务上优势明显，但在 WC、CTC 与 CTP 等部分任务上仍未全面超过最优对比方法。这一现象说明动态图问题内部也存在明显异质性：当任务更依赖图结构约束与过程验证时，规划反馈闭环的收益更突出；而当任务需要更细粒度的时间建模或连续状态跟踪时，当前方法仍有进一步优化空间。这一结果也与正文中对 LLM4DyG 整体表现的分析保持一致。

\section{GraphInstruct 逐任务结果}

GraphInstruct 面向图指令跟随场景，强调模型能否根据任务指令稳定完成邻居查询、边判断、连通性分析、遍历与拓扑排序等基础图操作\cite{graphinstruct2024}。与以复杂组合优化为主的数据集相比，该基准测试集更强调指令理解、输出格式一致性以及基础图操作的稳健性。表~\ref{tab:appendix_graphinstruct}给出了各方法在该基准测试集各子任务上的逐项结果。

\begin{table}[H]
\centering
\small
\caption{GraphInstruct 各任务精确匹配率（\%）}
\label{tab:appendix_graphinstruct}
\begin{tabular}{lccccc}
\toprule
任务 & GPT-4o & GraphInstruct & GraphTeam & GCoder & PlanGraph \\
\midrule
NB & 98.00 & 99.00 & 100.00 & 99.53 & 100.00 \\
BIP & 89.67 & 85.00 & 99.00 & 100.00 & 100.00 \\
EDGE & 90.67 & 84.00 & 99.33 & 97.47 & 98.63 \\
CONN & 92.22 & 83.00 & 100.00 & 100.00 & 100.00 \\
DEG & 98.00 & 81.00 & 100.00 & 98.67 & 100.00 \\
DFS & 89.33 & 46.00 & 95.67 & 94.33 & 96.33 \\
PRED & 47.41 & 41.00 & 98.00 & 99.75 & 99.75 \\
TOPO & 59.00 & 33.00 & 98.33 & 99.50 & 99.25 \\
CC & 39.30 & 83.00 & 94.67 & 83.30 & 94.74 \\
\bottomrule
\end{tabular}
\end{table}

GraphInstruct 主要考察图指令执行能力。PlanGraph 在大多数任务上与最优方法持平或更优，尤其在 NB、BIP、CONN、DEG 和 DFS 等任务上表现稳定，说明所提框架不仅能处理复杂求解型任务，也能处理相对基础但格式要求极严的图查询任务。与此同时，TOPO 和 CC 等任务上仍存在与最优方法的轻微差距，这表明在面向高规范性输出的基础图指令场景中，后续仍可围绕输出约束建模与轻量验证策略继续改进。
```

---

## reference.bib

```bibtex
@book{cormen2009clrs,
  author = {Cormen, Thomas H. and Leiserson, Charles E. and Rivest, Ronald L. and Stein, Clifford},
  title = {Introduction to Algorithms},
  publisher = {MIT Press},
  year = {2009},
  edition = {3rd}
}

@book{diestel2017graph,
  author = {Diestel, Reinhard},
  title = {Graph Theory},
  publisher = {Springer},
  year = {2017},
  edition = {5th}
}

@book{korte2018combinatorial,
  author = {Korte, Bernhard and Vygen, Jens},
  title = {Combinatorial Optimization: Theory and Algorithms},
  publisher = {Springer},
  year = {2018},
  edition = {6th}
}

@inproceedings{hagberg2008networkx,
  author = {Hagberg, Aric A. and Schult, Daniel A. and Swart, Pieter J.},
  title = {Exploring Network Structure, Dynamics, and Function Using NetworkX},
  booktitle = {Proceedings of the 7th Python in Science Conference},
  pages = {11--15},
  year = {2008}
}

@inproceedings{wei2022chain,
  author = {Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Ichter, Brian and Xia, Fei and Chi, Ed and Le, Quoc and Zhou, Denny},
  title = {Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2022}
}

@inproceedings{wang2023selfconsistency,
  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2023}
}

@inproceedings{yao2023tree,
  author = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas and Cao, Yuan and Narasimhan, Karthik},
  title = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@inproceedings{besta2024graph,
  author = {Besta, Maciej and Blach, Nils and Kubicek, Ales and Gerstenberger, Robert and Podstawski, Marcin and Gianinazzi, Lukas and Gajda, Joanna and Lehmann, Tomasz and Niewiadomski, Hubert and Nyczyk, Piotr and Hoefler, Torsten},
  title = {Graph of Thoughts: Solving Elaborate Problems with Large Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@inproceedings{zhou2023least,
  author = {Zhou, Denny and Sch{\"a}rli, Nathanael and Hou, Le and Wei, Jason and Scales, Nathan and Wang, Xuezhi and Schuurmans, Dale and Cui, Claire and Bousquet, Olivier and Le, Quoc and Chi, Ed},
  title = {Least-to-Most Prompting Enables Complex Reasoning in Large Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2023}
}

@inproceedings{gao2023pal,
  author = {Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Yang, Pengfei and Callan, Jamie and Neubig, Graham},
  title = {PAL: Program-aided Language Models},
  booktitle = {International Conference on Machine Learning},
  year = {2023}
}

@inproceedings{schick2023toolformer,
  author = {Schick, Timo and Dwivedi-Yu, Jane and Dessi, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  title = {Toolformer: Language Models Can Teach Themselves to Use Tools},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@inproceedings{qin2023toolllm,
  author = {Qin, Yujia and Ye, Yining and Fang, Lei and Zhang, Haoyu and Chen, Xiaoyang and Yang, Jinghua and Hu, Songfang and Tian, Xiangrong and Xu, Peng and Li, Shizhe and Su, Huan},
  title = {ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@inproceedings{chen2024nlgraph,
  author = {Wang, Heng and Feng, Shangbin and He, Tianxing and Tan, Zhaoxuan and Han, Xiaochuang and Tsvetkov, Yulia},
  title = {Can Language Models Solve Graph Problems in Natural Language?},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@inproceedings{gong2024graphwiz,
  author = {Chen, Nuo and Li, Yuhan and Tang, Jianheng and Li, Jia},
  title = {GraphWiz: An Instruction-Following Language Model for Graph Computational Problems},
  booktitle = {Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  year = {2024},
  pages = {353--364},
  doi = {10.1145/3637528.3672010}
}

@inproceedings{tang2025grapharena,
  author = {Tang, Jianheng and Zhang, Qifan and Li, Yuhan and Chen, Nuo and Li, Jia},
  title = {GraphArena: Evaluating and Exploring Large Language Models on Graph Computation},
  booktitle = {International Conference on Learning Representations},
  year = {2025}
}

@article{graphinstruct2024,
  author = {Luo, Zihan and Song, Xiran and Huang, Hong and Lian, Jianxun and Zhang, Chenhao and Jiang, Jinqi and Xie, Xing},
  title = {GraphInstruct: Empowering Large Language Models with Graph Understanding and Reasoning Capability},
  journal = {CoRR},
  volume = {abs/2403.04483},
  year = {2024}
}

@inproceedings{llm4dyg2024,
  author = {Zhang, Zeyang and Wang, Xin and Zhang, Ziwei and Li, Haoyang and Qin, Yijian and Zhu, Wenwu},
  title = {LLM4DyG: Can Large Language Models Solve Spatial-Temporal Problems on Dynamic Graphs?},
  booktitle = {Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  year = {2024},
  doi = {10.1145/3637528.3671709}
}

@inproceedings{tang2024graphgpt,
  author = {Tang, Jiabin and Yang, Yuhao and Wei, Wei and Shi, Lei and Su, Lixin and Cheng, Suqi and Yin, Dawei and Huang, Chao},
  title = {GraphGPT: Graph Instruction Tuning for Large Language Models},
  booktitle = {Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  pages = {491--500},
  year = {2024},
  doi = {10.1145/3626772.3657775}
}

@article{pan2024graphllm,
  author = {Chai, Ziwei and Zhang, Tianjie and Wu, Liang and Han, Kaiqiao and Hu, Xiaohai and Huang, Xuanwen and Yang, Yang},
  title = {GraphLLM: Boosting Graph Reasoning Ability of Large Language Model},
  journal = {CoRR},
  volume = {abs/2310.05845},
  year = {2023}
}

@inproceedings{zhang2025gcoder,
  author = {Zhang, Qifan and Hong, Xiaobin and Tang, Jianheng and Chen, Nuo and Li, Yuhan and Li, Wenzhong and Tang, Jing and Li, Jia},
  title = {GCoder: Improving Large Language Model for Generalized Graph Reasoning},
  booktitle = {Proceedings of the ACM Web Conference 2025},
  year = {2025},
  doi = {10.1145/3746252.3761066}
}

@article{li2024graphteam,
  author = {Li, Xin and Chu, Qizhi and Chen, Yubin and Liu, Yang and Liu, Yaoqi and Yu, Zekai and Chen, Weize and Qian, Chen and Shi, Chuan and Yang, Cheng},
  title = {GraphTeam: Facilitating Large Language Model-based Graph Analysis via Multi-Agent Collaboration},
  journal = {CoRR},
  volume = {abs/2410.18032},
  year = {2024}
}

@inproceedings{yao2023react,
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  title = {ReAct: Synergizing Reasoning and Acting in Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2023}
}

@inproceedings{kojima2022zeroshot,
  author = {Kojima, Takeshi and Gu, Shixiang Shane and Reid, Machel and Matsuo, Yutaka and Iwasawa, Yusuke},
  title = {Large Language Models are Zero-Shot Reasoners},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2022}
}

@inproceedings{creswell2023selection,
  author = {Creswell, Antonia and Shanahan, Murray and Higgins, Irina},
  title = {Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning},
  booktitle = {International Conference on Learning Representations},
  year = {2023}
}

@inproceedings{critic2023,
  author = {Gou, Zhibin and Shao, Zhihong and Gong, Yeyun and Shen, Yelong and Yang, Yujiu and Duan, Nan and Chen, Weizhu},
  title = {CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@inproceedings{gorilla2023,
  author = {Patil, Shishir G. and Zhang, Tianjun and Wang, Xin and Gonzalez, Joseph E.},
  title = {Gorilla: Large Language Model Connected with Massive APIs},
  booktitle = {Advances in Neural Information Processing Systems},
  pages = {126544--126565},
  year = {2024},
  doi = {10.52202/079017-4020}
}

@article{liang2022alphacode,
  author = {Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and Leblond, Remi and Eccles, Tom and Keeling, James and Gimeno, Felix and Dal Lago, Agustin and Hubert, Thomas and Choy, Peter and de Masson d'Autume, Cyprien and Babuschkin, Igor and Chen, Xinyun and Huang, Po-Sen and Welbl, Johannes and Gowal, Sven and Cherepanov, Alexey and Molloy, James and Mankowitz, Daniel and Sutherland Robson, Esme and Kohli, Pushmeet and de Freitas, Nando and Kavukcuoglu, Koray and Vinyals, Oriol},
  title = {Competition-Level Code Generation with AlphaCode},
  journal = {Science},
  volume = {378},
  number = {6624},
  pages = {1092--1097},
  year = {2022},
  doi = {10.1126/science.abq1158}
}

@inproceedings{zhou2023promptbreeder,
  author = {Fernando, Chrisantha and Banarse, Dylan Sunil and Michalewski, Henryk and Osindero, Simon and Rockt{\"a}schel, Tim},
  title = {Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  volume = {235},
  pages = {13481--13544},
  year = {2024}
}

@inproceedings{madaan2023selfrefine,
  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
  title = {Self-Refine: Iterative Refinement with Self-Feedback},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@article{lightman2023processreward,
  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yuri and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
  title = {Let's Verify Step by Step},
  journal = {CoRR},
  volume = {abs/2305.20050},
  year = {2023}
}

@inproceedings{park2023generativeagents,
  author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie Jun and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},
  title = {Generative Agents: Interactive Simulacra of Human Behavior},
  booktitle = {Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology},
  year = {2023}
}

@article{wang2023voyager,
  author = {Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},
  title = {Voyager: An Open-Ended Embodied Agent with Large Language Models},
  journal = {Transactions on Machine Learning Research},
  year = {2024}
}

@inproceedings{lewis2020rag,
  author = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and Kuttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rocktaschel, Tim and Riedel, Sebastian and Kiela, Douwe},
  title = {Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2020}
}

@article{izacard2022atlas,
  author = {Izacard, Gautier and Lewis, Patrick and Lomeli, Maria and Hosseini, Lucas and Petroni, Fabio and Schick, Timo and Dwivedi-Yu, Jane and Joulin, Armand and Riedel, Sebastian and Grave, Edouard},
  title = {Atlas: Few-shot Learning with Retrieval Augmented Language Models},
  journal = {Journal of Machine Learning Research},
  volume = {24},
  pages = {1--43},
  year = {2023}
}

@misc{leskovec2016snap,
  author = {Leskovec, Jure and Krevl, Andrej},
  title = {SNAP Datasets: Stanford Large Network Dataset Collection},
  howpublished = {\url{http://snap.stanford.edu/data}},
  month = {jun},
  year = {2014}
}

@article{graphthought2025,
  author = {Huang, Zixiao and Guo, Lifeng and Sheng, Junjie and Chen, Haosheng and Li, Wenhao and Jin, Bo and Lu, Changhong},
  title = {GraphThought: Graph Combinatorial Optimization with Thought Generation},
  journal = {CoRR},
  volume = {abs/2502.11607},
  year = {2025}
}

@article{pseudocode2025,
  author = {Gong, Chang and Bian, Wanrui and Zhang, Zhijie and Zheng, Weiguo},
  title = {Pseudocode-Injection Magic: Enabling LLMs to Tackle Graph Computational Tasks},
  journal = {CoRR},
  volume = {abs/2501.13731},
  year = {2025}
}

@article{gundam2024,
  author = {Ouyang, Sheng and Hu, Yulan and Chen, Ge and Liu, Yong},
  title = {GUNDAM: Aligning Large Language Models with Graph Understanding},
  journal = {CoRR},
  volume = {abs/2409.20053},
  year = {2024}
}

@inproceedings{metagpt2023,
  author = {Hong, Sirui and Zhuge, Mingchen and Chen, Jonathan and Zheng, Xiawu and Cheng, Yuheng and Wang, Jinlin and Zhang, Ceyao and Wang, Zili and Yau, Steven Ka Shing and Lin, Zijuan and Zhou, Liyang and Ran, Chenyu and Xiao, Lingfeng and Wu, Chenglin and Schmidhuber, J{\"u}rgen},
  title = {MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@inproceedings{camel2023,
  author = {Li, Guohao and Hammoud, Hasan and Itani, Hani and Khizbullin, Dmitrii and Ghanem, Bernard},
  title = {{CAMEL}: Communicative Agents for {Mind} Exploration of Large Scale Language Model Society},
  booktitle = {Advances in Neural Information Processing Systems},
  pages = {51991--52008},
  year = {2023},
  doi = {10.52202/075280-2264}
}

@inproceedings{agentverse2023,
  author = {Chen, Weize and Su, Yusheng and Zuo, Jingwei and Yang, Cheng and Yuan, Chenfei and Chan, Chi-Min and Yu, Heyang and Lu, Yaxi and Hung, Yi-Hsin and Qian, Chen and Qin, Yujia and Cong, Xin and Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong and Zhou, Jie},
  title = {AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@inproceedings{kipf2017gcn,
  author = {Kipf, Thomas and Welling, Max},
  title = {Semi-Supervised Classification with Graph Convolutional Networks},
  booktitle = {International Conference on Learning Representations},
  year = {2017}
}

@inproceedings{velickovic2018gat,
  author = {Velickovic, Petar and Cucurull, Guillem and Casanova, Arantxa and Romero, Adriana and Lio, Pietro and Bengio, Yoshua},
  title = {Graph Attention Networks},
  booktitle = {International Conference on Learning Representations},
  year = {2018}
}

@inproceedings{hamilton2017graphsage,
  author = {Hamilton, William L. and Ying, Rex and Leskovec, Jure},
  title = {Inductive Representation Learning on Large Graphs},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2017}
}

@inproceedings{hu2020ogb,
  author = {Hu, Weihua and Fey, Matthias and Zitnik, Marinka and Dong, Yuxiao and Ren, Hongyu and Liu, Bowen and Catasta, Michele and Leskovec, Jure},
  title = {Open Graph Benchmark},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2020}
}

@article{dwivedi2023benchmarking,
  author = {Dwivedi, Vijay Prakash and Joshi, Chaitanya K. and Laurent, Thomas and Bengio, Yoshua and Bresson, Xavier},
  title = {Benchmarking Graph Neural Networks},
  journal = {Journal of Machine Learning Research},
  volume = {24},
  pages = {1--48},
  year = {2023}
}

@inproceedings{ding2025dpts,
  author = {Ding, Yifu and Jiang, Wentao and Liu, Shunyu and Jing, Yongcheng and Guo, Jinyang and Wang, Yingjie and Zhang, Jing and Wang, Zengmao and Liu, Ziwei and Du, Bo and Liu, Xianglong and Tao, Dacheng},
  title = {Dynamic Parallel Tree Search for Efficient LLM Reasoning},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages = {11233--11252},
  year = {2025},
  doi = {10.18653/v1/2025.acl-long.550}
}

@article{gui2025hypertree,
  author = {Gui, Runquan and Wang, Zhihai and Wang, Jie and Ma, Chi and Zhen, Huiling and Yuan, Mingxuan and Hao, Jianye and Lian, Defu and Chen, Enhong and Wu, Feng},
  title = {HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking},
  journal = {CoRR},
  volume = {abs/2505.02322},
  year = {2025}
}

@inproceedings{zhang2025arise,
  author = {Zhang, Yize and Wang, Tianshu and Chen, Sirui and Wang, Kun and Zeng, Xingyu and Lin, Hongyu and Han, Xianpei and Sun, Le and Lu, Chaochao},
  title = {{ARise}: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages = {10978--10995},
  year = {2025},
  doi = {10.18653/v1/2025.acl-long.538}
}

@article{cho2025decisionpivots,
  author = {Cho, Dongkyu and Zhang, Amy B. Z. and Fehri, Bilel and Wang, Sheng and Chunara, Rumi and Song, Rui and Cai, Hengrui},
  title = {Correct Reasoning Paths Visit Shared Decision Pivots},
  journal = {CoRR},
  volume = {abs/2509.21549},
  year = {2025}
}

@article{hu2024graphagentreasoner,
  author = {Hu, Yuwei and Lei, Runlin and Huang, Xinyi and Wei, Zhewei and Liu, Yongchao},
  title = {Scalable and Accurate Graph Reasoning with LLM-based Multi-Agents},
  journal = {CoRR},
  volume = {abs/2410.05130},
  year = {2024}
}

@inproceedings{yuan2025magts,
  author = {Yuan, Zike and Liu, Ming and Wang, Hui and Qin, Bing},
  title = {{MA-GTS}: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications},
  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  pages = {19286--19304},
  year = {2025},
  doi = {10.18653/v1/2025.emnlp-main.973}
}

@inproceedings{vaswani2017attention,
  author = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, Lukasz and Polosukhin, Illia},
  title = {Attention Is All You Need},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2017}
}

@inproceedings{brown2020language,
  author = {Brown, Tom B. and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie and Kaplan, Jared and Dhariwal, Prafulla and Neelakantan, Arvind and Shyam, Pranav and Sastry, Girish and Askell, Amanda and Agarwal, Sandhini and Herbert-Voss, Ariel and Krueger, Gretchen and Henighan, Tom and Child, Rewon and Ramesh, Aditya and Ziegler, Daniel M. and Wu, Jeffrey and Winter, Clemens and Hesse, Christopher and Chen, Mark and Sigler, Eric and Litwin, Mateusz and Gray, Scott and Chess, Benjamin and Clark, Jack and Berner, Christopher and McCandlish, Sam and Radford, Alec and Sutskever, Ilya and Amodei, Dario},
  title = {Language Models are Few-Shot Learners},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2020}
}

@article{touvron2023llama,
  author = {Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timothee and Roziere, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  title = {{LLaMA}: Open and Efficient Foundation Language Models},
  journal = {CoRR},
  volume = {abs/2302.13971},
  year = {2023}
}

@article{bubeck2023sparks,
  author = {Bubeck, Sebastien and Chandrasekaran, Varun and Eldan, Ronen and Gehrke, Johannes and Horvitz, Eric and Kamar, Ece and Lee, Peter and Lee, Yin Tat and Li, Yuanzhi and Lundberg, Scott and Nori, Harsha and Palangi, Hamid and Ribeiro, Marco Tulio and Zhang, Yi},
  title = {Sparks of Artificial General Intelligence: Early Experiments with {GPT-4}},
  journal = {CoRR},
  volume = {abs/2303.12712},
  year = {2023}
}

@inproceedings{ouyang2022instructgpt,
  author = {Ouyang, Long and Wu, Jeff and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll L. and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul and Leike, Jan and Lowe, Ryan},
  title = {Training Language Models to Follow Instructions with Human Feedback},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2022}
}

@article{nye2021scratchpads,
  author = {Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk and Austin, Jacob and Bieber, David and Dohan, David and Lewkowycz, Aitor and Bosma, Maarten and Luan, David and Sutton, Charles and Odena, Augustus},
  title = {Show Your Work: Scratchpads for Intermediate Computation with Language Models},
  journal = {CoRR},
  volume = {abs/2112.00114},
  year = {2021}
}

@article{cobbe2021verifiers,
  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  title = {Training Verifiers to Solve Math Word Problems},
  journal = {CoRR},
  volume = {abs/2110.14168},
  year = {2021}
}

@article{chen2023pot,
  author = {Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
  title = {Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
  journal = {Transactions on Machine Learning Research},
  year = {2023}
}

@inproceedings{shinn2023reflexion,
  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023}
}

@inproceedings{zhou2024lats,
  author = {Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong},
  title = {Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models},
  booktitle = {International Conference on Machine Learning},
  year = {2024}
}

@article{wu2023autogen,
  author = {Wu, Qingyun and Bansal, Gagan and Zhang, Jieyu and Wu, Yiran and Li, Beibin and Zhu, Erkang and Jiang, Li and Zhang, Xiaoyun and Zhang, Shaokun and Liu, Jiale and Awadallah, Ahmed Hassan and White, Ryen W. and Burger, Doug and Wang, Chi},
  title = {{AutoGen}: Enabling Next-Gen {LLM} Applications via Multi-Agent Conversation},
  journal = {CoRR},
  volume = {abs/2308.08155},
  year = {2023}
}

@inproceedings{zhuge2024languageagents,
  author = {Zhuge, Mingchen and Wang, Wenyi and Kirsch, Louis and Faccio, Francesco and Khizbullin, Dmitrii and Schmidhuber, Juergen},
  title = {Language Agents as Optimizable Graphs},
  booktitle = {International Conference on Machine Learning},
  year = {2024}
}

@article{lin2024plangraph,
  author = {Lin, Fangru and La Malfa, Emanuele and Hofmann, Valentin and Yang, Elle Michelle and Cohn, Anthony and Pierrehumbert, Janet B.},
  title = {Graph-Enhanced Large Language Models in Asynchronous Plan Reasoning},
  journal = {CoRR},
  volume = {abs/2402.02805},
  year = {2024}
}

@inproceedings{fatemi2024talk,
  author = {Fatemi, Bahare and Halcrow, Jonathan and Perozzi, Bryan},
  title = {Talk Like a Graph: Encoding Graphs for Large Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@article{jin2024llmgraphs,
  author = {Jin, Bowen and Liu, Gang and Han, Chi and Jiang, Meng and Ji, Heng and Han, Jiawei},
  title = {Large Language Models on Graphs: A Comprehensive Survey},
  journal = {CoRR},
  volume = {abs/2312.02783},
  year = {2024}
}

@article{zhang2023graphmeetsllms,
  author = {Zhang, Ziwei and Li, Haoyang and Zhang, Zeyang and Qin, Yijian and Wang, Xin and Zhu, Wenwu},
  title = {Graph Meets {LLM}s: Towards Large Graph Models},
  journal = {CoRR},
  volume = {abs/2308.14522},
  year = {2023}
}

@article{zhang2024memorization,
  author = {Zhang, Yizhuo and Wang, Heng and Feng, Shangbin and Tan, Zhaoxuan and Han, Xiaochuang and He, Tianxing and Tsvetkov, Yulia},
  title = {Can {LLM} Graph Reasoning Generalize Beyond Pattern Memorization?},
  journal = {CoRR},
  volume = {abs/2406.15992},
  year = {2024}
}

@article{yuan2025gracore,
  author = {Yuan, Zike and Liu, Ming and Wang, Hui and Qin, Bing},
  title = {{GraCoRe}: Benchmarking Graph Comprehension and Complex Reasoning in Large Language Models},
  journal = {CoRR},
  volume = {abs/2407.02936},
  year = {2024}
}

@inproceedings{wu2025grapheval36k,
  author = {Wu, Qiming and Chen, Zichen and Corcoran, Will and Sra, Misha and Singh, Ambuj K.},
  title = {{GraphEval36K}: Benchmarking Coding and Reasoning Capabilities of Large Language Models on Graph Datasets},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
  pages = {8110--8132},
  year = {2025},
  doi = {10.18653/v1/2025.findings-naacl.452}
}

@article{guo2025g1,
  author = {Guo, Xiaojun and Li, Ang and Wang, Yifei and Jegelka, Stefanie and Wang, Yisen},
  title = {{G1}: Teaching {LLM}s to Reason on Graphs with Reinforcement Learning},
  journal = {CoRR},
  volume = {abs/2505.18499},
  year = {2025}
}

@inproceedings{perozzi2014deepwalk,
  author = {Perozzi, Bryan and Al-Rfou, Rami and Skiena, Steven},
  title = {DeepWalk: Online Learning of Social Representations},
  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
  pages = {701--710},
  year = {2014}
}

@inproceedings{grover2016node2vec,
  author = {Grover, Aditya and Leskovec, Jure},
  title = {node2vec: Scalable Feature Learning for Networks},
  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
  pages = {855--864},
  year = {2016}
}

@inproceedings{xu2019gin,
  author = {Xu, Keyulu and Hu, Weihua and Leskovec, Jure and Jegelka, Stefanie},
  title = {How Powerful are Graph Neural Networks?},
  booktitle = {International Conference on Learning Representations},
  year = {2019}
}

@inproceedings{you2020graphgym,
  author = {You, Jiaxuan and Ying, Rex and Leskovec, Jure},
  title = {Design Space for Graph Neural Networks},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2020}
}

@inproceedings{rampasek2022graphgps,
  author = {Rampasek, Ladislav and Galkin, Mikhail and Dwivedi, Vijay Prakash and Luu, Anh Tuan and Wolf, Guy and Beaini, Dominique},
  title = {Recipe for a General, Powerful, Scalable Graph Transformer},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2022}
}

@inproceedings{karpukhin2020dpr,
  author = {Karpukhin, Vladimir and Oguz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},
  title = {Dense Passage Retrieval for Open-Domain Question Answering},
  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  pages = {6769--6781},
  year = {2020}
}

@article{johnson2019faiss,
  author = {Johnson, Jeff and Douze, Matthijs and Jegou, Herve},
  title = {Billion-Scale Similarity Search with {GPU}s},
  journal = {IEEE Transactions on Big Data},
  volume = {7},
  number = {3},
  pages = {535--547},
  year = {2019}
}

@article{gao2024ragsurvey,
  author = {Gao, Yunfan and Xiong, Yun and Gao, Xinyu and Jia, Kangxiang and Pan, Jinliu and Bi, Yuxi and Dai, Yi and Sun, Jiawei and Wang, Meng and Wang, Haofen},
  title = {Retrieval-Augmented Generation for Large Language Models: A Survey},
  journal = {CoRR},
  volume = {abs/2312.10997},
  year = {2024}
}

@inproceedings{asai2024selfrag,
  author = {Asai, Akari and Wu, Zeqiu and Wang, Yizhong and Sil, Avirup and Hajishirzi, Hannaneh},
  title = {Self-{RAG}: Learning to Retrieve, Generate, and Critique Through Self-Reflection},
  booktitle = {International Conference on Learning Representations},
  year = {2024}
}

@inproceedings{borgeaud2022retro,
  author = {Borgeaud, Sebastian and Mensch, Arthur and Hoffmann, Jordan and Cai, Trevor and Rutherford, Eliza and Millican, Katie and van den Driessche, George and Lespiau, Jean-Baptiste and Damoc, Bogdan and Clark, Aidan and de Las Casas, Diego and Guy, Aurelia and Menick, Jacob and Ring, Roman and Hennigan, Tom and Huang, Saffron and Maggiore, Loren and Jones, Chris and Cassirer, Albin and Brock, Andy and Paganini, Michela and Irving, Geoffrey and Vinyals, Oriol and Osindero, Simon and Simonyan, Karen and Rae, Jack W. and Elsen, Erich and Sifre, Laurent},
  title = {Improving Language Models by Retrieving from Trillions of Tokens},
  booktitle = {International Conference on Machine Learning},
  pages = {2206--2240},
  year = {2022}
}
```
