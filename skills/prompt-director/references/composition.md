# 构图与空间纵深

> 涵盖：§1 · §9 · §26 · §39
> 工具：Midjourney --ar/ --s

---

## §1 构图位置与平衡

### 主体位置

**❌ 不要**


a girl standing in a field, cinematic lighting


**✅ 要**


a girl standing in a field, positioned at left one-third of the frame,
soft sunlight from right, --ar 3:4


| 需求 | 写法 |
|------|------|
| 偏左 | subject positioned at left one-third of the frame|
| 偏右 | subject at right one-third of the frame|
| 偏上 | subject placed at top one-third of the frame|
| 偏下 | subject positioned near bottom third|

### 视觉动线

**❌ 不要**


a man walking on the street, cinematic lighting


**✅ 要**


a man walking on the street, positioned at right one-third of the frame,
road leading lines from bottom-left toward the subject,
sunlight diagonal from top-right, --ar 3:4


| 动线类型 | 写法 |
|---------|------|
| 道路 | leading lines from foreground toward the subject|
| 光线 | diagonal light from top-right guiding viewer's eye|
| 透视 | path leading into depth, vanishing perspective|
| 目光 | subject looking toward distant light|

### 画面平衡

**❌ 不要**


a woman sitting by the window, cinematic light


**✅ 要**


a woman sitting by the window at right one-third,
balanced by soft shadow and curtain on the left,
asymmetrical composition, warm side light, --ar 3:4


### §1 组合模板


[主体], positioned at [left/right/top/bottom] one-third of the frame,
[leading lines / light direction] guiding toward the subject,
[balance element description],
[lighting style], [environment], --ar 3:4


---

## §9 伪透视

**归入文件:** 本文

> 分工：§1 给动线/平衡；§9 展开线性/空气/尺度透视。焦段细节见 [camera-movement.md](camera-movement.md)。

**原理：** AI 不懂真实三维，只模仿像素排列规律。伪透视词诱导算法误判纵深需求，打破默认 35–50mm 平面感。

### ❌ 不要

- 静态方位堆砌：A street, buildings on both sides, blue sky→ 正视立面、无消失点
- 环境物件堆砌：A forest with many trees, bushes, grass, rocks, mountains→ 元素挤在同一平面
- 均衡比例：A man standing in front of a tall building→ 游客照式 1/3 人 2/3 楼
- 画面塞满无留白 → 无空间表现「距离」
- 正方形画幅做电影级大透视 → 1:1 最难表现纵深
- Midjourney --s 1000追求物理空间感 → 过高 stylize 牺牲透视逻辑（建议 --s 100–250）

### ✅ 要

**三大核心维度 + 镜头 + 光影**

---

### 维度 1｜线性延伸（方向词 / 消失点）

用矢量趋势替代静态方位。

**❌ 不要**


A street, buildings on both sides, blue sky.


**✅ 要**


A street stretching into the infinite horizon, buildings on both sides,
converging lines, leading towards a distant point,
strong perspective, wide angle, deep depth.


**方向词库：** stretching into, converging lines, vanishing point, leading towards, infinite horizon, receding into distance, one-point perspective

---

### 维度 2｜空气透视（密度词 / 不写环境写空气）

近处清晰对比高，远处模糊对比低 — 用雾气与虚化切层级。

**❌ 不要**


A forest with many trees, bushes, grass, rocks, mountains in the back.


**✅ 要**


A forest, layered fog, volumetric lighting, atmospheric depth,
foreground bokeh, misty background.


**密度词库：** layered fog, volumetric lighting, atmospheric depth, foreground bokeh, misty background, aerial perspective, haze gradient, depth haze

---

### 维度 3｜强制透视（尺度反差）

极端近大远小，打破 50mm 平庸视角。

**❌ 不要**


A man standing in front of a tall building.


**✅ 要**


A tiny silhouette of a man looking up at a gigantic monolithic skyscraper,
extreme low angle, worm's-eye view, overwhelming scale, dramatic contrast.


**尺度词库：** tiny silhouette, gigantic, monolithic, extreme low angle, worm's-eye view, overwhelming scale, dramatic scale contrast, bird's-eye view

---

### 镜头代码（焦段外挂）

| 焦段 | 效果 | 魔法词 | 适用 |
|------|------|--------|------|
| 广角 14–24mm | 桶形畸变、拉长近处线条 | wide angle, 14mm, barrel distortion, exaggerated perspective| 赛博街道、宫殿内部、动作场面 |
| 长焦 85–200mm | 空间压缩、层叠感 | telephoto compression, 85mm, 200mm, flattened depth layers| 孤独背影、悬日、极简构图 |
| 移轴 | 微缩模型感 | tilt-shift, miniature effect, selective focus band| 城市俯瞰、小人国 |

**进阶：** 广角 + action shot→ 物体仿佛冲出画面。

---

### 光影雕刻空间（明暗切分前中后景）

**明暗对照 Chiaroscuro**


Chiaroscuro lighting, deep shadows receding into background,
bright subject jumping forward, strong tonal separation.


**逆光剪影**


Strong backlight, subject as dark silhouette,
background separated by brightness, depth through contrast only.


**丁达尔效应（可视透视线）**


Tyndall effect, visible light beams through dust,
radiating lines pointing toward vanishing point.


---

### 三套实战公式

**公式一｜无限延伸流**（街道、走廊、赛博朋克）


[主体/场景] + [线性引导词] + [消失点描述] + [广角镜头参数]



A neon cyberpunk alley stretching into the infinite horizon,
converging lines, leading towards a distant glowing vanishing point,
wide angle 18mm, strong perspective, --ar 21:9


**公式二｜巨物压迫流**（奇幻、科幻、史诗）


[渺小主体] + [巨大对立物] + [仰视视角] + [尺度对比词]



A tiny lone astronaut before a colossal ancient alien gate,
worm's-eye view, overwhelming scale, dramatic contrast, --ar 9:16


**公式三｜空气纵深流**（风景、森林、悬疑）


[前景遮挡物] + [中景主体] + [多层雾气] + [虚化背景]



Foreground tree branches framing the view,
a figure in mid-ground forest, layered fog, volumetric light rays,
misty background fading to white, atmospheric depth.


**留白修正：** 透视弱时加 minimalism, negative space给视线跑道。

**画幅建议：** 左右延伸用 --ar 16:9或 21:9；上下落差用 --ar 9:16。

---

## §26 三大构图原则

> 与 §1 去重：§1 给公式与写法表；§26 补**负空间/视频调度/产品构图**。

### 原则一：三分法 + 负空间

**❌ 不要**

a beautiful girl in the rain

- 默认居中证件照，视线阻断

**✅ 要**

woman sitting in cafe, positioned at right one-third,
gazing toward large negative space on the left showing rainy street outside


### 原则二：视觉动线

**❌ 不要** 主体居中 + 无引导元素

**✅ 要** 道路/栏杆/目光/光线对角线引向主体（见 §1 动线表）

### 原则三：视频与产品的构图调度

**❌ 不要** 视频首帧用居中定妆照 → 摆拍 PPT 感

**✅ 要**
- 视频首帧用三分法留白 → 便于 Pan Right 等运镜
- 产品：主体 + 光影配重（暗部衬亮部），非永远居中

---

## §39 前景遮挡：物理层与氛围层

> 与 §9 公式三「前景遮挡物」互补：§9 管纵深词库；§39 管**机位感**与**空气厚度**，破除塑料 AI 味。

### 物理遮挡——建立机位感

### ❌ 不要


A beautiful girl, white dress, standing in a forest, highly detailed face, 8k, cinematic lighting

- 只有主体无前景 → 悬浮全知之眼、壁纸感、零机位感
- 室内硬加树叶、沙漠硬加水滴玻璃 → 逻辑穿帮

### ✅ 要


Shot on ARRI Alexa 35, Leitz Summilux-C lens, shallow depth of field,
silhouetted edge of textured marble pillar heavily blurred in extreme foreground,
elegant woman on phone in dim luxury hotel lobby visible through the gap,
cinematic film grain, warm amber practical light

- 公式：[摄影参数] + [极度前景虚化叙事介质] + [中景主体动作] + [背景环境] + [胶片质感]
- 图生视频：镜头微微向前推进掠过柱子，女子紧张打电话→ 视差拉开裸眼 3D 感

### 氛围遮挡——让空气被看见

### ❌ 不要


Makoto Shinkai style, highly detailed, 8k, clean clear sky

- 8k / clean sharp focus抹除空气杂质 → 真空塑料感
- 只写丁达尔光无介质 → 光柱像后期硬涂

### ✅ 要


Tyndall effect, atmospheric haze, dust motes floating and glowing in sunbeams,
warm sunset light entering through window with visible volumetric rays,
subject softly wrapped in layered air, matte skin, breathing room depth

- 必须同时具备**发光源 + 受光介质**（particles/ haze/ dust motes）
- 图生视频：只写 空气中缓缓流动的发光灰尘即可撑起长镜头呼吸感

---

## 跨节组合公式（§1 + §9 + §39）


[主体] + [§1 构图位置/动线/平衡]
+ [§9 伪透视维度择一：线性 / 空气 / 尺度]
+ [可选：焦段参数] + [可选：光影切分]
+ [光线] + [风格], --ar [按透视选比例]


光线细则 → [lighting.md](lighting.md)；焦段运镜 → [camera-movement.md](camera-movement.md)。
