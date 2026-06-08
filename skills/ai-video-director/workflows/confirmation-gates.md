# 确认闸门（叙事制片）

## 闸门 A：路由

### A1 主轨道 `track`（单选）

| id | 选项 |
|----|------|
| `narrative` | 短剧/漫剧/短片全流程 |
| `production` | 一致性/分镜/故事板/动作 |
| `both` | 两者都要 |

### A2 内容类型 `genre`（单选，narrative 时）

| id | 选项 |
|----|------|
| `ancient_romance` | 女频古风 |
| `3d_anime` | 3D 漫剧 |
| `film_style` | 电影感/奇幻世界观 |
| `short_preview` | 30s 预告/概念片 |
| `fairy_tale` | 童话/剧场 |

### A3 痛点 `pain`（多选，production 时）

| id | 选项 |
|----|------|
| `face_drift` | 角色变脸 |
| `scene_jump` | 场景跳戏/不穿帮 |
| `action_fail` | 复杂动作崩 |
| `storyboard` | 故事板不稳定 |
| `shot_logic` | 分镜逻辑弱 |

### A4 已有素材 `assets`（多选）

| id | 选项 |
|----|------|
| `script` | 剧本 |
| `storyboard` | 分镜/故事板 |
| `char_sheet` | 角色设定/三视图 |
| `scene_ref` | 场景参考 |
| `reference_film` | 参考片 |
| `none` | 从零 |

### A5 画幅 `aspect`（单选）

| id | 选项 |
|----|------|
| `9_16` | 竖屏短剧 |
| `16_9` | 横屏影视 |
| `other` | 其他 |

### A6 工具 `tools`（多选）

| id | 选项 |
|----|------|
| `seedance` | Seedance 2.0 |
| `kling` | 可灵 |
| `jimeng` | 即梦 |
| `flowpix` | FlowPix |
| `chatgpt_script` | ChatGPT 剧本/分镜 |

---

## 闸门 B：分镜草案

输出镜号列表后确认；用户多选要生成的镜号。

---

## 收齐后

1. cheatsheet.md → 对应 narrative/ 或 production/ reference
2. Prompt 技法 → `prompt-director`
3. 产品广告误入 → 转 `brand-ad-cg` / `ecommerce`
