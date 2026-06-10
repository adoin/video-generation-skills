---
name: prompt-director
description: >-
  Turn novels, scripts, scenes, or creative briefs into AI image/video prompts.
  Asks structured single/multi-select questions before generating when settings
  are unclear. Use when user pastes 小说/剧本/情节, asks 生成提示词/分镜,
  or needs prompt optimization.
---

# Prompt Director

叙事 → **先确认关键设定** → 分镜草案 → 分镜 Prompt。不是一次性黑盒生成。

## 模式

| 模式 | 触发 | 流程 |
|------|------|------|
| **A 创作** | 小说/剧本/情节、要生成提示词 | 确认闸门 → 草案 → Prompt |
| **B 诊断** | 已有 Prompt 效果不好 | [workflows/debug-prompt.md](workflows/debug-prompt.md) + 闸门 D |

## 创作流水线（模式 A）

```
1. 读 cheatsheet.md
2. 读 confirmation-gates.md — 用 AskQuestion 收集未明确项（单选/多选）
3. 输出「分镜草案」— 等用户确认镜号
4. 仅对确认镜生成 Prompt（见 narrative-to-prompt.md）
5. references 按 flags 最多再开 1–2 个
```

**硬性：**

- 用户只贴情节、未说明画幅/工具/要图还是视频 → **必须先 AskQuestion**，禁止猜完直接出 Prompt
- 用户已全说明 → 可跳过闸门 A，仍建议 **分镜草案** 一轮确认
- 有 AskQuestion 工具 → **必须用**；没有 → 用编号选项让用户回复

## 确认闸门速览

详见 [workflows/confirmation-gates.md](workflows/confirmation-gates.md)

| 轮次 | 内容 | 选择类型 |
|------|------|---------|
| A 全局 | 产出形态、画幅、工具、风格、镜头基调、分镜密度 | 单选为主 |
| B 草案 | 分镜列表是否 OK；生成哪些镜 | 单选 + **镜号多选** |
| B 质感 | 胶片颗粒/抓拍/光晕等 | **多选**（可选） |
| C 单镜 | 情绪外化、构图左右等歧义 | 单选，仅疑点 |

## 上下文预算

1. `cheatsheet.md` — 每次必读
2. `confirmation-gates.md` 或一个 `workflows/*.md`
3. `references/` — 最多 1–2 个，按 flags

## § 定位（用户点名某一节时）

```
INDEX / SECTIONS.md → 得文件名 → 文件内搜 `§N` → 只读该标题到下一 `## §` 段
```

- 平铺表：[references/SECTIONS.md](references/SECTIONS.md)（比 INDEX 更适合「§50 在哪」）
- 各 reference 正文标题均含 `§` 编号，可用 grep 直达
- 用户只说场景、未点名 § → 走 cheatsheet 场景表，**不必查 §**

## 输出格式

```markdown
## creative_brief
[闸门答案 YAML]

## 分镜草案（若本轮刚确认）
...

## 分镜 01 — 首帧
**Prompt:** `...`

## 分镜 01 — 视频（如需）
**运动/时间线:** `...`

---
**还可调整：** [列出 2–3 个可改旋钮]
```

## 深度参考（按需，见 INDEX）

| 文件 | 覆盖 |
|------|------|
| [INDEX.md](references/INDEX.md) | 教程索引（按主题） |
| [SECTIONS.md](references/SECTIONS.md) | **§ 平铺速查**（点名某一节时用） |
| [composition.md](references/composition.md) | §1/9/26/39 构图 |
| [lighting.md](references/lighting.md) | §2/20/25/47 光线 |
| [camera-movement.md](references/camera-movement.md) | §3/21/33/36/41 镜头 |
| [candid-capture.md](references/candid-capture.md) | §4 抓拍 |
| [prompt-precision.md](references/prompt-precision.md) | §5–8/10/12 精度控制 |
| [time-causality.md](references/time-causality.md) | §11/13 时间/因果 |
| [json-and-reverse.md](references/json-and-reverse.md) | §14–16/19/22/27/31/52 反推JSON |
| [style-prompts.md](references/style-prompts.md) | §17/18 风格 |
| [video-prompt.md](references/video-prompt.md) | §28/50/54 图生视频 · seedance2.0 全能参考 |
| [color-grading.md](references/color-grading.md) | §23/38 调色 |
| [consistency.md](references/consistency.md) | §24/37/40/43/45/46 一致性 |
| [atmosphere.md](references/atmosphere.md) | §32 氛围 |
| [waste-recovery.md](references/waste-recovery.md) | §30 废片 |
| [director-storyboard.md](references/director-storyboard.md) | §34/35/57 导演/故事板 |
| [edit-fusion.md](references/edit-fusion.md) | §42/44 融合改图 |
| [character-performance.md](references/character-performance.md) | §29/48–49/51/53/55 角色 |

## 与其他 Skill

- 短剧制片全流程 → `ai-video-director`
- 电商素材 → `ecommerce`
