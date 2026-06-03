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

const ASSET = "/Users/wtl/Desktop/我的毕业论文 /outputs/manual-defense-ppt/presentations/opportunity-challenge/assets";

function base(presentation, ctx, no) {
  const s = presentation.slides.add();
  ctx.addShape(s, { x: 0, y: 0, w: ctx.W, h: ctx.H, fill: C.white });
  ctx.addShape(s, { x: 0, y: 0, w: ctx.W, h: 10, fill: C.teal });
  ctx.addText(s, {
    x: 64, y: 25, w: 220, h: 24, text: `机遇与挑战 ${no}`,
    fontSize: 15, color: C.teal, bold: true, typeface: "PingFang SC",
  });
  ctx.addText(s, {
    x: 1130, y: 670, w: 80, h: 24, text: String(no),
    fontSize: 12, color: "#9AA5B1", align: "right", typeface: "PingFang SC",
  });
  return s;
}

function title(ctx, s, head, sub) {
  ctx.addText(s, {
    x: 64, y: 63, w: 980, h: 42, text: head,
    fontSize: 30, color: C.ink, bold: true, typeface: "PingFang SC",
  });
  ctx.addText(s, {
    x: 66, y: 110, w: 1000, h: 30, text: sub,
    fontSize: 18, color: C.muted, typeface: "PingFang SC",
  });
}

function box(ctx, s, x, y, w, h, text, fill, color = C.ink, fs = 18) {
  ctx.addShape(s, { x, y, w, h, fill, line: { fill: "#C9D5DF", width: 1 } });
  ctx.addText(s, {
    x: x + 12, y: y + 10, w: w - 24, h: h - 20, text,
    fontSize: fs, color, bold: true, align: "center", valign: "middle", typeface: "PingFang SC",
  });
}

function arrow(ctx, s, x, y, w = 44, color = C.teal) {
  ctx.addShape(s, { x, y: y + 14, w, h: 4, fill: color });
  ctx.addText(s, { x: x + w - 2, y: y - 2, w: 22, h: 30, text: "›", fontSize: 34, color, bold: true, align: "center", typeface: "PingFang SC" });
}

function tag(ctx, s, x, y, text, fill, color) {
  ctx.addShape(s, { x, y, w: 142, h: 34, fill, line: { fill: color, width: 1 } });
  ctx.addText(s, { x: x + 10, y: y + 8, w: 122, h: 18, text, fontSize: 14, color, bold: true, align: "center", typeface: "PingFang SC" });
}

function challenge(ctx, s, x, y, no, text) {
  ctx.addShape(s, { x, y, w: 360, h: 148, fill: C.paleOrange, line: { fill: C.orange, width: 1 } });
  ctx.addText(s, { x: x + 22, y: y + 18, w: 110, h: 30, text: `挑战 ${no}`, fontSize: 23, color: C.orange, bold: true, typeface: "PingFang SC" });
  ctx.addText(s, { x: x + 22, y: y + 62, w: 308, h: 62, text, fontSize: 20, color: C.ink, bold: true, valign: "middle", typeface: "PingFang SC" });
}

function foot(ctx, s, text) {
  ctx.addText(s, { x: 74, y: 628, w: 1040, h: 24, text, fontSize: 14, color: C.muted, typeface: "PingFang SC" });
}

export async function slide01(presentation, ctx) {
  const s = base(presentation, ctx, 1);
  title(ctx, s, "机遇一：复杂图任务可通过显式规划进行结构化拆解", "把原始长文本输入转化为任务目标、图结构、约束条件和伪代码步骤");

  tag(ctx, s, 80, 168, "不足点 1", C.paleRed, C.red);
  ctx.addText(s, {
    x: 240, y: 166, w: 650, h: 40,
    text: "端到端推理在长序列图结构输入下，拓扑理解与约束推理不稳定",
    fontSize: 20, color: C.ink, bold: true, typeface: "PingFang SC",
  });
  await ctx.addImage(s, { path: `${ASSET}/opportunity-1-context.png`, x: 74, y: 232, w: 800, h: 300, fit: "contain" });
  challenge(ctx, s, 880, 300, 1, "如何将自然语言图任务稳定映射为可执行规划？");
  ctx.addText(s, {
    x: 105, y: 552, w: 720, h: 42,
    text: "答辩表达重点：规划不是普通思维链，而是连接任务语义、算法步骤和程序实现的中间层。",
    fontSize: 20, color: C.ink, bold: true, align: "center", typeface: "PingFang SC",
  });
  foot(ctx, s, "参考思路：GraphArena 揭示复杂图任务下 LLM 幻觉问题；PIE 等工作说明伪代码中间表示对图计算任务有帮助。");
  return s;
}

export async function slide02(presentation, ctx) {
  const s = base(presentation, ctx, 2);
  title(ctx, s, "机遇二：规划路径可作为外部知识检索的高效查询依据", "检索目标从原始问题文本转向算法步骤与结构化约束标签");

  tag(ctx, s, 80, 168, "不足点 2", C.paleRed, C.red);
  ctx.addText(s, {
    x: 240, y: 166, w: 720, h: 40,
    text: "程序生成式图推理依赖历史样本或经验代码库，知识构建成本高、泛化受限",
    fontSize: 20, color: C.ink, bold: true, typeface: "PingFang SC",
  });
  await ctx.addImage(s, { path: `${ASSET}/opportunity-2-context.png`, x: 72, y: 230, w: 815, h: 305, fit: "contain" });
  challenge(ctx, s, 880, 300, 2, "如何让检索知识与算法步骤、任务约束保持一致？");
  ctx.addText(s, {
    x: 108, y: 552, w: 720, h: 42,
    text: "答辩表达重点：规划把检索目标从原始文本转为算法步骤，使外部知识更贴近程序实现。",
    fontSize: 20, color: C.ink, bold: true, align: "center", typeface: "PingFang SC",
  });
  foot(ctx, s, "参考思路：GCoder 证明程序化求解有效；本文进一步用规划引导实时检索，减少对历史经验库的依赖。");
  return s;
}

export async function slide03(presentation, ctx) {
  const s = base(presentation, ctx, 3);
  title(ctx, s, "机遇三：程序执行结果可作为错误定位与修复反馈", "把生成错误从文本层面暴露到执行层面，再反向驱动修复和恢复");

  tag(ctx, s, 80, 168, "不足点 3", C.paleRed, C.red);
  ctx.addText(s, {
    x: 240, y: 166, w: 760, h: 40,
    text: "现有多智能体方法偏重角色分工，缺少面向执行错误和约束遗漏的稳定闭环",
    fontSize: 20, color: C.ink, bold: true, typeface: "PingFang SC",
  });
  await ctx.addImage(s, { path: `${ASSET}/opportunity-3-context.png`, x: 72, y: 230, w: 820, h: 305, fit: "contain" });
  challenge(ctx, s, 880, 300, 3, "如何通过执行反馈修正程序错误、约束遗漏和输出偏差？");
  ctx.addText(s, {
    x: 105, y: 552, w: 730, h: 42,
    text: "答辩表达重点：反馈不是重复生成，而是按错误类型选择局部修复、补充检索或有界重生成。",
    fontSize: 20, color: C.ink, bold: true, align: "center", typeface: "PingFang SC",
  });
  foot(ctx, s, "参考思路：GraphTeam 体现多智能体协作价值；本文强调黑板调度、工件链和执行反馈恢复。");
  return s;
}
