# 废片回收与精准修图

> 涵盖：§30（废片补救）
> 精准迭代流水线见 [json-and-reverse.md](json-and-reverse.md) §31 第三阶段

---

### §30 拒绝盲盒式烧钱：榨干废片价值

> 90% 废片 = 部分正确理解。不要为 1% 瑕疵全盘重 roll。

#### 一、拆分画面，复用光影与构图

### ❌ 不要

- 光影构图满意、仅手部崩坏 → 直接 Re-roll
- 结果：手可能对了，氛围和构图全变

### ✅ 要

1. **保存废片**（光影/构图满意即留）
2. **上传为参考图**（Nano Banana 垫图 / Midjourney --sref）
3. **简化文字 Prompt，只纠正主体动作：**


same lighting and atmosphere as reference image,
woman in luxury cashmere coat, golden hour backlight,
hands resting naturally at sides, elegant relaxed pose,
film photography, soft hair glow


- 参考图锁定色板与环境光，算力集中在新动作描述

#### 二、局部重绘（Inpainting）——蒙版 + 局部 Prompt

### ❌ 不要

- 为一根多指手指 Re-roll 整张（概率极低同时完美）
- 局部框内粘贴全文 Prompt：一个穿着真丝连衣裙的美女……
  → AI 困惑要在手指大小区域塞进整个人

### ✅ 要

1. 画笔涂抹错误区域（略大于瑕疵，留融合边）
2. **局部 Prompt 只写框内内容：**


natural human hand with five fingers, relaxed pose,
matching skin tone and lighting of surrounding area


3. 锁定画面 99%，只重绘 1%，光影自动融合

#### 三、废片变避坑指南（负面约束）

### ❌ 不要

- 极简客厅图出现数据线、宠物、脏墙 → 删图重抽，同一毛病反复出现

### ✅ 要

审视废片提取错误 → 写入排除指令：


ultra-minimalist living room, cream tones,
floor must be completely clean — no cables, clutter, or pets,
walls pristine, window shows clear blue sky without buildings blocking


| 废片问题 | 排除词 |
|---------|--------|
| 乱线 | messy cables, wires|
| 脏墙 | dirty spots, stains on wall|
| 多余宠物 | pets, animals|

**三轮工作流：**


定调：光影好的废片 → 存参考图
精修：主体细节不对 → 蒙版 + 局部 Prompt
清场：背景杂物 → 自然语言排除 / --no

