# 贡献指南

## 添加/修改 Skill 内容

1. 编辑 `skills/<skill-name>/SKILL.md`（主入口，保持 < 500 行）
2. 详细知识放 `skills/<skill-name>/references/*.md`（渐进式披露）
3. 更新 `sources/tutorial-index.md` 中的教程映射
4. 本地验证：`npx skills add ./ --list`

## SKILL.md 规范

```yaml
---
name: skill-name          # 小写+连字符，与目录名一致
description: >            # 第三人称，含 WHAT + WHEN 触发词
  ...
---
```

- `description` 决定 Agent 何时自动选用该 skill
- 引用 references 只一层深度：`[foo.md](references/foo.md)`
- 路径用正斜杠，不用反斜杠

## 教程迁移流程（Scrapling → skill）

```
1. 在 Scrapling/output/tutorials_md/ 找到目标教程
2. 确定归属 skill（见 sources/tutorial-index.md）
3. 提炼为 references 下的主题文档（非全文复制）
4. 在 SKILL.md 中添加链接和触发条件
5. 在 tutorial-index.md 标记 status: migrated
```

## 目录约定

| 路径 | 用途 |
|------|------|
| `skills/` | **唯一** skill 发现路径（npx skills 标准） |
| `skills/*/cheatsheet.md` | 创作时必读，~80 行，含拼装公式 |
| `skills/*/workflows/` | 按任务类型的流水线（叙事→Prompt 等） |
| `skills/*/references/` | 深度手册，**按需最多读 1–2 个**，禁止全量加载 |
| `sources/` | 教程索引、映射表、未来同步脚本配置 |
| `scripts/` | 自动化工具（索引生成、批量提炼等） |
| `catalog.json` | 技能包元数据（非 CLI 必需） |

### 三层上下文模型

```
SKILL.md（入口：判模式 + 选 workflow）
  → cheatsheet.md（每次创作必读）
  → workflows/*.md（任务流水线）
  → references/*.md（仅 flags 触发，≤2 个）
```

教程提炼进 references 时写 ❌/✅ 操作清单；创作路径靠 cheatsheet 内化高频规则，避免全量 references。

**不要**在仓库根目录放 `SKILL.md`，避免被误识别为第五个 skill。

## 新增第 5 个 skill 时

1. 创建 `skills/<new-skill>/SKILL.md`
2. 在 `catalog.json` 的 `skills` 数组追加条目
3. 更新 `README.md` 技能表
4. 更新 `sources/tutorial-index.md`
