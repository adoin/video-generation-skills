# 安装指南

## 这是什么？

`video-generation-skills` 是一个 **多 Skill 技能包仓库**（plugin bundle），不是单个 skill。

- 兼容 [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI（`npx skills`）
- 可被 Cursor、Claude Code、Codex 等 50+ agent 安装
- 每个子目录 `skills/<name>/` 是独立可安装的 skill

## 安装到 Cursor

### 方式 A：全局安装（所有项目可用）

```bash
npx skills add <owner>/video-generation-skills --all -g -a cursor -y
```

安装后 skill 位于用户级 agent 目录（由 skills CLI 管理）。

### 方式 B：项目级安装（随仓库共享）

在项目根目录执行：

```bash
npx skills add <owner>/video-generation-skills --all -a cursor -y
```

可将生成的 `skills-lock.json` 提交到 git，团队成员用：

```bash
npx skills experimental_install
```

恢复相同版本。

### 方式 C：手动 symlink（不推荐，仅调试用）

```powershell
# 示例：将单个 skill 链到项目 .cursor/skills/
New-Item -ItemType Directory -Force -Path .cursor\skills
cmd /c mklink /D .cursor\skills\prompt-director D:\workspace\video-generation-skills\skills\prompt-director
```

优先使用 `npx skills add`，可自动处理多 agent 路径。

## 按需安装

```bash
# 只看有哪些 skill
npx skills add <owner>/video-generation-skills --list

# 只装电商相关
npx skills add <owner>/video-generation-skills -s ecommerce -g -a cursor -y

# 装两个
npx skills add <owner>/video-generation-skills -s prompt-director -s ai-video-director -g -a cursor -y
```

## 本地开发

克隆本仓库后：

```bash
cd video-generation-skills
npx skills add ./ --list
npx skills add ./ --skill prompt-director -g -a cursor -y
```

修改 `skills/*/SKILL.md` 后，重新执行 `npx skills add` 即可更新（或使用 `--copy` 复制模式）。

## 验证安装

```bash
npx skills list -g -a cursor
```

应能看到 `prompt-director`、`ecommerce`、`brand-ad-cg`、`ai-video-director`。

## 与 Scrapling 教程仓库的关系

| 仓库 | 角色 |
|------|------|
| `Scrapling` | 教程原文数据源（`output/tutorials_md/`） |
| `video-generation-skills` | 面向 Agent 的技能包（提炼后的 SKILL.md + references） |

开发时两个仓库可同时 attach 到 Cursor workspace；Agent 读 skill 指令，需要查原文时再读 Scrapling 中的 md。

## 发布到 skills.sh（预留）

1. Push 到 GitHub 公开仓库
2. 确保 `skills/<name>/SKILL.md` 含合法 frontmatter（`name` + `description`）
3. 用户即可 `npx skills add <owner>/video-generation-skills`
4. 可选：在 [skills.sh](https://skills.sh/) 提交收录

`catalog.json` 为本仓库自定义清单，供 README/脚本读取；skills CLI 不依赖此文件，靠目录扫描发现 skill。
