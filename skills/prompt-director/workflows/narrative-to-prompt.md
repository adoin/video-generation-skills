# 工作流：叙事文本 → 分镜提示词

> 适用：小说片段、剧本、故事大纲、用户口述情节
> 必读：[cheatsheet.md](../cheatsheet.md) → [confirmation-gates.md](confirmation-gates.md)
> **禁止** 跳过确认闸门直接出 Prompt（除非用户已给全设定）

## 步骤 0：确认闸门（优先）

读 [confirmation-gates.md](confirmation-gates.md)，执行：

1. 解析输入，列出 `已明确` / `待确认`
2. **AskQuestion** 只问待确认项（闸门 A → B；有歧义再 C）
3. 用户选定后，写入 `creative_brief`

用户已全给定时（例：「这段古风小说，9:16，即梦出图，Seedance 做视频，细拆」）→ 跳过 A，仍建议 **闸门 B 分镜草案** 让用户确认再写 Prompt。

## 步骤 1：分镜草案（闸门 B，先不给完整 Prompt）

```markdown
## 分镜草案
| 镜号 | 画面概要 | 建议镜头 |
```

等用户 `approve` / 勾选镜号后，再进入步骤 2。

## 步骤 2：场景简报（每镜一条）

```yaml
creative_brief: { ...闸门答案... }
shots:
  - id: 01
    主体:
    环境:
    动作:          # 一镜一个核心动作
    情绪:          # 可见表情/姿态，非抽象词
    镜头:          # 继承 camera_tone 或单镜覆盖
    flags:         # 纪实 | 图生视频 | 多动作
```

**叙事 → 可见物**（抽象词必须改写，有歧义走闸门 C）：

| 叙事 | 可见描述 |
|------|---------|
| 她很悲伤 | 低头、眼眶泛红、肩缩 |
| 大风 | 发丝贴脸、衣角贴腿 |

## 步骤 3：拼 Prompt（仅对已确认镜号）

按 [cheatsheet.md](../cheatsheet.md) 槽位 + `creative_brief` 参数。

- `target_tool: midjourney` → 保留 `--ar` / `--no`
- `target_tool: seedance` → 静图与运动词 **分两条**；运动见 cheatsheet 视频节
- `texture_flags` 多选 → 叠加对应质感词（胶片/抓拍/光晕）

## 步骤 4：按 flags 打开 reference（≤2 个）

| flags | 打开 |
|-------|------|
| 纪实 / candid | candid-capture.md |
| 抽象风格词 | prompt-precision.md |
| 图生视频 / 多动作 | video-prompt.md |
| 胶卷选型 | style-prompts.md |

## 步骤 5：输出 + 二次调整入口

```markdown
## creative_brief
[YAML]

## 分镜 01 — 首帧
**Prompt:** ...

## 分镜 01 — 视频（如 output_type 含视频）
**运动/时间线:** ...

---
**还可调整：** 风格 / 画幅 / 镜头基调（回复编号或文字即可）
```

## ❌ 禁止

- 跳过闸门直接堆 Prompt
- 小说原文贴进 Prompt
- 一次加载全部 references
