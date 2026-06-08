# 确认闸门（品牌广告 / CG）

> 追求大牌质感前，先锁调性与参考，禁止无方向出 Prompt。

## 闸门 A：全局

### A1 项目类型 `project_type`（单选）

| id | 选项 |
|----|------|
| `product_cg` | 产品 CG 视频/大片 |
| `tvc` | TVC 风格广告 |
| `brand_film` | 品牌故事 / 企业宣传片 |
| `logo_motion` | Logo / Banner 动效 |
| `style_board` | 只要风格美学提示词 |
| `creative_mv` | 创意 MV / 非标准广告 |

### A2 品牌调性 `brand_tone`（单选）

| id | 选项 |
|----|------|
| `tech` | 科技 / 未来 |
| `luxury` | 奢华 / 高级丝滑 |
| `youth` | 年轻 / 活力 |
| `guofeng` | 国风 / 人文 |
| `playful` | 趣味 / 迷幻 / 超现实 |
| `minimal` | 极简 / 留白 |

### A3 参考 `reference`（单选）

| id | 选项 |
|----|------|
| `has_brand_ref` | 有具体品牌/片子参考 |
| `has_mood_only` | 只有情绪/风格词 |
| `none` | 从零，需共同定调 |

### A4 产品类型 `product`（单选，产品类项目）

| id | 选项 |
|----|------|
| `auto` | 汽车 |
| `phone_3c` | 手机 / 3C |
| `beauty` | 美妆护肤 |
| `fashion_item` | 时尚单品 |
| `food_bev` | 食品饮料 |
| `none` | 非产品向 |

### A5 画幅与时长 `format`（单选）

| id | 选项 |
|----|------|
| `16_9_30s` | 16:9 · ~30s |
| `16_9_60s` | 16:9 · ~60s+ |
| `9_16_social` | 9:16 社交 |
| `1_1_banner` | 1:1 Banner |
| `keyframes_only` | 仅关键帧/静图 |

### A6 实景 vs CG `look`（单选）

| id | 选项 |
|----|------|
| `pure_cg` | 纯 CG / 超现实 |
| `photo_real` | 照片级写实 |
| `hybrid` | 实拍感 + AI 增强 |

---

## 闸门 B：视觉策略确认

输出 **光/镜头/色调** 一句话策略 + 分镜草案（如有）后确认。

---

## 收齐后

1. cheatsheet.md
2. 按 `project_type` 打开 reference（最多 2 个）
3. 提示词细节 → `prompt-director`
