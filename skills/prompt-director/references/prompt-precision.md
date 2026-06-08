# 提示词精度控制：扰动、剪词、鲁棒性破坏、特征塌陷、幻觉链

> 涵盖：§5 · §6 · §7 · §8 · §10 · §12
> 工具：Midjourney --no/ ::权重 · Stable Diffusion 负向提示词 · CFG Scale

---

## 与相邻文件的分工

| 文件 | 做什么 |
|------|--------|
| [candid-capture.md](candid-capture.md) | 主动加什么（抓拍、颗粒、真实皮肤） |
| [time-causality.md](time-causality.md) | 时间词、假因果（叙事因果） |
| [composition.md](composition.md) | 伪透视、空间纵深 |
| 本文 | 注意力干预、负向剪词、可控失控、信息塌陷、幻觉链引导 |

---

## §5 反向控制：禁止词、拆解抽象词、锁定边界

> 分工：--no 速查入口；塑料皮/脏纹理/假光完整词表见 §7。

### 用 --no拒绝 AI 默认加戏

**❌ 不要**


Ultra realistic

（会触发过度锐化、塑料皮肤）

**✅ 要**


Soft natural skin texture
--no over-sharpening, plastic skin, heavy contrast


**✅ 要（干净背景）**


Clean minimalistic background
--no grunge, noise, chaotic details


### 抽象形容词 → 具体视觉写法

**规则：不要写抽象词，改写为可看见的光/镜/构图词。**

| ❌ 不要写 | ✅ 改为 |
|----------|--------|
| Dreamy| Low saturation+ Soft diffused light+ Telephoto lens|
| High-end| Strong light contrast+ Negative space+ Clean composition|
| Texture| Subtle side lighting+ High shadow contrast+ Macro details|

### 锁定边界（禁止 AI 自动补齐）

**❌ 不要**


A car in street.


**✅ 要**


A classic yellow Jaguar E-Type parked in front of a brownstone building in Manhattan,
warm side light from late afternoon, wet asphalt reflections


**边界检查：** 地点具体到城市/建筑；背景数量可控；干净背景时配 --no噪点/杂乱细节。

---

## §6 扰动词

**归入文件:** 本文

**原理：** 扰动词（Noise / Distraction Token）不描述画面内容，但占用注意力权重，让 AI 不再死磕某一类词（主体细节、抽象滤镜、背景自动补齐）。

### ❌ 不要

- 主体词堆满 8k, ultra detailed, sharp face, cinematic texture→ 皮肤蜡化、毛发过硬、噪点爆炸
- 抽象词裸写 dreamy, soft light, misty atmosphere→ AI 自动加大光斑、粉光、雾化滤镜
- 只写 女孩在森林里不写光线/密度 → AI 自由补光补雾补树，背景抢戏
- 多效果词同时写、无顺序 → 光影/背景/滤镜互相抢占，主体落地晚、比例漂移
- 扰动词权重过高（>0.9）或乱塞无意义词 → 画面发虚、语义丢失

### ✅ 要

- **主体先落地：** 句首写主体 + 基础光影，再叠氛围
- **扰动词占位：** 放在主体后或效果词前，权重 **0.3～0.9**（模型越「用力」越高）
- **效果分层量化：** 氛围/滤镜用 low / medium / high或 ::0.3控制强度
- **三类打法对号入座：**
  1. 主体自然化 — 削弱过度锐化
  2. 抽象稳定化 — 削弱梦幻/柔和词的滤镜夸张
  3. 顺序控制 — 主体落地后再叠光斑/虚化

**用法一｜主体自然化**


A young woman in a misty forest, soft natural skin texture, gentle ambient light,
subject-priority token::0.5, natural imperfection::0.4


**用法二｜抽象稳定化**


A portrait in a garden, soft diffused light, low saturation,
base-style token::0.4, dreamy atmosphere::0.3, hazy glow::0.2

（dreamy降权；扰动词吸收多余「滤镜算力」）

**用法三｜多效果顺序控制**


[主体 + 基础光] → subject-priority token::0.5 → [氛围词 low 权重] → [装饰性光斑 optional]


**工作流：** 先低强度生成 → 对比 → 微调扰动词权重或效果强度。

---

## §7 剪词

**归入文件:** 本文

> 分工：负向词表主文件；正向真实皮肤见 [candid-capture.md](candid-capture.md)。

**原理：** 剪词 = 负向减法，让 AI 收敛时避开错误补偿（脏感、塑料感、假光），把算力留给主干信息。

### ❌ 不要

- 正向堆 高清、super detailed、8k、sharp face、照片级、超写实→ 触发过度纹理补偿
- 生成失败后才加 --no→ 剪词应是**前置结构**，不是事后补救
- 只写一两个词如 --no bad→ 覆盖面不足，挡不住自动补偿
- 正向又长又乱、剪词却很少 → 模型越不确定越乱补

### ✅ 要

**第一步：纯正向框架（不加滤镜意图）**


[主体] + [场景] + [光线方向] + [摄影参数] + [构图] + [风格主旨]


**第二步：分组剪词（每类选 3～5 个即可）**

| 剪什么 | 负向词（Midjourney --no/ SD Negative） |
|--------|------------------------------------------|
| 脏感 | noise, grain overlay, atmospheric haze, dust particles, grunge, muddy colors, chaotic details, fog overload|
| 塑料感 | plastic skin, wax texture, over-sharpening, glossy skin, harsh edge highlights, artificial reflections, chrome-like skin|
| 假光 | floating glow, lens flare abuse, bloom overload, god rays without source, soft haze light, rim glow without light source, ethereal mist light|

**组合示例**


A woman sitting by the window at right one-third, warm side light from left,
natural skin texture, 50mm lens
--no plastic skin, wax texture, floating glow, atmospheric haze, grunge, chaotic details


**调试法：** 分别只剪脏感 / 只剪塑料 / 只剪假光 / 全剪，观察哪类影响最大，固化个人模板。

---

## §8 鲁棒性破坏

**归入文件:** 本文

> 分工：抓拍偏主动加松弛词；鲁棒性破坏偏打破 AI 默认安全构图/均匀光。可组合，勿重复堆词。

**原理：** 提示词越稳，AI 越推向统计平均（模板化 AI 味）。鲁棒性破坏 = 可控范围内制造轻微不确定，保留方向、放开细节。

### ❌ 不要

- 乱写无关词 → 质量下降，不是艺术化
- 提示词越长越细 → 模型更稳、更模板
- 强风格滤镜堆满 → 风格一致性 = AI 塑料感
- 把「失控」理解成放弃主体描述 → 仍需主体 + 场景锚点

### ✅ 要

**心法：** 控制方向，不控制细节 — 像对模特说「自然一点」。

**方法 1｜构图破坏（选取 2～4 个）**


off-center framing, subject slightly off-axis, foreground obstruction,
slight dutch angle, casual asymmetrical composition, imperfect balance,
subject drift from center, unbalanced negative space


**方法 2｜光线破坏**


uneven lighting, inconsistent brightness, light spill,
mixed color temperature, overexposed highlights, underexposed shadows,
chaotic ambient light, light filtering unevenly through dusty window


**对比示例**


❌ A woman sitting by the window, soft light
✅ A woman casually leans against the window where light filters unevenly,
   mixed warm and cool tones, slight overexposure on the shoulder, off-center framing


**方法 3｜风格破坏**


inconsistent film grain, edge softness, slight texture mismatch,
imperfect focus, raw unpolished texture, subtle color drift, unretouched look


**三维度组合模板**


[构图基准 + 构图破坏] + [光线基准 + 光线破坏] + [风格基准 + 风格破坏]



A woman in a cafe, off-center framing, foreground cup partially blocking view,
uneven window light with mixed color temperature, Kodak Portra 400 grain,
slight color drift, unretouched look


---

## §10 特征塌陷

**归入文件:** 本文

> 分工：塌陷聚焦信息压缩（虚化/边缘衰减/局部锚点），非构图光线偏移。

**原理：** 算力有限时，AI 对非核心区域生成「统计平均」→ 细节丢失、边缘融化。主动诱导塌陷 = 模拟记忆/梦境的聚焦机制。

### ❌ 不要

- 全画面写满高清细节 → 糖水片、观众不知看哪里
- 背景流水账（路人袜子颜色都写） → 算力分散、主体崩坏
- 全图都糊、无锚点 → 不是艺术，是废片
- 背景油画塌陷 + 主体 3D 渲染风混搭 → 风格分裂
- 高清出图再 PS 高斯模糊 → 物理模糊 ≠ 语义塌陷

### ✅ 要

**技巧 1｜压缩非主体**


A cinematic portrait of a young woman on a city street at night.
Focus exclusively on her eyes and facial expression.
The busy city background rendered as soft creamy bokeh and abstract light circles.
Shallow depth of field isolates the subject.


**负向强化（SD）**


(detailed background:1.5), (complex pattern:1.3), clutter, busy, realistic background


**技巧 2｜特征衰减（情绪张力）**


motion blur, dissolving edges, smoke-like form, ethereal fade,
long exposure light streaks, semi-transparent body, melting contours


**技巧 3｜局部锚点（极虚 vs 极实）**


focus on eyes::2, hyper-detailed iris::1.5, razor-sharp on eyes

（MJ）；SD 用 (focus on eyes:1.5), (intricate jewelry:1.4)

**参数：** MJ --stop 80～90保留半塌陷质感；SD CFG 5～6 更易绘画感塌陷。

**风格配方**

| 风格 | 配方 |
|------|------|
| 情绪肖像 | 背景塌陷 + 眼神锐利 + 胶片颗粒 |
| 梦核/阈限 | 全局衰减 + 低对比 + 光晕 |
| 赛博写意 | 霓虹运动模糊 + 前景金属锚点锐利 |

**情绪肖像完整示例**


A moody cinematic portrait shot through a glass window on a rainy night.
Low-key chiaroscuro, illuminating only half of the subject's face;
hair and contours merge into dark shadows.
Focus razor-sharp on the eyes, deep loneliness.
Rich film grain, somber color palette.


**赛博写意完整示例**


A fine art photograph of a cyberpunk city at night during rainstorm, long exposure.
City lights streak into neon color lines, impressionistic background collapse.
In the foreground, a metallic robotic hand holding a glowing object remains perfectly sharp.
High contrast futuristic atmosphere.


---

## §12 幻觉链反应

**归入文件:** 本文

> 分工：扰动词分散注意力；幻觉链引导误读；边界锁定写死背景元素。

**原理：** AI 误读一词 → 自动补全逻辑 → 细节虚构爆发（多米诺）。预判链条 = 做「牧羊人」。

### 链条三阶段

| 阶段 | 机制 | 对策 |
|------|------|------|
| 词义偏读 | 多义词被读偏 | 无害偏读注入 |
| 逻辑补全 | 按误读脑补环境 | 方向锁定 |
| 细节虚构 | 过拟合加累赘 | 反向锚定 / 截断 |

### ❌ 不要

- 裸写易偏词：Hazy light/ Lonely/ Deep forest, heavy fog→ 雾霾废土、贫民窟、恐怖沼泽
- 易偏词后不加定性语境 → 链条向脏乱/阴间漂移
- 细节虚构阶段无 --no或 void background→ 背景乱建、多指多脸

### ✅ 要

**阶段 1｜无害偏读：** 抽象词旁加审美底线语境


❌ Hazy light, street photography
✅ Hazy light, dreamlike mechanism, glowing dust, street photography


**阶段 2｜方向锁定：** [易误读词] + [强制视觉定性词]


❌ Deep forest, heavy fog, hazy atmosphere, realistic
✅ Deep forest, heavy fog, bioluminescent blue ether, mint green haze, magical clean air



Hazy street alley, raining, damp atmosphere,
liquid chrome texture, futuristic white marble floor, sterile clean


**阶段 3｜反向锚定：** 末尾截断发散


Cyberpunk helmet design, intricate details,
dramatic spotlight, surrounded by total darkness, void background, minimal


**完整复盘：赛博雨夜少女**


❌ Cyberpunk girl, raining night, lonely
   → lonely 偏读为破败 → 破烂衣服、垃圾背景

✅ Cyberpunk girl, solitary grandeur, cinematic isolation,
   neon rain reflecting on clean wet pavement,
   melancholic but elegant, not poverty,
   void background, minimal clutter


**操作口诀：** 起点给「美丽的错误选项」→ 中段修「单行道」→ 末尾喊 Cut。

---

## 跨节组合公式（§5–§8、§10、§12）


[主体写死] → [构图/光线基准] → [可选：鲁棒性破坏词 2～4 个]
→ [可选：扰动词占位] → [氛围词低权重]
→ [剪词 --no 前置] → [可选：特征塌陷 + 局部锚点]
→ [幻觉链：易偏词 + 定性锁 + 末尾截断]


时间叙事、假因果见 [time-causality.md](time-causality.md)；空间纵深见 [composition.md](composition.md)。
