---
name: ecommerce
description: >-
  AI e-commerce asset workflows for fashion, 3C/digital, beauty, and general
  product marketing. Covers detail pages, main images, lookbooks, UGC seeding
  videos, TikTok/Ins content, and batch asset generation. Use when the user
  mentions 电商, 详情页, 主图, 种草, UGC, 服装/3C/美妆带货, lookbook,
  白底图裂变, Seedance product videos, or Amazon/TK shop assets.
---

# Ecommerce

AI **电商素材**工作流：产品图 → 详情页 / 主图 / 种草视频。

## 模式

| 模式 | 触发 | 流程 |
|------|------|------|
| **创作** | 要做电商素材、详情页、种草 | 闸门 → cheatsheet → reference |
| **诊断** | 已有图/视频效果不好 | 先问平台与品类，再对照 reference |

## 创作流水线

```
1. 读 cheatsheet.md
2. 读 confirmation-gates.md — AskQuestion 收集未明确项
3. 输出「工作流草案」— 等用户确认步骤
4. 按垂类打开 1 个 reference + 可选 workflows/product-to-assets.md
5. 逐步输出 Prompt / 操作要点（技法 → prompt-director）
```

**硬性：** 品类/平台/输入素材未说明 → **必须先 AskQuestion**。

## 垂类路由

| 垂类 | 读 |
|------|-----|
| 服装 | [references/fashion.md](references/fashion.md) |
| 3C / 数码 | [references/3c-digital.md](references/3c-digital.md) |
| 美妆 / 家居 / 宠物 / 保健 | [references/verticals.md](references/verticals.md) |
| 通用工作流 | [references/workflows.md](references/workflows.md) |

## 边界

- 大牌 TVC 质感 → `brand-ad-cg`
- 短剧叙事 → `ai-video-director`
- 纯提示词理论 → `prompt-director`

## 输出格式

```markdown
## 电商品类 & 平台
## 输入素材
## 工作流步骤
## 每步工具 & 提示词要点
## 批量裂变策略（如需要）
```

教程索引 → [references/INDEX.md](references/INDEX.md)（64 篇，无内部 ID）
