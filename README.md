# video-generation-skills

AI 视频生成 **Skill 技能包仓库**（兼容 [skills.sh](https://skills.sh/) / `npx skills` 生态）。

基于刺猬星球 243 篇 AI 视频/生图教程提炼，拆为 4 个可独立安装的技能模块。

## 技能一览

| Skill | 说明 | 覆盖教程量级 |
|-------|------|-------------|
| [`prompt-director`](skills/prompt-director/) | 提示词方法论：构图、光线、运镜、一致性、角色控制 | ~70 篇 |
| [`ecommerce`](skills/ecommerce/) | 电商素材：服装/3C/美妆详情页、主图、UGC 种草 | ~57 篇 |
| [`brand-ad-cg`](skills/brand-ad-cg/) | 品牌广告/TVC/产品 CG 大片 | ~74 篇 |
| [`ai-video-director`](skills/ai-video-director/) | 叙事制片：短剧/漫剧 + 分镜/故事板/一致性 | ~17 篇 |

## 安装方式

仓库地址：[github.com/adoin/video-generation-skills](https://github.com/adoin/video-generation-skills)

**前提：** 已安装 Node.js（能运行 `npx`），使用 Cursor 或其他受支持的 Agent。

### 查看有哪些 skill

```bash
npx skills add adoin/video-generation-skills --list
```

### 按需安装（推荐）

`-g` 为**全局**（所有项目可用）；去掉 `-g` 则为**当前项目**级。

```bash
# 只装提示词方法论
npx skills add adoin/video-generation-skills --skill prompt-director -g -a cursor -y

# 只装电商
npx skills add adoin/video-generation-skills --skill ecommerce -g -a cursor -y

# 同时装两个（-s 可重复）
npx skills add adoin/video-generation-skills -s prompt-director -s ai-video-director -g -a cursor -y
```

四个 skill 名称：`prompt-director` · `ecommerce` · `brand-ad-cg` · `ai-video-director`

### 一次装全部

```bash
npx skills add adoin/video-generation-skills --all -g -a cursor -y
```

### 验证安装

```bash
npx skills list -g -a cursor
```

### 装好后怎么用

无需手动 `@` skill。在 Cursor 中正常对话，Agent 会根据各 `SKILL.md` 的 `description` 自动匹配，例如：

- 「写图生视频提示词」→ `prompt-director`
- 「做淘宝详情页 / 种草视频」→ `ecommerce`
- 「做耳机 TVC / 品牌 CG」→ `brand-ad-cg`
- 「古风短剧分镜 / 场景一致性」→ `ai-video-director`

### 常见组合

| 用途 | 建议安装 |
|------|----------|
| 日常写提示词 | `prompt-director` |
| 电商带货 | `prompt-director` + `ecommerce` |
| 品牌广告 | `prompt-director` + `brand-ad-cg` |
| 短剧制片 | `prompt-director` + `ai-video-director` |
| 全能 | `--all` |

### 备用：完整 GitHub URL

若简写路径拉取失败：

```bash
npx skills add https://github.com/adoin/video-generation-skills --skill prompt-director -g -a cursor -y
```

### 本地开发 / 贡献者

克隆本仓库后，用 `./` 指向本地路径安装：

```bash
git clone https://github.com/adoin/video-generation-skills.git
cd video-generation-skills
npx skills add ./ --list
npx skills add ./ --skill prompt-director -g -a cursor -y   # 全局
npx skills add ./ --all -a cursor -y                           # 项目级
```

修改 `skills/*/SKILL.md` 后重新执行 `npx skills add` 即可更新。

## 仓库结构

```
video-generation-skills/
├── catalog.json              # 技能包清单（元数据，供工具/文档读取）
├── skills/                   # npx skills CLI 标准发现路径
│   ├── prompt-director/
│   ├── ecommerce/
│   ├── brand-ad-cg/
│   └── ai-video-director/
├── sources/                  # 维护用教程映射（不随 skill 安装）
├── docs/                     # 安装与贡献指南
└── scripts/                  # 辅助脚本（安装、索引生成等）
```

## Skill 路由关系

```
用户意图
  ├─ 「提示词怎么写」        → prompt-director
  ├─ 「电商详情页/种草」     → ecommerce
  ├─ 「品牌广告/TVC/CG」     → brand-ad-cg
  └─ 「做短剧/分镜/一致性」  → ai-video-director
```

`prompt-director` 是基础层，其他 3 个 skill 在制片流程中应交叉引用其方法论。

## 维护者：教程来源

原始教程 Markdown 在 Scrapling 仓库 `output/tutorials_md/`。`sources/` 仅作映射维护，**不会被打包进 skill**。

## 开发状态

- [x] 仓库骨架 + 4 skill 目录
- [x] `catalog.json` 技能包清单
- [x] 各 skill `references/` 内容填充
- [x] 发布到 GitHub（[adoin/video-generation-skills](https://github.com/adoin/video-generation-skills)）
- [ ] 注册 skills.sh 收录（可选）

详见 [docs/INSTALL.md](docs/INSTALL.md)、[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。
