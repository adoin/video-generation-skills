# 品牌体系搭建

> 涵盖：蕴光 Logo 升级 · 蕴光美妆包装升级 · AI 生成 MIDI 键盘宣传片 · 一张图搭建完整品牌体系 · AI 速成品牌故事 · 科技类 Logo 动效 · AI 去品牌化处理

---

## 模式 A：Logo 概念验证（美妆出海）

**适用：** 蕴光类高端品牌符号升级

### 四步工作流

```
理念抽象（光 / 云 → 线条 + 留白）→ MJ 多方案对比 → Upscale 精修 → PS/AI 替换标准字体交付
```

### Prompt 结构

| 板块 | ✅ 要 | ❌ 不要 |
|------|------|--------|
| 主体 | minimalist high-end beauty logo, abstract cloud and light pattern | 画具象的云朵或太阳光 |
| 意境 | single continuous line art, negative space, zen aesthetics | 复杂渐变填充 |
| 材质 | matte silver, dark sapphire blue background | 廉价彩虹色 |
| 字体 | ultra-thin sans-serif, vector logo | 依赖 AI 生成文字 |

### 方案筛选

| 方向 | 关键词 | 调性 |
|------|--------|------|
| A 几何秩序 | geometric, symmetrical | 稳重国际感 |
| B 东方留白 | abstract brush stroke, fluidity, ink painting inspired | 灵动、轻云意境 |

**交付铁律：** AI 出图形 + 设计师手排文字；贴产品 mockup 验证落地感

---

## 模式 B：包装工艺提案（印刷级）

**适用：** 蕴光外包装、需烫金 / 压印提案

### 四步迭代

1. **盒型材质** — square folding box + uncoated recycled cardboard texture
2. **印后工艺** — embossing, debossing, hot gold foil stamping + extreme negative space
3. **信息排版** — 正面 Logo 烫金占 ≤30%；侧面 ultra-thin sans-serif 产品信息
4. **精修交付** — Variations 选最佳纸张触感；PS 修正所有印刷文字

### ❌ 不要 / ✅ 要

| ❌ 不要 | ✅ 要 |
|--------|------|
| 图案描述权重高于工艺词 | Hot foil / Embossing 权重 > 普通图案 |
| 信息铺满盒面 | extreme negative space, minimalist typography |
| AI 文字直接交付印刷 | 最终稿必须在 PS/AI 校对容量与拼写 |

---

## 模式 C：一张图裂变品牌物料（Freepik 工作流）

**适用：** 鞋类、3C 等「单品 → 全案」

```
白底产品图 → Freepik 工作流上传 → 按节点顺序运行 → 导出海报 / 视频 / 多场景图
```

| ❌ 不要 | ✅ 要 |
|--------|------|
| 每张图重新写提示词 | 工作流内嵌风格节点，只换参考图与简短意图 |
| 低清产品图 | 清晰白底产品图作唯一锚点 |

---

## 模式 D：品牌故事短片（30 分钟剧本法）

**适用：** 品牌故事、企业人文片前置

### 四阶段

| 阶段 | 工具 | 产出 |
|------|------|------|
| 1 灵感捕手 | DeepSeek / 豆包 | 注入「角色 + 特殊道具 + 情感内核」的故事大纲 |
| 2 结构大师 | LLM | 三幕式：建置 ~1min / 对抗 ~2min / 结局 ~1min |
| 3 视觉导演 | Midjourney | 风格关键词前缀 + 关键场景分镜图 |
| 4 动态样片 | Runway / Pika + 剪映 | 图生视频 + BGM 节奏剪辑 |

### 追问模板（打破流水账）

> 你是一位擅长悬念与情感反转的编剧。核心要素：[场景] + [失意主角] + [揭示内心的道具] + [现实 vs 梦想冲突]。输出戏剧性问题与核心冲突。

---

## 模式 E：科技 Logo 动效（官网首屏）

**适用：** 赛丽科技类光芯片 / 高科技企业主页

### 三步动效

1. **视觉翻新** — 原 Logo 作主体框 + 科幻光带参考图 → 即梦重设计（保留轮廓 + 流动蓝光）
2. **循环动画** — 图生视频：光带缓慢流动（提示词 ≤2 句）
3. **入场衔接** — PS 净画面 → 首尾帧生成入场 → AE 交叉淡化拼接循环段

### ❌ 不要 / ✅ 要

| ❌ 不要 | ✅ 要 |
|--------|------|
| 灰度原 Logo 直接做动画 | 先与客户对齐参考案例再翻新 |
| 首尾帧尺寸不一致 | 统一画幅否则无法生成 |
| 5–10s 视频写长提示词 | 两句话：搅动 → 光带反向流动 |

---

## 模式 F：赛博朋克产品宣传片（MIDI 键盘）

**适用：** 电竞外设、科技乐器

```
MJ 首帧 Hero Shot（红色体积光 + 反光底座）→ 即梦 USB 插入过渡 → MJ 多分镜 Raw 模式 → 剪映卡点 BGM
```

| 要素 | 写法 |
|------|------|
| 主体 | black MIDI keyboard, red glowing keys, reflective mirror base |
| 光效 | god-ray light beams of deep red, ultra-realistic commercial lighting |
| 剪辑 | 快镜对鼓点 / 慢镜对延音；时间重映射变速 |

---

## 模式 G：去品牌化模特图（合规）

**适用：** 电商模特图版权风险处理

```
选清晰面部 + 干净背景模特 → MJ InsightFace /saveid → /swapid 换脸 → 比例不符则用 SD 局部重绘
```

| ❌ 不要 | ✅ 要 |
|--------|------|
| 带竞品 Logo 的原图直接换脸 | 先用 PS 修补工具去掉背景 / 衣服小标 |
| 新模特比例与原图差太多硬用 MJ | 比例差大时改 SD inpaint 修衔接 |
