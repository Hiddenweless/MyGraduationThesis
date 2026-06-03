const ASSET = "/Users/wtl/Desktop/我的毕业论文 /outputs/manual-defense-ppt/presentations/plangraph-defense/assets";
const SEU_LOGO = "/Users/wtl/Desktop/我的毕业论文 /SEU-master-thesis-template-master/figures/defined/seu-color-logo.png";

const C = {
  ink: "#18202A",
  muted: "#5B6675",
  blue: "#155A8A",
  teal: "#168C78",
  orange: "#D97706",
  red: "#B42318",
  line: "#D8E0E8",
  paleBlue: "#EAF4FA",
  paleTeal: "#E8F6F2",
  paleOrange: "#FFF4E5",
  paleRed: "#FDECEC",
  gray: "#F5F7FA",
  white: "#FFFFFF",
};

function slide(presentation, ctx, section = "") {
  const s = presentation.slides.add();
  ctx.addShape(s, { x: 0, y: 0, w: ctx.W, h: ctx.H, fill: C.white });
  ctx.addShape(s, { x: 0, y: 0, w: ctx.W, h: 10, fill: C.teal });
  if (section) {
    ctx.addText(s, {
      x: 64, y: 24, w: 420, h: 24, text: section,
      fontSize: 15, color: C.teal, bold: true, typeface: "PingFang SC",
    });
  }
  ctx.addText(s, {
    x: 1130, y: 670, w: 80, h: 24, text: String(ctx.slideNumber || ""),
    fontSize: 12, color: "#9AA5B1", align: "right", typeface: "PingFang SC",
  });
  return s;
}

function title(ctx, s, text, claim) {
  ctx.addText(s, {
    x: 64, y: 58, w: 740, h: 44, text,
    fontSize: 30, color: C.ink, bold: true, typeface: "PingFang SC",
  });
  if (claim) ctx.addText(s, {
    x: 66, y: 104, w: 900, h: 32, text: claim,
    fontSize: 18, color: C.muted, typeface: "PingFang SC",
  });
}

function pill(ctx, s, x, y, w, text, fill = C.paleTeal, color = C.teal) {
  ctx.addShape(s, { x, y, w, h: 30, fill, line: { fill: color, width: 1 } });
  ctx.addText(s, { x: x + 12, y: y + 6, w: w - 24, h: 20, text, fontSize: 13, color, bold: true, align: "center", typeface: "PingFang SC" });
}

function bullet(ctx, s, x, y, text, color = C.ink, size = 19) {
  ctx.addShape(s, { x, y: y + 9, w: 7, h: 7, fill: C.teal });
  ctx.addText(s, { x: x + 18, y, w: 500, h: 28, text, fontSize: size, color, typeface: "PingFang SC" });
}

function metricCard(ctx, s, x, y, w, h, value, label, fill = C.gray, color = C.blue) {
  ctx.addShape(s, { x, y, w, h, fill, line: { fill: "#DDE5ED", width: 1 } });
  ctx.addText(s, { x: x + 18, y: y + 18, w: w - 36, h: 42, text: value, fontSize: 30, color, bold: true, align: "center", typeface: "PingFang SC" });
  ctx.addText(s, { x: x + 18, y: y + 66, w: w - 36, h: 28, text: label, fontSize: 15, color: C.muted, align: "center", typeface: "PingFang SC" });
}

function box(ctx, s, x, y, w, h, text, fill, color = C.ink, fs = 18) {
  ctx.addShape(s, { x, y, w, h, fill, line: { fill: "#C9D5DF", width: 1 } });
  ctx.addText(s, { x: x + 12, y: y + 12, w: w - 24, h: h - 24, text, fontSize: fs, color, bold: true, align: "center", valign: "middle", typeface: "PingFang SC" });
}

function arrow(ctx, s, x, y, w = 28) {
  ctx.addShape(s, { x, y: y + 11, w, h: 3, fill: C.teal });
  ctx.addText(s, { x: x + w - 4, y: y - 4, w: 18, h: 24, text: "›", fontSize: 28, color: C.teal, bold: true, align: "center", typeface: "PingFang SC" });
}

function barChart(ctx, s, x, y, w, h, labels, series) {
  const max = 100;
  const groupW = w / labels.length;
  const colors = [C.blue, C.teal, C.orange, "#6B7280"];
  ctx.addShape(s, { x, y, w, h, fill: "#FAFBFC", line: { fill: C.line, width: 1 } });
  for (let g = 0; g < labels.length; g++) {
    const gx = x + g * groupW + 18;
    const bw = 14;
    for (let j = 0; j < series.length; j++) {
      const val = series[j].values[g];
      const bh = Math.max(2, (val / max) * (h - 80));
      ctx.addShape(s, { x: gx + j * (bw + 4), y: y + h - 48 - bh, w: bw, h: bh, fill: colors[j] });
    }
    ctx.addText(s, { x: x + g * groupW + 6, y: y + h - 36, w: groupW - 12, h: 28, text: labels[g], fontSize: 10, color: C.muted, align: "center", typeface: "PingFang SC" });
  }
  series.forEach((ss, i) => {
    ctx.addShape(s, { x: x + 20 + i * 120, y: y + 12, w: 12, h: 12, fill: colors[i] });
    ctx.addText(s, { x: x + 38 + i * 120, y: y + 8, w: 100, h: 20, text: ss.name, fontSize: 11, color: C.muted, typeface: "PingFang SC" });
  });
}

export async function slide01(presentation, ctx) {
  const s = presentation.slides.add();
  ctx.addShape(s, { x: 0, y: 0, w: ctx.W, h: ctx.H, fill: "#F7FAFC" });
  ctx.addShape(s, { x: 0, y: 0, w: 430, h: ctx.H, fill: C.paleTeal });
  await ctx.addImage(s, { path: SEU_LOGO, x: 70, y: 58, w: 92, h: 92, fit: "contain" });
  ctx.addText(s, { x: 70, y: 190, w: 940, h: 92, text: "基于规划反馈的多智能体图推理方法研究", fontSize: 42, color: C.ink, bold: true, typeface: "PingFang SC" });
  ctx.addText(s, { x: 74, y: 302, w: 760, h: 34, text: "硕士学位论文答辩报告", fontSize: 22, color: C.blue, bold: true, typeface: "PingFang SC" });
  ctx.addText(s, { x: 74, y: 400, w: 360, h: 32, text: "专业型硕士：王腾龙", fontSize: 20, color: C.ink, typeface: "PingFang SC" });
  ctx.addText(s, { x: 74, y: 438, w: 420, h: 32, text: "研究方向：LLM + 多智能体 + 图推理", fontSize: 18, color: C.muted, typeface: "PingFang SC" });
  box(ctx, s, 750, 390, 120, 56, "规划", C.white, C.teal);
  arrow(ctx, s, 884, 407);
  box(ctx, s, 930, 390, 120, 56, "检索", C.white, C.blue);
  arrow(ctx, s, 1064, 407);
  box(ctx, s, 1110, 390, 120, 56, "验证", C.white, C.orange);
  ctx.addText(s, { x: 74, y: 615, w: 550, h: 28, text: "东南大学硕士学位论文答辩", fontSize: 16, color: C.muted, typeface: "PingFang SC" });
  return s;
}

export async function slide02(presentation, ctx) {
  const s = slide(presentation, ctx, "汇报提纲");
  title(ctx, s, "汇报提纲", "围绕问题、方法、实验和系统实现展开");
  const items = [
    ["1", "研究背景与现状", "图推理价值、LLM 直接推理痛点、现有不足"],
    ["2", "研究目标与方法", "规划生成、规划引导检索、执行验证与反馈修复"],
    ["3", "实验验证与分析", "五个公开基准、复杂任务、稳定性、鲁棒性、消融"],
    ["4", "系统实现与总结", "PlanGraph Chat、中间工件链、贡献与展望"],
  ];
  items.forEach((it, i) => {
    const y = 178 + i * 105;
    ctx.addShape(s, { x: 100, y, w: 70, h: 70, fill: i === 1 ? C.paleTeal : C.gray, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 100, y: y + 15, w: 70, h: 40, text: it[0], fontSize: 27, color: i === 1 ? C.teal : C.blue, bold: true, align: "center", typeface: "PingFang SC" });
    ctx.addText(s, { x: 205, y: y + 4, w: 360, h: 30, text: it[1], fontSize: 24, color: C.ink, bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: 205, y: y + 42, w: 790, h: 28, text: it[2], fontSize: 17, color: C.muted, typeface: "PingFang SC" });
  });
  return s;
}

export async function slide03(presentation, ctx) {
  const s = slide(presentation, ctx, "研究背景");
  title(ctx, s, "图推理是结构化智能的重要任务", "关键不只是回答文本问题，而是对图结构执行可验证计算");
  await ctx.addImage(s, { path: `${ASSET}/intro.png`, x: 65, y: 158, w: 720, h: 410, fit: "contain" });
  metricCard(ctx, s, 830, 168, 300, 96, "路径规划", "交通、物流、网络路由", C.paleBlue, C.blue);
  metricCard(ctx, s, 830, 290, 300, 96, "组合优化", "TSP、最大团、点覆盖", C.paleOrange, C.orange);
  metricCard(ctx, s, 830, 412, 300, 96, "知识推断", "知识图谱与关系分析", C.paleTeal, C.teal);
  bullet(ctx, s, 104, 604, "图任务要求同时满足拓扑关系、算法步骤和输出格式。", C.ink, 19);
  return s;
}

export async function slide04(presentation, ctx) {
  const s = slide(presentation, ctx, "现实问题");
  title(ctx, s, "LLM 直接图推理容易失稳", "图结构序列化为文本后，结构约束在生成过程中容易丢失");
  await ctx.addImage(s, { path: `${ASSET}/graph_reasoning_challenge.png`, x: 645, y: 145, w: 525, h: 390, fit: "contain" });
  box(ctx, s, 92, 180, 180, 62, "图结构输入", C.paleBlue, C.blue);
  arrow(ctx, s, 294, 199, 46);
  box(ctx, s, 365, 180, 190, 62, "文本序列化", C.gray, C.ink);
  arrow(ctx, s, 578, 199, 42);
  const pains = [
    ["拓扑遗漏", "节点、边、方向、权重在长文本中被忽略"],
    ["约束违反", "路径闭合、节点不重复、容量限制未被满足"],
    ["幻觉答案", "输出看似合理，但不可执行或不可验证"],
  ];
  pains.forEach((p, i) => {
    const y = 300 + i * 84;
    ctx.addShape(s, { x: 94, y, w: 455, h: 58, fill: [C.paleRed, C.paleOrange, C.paleBlue][i], line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 118, y: y + 10, w: 120, h: 28, text: p[0], fontSize: 20, color: [C.red, C.orange, C.blue][i], bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: 246, y: y + 12, w: 280, h: 24, text: p[1], fontSize: 15, color: C.ink, typeface: "PingFang SC" });
  });
  return s;
}

export async function slide05(presentation, ctx) {
  const s = slide(presentation, ctx, "研究现状");
  title(ctx, s, "现有方法仍缺少稳定的规划反馈闭环", "主要不足不是单个环节能力弱，而是任务理解、知识调用和执行验证缺少统一组织");
  const cols = ["端到端推理", "单纯程序生成", "样本/微调增强", "多智能体协作"];
  const bads = ["长序列下拓扑遗漏", "一次性代码易偏离约束", "构建维护成本较高", "角色协作缺少受控回退"];
  const needs = ["显式中间表示", "执行级验证", "轻量知识更新", "状态化调度闭环"];
  cols.forEach((c, i) => {
    const x = 72 + i * 290;
    ctx.addShape(s, { x, y: 170, w: 250, h: 330, fill: C.gray, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: x + 18, y: 196, w: 214, h: 30, text: c, fontSize: 22, color: C.blue, bold: true, align: "center", typeface: "PingFang SC" });
    ctx.addShape(s, { x: x + 26, y: 250, w: 198, h: 70, fill: C.paleRed });
    ctx.addText(s, { x: x + 38, y: 266, w: 174, h: 42, text: bads[i], fontSize: 17, color: C.red, bold: true, align: "center", typeface: "PingFang SC" });
    ctx.addShape(s, { x: x + 26, y: 356, w: 198, h: 70, fill: C.paleTeal });
    ctx.addText(s, { x: x + 38, y: 372, w: 174, h: 42, text: needs[i], fontSize: 17, color: C.teal, bold: true, align: "center", typeface: "PingFang SC" });
  });
  ctx.addText(s, { x: 90, y: 560, w: 1020, h: 34, text: "本文切入点：将图推理组织为“规划约束生成 + 执行反馈修正”的可追踪求解过程。", fontSize: 22, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide06(presentation, ctx) {
  const s = slide(presentation, ctx, "研究目标");
  title(ctx, s, "构建可规划、可检索、可执行、可验证、可修复的图推理系统", "面向工程可靠性，而不是单纯追求更长推理文本");
  ["可规划", "可检索", "可执行", "可验证", "可修复"].forEach((t, i) => {
    box(ctx, s, 90 + i * 220, 168, 160, 62, t, i % 2 ? C.paleBlue : C.paleTeal, i % 2 ? C.blue : C.teal, 22);
    if (i < 4) arrow(ctx, s, 258 + i * 220, 187, 28);
  });
  const challenges = [
    ["挑战一", "自然语言图任务如何稳定映射为可执行规划"],
    ["挑战二", "检索知识如何与算法步骤和约束条件保持一致"],
    ["挑战三", "执行反馈如何修正程序错误和约束遗漏"],
  ];
  challenges.forEach((c, i) => {
    const y = 310 + i * 82;
    ctx.addShape(s, { x: 168, y, w: 160, h: 52, fill: C.blue });
    ctx.addText(s, { x: 168, y: y + 13, w: 160, h: 26, text: c[0], fontSize: 20, color: C.white, bold: true, align: "center", typeface: "PingFang SC" });
    ctx.addShape(s, { x: 350, y, w: 680, h: 52, fill: C.gray, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 374, y: y + 13, w: 620, h: 26, text: c[1], fontSize: 20, color: C.ink, typeface: "PingFang SC" });
  });
  return s;
}

export async function slide07(presentation, ctx) {
  const s = slide(presentation, ctx, "技术路线");
  title(ctx, s, "PlanGraph：以规划为前向约束，以反馈为反向修正", "把不可观察的一次性生成转化为可检查、可恢复的多阶段求解链路");
  await ctx.addImage(s, { path: `${ASSET}/research_roadmap.png`, x: 62, y: 150, w: 760, h: 430, fit: "contain" });
  const chain = ["Question", "Planning", "Retrieval", "Coding", "Verify", "Repair", "Answer"];
  chain.forEach((c, i) => {
    const x = 850 + (i % 2) * 170;
    const y = 158 + Math.floor(i / 2) * 98;
    box(ctx, s, x, y, 130, 48, c, i < 2 ? C.paleTeal : i < 4 ? C.paleBlue : C.paleOrange, i < 2 ? C.teal : i < 4 ? C.blue : C.orange, 15);
  });
  ctx.addText(s, { x: 858, y: 540, w: 310, h: 48, text: "核心机制：规划约束检索与代码生成；执行反馈定位并修复偏差。", fontSize: 18, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide08(presentation, ctx) {
  const s = slide(presentation, ctx, "方法一");
  title(ctx, s, "面向图推理的规划生成方法", "规划是自然语言任务和可执行程序之间的中间求解语义");
  const steps = [
    ["任务解析", "任务类型、图结构、约束集合、输出格式"],
    ["伪代码规划", "图构建、算法调用、约束校验、结果整理"],
    ["规划评价", "约束覆盖、步骤一致、可执行性评分"],
  ];
  steps.forEach((st, i) => {
    const x = 95 + i * 360;
    ctx.addShape(s, { x, y: 178, w: 292, h: 250, fill: i === 1 ? C.paleTeal : C.gray, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: x + 22, y: 205, w: 248, h: 34, text: st[0], fontSize: 24, color: i === 1 ? C.teal : C.blue, bold: true, align: "center", typeface: "PingFang SC" });
    ctx.addShape(s, { x: x + 40, y: 270, w: 212, h: 1, fill: C.line });
    ctx.addText(s, { x: x + 30, y: 304, w: 232, h: 82, text: st[1], fontSize: 19, color: C.ink, align: "center", valign: "middle", typeface: "PingFang SC" });
    if (i < 2) arrow(ctx, s, x + 306, 286, 28);
  });
  ctx.addText(s, { x: 170, y: 500, w: 890, h: 44, text: "规划不追求长篇解释，而是显式保留算法步骤与关键约束，作为检索、编码和验证的共同锚点。", fontSize: 22, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide09(presentation, ctx) {
  const s = slide(presentation, ctx, "方法二");
  title(ctx, s, "规划引导的知识检索与程序生成", "检索查询从原始文本转向结构化规划，知识更贴近当前求解步骤");
  const labels = ["原始问题文本", "任务类型+关键词", "规划伪代码", "规划+约束标签"];
  const vals = [42.6, 68.9, 76.4, 82.1];
  ctx.addShape(s, { x: 80, y: 178, w: 530, h: 340, fill: "#FAFBFC", line: { fill: C.line, width: 1 } });
  labels.forEach((l, i) => {
    const y = 210 + i * 70;
    const bw = vals[i] * 4.5;
    ctx.addText(s, { x: 105, y: y + 8, w: 130, h: 24, text: l, fontSize: 15, color: C.ink, typeface: "PingFang SC" });
    ctx.addShape(s, { x: 250, y: y + 10, w: 330, h: 18, fill: "#E6EBF0" });
    ctx.addShape(s, { x: 250, y: y + 10, w: bw, h: 18, fill: i >= 2 ? C.teal : C.blue });
    ctx.addText(s, { x: 590, y: y + 4, w: 54, h: 24, text: `${vals[i]}%`, fontSize: 14, color: C.muted, typeface: "PingFang SC" });
  });
  ctx.addText(s, { x: 95, y: 540, w: 500, h: 22, text: "Hit@1 对比：规划与约束标签显著提升知识命中质量", fontSize: 16, color: C.muted, align: "center", typeface: "PingFang SC" });
  box(ctx, s, 690, 190, 180, 64, "规划伪代码", C.paleTeal, C.teal);
  arrow(ctx, s, 890, 210, 34);
  box(ctx, s, 946, 190, 180, 64, "图算法知识", C.paleBlue, C.blue);
  box(ctx, s, 690, 330, 180, 64, "API / 示例", C.gray, C.ink);
  arrow(ctx, s, 890, 350, 34);
  box(ctx, s, 946, 330, 180, 64, "候选程序", C.paleOrange, C.orange);
  ctx.addText(s, { x: 700, y: 458, w: 420, h: 52, text: "规划解决“该查什么”，检索解决“依据什么实现”，编码负责把二者落为可执行程序。", fontSize: 20, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide10(presentation, ctx) {
  const s = slide(presentation, ctx, "方法三");
  title(ctx, s, "执行验证与反馈修复方法", "用外部执行结果检查程序错误、约束遗漏和输出格式偏差");
  await ctx.addImage(s, { path: `${ASSET}/fig3_2.png`, x: 62, y: 148, w: 720, h: 430, fit: "contain" });
  const errs = [
    ["语法/导入错误", "局部修复"],
    ["API 或图构建错误", "二次检索 + 修复"],
    ["约束违反", "验证反馈修复"],
    ["超时或多轮失败", "有界重生成"],
  ];
  errs.forEach((e, i) => {
    const y = 174 + i * 85;
    ctx.addShape(s, { x: 830, y, w: 280, h: 56, fill: i === 1 ? C.paleOrange : C.gray, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 848, y: y + 8, w: 134, h: 24, text: e[0], fontSize: 17, color: C.ink, bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: 992, y: y + 8, w: 96, h: 24, text: e[1], fontSize: 15, color: i === 1 ? C.orange : C.teal, bold: true, align: "right", typeface: "PingFang SC" });
  });
  ctx.addText(s, { x: 825, y: 535, w: 295, h: 38, text: "反馈不是盲目重试，而是按错误类型选择恢复路径。", fontSize: 18, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide11(presentation, ctx) {
  const s = slide(presentation, ctx, "协同框架");
  title(ctx, s, "基于黑板调度的多智能体协同框架", "把多智能体自由对话转化为围绕状态、事件和工件的受控协同");
  await ctx.addImage(s, { path: `${ASSET}/SystemArchitecture.png`, x: 64, y: 150, w: 780, h: 420, fit: "contain" });
  metricCard(ctx, s, 890, 176, 250, 88, "共享黑板", "记录阶段事件与状态", C.paleTeal, C.teal);
  metricCard(ctx, s, 890, 294, 250, 88, "工件链", "保存规划、检索、代码、反馈", C.paleBlue, C.blue);
  metricCard(ctx, s, 890, 412, 250, 88, "有界恢复", "限制修复轮数与重生成成本", C.paleOrange, C.orange);
  return s;
}

export async function slide12(presentation, ctx) {
  const s = slide(presentation, ctx, "实验设计");
  title(ctx, s, "五个公开基准覆盖经典图算法、组合优化和动态图任务", "统一采用 Exact Match，所有运行错误、超时和格式错误均计入失败");
  const ds = [
    ["GraphArena", "10 类任务", "经典图计算与组合优化"],
    ["NLGraph", "8 类任务", "自然语言图算法任务"],
    ["GraphWiz", "9 类任务", "指令式图问题"],
    ["LLM4DyG", "9 类任务", "动态图与时序约束"],
    ["GraphInstruct", "21 类任务", "图指令跟随"],
  ];
  ds.forEach((d, i) => {
    const x = 68 + (i % 3) * 375;
    const y = 178 + Math.floor(i / 3) * 160;
    ctx.addShape(s, { x, y, w: 315, h: 110, fill: i % 2 ? C.paleBlue : C.paleTeal, line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: x + 20, y: y + 18, w: 260, h: 28, text: d[0], fontSize: 23, color: i % 2 ? C.blue : C.teal, bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: x + 20, y: y + 55, w: 120, h: 24, text: d[1], fontSize: 17, color: C.ink, bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: x + 140, y: y + 55, w: 150, h: 24, text: d[2], fontSize: 15, color: C.muted, typeface: "PingFang SC" });
  });
  box(ctx, s, 810, 500, 150, 54, "GPT-4o", C.gray, C.ink, 18);
  box(ctx, s, 980, 500, 150, 54, "GraphTeam", C.gray, C.ink, 18);
  box(ctx, s, 810, 570, 150, 54, "GCoder", C.gray, C.ink, 18);
  box(ctx, s, 980, 570, 150, 54, "PlanGraph", C.paleTeal, C.teal, 18);
  ctx.addText(s, { x: 80, y: 532, w: 630, h: 36, text: "对比对象覆盖通用大模型直接推理、多智能体路线和程序生成路线。", fontSize: 22, color: C.ink, bold: true, typeface: "PingFang SC" });
  return s;
}

export async function slide13(presentation, ctx) {
  const s = slide(presentation, ctx, "总体性能");
  title(ctx, s, "PlanGraph 在五个基准中四个取得最优", "平均精确匹配率达到 96.89%，较最佳现有方法平均提升 2.31 个百分点");
  const labels = ["GraphArena", "NLGraph", "GraphWiz", "LLM4DyG", "GraphInstruct"];
  const series = [
    { name: "GPT-4o", values: [49.08, 51.40, 47.61, 58.04, 51.14] },
    { name: "GraphTeam", values: [95.14, 97.71, 88.62, 96.35, 93.48] },
    { name: "GCoder", values: [94.27, 96.90, 90.20, 93.78, 92.56] },
    { name: "PlanGraph", values: [97.74, 98.72, 97.01, 96.11, 94.87] },
  ];
  barChart(ctx, s, 70, 165, 820, 390, labels, series);
  metricCard(ctx, s, 930, 178, 230, 90, "96.89%", "平均 EM", C.paleTeal, C.teal);
  metricCard(ctx, s, 930, 300, 230, 90, "4 / 5", "基准最优", C.paleBlue, C.blue);
  metricCard(ctx, s, 930, 422, 230, 90, "+6.81", "GraphWiz 最大提升", C.paleOrange, C.orange);
  return s;
}

export async function slide14(presentation, ctx) {
  const s = slide(presentation, ctx, "复杂任务");
  title(ctx, s, "性能收益主要来自高约束、强组合性的图任务", "在简单任务趋于饱和时，规划与验证闭环在复杂任务上更有价值");
  await ctx.addImage(s, { path: `${ASSET}/exp_complexity_trend.png`, x: 70, y: 165, w: 520, h: 330, fit: "contain" });
  await ctx.addImage(s, { path: `${ASSET}/exp_sample_difficulty_trend.png`, x: 650, y: 165, w: 520, h: 330, fit: "contain" });
  metricCard(ctx, s, 148, 535, 260, 78, "96.23%", "NP 完全任务 EM", C.paleTeal, C.teal);
  metricCard(ctx, s, 490, 535, 260, 78, "+3.36", "较最佳基线提升", C.paleOrange, C.orange);
  metricCard(ctx, s, 832, 535, 260, 78, "优势扩大", "困难样本中更稳定", C.paleBlue, C.blue);
  return s;
}

export async function slide15(presentation, ctx) {
  const s = slide(presentation, ctx, "机制验证");
  title(ctx, s, "稳定性、鲁棒性和消融实验验证闭环机制有效", "规划、检索和验证不是附属模块，而是共同决定最终可靠性");
  await ctx.addImage(s, { path: `${ASSET}/exp_ablation.png`, x: 72, y: 165, w: 525, h: 330, fit: "contain" });
  const robust = [
    ["节点顺序打乱", "96.8%"],
    ["边描述改写", "95.7%"],
    ["输出格式切换", "94.9%"],
  ];
  robust.forEach((r, i) => {
    ctx.addShape(s, { x: 690, y: 174 + i * 82, w: 380, h: 58, fill: [C.paleTeal, C.paleBlue, C.paleOrange][i], line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 716, y: 188 + i * 82, w: 190, h: 24, text: r[0], fontSize: 19, color: C.ink, bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: 942, y: 184 + i * 82, w: 90, h: 28, text: r[1], fontSize: 24, color: [C.teal, C.blue, C.orange][i], bold: true, align: "right", typeface: "PingFang SC" });
  });
  ctx.addText(s, { x: 674, y: 450, w: 430, h: 60, text: "去除规划模块下降最明显；去除验证模块在 GraphWiz 上由 97.01% 降至 90.72%。", fontSize: 21, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide16(presentation, ctx) {
  const s = slide(presentation, ctx, "案例分析");
  title(ctx, s, "旅行商问题案例：反馈闭环修正回路约束遗漏", "将组合优化任务转化为可执行、可检查、可修复的程序化求解过程");
  await ctx.addImage(s, { path: `${ASSET}/case2.png`, x: 60, y: 145, w: 760, h: 430, fit: "contain" });
  const pts = [
    "构建带权无向图",
    "固定起点 A",
    "枚举哈密顿回路",
    "检查回到起点与总代价",
    "输出最优路径与代价",
  ];
  pts.forEach((p, i) => bullet(ctx, s, 860, 176 + i * 58, p, C.ink, 19));
  ctx.addShape(s, { x: 850, y: 500, w: 300, h: 78, fill: C.paleTeal, line: { fill: C.teal, width: 1 } });
  ctx.addText(s, { x: 872, y: 518, w: 256, h: 30, text: "A → B → E → D → C → A", fontSize: 18, color: C.teal, bold: true, align: "center", typeface: "PingFang SC" });
  ctx.addText(s, { x: 872, y: 548, w: 256, h: 22, text: "总代价：18", fontSize: 16, color: C.ink, align: "center", typeface: "PingFang SC" });
  return s;
}

export async function slide17(presentation, ctx) {
  const s = slide(presentation, ctx, "系统实现");
  title(ctx, s, "PlanGraph Chat 展示多智能体中间工件链", "系统侧重点是可追踪、可恢复和可解释，而不是只返回最终答案");
  ctx.addShape(s, { x: 80, y: 150, w: 690, h: 430, fill: "#F9FBFC", line: { fill: C.line, width: 1 } });
  ctx.addShape(s, { x: 80, y: 150, w: 690, h: 42, fill: "#E9EEF5" });
  ctx.addText(s, { x: 105, y: 162, w: 420, h: 20, text: "PlanGraph Chat 网页端截图占位", fontSize: 16, color: C.muted, bold: true, typeface: "PingFang SC" });
  ctx.addText(s, { x: 140, y: 315, w: 560, h: 70, text: "请在最终制作时替换为真实系统截图：输入问题、规划结果、检索结果、候选代码、执行反馈、最终答案", fontSize: 22, color: C.blue, bold: true, align: "center", valign: "middle", typeface: "PingFang SC" });
  const artifacts = ["task_spec", "plan", "retrieval", "candidate_code", "verification", "repair", "final_answer"];
  artifacts.forEach((a, i) => {
    const y = 162 + i * 58;
    box(ctx, s, 835, y, 220, 42, a, i < 2 ? C.paleTeal : i < 4 ? C.paleBlue : C.paleOrange, i < 2 ? C.teal : i < 4 ? C.blue : C.orange, 15);
    if (i < artifacts.length - 1) ctx.addShape(s, { x: 943, y: y + 46, w: 3, h: 16, fill: C.line });
  });
  return s;
}

export async function slide18(presentation, ctx) {
  const s = slide(presentation, ctx, "总结展望");
  title(ctx, s, "总结与展望", "本文提供了一条面向图推理任务的工程化可靠求解路径");
  const contrib = [
    ["方法贡献", "提出规划反馈图推理协同求解方法，将规划约束与执行反馈组织为闭环。"],
    ["系统贡献", "构建基于黑板调度的多智能体框架，支持中间工件记录、版本管理和异常恢复。"],
    ["实验贡献", "在五个公开基准上验证有效性，平均 EM 达到 96.89%，复杂任务优势更明显。"],
  ];
  contrib.forEach((c, i) => {
    ctx.addShape(s, { x: 95, y: 165 + i * 110, w: 475, h: 78, fill: [C.paleTeal, C.paleBlue, C.paleOrange][i], line: { fill: C.line, width: 1 } });
    ctx.addText(s, { x: 118, y: 181 + i * 110, w: 120, h: 28, text: c[0], fontSize: 21, color: [C.teal, C.blue, C.orange][i], bold: true, typeface: "PingFang SC" });
    ctx.addText(s, { x: 246, y: 181 + i * 110, w: 290, h: 38, text: c[1], fontSize: 16, color: C.ink, typeface: "PingFang SC" });
  });
  ctx.addShape(s, { x: 690, y: 170, w: 380, h: 320, fill: C.gray, line: { fill: C.line, width: 1 } });
  ctx.addText(s, { x: 730, y: 205, w: 300, h: 32, text: "后续工作", fontSize: 25, color: C.ink, bold: true, align: "center", typeface: "PingFang SC" });
  bullet(ctx, s, 740, 270, "细粒度时序规划", C.ink, 19);
  bullet(ctx, s, 740, 330, "反馈驱动的知识重排序", C.ink, 19);
  bullet(ctx, s, 740, 390, "更具代表性的验证样例构造", C.ink, 19);
  ctx.addText(s, { x: 730, y: 560, w: 310, h: 38, text: "感谢各位评委老师，请批评指正。", fontSize: 22, color: C.teal, bold: true, align: "center", typeface: "PingFang SC" });
  return s;
}
