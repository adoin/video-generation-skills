# 确认闸门（电商素材必过）

> 用户没一次性说清时，**必须先 AskQuestion**，禁止猜完直接出方案。

## 总规则

```
解析需求 → 标出已明确/待确认 → 只问待确认 → 收齐 → 输出工作流草案 → 用户确认 → 逐步 Prompt
```

| 情况 | 行为 |
|------|------|
| 已写明（如「9:16 TikTok 白底冲锋衣种草」） | 该项跳过 |
| 「你看着办」 | 用推荐默认，草案里标注 |
| 品类/平台含糊 | **必问** |

---

## 闸门 A：全局（首轮尽量一次问完）

### A1 电商品类 `vertical`（单选）

| id | 选项 |
|----|------|
| `fashion` | 服装 / 鞋包 |
| `3c` | 3C / 数码 |
| `beauty` | 美妆 |
| `home` | 家居 |
| `pet` | 宠物 |
| `health` | 保健 / 功效 |
| `food` | 食品 |
| `other` | 其他 |

### A2 目标平台 `platform`（单选）

| id | 选项 |
|----|------|
| `taobao_detail` | 淘宝/天猫详情页 |
| `amazon` | 亚马逊头图/A+ |
| `tiktok` | TikTok / 短视频带货 |
| `xiaohongshu` | 小红书种草 |
| `instagram` | Ins / 出海社媒 |
| `official` | 品牌官网 |
| `multi` | 多平台一套裂变 |

### A3 产出形态 `deliverable`（多选）

| id | 选项 |
|----|------|
| `detail_page` | 详情页长图 |
| `main_image` | 主图 / 海报 |
| `lookbook` | Lookbook / 穿搭图 |
| `ugc_video` | UGC 种草视频 |
| `product_video` | 产品展示/CG 视频 |
| `tryon` | 换装 / 变装 / 试衣 |

### A4 输入素材 `input_asset`（单选）

| id | 选项 |
|----|------|
| `white_bg` | 白底产品图 |
| `lifestyle_photo` | 实拍场景图 |
| `link_only` | 仅商品链接 |
| `competitor_ref` | 有竞品参考 |
| `nothing` | 从零（需定风格） |

### A5 一致性要求 `consistency`（多选，可选）

| id | 选项 |
|----|------|
| `product_lock` | 产品外观严格一致 |
| `model_lock` | 同一模特多图/多镜 |
| `batch_variants` | 批量裂变多场景即可 |

### A6 目标工具 `toolchain`（单选）

| id | 选项 |
|----|------|
| `nano_banana` | Nano Banana Pro |
| `gpt_image` | GPT Image 2.0 |
| `jimeng` | 即梦 |
| `seedance` | Seedance 2.0 |
| `sora2` | Sora2 |
| `lovart` | Lovart 对话流 |
| `flowpix` | FlowPix 多模型 |
| `mixed` | 混合（我来推荐） |

---

## 闸门 B：工作流草案确认

输出 **步骤列表 + 每步工具** 后问：

| 问题 | 类型 |
|------|------|
| 流程是否 OK？ | 单选：确认 / 调整 |
| 先做哪几步？ | 多选步骤编号 |

---

## 闸门 C：单步歧义（按需）

- 详情页屏数 / 主图数量
- UGC：口播 vs 对镜拍 vs 低头杀
- 裂变数量（3 / 9 / 10 场景）

---

## 收齐后

1. 读 [cheatsheet.md](../cheatsheet.md)
2. 按 `vertical` 打开对应 reference（最多 1 个 + workflows.md）
3. 按确认步骤输出 Prompt / 操作要点
