# 相机角度、焦段与镜头情绪

> 涵盖：§3 · §21 · §33 · §36 · §41
> 图生视频运镜冲突 → [video-prompt.md](video-prompt.md) §50；氛围虚实 → [atmosphere.md](atmosphere.md) §32

**硬性规则：角度和焦段必须成对写。**

---

## §3 角度与焦段基础

### 相机角度

| 角度 | 什么时候用 | 写法 |
|------|-----------|------|
| 平视 | 纪实、街拍、产品、最真实 | eye-level angle, camera at human eye height, natural perspective|
| 低角度仰视 | 力量感、史诗、商业冲击 | low-angle shot, camera near ground, slight upward perspective|
| 高角度俯视 | 戏剧编排、时尚、上帝视角 | high-angle shot, overhead view, dramatic top-down perspective|

### ❌ 不要

- 只写 portrait/ close-up不写焦段 → 脸型随机变形
- 只写角度不写焦段（或反之）

### ✅ 要


close-up portrait shot with 85mm lens, f1.8


### 焦段速查

| 焦段 | 效果 | 写法 |
|------|------|------|
| 24–35mm | 空间大、环境叙事 | 35mm lens, wide perspective, cinematic depth|
| 50mm | 最接近人眼、写实 | 50mm lens, natural field of view|
| 85mm | 人像、背景虚化 | 85mm portrait lens, shallow depth of field, soft bokeh|
| 鱼眼 | 夸张冲击 | fisheye lens, exaggerated perspective|

### 角度 + 焦段组合

| 场景 | 组合 |
|------|------|
| 纪实真实 | eye-level+ 35mm f/2.8|
| 人像广告 | low-angle+ 85mm f/1.8|
| 电影环境人像 | eye-level+ 35mm f/2.8+ cinematic depth|

---

## §21 告别摆拍运镜

> 与 §36 蒙太奇、§39 前景遮挡联动；与 [video-prompt.md](video-prompt.md) §50 互斥运镜规则一致。

### 方法一：不完整起幅

**❌ 不要** 首帧完美居中定妆照

**✅ 要**
- 首帧：铁丝网遮挡 / 构图偏移 / 窥视视角 / 部分失焦
- 视频：[起始状态] + [运镜寻找主体] + [最终落幅]

starts partially obscured by foreground blur, camera slowly reveals subject in focus


### 方法二：轨迹去平滑

**❌ 不要** smooth cinematic camera movement（模拟手持时）

**✅ 要**
- handheld micro-shake/ decelerating push-in/ micro-pause before settling
- 推进带减速，非匀速直线

### 方法三：延迟跟随

**❌ 不要** 镜头与主体同步完美预判

**✅ 要**
- 主体先动，镜头稍后跟上（camera follows with slight delay）
- 制造「人在拍、机在追」的呼吸感

---

### §33 镜头情绪匹配三维度

> 与 §3 去重：§3 给焦段表；§33 给**情绪→景别/焦段**匹配与逻辑归一。

#### 一、景别控制心理距离

**远景 Long Shot — 情绪去参与化**

### ❌ 不要

- 表达狂喜/恐惧高潮却用远景 → 表情肢体被稀释

### ✅ 要


Extreme long shot, tiny lone figure in vast snowy landscape,
immense mountains under overcast sky, deep loneliness and fate,
muted cold tones, epic scale, --ar 21:9

- 适用：孤独、渺小、无力、史诗、宿命

**中景 Medium Shot — 叙事最佳载体**

### ❌ 不要

- 情绪崩溃高潮 / 战场气势全程中景 → 张力不足像情景喜剧

### ✅ 要


Medium shot, waist-up, woman leaning against train window at golden hour,
wind moving loose linen shirt, dust motes in glowing light,
nostalgic atmosphere, environment relationship visible, --ar 16:9

- 适用：日常对话、情节推进、人与环境互动

**特写 Close-up — 情绪放大器**

### ❌ 不要

- 无铺垫直接 Extreme Close-up 流泪 → 生硬惊悚无法共情

### ✅ 要

- 远景/中景铺垫后，高潮时刻上特写
- 视频：静帧特写 + 微动 Prompt（见 §29）

#### 二、焦段控制空间压迫

| 焦段区间 | 情绪语言 | 适用 |
|---------|---------|------|
| 8–14mm 鱼眼 | 怪诞、压迫、监控感 | 赛博仰拍、CCTV 伪纪实 |
| 24–35mm 广角 | 临场、宏大、人在环境中 | 废土建置、Vlog、全身动感 |
| 50mm 标准 | 平静、客观、真实 | 日常写实、消除 AI 用力感 |
| 85mm 人像 | 唯美、专注、商业质感 | 电商模特、情绪半身 |
| 135–200mm 长焦 | 偷窥、疏离、空间压缩 | 王家卫式人群孤独 |

**广角压迫示例：**

### ✅ 要


Low-angle wide shot, 16mm lens, rain-soaked street at night,
wet asphalt reflecting chaotic neon, pedestrians as motion-blurred shadows,
high contrast, dynamic energy, unsettling perspective distortion


**长焦隔离示例：**

### ✅ 要


200mm telephoto, extreme spatial compression,
exhausted office worker frozen in crowded crosswalk,
foreground shoulders heavily blurred, background buildings unnaturally close,
shallow DOF isolating tired face, cold blue tones


#### 三、统一空间逻辑——逻辑归一

### ❌ 不要


Long shot, wide angle lens, extremely shallow depth of field, background compressed

- 远景需深景深交代环境 + 广角拉开纵深 + 长焦压缩背景 = 三矛盾缝合怪

### ✅ 要

| 目标情绪 | 景别 + 焦段 + 景深 |
|---------|-------------------|
| 压迫感 | 特写/中景 + 广角畸变仰拍 **或** 长焦压缩 |
| 大动态视效 | 全景/中景 + 超广角透视差 + 动感模糊 |
| 纪实人像 | 中近景 + 85mm + 浅景深 |
| 环境叙事 | 中景 + 35mm + 较深景深 |

**片场搭建顺序写 Prompt：**


摄像机位置 → 镜头焦段 → 与演员距离 → 景深 → 光线


---

### §36 打破摆拍感：情绪蒙太奇

> 与 §29 去重：§29 控单镜头微表情幅度；§36 控**多镜头情绪节奏**（环境/对比/特写）。
> 与 [director-storyboard.md](director-storyboard.md) §34 剪辑思维配合使用。

#### 一、用环境代替情绪（客观对应物）

### ❌ 不要


A young man standing in the room, looking very sad, crying, depressed.

- 高清哭泣大头照 → 假哭素材库感

### ✅ 要


Cinematic wide shot, lone figure sitting in empty dim apartment, back to camera,
heavy rain pounding floor-to-ceiling windows blurring city neon outside,
wilted potted plant on table, cold blue-gray tones, high contrast melancholy

- 环境写满情绪，人物可不露脸

#### 二、用对比制造情绪冲突（库里肖夫效应）

### ❌ 不要

连续生成：奔跑 → 追车 → 砸桌 → 争吵（紧张+紧张+紧张）
- 视觉疲劳，情绪变平

### ✅ 要

**镜头 A（喧闹高点）：**


Chaotic crowded house party, warm golden light, people laughing and dancing,
champagne splashing, handheld energy, dense composition


**硬切 → 镜头 B（孤绝低点）：**


Same character alone in bathroom corner, harsh cold fluorescent light,
knees pulled to chest, absolute silence, extreme negative space

- 极动接极静 → 孤独窒息感爆发

#### 三、用特写放大情绪（强制聚焦）

### ❌ 不要


A man is very angry trying to hold back anger, standing in the office.

- 半身/全身 + 办公桌电脑 → 情绪被环境稀释

### ✅ 要

**手部特写：**


Extreme close-up macro shot of clenched fist on desk,
knuckles white, trembling slightly, veins visible,
shallow depth of field, dramatic side light, no face visible


**眼部特写：**


Extreme close-up of eyes only, pupils dilated, a single tear forming,
no background visible, forced intimate attention, cinematic grain

- 微距局部 → 情绪穿透力倍增，且不易崩脸

---

## §41 大透视空间感与实拍美学

> 与 [composition.md](composition.md) §39 前景遮挡、§9 伪透视联动；与 [consistency.md](consistency.md) §40 镜头前置互补。
> **算力原则：** 大透视场景少写服装款式，把权重留给空间、胶片色与场面调度。

### 压低机位与大透视

### ❌ 不要


90s Hong Kong street, man in worn jacket and collar shirt, detailed fabric texture, 8k

- 琐碎服装描述分散算力 → 标准平视、Z 轴坍塌、数码旁观者感


eye-level centered composition, clean sharp focus


### ✅ 要


ground-level low-angle wide shot, 24mm lens, strong upward perspective,
neon signs converging toward center, wet asphalt foreground,
simple dark jacket, muted vintage sweater,
prominent film grain, warm amber and cyan color grading

- 低机位强制消失点重组；两侧建筑向中心压迫 → 时代漂泊感与厚重感

### 前景遮挡确立 Z 轴

### ❌ 不要

- 低角度却无前景 → 全局绝对清晰，塑料景深

### ✅ 要


camera hidden behind blurred rain puddles and phone booth edge in extreme foreground,
shallow depth of field, subject sharp in midground,
retro amber bokeh, gritty film grain


### 摄影机物理状态

### ❌ 不要


smooth steady camera glide, perfect gimbal movement

- 零阻力滑动 → 浓重数码感

### ✅ 要


handheld camera with subtle breathing shake, physical weight from operator footsteps,
low-angle perspective reinforcing nostalgic documentary texture


### 完形心理：缓慢揭示

### ❌ 不要


wide shot revealing entire noodle shop, man and woman sitting back to back in center

- 首帧信息全盘托出 → 无探索欲

### ✅ 要


opening on blurred table legs and rising noodle steam in foreground,
slow lateral truck gradually revealing couple eating separately in corner,
wide-angle distortion, warm tungsten haze through steam


### 大透视标准工作流


1. 净化指令（剔除服装细节，只留身份+情绪）
2. 低角度确立透视骨架
3. 前景遮挡建 Z 轴层次
4. 胶片色彩术语消数码痕迹
5. 注入手持呼吸等物理瑕疵

