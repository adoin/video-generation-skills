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

