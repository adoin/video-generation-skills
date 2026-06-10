# 图生视频提示词优化

> 涵盖：§50 · §28 · §54
> 适用：**图生视频（I2V）**；运镜写法见 [camera-movement.md](camera-movement.md)；锚点/状态流见 §28

**本文件目录：** [§50](#§50-图生视频三大法则) · [§28](#§28-动作清单--状态流) · [§54](#§54-人物动作自然写法)

---

## §50 图生视频三大法则

### 一、首帧已定调，提示词只写运动

### ❌ 不要写

| 类型 | 示例 |
|------|------|
| 渲染/画质词 | 超写实、8K、UE5、电影级光影 |
| 与首帧冲突的风格 | 原图日系胶片 + 提示词赛博朋克 |
| 物理数值 | 风力6级、每秒1米、走5米 |

### ✅ 要写

只写首帧里 **还没有发生** 的可见物理变化：


❌ 赛博朋克光影，UE5渲染，女孩缓缓转动看向镜头
✅ 女孩在雪地缓缓转身，目光自然落向镜头；转身时寒风扬起发丝和衣角


### 二、一条提示词只确立一种主导逻辑

### ❌ 不要（互斥指令同句）


电影级运镜，强烈肩扛手持展现情绪张力，同时镜头极其平滑向前推进。
极具戏剧性高对比影棚打光，女孩静静翻书。


### ✅ 要


固定机位。维持原图柔和自然光。
女孩缓缓翻开书的下一页，指尖轻压纸页边缘。


### 三、多动作用时间线，不要一锅炖

### ❌ 不要


狂风刮过，几十封信全部卷起飞向天空。女孩猛地站起向前追赶，无人机360度快速环绕。


### ✅ 要（固定机位 + 按秒拆分）


0-2s：微风扬起发丝，女孩保持蹲姿，视线低垂
2-5s：阵风加剧，地面信纸陆续翻卷、贴地滑行
5-8s：女孩抬头望向飞散的纸页，身体开始站起


---

### §28 动作清单 → 状态流

> 与 §50 去重：§50 管 I2V 卫生（删风格词、互斥运镜、时间线）；§28 管**动作物理逻辑**（动词/锚点/状态）。时间线写法两处通用，§28 侧重单动作质感。

#### 一、减少动词，增加方式词（Manner）

### ❌ 不要


A man runs, jumps over a barrier, and rolls on the ground.

- 多动词堆叠 → 几何形变冲突，四肢滑行扭曲

### ✅ 要


A man sprinting desperately through the forest,
torso leaning forward at 45 degrees, hair blown back by wind,
mud splashing from each footfall, heavy breathing visible

- **一个核心动词** + 物理状态限定节奏/重力/方向

#### 二、锚点锁定法（Anchor Method）

### ❌ 不要（平级描述）


A parkour athlete is jumping across rooftops. He is twisting his body sideways.
He is tucking his legs up. He is throwing his arms backward.
All actions happening at the same time.

- 算力平均分配 → 身体各部位「各玩各的」，机械木偶感

### ✅ 要


Anchor: explosive torso twist driving a powerful leap across the rooftop gap.
Satellite: legs tucking tight to clear the edge, arms whipping backward for balance.
Muscles coordinated as one kinetic chain, sunset rim light.

- **锚点动作**（躯干/腿部位移）决定惯性；**从属动作**（头/手/表情）顺应锚点节奏

| 层级 | 典型动作 |
|------|---------|
| 锚点 | Walking, Sitting, Sprinting, Torso twist leap |
| 从属 | Looking back, Waving, Drinking, Micro-expression |

#### 三、状态快照法——删掉 then / after

### ❌ 不要


He finishes the drink, then slams the glass on the table angrily.

- AI 无时间轴 → 三状态同时融合（嘴里塞蛋糕+半站半坐+诡异微笑）

### ✅ 要


Mid-action state: empty glass pressed flat on the table,
liquid droplets still airborne from the impact,
man's hand white-knuckled on the glass base, jaw clenched.

- 描述**动作中段瞬间**，大脑自动补全前后连贯

#### §28 × §50 交叉排查

1. [ ] 动词 > 1 个？→ 减为一个 + 方式词（§28）
2. [ ] 主次不分？→ 标出锚点/从属（§28）
3. [ ] 有 then/after？→ 改 mid-action state（§28）
4. [ ] 含风格/画质词？→ 删掉（§50）
5. [ ] 互斥运镜/光影？→ 只留一种主导逻辑（§50）
6. [ ] 动作 > 2 个且无主次？→ 改时间线或拆镜（§50 + [director-storyboard.md](director-storyboard.md)）

---

## §54 人物动作自然写法

> 与 §28 去重：§28 管锚点/状态流；§54 管**步态、联动、动作链、分角色**。
> 行为动机 → [character-performance.md](character-performance.md) §53

### 第一步：写清步态（怎么 walk）

### ❌ 不要


一个女孩往前走
让人物向前走


### ✅ 要


缓缓端庄平稳向前走（宫廷气质）
慢慢地轻轻地谨慎向前走（夜色古街）

- 先判断首帧气质，再定走法；图生视频第一步不是「动起来」而是「该怎么动」

### 第二步：身体联动

### ❌ 不要


轻轻抬头看向前方

- 只有头动 → 画面单薄

### ✅ 要


缓缓抬头，视线前移，肩膀微带动，抱在胸前的木牌随上身细微位移
头部一动，肩、手臂、手持物同步微反应


### 第三步：情绪状态入动作

### ❌ 不要


女子低头看着手中布帛


### ✅ 要


低头凝视旧布帛，右手手指缓缓收紧，压抑惊人秘密；
下颌绷紧，轻吞咽，呼吸带动胸腔起伏；
抬眼睑，眼神由波动沉淀为隐忍与决绝

- **动作前加原因，动作中加情绪，动作后加状态**

### 动作链公式

### ❌ 不要


少年挥动长杆


### ✅ 要


起始：双手握杆，目光锁定前方
蓄力：手指收紧，手腕下压，肩绷，重心降低
发力：腰肩带动，双臂跟进
轨迹：杆从右向左横扫，弧线掠过镜头前
结束：身体微侧转，杆停左侧，眼神仍锁定
镜头：轻微后退跟随横扫方向


### 多人：分角色写互动链

### ❌ 不要


一男一女在房间里对视


### ✅ 要


男子向前靠近带压迫感 → 女子下意识后撤 → 男子抬手按手腕 → 女子抬头反问 → 对视停住


### 通用拼装公式


人物身份 + 场景氛围 + 情绪状态 + 主动作 + 辅助动态 + 身体联动 + 结束状态 + 简单镜头


---

## seedance2.0 全能参考（短剧/短片成片）

> 溯源：[info-2859](https://www.super-i.cn/info-2859.html) · 制片流程 → `ai-video-director` narrative/short-drama.md

**适用：** 已有人物/场景/道具资产图，需要多参考图 + 分镜一起驱动视频（站内称「全能参考」）。

### 提示词六段结构

```
【光线布置】  ← 参考片拆解（第一步母版）
【风格】
【拍摄参数】
【画面处理】
【主角形象】  ← 可复用人物描述模板
【分镜画面】  ← 15 秒段落级分镜输出
```

### 参考图编号（必须写进 prompt）

上传人物/道具/场景/声线后，在提示词里**显式标注**，勿只上传不引用：

```
女主图1
男主图2
铃铛图3
河灯图4
场景图5
```

### 声线参考

1. 先生成一段**含男女主对白**的视频（可不作成片）
2. 剪映分别导出男主声线、女主声线
3. 声线文件作为后续全能参考素材之一

### 与 §50 的关系

| 层级 | 规则 |
|------|------|
| §50 | 单镜 I2V：首帧已定调，只写运动；一镜一种逻辑 |
| 全能参考 | 多资产编号 + 六段结构；单段 ≤15s、少塞动作 |
| 二者叠加 | 六段里【分镜画面】仍遵守 §50，勿重新堆 8K/冲突风格词 |

---

## 与其他文件的分工

| 情况 | 读 |
|------|-----|
| 单动作质感 | 本文 §28 |
| 图生视频卫生/时间线 | 本文 §50 |
| 步态/动作链/身体联动 | 本文 §54 |
| seedance2.0 多参考成片 | 本文「全能参考」+ ai-video-director/short-drama.md |
| 角度/焦段/景别情绪 | [camera-movement.md](camera-movement.md) §33 |
| 微表情幅度 | [character-performance.md](character-performance.md) §29 |
| 行为动机/活人感 | [character-performance.md](character-performance.md) §53 |
| 摆拍感/蒙太奇 | [camera-movement.md](camera-movement.md) §36 |
