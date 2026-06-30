# 导演思维与分镜

> 涵盖：§34 · §35 · §57
> 动作状态流 → [video-prompt.md](video-prompt.md) §28；蒙太奇节奏 → [camera-movement.md](camera-movement.md) §36
> 多角色分镜接力 → [consistency.md](consistency.md) §37

---

### §34 告别工具人：AI 视频导演思维

#### 一、调度优先，而非分镜优先

### ❌ 不要


一个精致男人情绪低落坐在昏暗凌乱房间，电影感光影，8k，UE5渲染
→ 生成后只写「镜头缓慢推进」

- AI 默认调度 → 人物木桩坐、室内大平光、无戏剧张力

### ✅ 要

**Z 轴纵深——划分三层：**


Foreground: blurred door frame or window blinds partially blocking view.
Midground: man slumped on vintage armchair, slouched posture.
Background: cluttered bookshelf fading into deep shadow.


**室内动机光源（Motivated Lighting）：**

### ❌ 不要


dim lighting in a room


### ✅ 要


sole warm amber desk lamp illuminating only left half of his face,
cold blue moonlight slicing through venetian blinds on the right,
motivated lighting, chiaroscuro cutting the space


**视差运镜（结合纵深）：**

### ❌ 不要


camera zoom in


### ✅ 要


truck right behind foreground blinds,
parallax between near blinds and distant bookshelf,
subject remains in midground, real spatial depth


#### 二、叙事优先，而非画面优先

**每场戏围绕一个核心行动。**

**过程 vs 结果（微表情）：**

### ❌ 不要


女士坐在医院走廊，极度悲伤绝望，眼泪流下来，8k
→ 视频：伤心地哭，眼泪流下，镜头推进


### ✅ 要


女士坐在医院走廊长椅， eyes staring blankly at floor,
lips slightly parted trembling, shallow rapid breath visible in chest,
hands gripping crumpled paper ticket, knuckles white
→ 视频：她低头看手中揉皱的票，喉结艰难滚动，眼眶慢慢泛红但尚未落泪


**情绪降级 + 动词升级（对抗性）：**

### ❌ 不要


极其孤独的剑客站在狂风大雪中，唯美苍凉，史诗级，雪花飘落


### ✅ 要


lone swordsman leaning hard into blizzard wind,
pressing bamboo hat brim down with one hand, coat whipping violently,
body angled 30° forward fighting the gale, boots digging into snow


**叙事行动模板：**


[核心目标] + [具体动作] + [环境阻力]

示例：女孩在暴雨中疯狂翻垃圾桶找被扔的戒指，
手指划破也不停， rain hammering her back, wind pushing against her


#### 三、剪辑与补拍思维

### ❌ 不要

一条 Prompt 塞满 15 秒：走进咖啡厅 → 点咖啡 → 坐下 → 发现外星人 → 震惊站起
- 匀速监控探头感，无节奏突变

### ✅ 要

**步骤 1** — 生成主镜头 A-roll（15s 基础动作长镜头）

**步骤 2** — 情绪断点硬切，补拍 B-roll：
- 惊恐瞳孔 Extreme Close-up（2s 微动视频）
- 手机落地高速摄影空镜头（3s）

**步骤 3** — 剪辑拼接：主镜头 + 特写突刺 + 空镜留白 = 蒙太奇节奏


主镜头打底 + 特写突刺 + 空镜头呼吸


---

### §35 重塑想象力：打破「大片感」执念

> 技术卷到天花板后，脱颖而出靠**巧思**而非画质堆砌。

#### 一、打破物理定律

**反重力：**

### ❌ 不要


a polar bear sitting by a waterfall, realistic


### ✅ 要


polar bear on a moss-covered boulder floating mid-air,
massive waterfall flowing upward defying gravity,
weightless water droplets and rocks suspended, surreal hyperrealism


**图生视频** — 只写环境动态，克制防「纠正」：

### ✅ 要


waterfall continues flowing upward, floating debris drifts slowly,
polar bear stable on levitating rock, thumb scrolling phone screen gently


**巨型建筑漂浮：**


skyscraper hovering slightly above ground, disconnected base with exposed rebar,
dust and soil falling from underside, slow subtle levitation in clouds


**关键词：** anti-gravity/ levitating/ flowing upwards

#### 二、让时间失控

**时空割裂（背景飞逝 + 主体静止）：**

### ✅ 要


a man standing perfectly frozen in center,
surrounding crowd and city traffic rendered as extreme motion blur streaks,
time-lapse background vs static subject, surreal time fracture


**动作非自然阻断：**

### ✅ 要


woman mid-stride running, body frozen at the peak of a step,
one foot suspended in air, hair halted mid-swing, temporal pause


#### 三、把镜头变成角色

**巨物降临视角：**

### ✅ 要


extreme low angle from ground level, ant's-eye view,
giant human legs and shoes towering overhead filling the frame,
cracked pavement texture in sharp foreground, overwhelming scale


**局限物理视角：**

### ✅ 要


first-person POV from inside a glass of water on the table,
world viewed through curved liquid distortion,
blurred restaurant scene beyond the rim, refraction effects


**起手式：** First-person POV from.../ Extreme low/high angle looking at...

---

## §57 AI 故事板稳定工作流

> 与 §34 剪辑思维互补：§34 管单镜调度与补拍；§57 管**生成前规划**降随机。
> 结构反推 → [json-and-reverse.md](json-and-reverse.md) §52；妆造人物 → [character-performance.md](character-performance.md) §55

### 任务拆分（提示词不能包打天下）

### ❌ 不要

- 只靠一段长提示词生成多镜头视频 → 镜头随机、人物变脸、风格跳变

### ✅ 要

| 环节 | 控制什么 |
|------|---------|
| 人物身份板（三视图） | 脸型、发型、服装、气质 |
| AI 生成剧情 | 6–8 个可拍镜头的故事 |
| AI 故事板 | 景别、站位、动作、运镜 |
| 预想效果图 | 最终光影/色调/质感方向 |
| 视频提示词 | 整合以上，保持简短 |

### 标准流程

### ❌ 不要


直接让 AI 生成故事板（无人物无剧情）
故事板塞满人物细节与最终画质词
最终视频提示词与故事板/效果图方向冲突


### ✅ 要


1. 人物三视图（身份板锁定）
2. 将人物交给 LLM 生成可画面化短剧情节（每镜可拍）
3. LLM/GPT image 生成多格故事板（标位置/景别/动作/运镜）
4. Nano Banana 生成一张预想效果图（风格样片，非全镜头）
5. LLM 据故事板补对话情节（勿依赖故事板内文字 OCR）
6. 视频工具：身份板 + 故事板 + 效果图 + 对话 → 简短整合提示词


### 故事板质检三项

### ❌ 不要

- 上一格室内下一格街头无过渡
- 动作含糊（「站着」看不出走/回头/坐下）
- 每格都复杂环绕运镜

### ✅ 要

- 镜头顺序连贯；人物动作可辨识；运镜匹配内容且克制

### 最终视频提示词

### ❌ 不要

- 重新堆砌 8K/新风格/与效果图矛盾的打光

### ✅ 要


按故事板镜号简述动作与运镜；人物与风格引用已上传参考；对话情节单独文本附上

### 案例：30 秒日系预告（info-2851）

与 §57 同一思想，**落地顺序**为：

```
四大风格板块 → 编剧 Skill 出剧本 → 场景四宫格（先于人物）
→ 人物三视图资产 → 逐镜分镜四宫格 → seedance2.0 一镜一 prompt → 剪辑
```

要点：故事板不是一次文生视频，而是**风格规则 + 场景底图 + 角色资产 + 分镜图**四层锁定后再视频化。详见 `ai-video-director/references/narrative/film-style.md` §三。

### 案例：单张动画前期故事板 → 15s 短片（info-2898）

> 溯源：[info-2898](https://www.super-i.cn/info-2898.html)（2026-06 站更）
> 制片落地 → `ai-video-director/references/production/storyboard.md` §四

**定位：** 非专业分镜表，而是给视频模型的**视觉提示板**——一图同时承载镜头顺序、角色参考、场景氛围、色板与 Notes。

**版式（约 12 格）：** 左侧竖列 = 镜头顺序与段落；右侧 = 角色/道具参考；底部 = Notes / Camera / Color Palette / Details。

| 步 | 动作 |
|----|------|
| 1 | LLM 用模板产出故事板提示词（先锁角色名、镜头顺序、场景范围） |
| 2 | Image 2.0 出故事板；质检：12 格顺序、角色是否可辨、画风统一 |
| 3 | 整板上传 Seedance 2.0 作视频参考 |

| ❌ 不要 | ✅ 要 |
|--------|------|
| 无角色/剧情直接出板 | 先定角色与分镜顺序再画图 |
| 单图赌多镜头视频 | 故事板 + 全能参考组合 |
| 商业长片只靠此法 | 快速验证、教程展示、概念预演；正片仍须完整资产链 |

---

## §60 空镜与插入镜头

> 溯源：[info-2881](https://www.super-i.cn/info-2881.html)（2026-06 站更）
> 长片衔接 → [video-prompt.md](video-prompt.md) §58；情绪蒙太奇 → [camera-movement.md](camera-movement.md) §36

### 定义：不限于无人风景

**空镜 / 插入镜头** = 暂时不正面表现主角，仍传递剧情信息的镜头。

| 类型 | 替剧情表达什么 | 示例 |
|------|---------------|------|
| 环境空镜 | 时间、地点、氛围 | 雨夜屋檐、湿窗、空巷 |
| 道具空镜 | 人物关系与处境痕迹 | 凉透的茶、掉落发簪、未推门 |
| 情绪空镜 | 内部情绪的外化 | 摇晃灯影、将尽蜡烛、垂落红绸 |

**判断：** 删掉该镜后，观众对地点/时间/关系/情绪理解**完全不变** → 多半是装饰，应删。

### 三个核心作用

1. **交代环境** — 几秒内完成「何时何地何种气氛」，胜过角色口述
2. **控制节奏** — 重要台词/动作后留 1–2s 停顿，让情绪被接住（非拖慢）
3. **含蓄表达情绪** — 用外部事物代替反复哭/皱眉

### 从剧本提取三类空镜

写 prompt 前先问：**环境 / 道具 / 情绪** 各需什么？

- **环境** — 雨夜古宅、湿屋瓦、昏暗灯笼 → 定光线与色彩基调
- **道具** — 与婚礼/等待/诀别相关的物（酒杯、红绸、绣鞋、烛台）
- **情绪** — 雨水持续落、烛火轻摇、空荡房间垂红绸

### 空镜五要素公式

```
拍摄主体 + 主体状态 + 动态细节 + 光线氛围 + 镜头运动
```

| 要素 | ❌ 不要 | ✅ 要 |
|------|--------|------|
| 主体 | 「归来的将军」 | 「剑柄上磨损的红色同心结」 |
| 状态 | 名词堆砌 | 微距特写 + 材质 + 当前状况（雪水浸湿、半开府门） |
| 动态 | 纯静物名词 | 一条主变化：线头随风摆、手指缓慢合拢 |
| 光线 | 电影感/高级感 | 冷灰晨光 + 府门暖光落在红衣上 |
| 运镜 | 同时推拉环绕升降 | 低机位沿脚印缓慢推向府门 |

**含人物系列：** 固定同一组角色参考图；同一场戏参考同一张场景九宫格，防空间重设计。

### 放置位置

| 时机 | 作用 |
|------|------|
| 一场戏开始前 | 环境空镜 → 再进人物 |
| 重要台词/动作之后 | 道具/手部特写，让承诺或情绪停留 |
| 两场戏之间 | 相似视觉母题衔接（如马蹄印：宫门石阶 → 边关泥地） |

**推荐结构：** 环境 → 人物处境 → 关系道具 → 人物反应 → 情绪空镜落点

### 常见问题

| 问题 | 改法 |
|------|------|
| 与主角无关的云海宫殿 | 改拍与关系绑定的物件（同心结、发簪） |
| 一镜多动作 | 3s 内只保留一个主变化 |
| 台词与画面脱节 | 说「缺角朱砂印」时切印记特写，非无关花草 |
| 空镜过多 | 诀别保留发簪+马蹄印即可，勿叠落花孤雁流水 |
| 人物/场景漂移 | 每镜上传同一参考组 + 场景九宫格 |

**流程：** 先生成 **5–7 格连续故事板**（含空镜位）→ 再逐镜 I2V；见 §57。

