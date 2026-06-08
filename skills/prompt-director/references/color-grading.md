# 调色与电影感

> 涵盖：§23 · §38
> 冷暖阶级与氛围骨架见 [atmosphere.md](atmosphere.md) §32

---

## §23 数据驱动调色

### ❌ 不要
- 堆 4k, 8k, cinematic lighting, masterpiece冒充电影感
- 只写 Wong Kar-wai style让 AI 猜平均值

### ✅ 要（三步）

**1. 色彩 DNA 提取**（上传参考帧给 LLM）：

分析这张图的色彩DNA：色相分布、明暗比例、色温倾向、饱和度映射。
输出可写入 Prompt 的调色指令。


**2. 参数嵌入 Prompt**（示例沙丘橙青）：

desaturated palette, monochromatic sand tones,
bleach bypass effect, teal in shadows, creamy highlights, harsh directional sunlight


**3. A/B 验证** — 生成对比 → 只调一个色彩参数再生成

> 与 §38 分工：§23 用**文字色彩参数**；§38 用 **HEX 色卡**批量统一。

---

### §38 HEX 调色法

> 把颜色控制从「后期碰运气」前移到「生成前锁定」。不用堆砌 teal and orange/ Kodak film赌色系。

#### 底层逻辑

### ❌ 不要


cinematic lighting, teal and orange, Kodak film, vintage mood

- 每张图色系随机 → 后期逐张拉曲线套 LUT

### ✅ 要

1. 上传 10 张同风格参考图到 HEX 工作流
2. 自动提取核心 **十六进制色值**（如 #FF5733）
3. 生成**专属色卡图**作为视觉参考
4. 生图/生视频时**垫色卡** → 色域精准锁定

- 文字说「蓝色」= 几万种蓝；HEX 色板 = 色域锚点

#### 三步工作流

**步骤 1 — 获取色卡**

### ✅ 要


上传 10 张目标风格参考图（如废土科幻截图）
→ 工作流扫描色彩构成 → 输出纯色卡图 + HEX 列表
→ 可手动微调色值


**步骤 2 — 生图锁定**

### ✅ 要


[垫入色卡图作为 style/color reference]
+ 只写主体/构图/动作 Prompt，不写颜色形容词

示例：
A lone wanderer crossing ruined highway overpass,
wide cinematic composition, dust particles in air
（颜色由色卡决定，不在文字里描述）


**步骤 3 — 视频色彩延续**

### ❌ 不要


用色卡出好首帧后，视频 Prompt 又写 warm golden sunset lighting

- 与首帧色系冲突，视频模型漂移

### ✅ 要


首帧 = 色卡生成的静态图
视频 Prompt 只写动作/运镜：
slow camera dolly in, dust drifting, fabric moving in wind
（死死咬住首帧色彩体系，不写光影词）


#### 与 §32 分工

| 手段 | 适用 |
|------|------|
| §32 文字物理调色 | 单张即兴创作、精细控制明暗/冷暖/虚实 |
| §38 HEX 色卡 | 系列账号/品牌视觉统一、批量出图出片 |

#### §38 排查清单

1. [ ] 要系列统一？→ 先建 HEX 色卡再写 Prompt
2. [ ] 色卡已垫？→ 删掉 Prompt 里所有颜色/胶片词
3. [ ] 图生视频？→ 首帧用色卡图，运动 Prompt 零光影描述
