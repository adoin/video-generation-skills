# 光线控制

> 涵盖：§2 · §20 · §25 · §47
> 写法必须同时给出：**方向、光比、色温**（室外人像/街景）；室内另加**光源实体、衰减路径、反射**

---

## §2 光的方向、光比、色温（室外/通用）

### ❌ 不要


cinematic lighting, detailed portrait

- 无方向、无照射对象、无阴影结果 → 全亮、无体积、主体浮

### ✅ 要


soft sunlight entering from the right window, lighting the subject's face,
casting long shadows on the table

- 必须包含：from [方向]+ lighting [对象]+ casting [阴影/高光结果]

**布光角色写法：**


(subject), lit by warm key light from the right,
soft fill light from the left, creating balanced shadows


| 光位 | 写法片段 |
|------|---------|
| 右侧窗光 | soft sunlight entering from the right window|
| 伦勃朗侧光 | 45-degree key light from upper left, triangle shadow on cheek|
| 逆光轮廓 | backlight separating subject from background|

---

## 二、光比（亮暗分布）

### ❌ 不要

- 只写 high quality lighting/ 不写明暗区域
- 让 AI 自行平均亮度

### ✅ 要


a man standing under a streetlight, face illuminated brightly,
background fading into shadow, strong contrast ratio, smooth light falloff


或：


strong contrast lighting, bright on face, dark background, deep shadow on left side


| 目标 | 写法 |
|------|------|
| 主体亮、背景暗 | face illuminated brightly, background fading into shadow|
| 强对比 | strong contrast ratio, smooth light falloff|
| 低对比均匀 | soft even lighting, minimal shadow|

---

## 三、色温

### ❌ 不要


warm lighting

- 整图偏橙，像套滤镜

### ✅ 要


warm sunlight hitting the character's face, cool blue ambient light in the background

- 前景暖 + 背景冷，分出层次

| 时段 | 写法 |
|------|------|
| 清晨 | misty morning light, cool tone|
| 正午 | neutral daylight|
| 傍晚 | golden hour sunlight|
| 夜晚 | warm lamp light, cool ambient shadow|

---

## 四、综合模板（室外直接套用）


a woman standing near a window,
lit by warm sunlight entering from the right,
soft highlight on her face, background in cool shadow,
medium contrast lighting ratio, smooth gradient light transition


---

### §20 室内光线

**原则：** 室内 = 封闭黑盒；拒绝无源漫反射白光

#### 光源实体（先定义谁发光）

| ❌ 不要 | ✅ 要 |
|--------|------|
| cozy living room, warm light, 8k（无光源实体） | [场景] + [具体发光体] + [光线投射动作] + [受光物]|
| AI 随机抓物体当光源 → 光位混乱 | 窗光：afternoon sun through sheer curtains casting striped shadows on floor|
| 无宿主之光 | 人造光：neon sign from left casting magenta rim on wet pavement|

#### 衰减路径（写路程，不写亮度形容词）

| ❌ 不要 | ✅ 要 |
|--------|------|
| soft, weak, bright当主指令 | 写光从哪开始、在哪消失 |
| 柔光→ 阴影全提亮、画面发灰 | candle strictly illuminates book pages and fingers, rapid falloff to shoulders, shelves in deep shadow|
| 这里很暗| light doesn't reach [区域]→ AI 自动拉开层次 |

| 衰减词 | 用途 |
|--------|------|
| rapid falloff / high contrast falloff| 黑色电影、强戏剧 |
| gradual fade / soft gradient| 日系家居、漫延感 |
| pool of light| 光圈外全黑 |

#### 反射填充（第二束光）

| ❌ 不要 | ✅ 要 |
|--------|------|
| 大灯直射 → 探照灯效应、死黑阴影 | 写主光撞击材质后的反弹 |
| 只写主光无环境填充 | sun hits polished orange floor, warm bounce fills white ceiling and wall shadows|
| 不定义反光面材质 | matte/rough吸收柔化；glossy/polished强镜面反射 |

**室内公式：**


[场景] + [key light 实体与方向] + [falloff 终点] + [bounce: 材质→反射色温填充暗部]


---

### §25 环境光与天气

**原则：** 环境塑料感常来自「自动补光」；用因果链 + 光矢量替代标签

#### 光影因果（动词连接名词）

| ❌ 不要 | ✅ 要 |
|--------|------|
| sunlight, window, sofa, plants名词并列 | Because plants block window light, dappled shadows fall on face and cushions|
| rainy street, neon, puddles| neon reflects in oily puddles, ripples distort reflection|
| 元素无相互作用 → 拼贴感 | 每条光路写：[光源] → [遮挡/介质] → [落点阴影/反射]|

#### 光矢量（方向 + 反差 + 介质）

| ❌ 不要 | ✅ 要 |
|--------|------|
| perfect lighting, clean composition| rim lighting勾轮廓；volumetric lighting让光可见 |
| 害怕暗部 → 画面平 | chiaroscuro/ low key lighting：大面积暗，只留关键细节 |
| split lighting无方向 | harsh light source from left, pitch-black shadow on right cheek|

#### 天气 = 环境状态（非 Tag）

| ❌ 不要 | ✅ 要 |
|--------|------|
| raining| mist rising from warm ground, clothes soaked and clinging to body|
| windy| hair whipped across face, trash tumbling in turbulent air|
| 天气词无物理后果 | 写天气如何改变：材质、衣物、能见度、反光 |

#### 空间景深（破平面背景）

| ❌ 不要 | ✅ 要 |
|--------|------|
| a bustling street/ a forest单词标签 | 分层写：前景遮挡 → 中景接触 → 远景退晕 |
| 人物「贴」在背景布前 | 前景：blurred fern fronds obstructing lens, peeking through|
| 无物理接触 | 中景：boots sinking into saturated mud, hand on mossy rock|
| 无纵深 | 远景：pine layers fade into fog, distant mountains barely visible|

**线性扫描模板：**


Foreground: [遮挡/失焦元素] →
Midground: [主体 + 与地面/物体物理接触] →
Background: [大气透视退晕 + 远处轮廓]


---

## §47 光影重构：提示词到后期控光

> 与 §20/§25 去重：本文管**方向失效**的修正策略与**去光再加光**工作流；基础三要素仍见上文。
> 视觉标注箭头 → [edit-fusion.md](edit-fusion.md) §44

### 提示词：写效果不写来源

### ❌ 不要


light from left
side lighting
cinematic lighting

- AI 按像素惯性猜方向 → 左右随机；只写来源不写落点与阴影后果

### ✅ 要

| 层级 | 写法 |
|------|------|
| 初级 | 从左侧打光→ 仍不稳 |
| 中级 | 侧面照明，戏剧性阴影|
| 高级 | 伦勃朗照明，45° 主光，面颊三角光斑，强明暗对比，暗背景|

- 用灯位术语替代左右：Rembrandt lighting/ rim light from behind/ key light from upper left
- 必须写**物理效果**：bright highlight on cheekbone, deep shadow swallowing opposite side

### 初阶：Tapnow 打光（底图已满意）

### ❌ 不要

- 在提示词里死磕改光十几次 → 原图像素惯性难推翻

### ✅ 要

- Tapnow 3D 画布拖拽光源 → 快速试色与半径；适合单主体、浅场景

### 进阶：去光 → 标注 → 加光（Nano Banana Pro）

### ❌ 不要

- 直接在复杂原图上硬盖新光 → 旧光影残留打架

### ✅ 要


1. 提示词去光：even diffuse ambient, remove strong directional shadows（还原散射底噪）
2. 画面画箭头标主光/补光方向
3. 提示词：蓝色箭头方向伦勃朗主光，红色箭头方向微弱柔光补亮暗部


**核心：** 光影不是赌注，而是可定向的叙事工具；复杂场景先净底再布光。

