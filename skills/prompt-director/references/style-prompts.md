# 风格与质感词表

> 涵盖：§17 · §18
> 艺术家/美学借用 → [candid-capture.md](candid-capture.md) §4

## 胶卷（Film Stock）

| 胶卷 | 色调/用途 | 写法 |
|------|----------|------|
| Kodak Portra 400 | 肤色温润，人像/生活 | shot on Kodak Portra 400/ soft Kodak Portra 400 grain|
| Fujifilm Pro 400H | 偏冷，日系/清冷/风景 | Fujifilm Pro 400H color|
| Kodak Gold 200 | 暖调高饱和，怀旧街头 | Kodak Gold 200 warmth|
| Cinestill 800T | 夜景光晕 Halation，电影感 | Cinestill 800T, halation glow|

## 渲染引擎（数字化/商业）

| 引擎 | 用途 | 写法 |
|------|------|------|
| Unreal Engine 5 | 科幻、产品、超现实 | Unreal Engine 5|
| Octane Render | 商业广告级光影 | Octane Render|
| 光线追踪 | 反射折射真实 | ray tracing|

### ❌ 不要

- 胶卷词 + 渲染引擎词同句（如 Kodak Portra+ Octane Render）

---

### §17 风格提取三步法

**原则：** 风格 = 被拒绝的选项（约束逻辑），不是元素堆砌

#### 第一步：看「没什么」（单张约束）

| ❌ 不要 | ✅ 要 |
|--------|------|
| /describe或 描述这张图| 忽略内容，只分析形式：被拒绝的色调/快门/空间选项是什么？|
| 输出 女人、隧道、模糊、颗粒| 输出不可变约束：step-printing 拖影/ heavy cyan-green cast/ practical lights 引导线|
| 把偶然内容（刀、门框）当风格 | 只保留形式铁律：模糊类型、色偏、透视压迫感 |

#### 第二步：多样本提纯（找共性）

| ❌ 不要 | ✅ 要 |
|--------|------|
| 单张图定风格 → 过拟合偶然元素 | 3 张「内容不同、视觉同源」图同批投喂 |
| 每张单独问 | 找出三张图的视觉共性，忽略剧情与道具|
| 把「拿刀」「几何门框」写进风格包 | 共性层：单色色谱 / 逆光剪影 / 高密度大气介质 |

**《沙丘》类风格 DNA 示例槽：**

| 共性维度 | 写法片段 |
|---------|---------|
| 色彩 | monochromatic amber/ochre, no blue/green/vibrant red|
| 光影 | absolute backlight, silhouettes, no facial detail|
| 大气 | heavy haze/dust, rapid aerial perspective|

#### 第三步：四维风格包（可迁移）

| 板块 | ❌ 不要 | ✅ 要 |
|------|--------|------|
| 空间构图 | 绑定「玉米地」「宇航服」 | IMAX wide, tiny figure in vast landscape, horizon line|
| 光线氛围 | neon、studio fill| natural/practical light, dusty atmosphere, harsh sunlight, no artificial fill|
| 色彩质感 | 高饱和鲜艳 | muted earth tones, desaturated, Kodak Vision3 grain, matte finish|
| 负向约束 | 无 --no| --no neon, cyberpunk, glossy plastic, 3d render, vibrant colors, holograms|

---

### §18 Midjourney 人像去油腻

**原则：** MJ 默认 Effect 优先；用「降维」拉回 Material + 物理光 + 光学柔和

#### 材质降维

| ❌ 不要 | ✅ 要 |
|--------|------|
| perfect skin, smooth face, highly detailed, 8k render| biological skin texture, visible pores, uneven skin tone|
| soft skin, glossy finish, unreal engine style| fine peach fuzz, subsurface scattering on ears/nose|
| 只写视觉亮感 shiny, bright| 触觉系：raw photograph, digital noise|
| 默认美颜 | 加 --style raw（v7） |

#### 光影降维

| ❌ 不要 | ✅ 要 |
|--------|------|
| golden hour, cinematic mood, soft diffused glow across face| harsh direct camera flash, hard shadows on nose/chin|
| dreamy atmosphere, polished skin| Rembrandt lighting或 flashlit snapshot：高光点状非片状 |
| 漫反射包脸 → 油膜感 | 物理切割：key light from [方向]+ 明确暗部保留 |

#### 锐度降维

| ❌ 不要 | ✅ 要 |
|--------|------|
| sharp focus, hyper detailed| soft optical focus, low contrast edges|
| 数码锐化 → 塑料紧绷 | film halation around highlights|
| 无媒介声明 | Kodak Portra 400 grain, analog texture|
| — | without over-sharpening（或 --no over-sharpening） |

**去油腻组合示例：**


extreme close-up candid photograph, biological skin texture, visible pores,
fine peach fuzz, uneven skin tone, harsh direct camera flash, hard shadows,
soft optical lens quality, film halation around highlights,
Kodak Portra 400 grain, low contrast edges
--style raw --no glossy skin, smooth face, 8k render, cinematic glow

