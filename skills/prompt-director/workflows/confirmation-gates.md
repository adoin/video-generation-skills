# 确认闸门（创作必过，再出 Prompt）

> 适用：模式 A 创作。用户没一次性说清时，**必须先问，禁止猜完直接出 Prompt**。
> 工具：优先用 **AskQuestion** 弹出单选/多选；不可用时用文字列出选项编号让用户回复。

## 总规则

```
解析用户输入 → 标出「已明确 / 待确认」→ 只问待确认项 → 收齐答案 → 分镜草案 → 出 Prompt
```

| 情况 | 行为 |
|------|------|
| 用户已写明（如「9:16 竖屏 Seedance 图生视频」） | 该项 **跳过不问** |
| 用户说「你看着办」「随便」 | 该项用 **推荐默认值**，在分镜草案里标注「已默认」，用户可改 |
| 叙事可多种解读（时代、风格、谁视角） | **必须问**，不可擅自定 |
| 问完一轮仍缺关键项 | 可合并为 **一批 AskQuestion**（多题同时弹出） |

---

## 闸门 A：全局设定（首轮，尽量一次问完）

用户未提供时，用 AskQuestion。**单选 unless 标注多选**。

### A1 产出形态 `output_type`（单选）

| id | 选项 |
|----|------|
| `image_only` | 仅静图首帧 Prompt（用于生图） |
| `image_and_video` | 静图首帧 + 图生视频运动 Prompt |
| `video_motion_only` | 已有首帧图，只要运动/时间线 Prompt |

### A2 画幅比例 `aspect_ratio`（单选）

| id | 选项 |
|----|------|
| `16:9` | 横屏电影 / 短片 |
| `9:16` | 竖屏短剧 / 抖音 |
| `3:4` | 人像海报 |
| `1:1` | 方形社交 |
| `2.35:1` | 宽银幕 |

### A3 目标工具 `target_tool`（单选，影响 Prompt 语言习惯）

| id | 选项 |
|----|------|
| `general_en` | 通用英文 Prompt |
| `midjourney` | Midjourney（可带 `--ar` `--no`） |
| `jimeng` | 即梦 |
| `seedance` | Seedance 2.0 图生视频 |
| `kling` | 可灵 |

### A4 视觉风格 `visual_style`（单选，叙事含糊时必问）

| id | 选项 |
|----|------|
| `cinematic` | 电影叙事写实 |
| `candid` | 纪实抓拍 / 松弛感 |
| `period_ancient` | 古风 / 年代片 |
| `cyberpunk` | 赛博 / 霓虹科幻 |
| `commercial` | 商业广告质感 |
| `anime_illust` | 动漫插画 |
| `dreamy_art` | 梦幻艺术片 |

### A5 镜头基调 `camera_tone`（单选，全局默认，单镜可覆盖）

| id | 选项 |
|----|------|
| `eye_doc` | 平视 + 35mm 纪实 |
| `low_hero` | 低角度 + 85mm 英雄感 |
| `high_drama` | 俯视 + 50mm 戏剧 |
| `close_portrait` | 特写 + 85mm 情绪 |

### A6 分镜数量 `shot_granularity`（单选）

| id | 选项 |
|----|------|
| `few` | 精简 1–3 镜（关键帧） |
| `standard` | 标准 4–6 镜 |
| `fine` | 细拆 7+ 镜 |

**AskQuestion 示例（合并一轮）：**

```
title: "Prompt Director — 创作设定"
questions:
  - id: output_type
    prompt: 需要什么产出？
    options: [仅静图 / 静图+视频 / 仅运动Prompt]
  - id: aspect_ratio
    prompt: 画幅比例？
    options: [16:9, 9:16, 3:4, 1:1, 2.35:1]
  - id: target_tool
    prompt: 主要用在哪个工具？
    options: [通用英文, Midjourney, 即梦, Seedance, 可灵]
  ...（仅问用户未提供的项）
```

---

## 闸门 B：分镜草案确认（第二轮）

根据叙事 **先出分镜标题列表**（还不写完整 Prompt），再让用户确认。

```markdown
## 分镜草案（待确认）
| 镜号 | 画面概要 | 建议镜头 |
| 01 | 雨夜巷口，女子回望 | 平视 35mm |
| 02 | 特写攥信的手指 | 85mm |
| 03 | 霓虹倒影路面 | 低角度 |
```

### B1 草案是否 OK（单选）

| id | 选项 |
|----|------|
| `approve` | 全部生成 |
| `edit` | 我要改镜号/增减（用户文字说明） |
| `partial` | 只生成部分镜头（进入 B2） |

### B2 生成哪些镜（多选，`allow_multiple: true`）

选项 = 草案中每镜一条，例如 `shot_01`, `shot_02` …

### B3 质感增强（多选，可选，不选则用基调默认值）

| id | 选项 |
|----|------|
| `film_grain` | 胶片颗粒 |
| `candid_shake` | 抓拍微晃 |
| `neon_halation` | 夜景光晕 Cinestill |
| `soft_portra` | Kodak Portra 肤色 |
| `high_contrast` | 强明暗对比 |

---

## 闸门 C：单镜疑点（细拆或用户改稿时）

某一镜存在多种合理画法时，**只问该镜**，不要为每镜都问一遍。

| 疑点类型 | 问法（单选） |
|---------|-------------|
| 情绪外化 | 低头沉默 / 回望镜头 / 眼眶含泪 三选一 |
| 构图重心 | 主体居左三分 / 居右三分 |
| 图生视频动作 | 固定机位微动 / 单一推镜 / 按秒时间线（多动作时） |

---

## 闸门 D：诊断模式（模式 B）

优化已有 Prompt 时，先问：

| id | 问题 | 单选选项 |
|----|------|---------|
| `medium` | 当前是？ | 静图 / 图生视频 |
| `symptom` | 主要问题？ | 太假塑料 / 构图平 / 光线平 / 脸型怪 / 动作僵 / 风格不对 |
| `tool` | 用的工具？ | 同 A3 |

---

## 收齐答案后的执行顺序

1. 把闸门答案写入场景简报头部 `creative_brief`
2. 仅对 **B2 选中的镜** 生成完整 Prompt
3. `image_and_video` 时：每镜 **两条**（首帧 + 运动），运动遵守 cheatsheet 视频节
4. 末尾附 **「可二次调整项」**：列出用户还可改的 2–3 个旋钮（风格/镜头/比例）

```yaml
creative_brief:
  output_type: image_and_video
  aspect_ratio: "9:16"
  target_tool: seedance
  visual_style: period_ancient
  camera_tone: eye_doc
  shot_granularity: standard
  texture_flags: [film_grain, soft_portra]
  user_confirmed: true
```

---

## ❌ 禁止

- 用户只贴了小说段落，未确认画幅/工具/产出形态，就直接输出完整 Prompt
- 把「悲伤、神秘」等抽象风格词擅自具象化而不经 A4 或 C 闸门
- 一次问超过 **8 个问题**（合并为 1–2 轮 AskQuestion，每轮 ≤5 题）
