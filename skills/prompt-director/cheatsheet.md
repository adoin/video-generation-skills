# 提示词拼装速查（创作时必读，仅此一份）

> 创作顺序：**确认闸门** → 分镜草案 → 本文件拼装 Prompt。
> references 按场景简报 **最多再开 1–2 个**。闸门题面见 [workflows/confirmation-gates.md](workflows/confirmation-gates.md)。

## 静图 Prompt 拼装顺序

```
[主体+动作] → [构图位置] → [光线三要素] → [角度+焦段] → [风格/质感]
```

| 槽位 | 必填写法 | ❌ 禁止 |
|------|---------|--------|
| 构图 | `positioned at left/right one-third of the frame` | 不写位置 |
| 光线 | `from [方向]` + 照谁 + `casting shadows`；写光比+色温 | 单独 `cinematic lighting` |
| 镜头 | `eye-level/low-angle/high-angle` + `35mm/50mm/85mm` 成对 | 只写 portrait 无焦段 |
| 风格 | 一种胶卷或一种美学词，放句尾 | 胶卷+渲染引擎混写 |
| 精度 | 抽象词改具体；背景写死到街道/建筑级 | `A car in street` |

## 图生视频 Prompt 拼装顺序

```
[固定机位或单一运镜] → [维持原图光影] → [可见物理运动] → [多动作时按秒时间线]
```

| ❌ 禁止 | ✅ 要写 |
|--------|--------|
| 8K/UE5/赛博朋克等与首帧冲突的风格词 | 转身、发丝扬起、踩脚印、呼出白雾 |
| 手持+平滑推轨同句 | 只留一种运镜或 `固定机位` |
| 风力6级、走5米 | 衣角扬起、迈出一步 |
| 多动作一句说完 | `0-2s … 2-5s … 5-8s …` |

## 场景简报 → 打开哪个 reference（最多 2 个）

| 简报标记 | 打开 |
|---------|------|
| `纪实/随手拍/松弛感` | candid-capture.md |
| `抽象风格词/禁止词/扰动词` | prompt-precision.md |
| `过去式/假因果/时间态` | time-causality.md |
| `反推/JSON/脑海画面没词` | json-and-reverse.md |
| `图生视频/多动作` | video-prompt.md |
| `人物一致/多角色/产品一致` | consistency.md |
| `故事板/多镜/导演调度` | director-storyboard.md |
| `演技/声音/妆造/活人感` | character-performance.md |
| `局部改图/标注融合` | edit-fusion.md |
| `胶卷/风格提取/MJ人像` | style-prompts.md |
| `调色/HEX色卡` | color-grading.md |
| `废片补救` | waste-recovery.md |
| 以上都不突出 | **不打开 reference**，速查表够用 |

按场景 → [INDEX.md](references/INDEX.md) · 点名 § → [SECTIONS.md](references/SECTIONS.md)（搜 `§N` 只读该段）

## 输出结构（创作默认）

```markdown
## 场景简报
[主体/环境/动作/情绪/媒介]

## 分镜 01（静图或首帧）
**Prompt:** ...

## 分镜 02（如有）
...

## 图生视频（如有）
**运动:** ... / **时间线:** ...
```
