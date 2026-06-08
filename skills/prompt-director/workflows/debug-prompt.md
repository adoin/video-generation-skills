# 工作流：已有 Prompt 诊断/优化

> 适用：「效果不好」「太 AI 了」「帮我改提示词」
> 必读：[cheatsheet.md](../cheatsheet.md) → 闸门 D [confirmation-gates.md](confirmation-gates.md)

## 步骤

0. **AskQuestion 闸门 D**：媒介、主要症状、用的工具（用户未说明时必问）

1. **判断媒介**：静图 / 图生视频
2. **图生视频** → 只读 [video-prompt.md](../references/video-prompt.md)，按首帧/冲突/时间线排查
3. **静图** → 对照 cheatsheet 槽位，缺哪个补哪个，**默认不读 reference**
4. 仍失败 → 按症状 **只开一个** reference：

| 症状 | 只读 |
|------|------|
| 主体居中、画面平 | composition.md |
| 光线假、无阴影 | lighting.md |
| 脸型怪、透视怪 | camera-movement.md |
| 太锐利/太脏/抽象词失灵 | prompt-precision.md |
| 太摆拍 | candid-capture.md |

5. 输出：原 Prompt 划线删减 + 改写后完整 Prompt
