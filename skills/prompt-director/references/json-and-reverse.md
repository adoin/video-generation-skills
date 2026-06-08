# JSON 结构化提示词与误区

> 涵盖：§14 · §15 · §16 · §19 · §22 · §27 · §31 · §52
> 工具：ChatGPT / Gemini（翻译层）→ Midjourney / Flux / SD / 即梦 / Nano Banana

---

## 与相邻文件的分工

| 文件 | 做什么 |
|------|--------|
| [lighting.md](lighting.md) · [composition.md](composition.md) · [style-prompts.md](style-prompts.md) | 美学参数来源（JSON 的 Cinematography_Lock 填什么） |
| [video-prompt.md](video-prompt.md) | 图生视频运镜与时间线 |
| 本文 | JSON 架构、LLM 中台、锚点优先级、三大误区 |

---

## §16 反推拆解三法

> 与 §52 画面结构拆解互补：§16 管**静图反推**；§52 管**视频画面复刻**。

### 方法一：锁定不变项

**❌ 不要**

请描述这张图片，给我生成它的提示词。

- AI 描述「有什么」，不是你被击中的那个特征

**✅ 要**
- 先人工定「不变项」（构图/配色/压迫感角度等）
- 带答案提问：我要保留[特征]，提示词该怎么写才能稳定复现？

### 方法二：提取结构骨架

**❌ 不要**

这张图很有电影感，请写一个提示词。

- 只堆 Cinematic / 8K / Masterpiece

**✅ 要**
- 强制 AI 从生成系统视角输出：**构图 + 光照逻辑 + 空间关系**
- 风格词最后加；结构先锁死

### 方法三：A/B 验证闭环

**❌ 不要** 反推一次就用到底

**✅ 要**
1. 生成 A
2. 对比参考图差异
3. 只改一个结构变量再生成 B
4. 确认有效再定稿

---

## §19 参考图降维

> 与 §16 联动：§16 反推文字；§19 管**垫图时锁维度**。

### 误区一：把参考图当成品目标

**❌ 不要**
- 垫图 + Prompt 写与参考图冲突的内容（红鞋 vs 参考运动鞋）
- 期望「一模一样」

**✅ 要**
- **维度锁定**：明确只要构图 / 只要光影 / 只要材质
- 参考图 = 原材料仓库，告诉 AI 取哪一维

### 误区二：既要又要（图文冲突）

**❌ 不要**
- 参考图是阴影忧郁女孩，文字写阳光快乐女孩
- 参考图已有霓虹，文字再写 5 行霓虹描述

**✅ 要**
- **单点突破，文本留白**：参考图负责一维，文字只写差异部分
- 例：参考俯拍餐桌构图 → Prompt 只换产品和节日元素

### 误区三：用垫图弥补文本无能

**❌ 不要** 不会写 Prompt 就全靠垫图

**✅ 要** 先文后图三步：
1. 文字定义主体与风格
2. 参考图只锁一个维度
3. 生成后迭代文字，不反复换参考图

---

## §22 运动学反推

> 与 §16 区别：§16 静图；§22 **视频**反推运动矢量。

### ❌ 不要
- 只截一帧问「这画了什么」
- 要 AI 写散文影评（史诗感、充满希望…）

### ✅ 要

**三帧取样：** 起始帧 / 爆发帧 / 结尾帧 → 同时喂给视觉模型

**问法模板：**

分析这三帧之间：相机运动矢量、主体位移方向与速度、
景深变化、光影变化。输出可执行的图生视频 Prompt，不要形容词堆砌。


**输出形态：**

缓慢推进的低角度镜头；主体从远景向镜头加速靠近，
伴随景深收缩与尘土扬起。


---

## §27 脑海画面破译

> 与 §31 采访法互补：§27 偏**感觉→视觉翻译**；§31 偏**AI 追问选择题**。

### 方法一：感性具象化

**❌ 不要** 直接写 lonely but hopeful

**✅ 要** 三步：
1. 向 LLM 描述直觉感受（不专业也行）
2. 让 AI 拆解：光影 / 构图 / 色调 / 细节物件
3. 把拆解结果拼成绘图 Prompt

**LLM 指令模板：**

基于我描述的[氛围]，从摄影师角度拆解：
Lighting / Composition / Color Palette / Details 各给关键词。


### 方法二：参考图 + 文字混合（见 §19）

### 方法三：迭代对话而非一次生成

**❌ 不要** 第一句 Prompt 不满意就全盘重来

**✅ 要** 保留有效片段，只改失败维度

---

## §31 逆向采访三步法

> **与本 skill 的 confirmation-gates 同源**：让 AI 采访用户，用户做选择题。

### 阶段一：AI 采访（反客为主）

**❌ 不要** 自己堆 高画质、美女、宫崎骏风格

**✅ 要** 启动指令：

我想生成[模糊感觉]的画面。请作为摄影导演采访我：
每次只问一个问题，给我选项让我选。问清：景别、构图、主体细节、光影色调。


用户用 **选择题** 回答（中景 / 框中框构图 / 半开木门为前景…）

### 阶段二：LLM 整合成结构化 Prompt

### 阶段三：绘图 → 对比脑内画面 → 只改一个变量迭代

---

## §14 JSON 生图三阶段

**归入文件:** 本文

**原理：** 自然语言发散 → 风格漂移。JSON 把导演思维代码化，锁死摄影/光影/构图参数；**不直接喂给绘图 AI**，而是喂给 LLM 生成「纯净 Prompt」。

### ❌ 不要

- 没建视觉词汇库就填 JSON → 平庸创意只能得到平庸的稳定输出
- 把 JSON 原样粘贴进 Midjourney / SD 输入框 → { } " :被当噪音，甚至画出乱码符号
- 静态图 Prompt 原样复制到视频 AI → 干扰图生视频的运动判断
- 视频阶段仍写赛博朋克/霓虹/8K 等风格词 → 首帧已有，重复描述引发乱动

### ✅ 要

**三阶段流水线**


① 美学逆向工程（视觉词汇库）
        ↓
② JSON 中台架构（逻辑锁）
        ↓
③ LLM 翻译 → 目标模型 Prompt
        ↓
④ 图生视频时返璞归真（仅运镜+微动）


---

### 阶段 1｜美学逆向工程（视觉词汇库）

写 JSON 前先确定物理参数：

| 类别 | 选项 | 关键词示例 |
|------|------|-----------|
| 物理介质 | 胶片感 | Kodak Vision3, Halation, Film Grain|
| 物理介质 | 数码感 | Arri Alexa 65, Clean Sharp Focus|
| 镜头语言 | 变形宽银幕 | Anamorphic Lens, Oval Bokeh, Horizontal Flare|
| 镜头语言 | 长焦压缩 | Telephoto Lens, 85mm, Compressed Space|
| 光影逻辑 | 体积光 | Volumetric Lighting, Dust in Light Beams|
| 光影逻辑 | 伦勃朗光 | Rembrandt Lighting, Triangle Highlight on Cheek|

---

### 阶段 2｜JSON 中台架构（导演控制台）

**通用模板（保存为个人控制台）：**

json
{
  "Subject_Layer": {
    "core": "主体描述：外貌、动作、情绪、服装",
    "emotion": "叙事情绪（非滤镜词）",
    "must_not_beautify": ["raw emotion", "messy hair", "dirty face"]
  },
  "Environment": {
    "location": "具体地点与时代",
    "atmosphere": "空气质感、天气、时间"
  },
  "Cinematography_Lock": {
    "medium": "Kodak Vision3 500T film look",
    "lens": "Anamorphic 40mm",
    "lighting": "Rembrandt lighting from camera-left",
    "composition": "subject at right one-third, negative space left",
    "color_grade": "muted teal and amber, halation on highlights"
  },
  "Style": {
    "reference": "cinematic still, 1970s thriller",
    "stylize_level": "low — preserve physical space"
  }
}


**为何经 LLM：** MJ/即梦擅长语义长句 → LLM 把 Lock 参数**融入**描写；Flux/SD 擅长标签 → LLM 提取高权重 Tag 置前。换 Subject 时 Lock 不变 → 系列一致。

---

### 阶段 3｜LLM 翻译指令（复制即用）


你是一位电影摄影大师。请基于我提供的 JSON 数据，为 [目标模型名称] 撰写提示词。

规则：
1. 读取 Cinematography_Lock，确保镜头/胶片/布光/构图在 Prompt 中占主导地位。
2. 读取 Subject_Layer，融入场景；Subject_Core 不得被美化或削弱。
3. 若目标为 Midjourney / Nano Banana / 即梦：输出一段画面感强的英文自然语言段落。
4. 若目标为 Stable Diffusion / Flux：输出逗号分隔英文标签，Lock 参数前置并标注权重 (keyword:1.2)。
5. 删除所有 JSON 符号，不输出代码块。


**翻译输出示例（MJ 自然语言派）**


A weary detective in a rumpled trench coat stands at the right third of the frame,
Rembrandt light from camera-left carving a triangle on his cheek.
Shot on Kodak Vision3 500T with anamorphic 40mm glass — oval bokeh, horizontal flare,
muted teal-and-amber grade with halation on neon signs.
Rain-slicked alley, volumetric mist, cinematic still from a 1970s thriller.


---

### 阶段 4｜图生视频：动词的艺术（做减法）

首帧已含光影构图，视频 Prompt **只写运动**。

**公式：** [镜头运动] + [主体微动] + [环境氛围流动]

| 类型 | 示例 |
|------|------|
| 镜头 | Slow cinematic zoom out/ Slow zoom in/ Pan right|
| 人物微动 | Hair blowing in wind, Looking around, Subtle breathing|
| 环境 | Dust floating, Rain falling, Smoke rising|

**❌ 不要**


A cowboy on a horse in the canyon at sunset, cinematic, western style...


**✅ 要**


Slow cinematic zoom out, wind blowing the dust,
horse breathing, subtle coat movement.


> 分工：视频阶段忘掉 JSON，只保留运镜与自然语言微动（同 [video-prompt.md](video-prompt.md)）。

---

## §15 JSON 三大误区

**归入文件:** 本文

### 误区 1｜格式崇拜：JSON 是收纳箱，不是化妆品

**❌ 不要**

- 以为套上 { }画质就从 720p 变 8k
- 平庸审美 + 标准 JSON = 平庸但整齐

**✅ 要**

- JSON **管理**元素优先级，不生成美感
- 先拆解电影/参考图（§14 阶段 1），再填入 JSON

---

### 误区 2｜风格糖衣化：锚点必须前置

AI 倾向把一切画得精致唯美，吞没叙事张力。

**❌ 风格前置**

json
{
  "Style": "Cyberpunk masterpiece 8k",
  "Subject": "A desperate crying girl"
}

→ 战损妆时尚模特，苦难被视觉特效吞没

**✅ 锚点优先**

json
{
  "Subject_Core": {
    "face": "dirty face, raw emotion, messy hair, despair",
    "priority": "absolute — do not beautify"
  },
  "Environment": "rain-soaked alley, neon reflections",
  "Style": "cyberpunk — apply last, low weight"
}


**法则：** Subject_Core是绝对指令；Style最后写入、低权重。

---

### 误区 3｜直接喂绘图 AI：JSON 是 LLM 的中间件

**❌ 不要**


{ "Subject": "Cat", "Lighting": "Rembrandt" }  → 粘贴进 Midjourney


**✅ 工业级流程**


JSON（导演剧本）→ LLM（ChatGPT/Gemini 翻译）→ 清洗后 Prompt → 绘图 AI


绘图模型训练于「图片 + 自然语言」，未学过 JSON 语法；{ } " :是噪音。

---

### 能力边界与工具适配

| 目标 | 策略 |
|------|------|
| **掌控感 / 一致性**（连载、商业系列） | JSON 架构 + LLM 翻译 |
| **探索 / 创造力**（单张实验） | 自由自然语言 |
| Midjourney / Nano Banana | JSON 思考 → 自然语言段落输出 |
| Flux / SD | JSON → 逗号 Tag + 权重 |
| Workflow / API 批量生产 | JSON 主场；锁 Style 模块，轮换 Subject |

**审美描述决定上限；JSON 只减少随机性，不自动生成美感。**

---

## 跨节组合公式


拆解参考图 → 填入 JSON（Subject 可变 + Cinematography_Lock 不变）
→ LLM 按目标模型翻译
→ 出图满意后，视频仅用 [运镜 + 微动 + 环境流动]


叙事时间/假因果可在 Subject_Layer.emotion中声明，细则见 [time-causality.md](time-causality.md)。

---

## §52 画面结构拆解法

> 与 §14 JSON 互补：JSON 锁参数；§52 管**视频/画面复刻**的结构化反推。
> 分镜落地 → [director-storyboard.md](director-storyboard.md) §57

**原则：** 不让 AI 猜标签词，让它拆**画面结构 + 时间线**。

### 反推雷区

### ❌ 不要


请描述这个视频并给我提示词

- 返回标签堆砌：电影级光影、动态运镜、欢快跳舞→ 买家秀与卖家秀

### 问题诊断

| 缺失维度 | 后果 |
|---------|------|
| 动作无时间线 | 「跳舞」随机分配太空步/扭动 |
| 镜头无轨迹 | 「动态运镜」可能是环绕也可能是推拉 |
| 空间无坐标 | 丧尸在脚边还是远处沙滩随机 |

### 画面结构五维

### ✅ 要（让 LLM 按维输出）


1. 构图与机位（远景/中景/特写，平视/仰视/俯视）
2. 主体特征（材质、姿态、表情）
3. 光影与氛围（主光方向、冷暖倾向）
4. 环境纵深（前景遮挡、景深）
5. 时间线与动作（视频灵魂：按秒切片）


### 逐帧拆解模板

### ❌ 不要

- 一段话概括 15 秒视频

### ✅ 要


0-2s：特写脚步，鞋底摩擦，背景微虚
2-4s：拉远中景，转身，衣摆物理摆动，侧脸主光
4-5s：推镜头，走向画面深处，融入背景光影

- 每段写明：**时间 + 景别 + 运镜 + 构图 + 主体动作 + 画面内容**

### 物理世界写法

### ❌ 不要


漂亮的光；他在走路


### ✅ 要


左侧45°主光打面部，右侧微弱蓝色环境补光
步伐沉重，双臂自然摆动，镜头平滑跟随其后背推进


### 超级提示词（强制 LLM 变拆解器）

复制给 Gemini/ChatGPT 分析目标视频，要求输出：


- 按镜头切换切时间片
- 每片含：机位/焦段/运镜轨迹/主体动向/光影/前景遮挡
- 禁止只列元素标签；必须写运动矢量与空间关系
- 可附参考图需求清单（人物/环境/道具分轨）


**结语：** 控制机位、光影、时间线每一帧 → 随机性最低、确定性最高。
