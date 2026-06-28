# Understanding

Understanding is a public Codex skill repository for `lijie`, a learning-oriented skill that helps an AI assistant turn unfamiliar material into clear, testable knowledge structure.

`Understanding` 是 `lijie` 这个 Codex skill 的公开仓库。它的目标不是简单压缩文本，而是帮助 AI 助手把陌生知识拆成「讲得清、拆得开、用得上、能验证」的结构。

## What This Skill Does / 这个 Skill 的作用

`lijie` guides Codex to process learning material through three lenses:

- Feynman explanation: explain simply first, then precisely.
- First principles: separate primitives, assumptions, mechanisms, constraints, examples, and consequences.
- Knowledge structure mapping: label sequences, parallel sets, hierarchies, dependencies, networks, many-to-one relations, one-to-many relations, closed loops, and open loops.

`lijie` 会引导 Codex 从三个角度处理学习材料：

- 费曼解释：先用简单语言讲清楚，再给出精确版本。
- 第一性原理：区分底层概念、事实、假设、机制、限制、例子和结果。
- 知识结构映射：标出顺序、并列、层级、依赖、网络、多对一、一对多、闭环和开环。

## When To Use It / 什么时候用

Use it when you want to understand, teach, summarize, or internalize:

- a concept, paper, article, book, course, video, or documentation page
- a technical system, workflow, business model, mental model, or research domain
- dense notes that need structure rather than compression
- hidden relationships between ideas, especially dependencies, feedback loops, tradeoffs, and prerequisites

当你想学习、解释、总结或内化这些内容时，可以使用它：

- 概念、论文、文章、书籍、课程、视频或文档
- 技术系统、工作流、商业模型、思维模型或研究领域
- 信息很密但结构不清的笔记
- 概念之间的隐藏关系，尤其是依赖、反馈闭环、权衡和前置知识

## Quick Start / 快速开始

Clone this repository:

```powershell
git clone https://github.com/aDragon0707/understanding.git
cd understanding
```

Install the skill into your local Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\skill\lijie C:\Users\<you>\.codex\skills\
```

Then invoke it in Codex:

```text
Use $lijie to explain reinforcement learning from first principles, then map its knowledge structure.
```

克隆仓库：

```powershell
git clone https://github.com/aDragon0707/understanding.git
cd understanding
```

安装到本地 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force .\skill\lijie C:\Users\<you>\.codex\skills\
```

然后在 Codex 中调用：

```text
用 $lijie 解释这篇论文：先给我费曼解释，再拆第一性原理，最后列出掌握检查题。
```

## Example Prompts / 示例提示词

```text
Use $lijie to summarize this article, then map the knowledge structure and open loops.
```

```text
Use $lijie to turn these notes into a study plan with mastery checks.
```

```text
用 $lijie 把这个商业模式拆成：底层假设、关键机制、依赖关系、反馈闭环和失败模式。
```

```text
用 $lijie 学习这个新概念：先讲人话，再讲专业版，最后给我自测题。
```

## Repository Structure / 仓库结构

```text
.
|-- README.md
|-- CHANGELOG.md
|-- LICENSE
|-- docs/
|   |-- INTRO.en.md
|   `-- INTRO.zh-CN.md
`-- skill/
    `-- lijie/
        |-- SKILL.md
        |-- agents/
        |   `-- openai.yaml
        `-- references/
            |-- formula-origin-protocol.md
            `-- structure-framework.md
```

## Skill Package / Skill 包内容

The installable skill lives in `skill/lijie/`.

- `skill/lijie/SKILL.md`: the main skill instructions and trigger metadata
- `skill/lijie/agents/openai.yaml`: UI-facing metadata for Codex
- `skill/lijie/references/formula-origin-protocol.md`: a protocol for explaining why formulas and transformations have their structure before using notation
- `skill/lijie/references/structure-framework.md`: a reference for mapping knowledge relationships and feedback loops

真正可安装的 skill 位于 `skill/lijie/`。

- `skill/lijie/SKILL.md`：主说明和触发元数据
- `skill/lijie/agents/openai.yaml`：Codex 界面使用的展示元数据
- `skill/lijie/references/formula-origin-protocol.md`：用于先解释公式和变换结构来源、再使用符号的协议
- `skill/lijie/references/structure-framework.md`：知识关系和反馈闭环的结构映射参考

## More Docs / 更多文档

- [English introduction](docs/INTRO.en.md)
- [中文介绍](docs/INTRO.zh-CN.md)
- [Changelog](CHANGELOG.md)

## Design Philosophy / 设计理念

Good learning is not just shorter text. It is structure, mechanism, feedback, and recall.

好的学习不是把文字变短，而是把知识变成结构、机制、反馈和可回忆的能力。

`lijie` therefore pushes the assistant to answer:

- What is the core question?
- What are the irreducible pieces?
- How do the pieces generate the result?
- What depends on what?
- Where is the feedback loop?
- How can the learner prove they can use it?

所以 `lijie` 会推动助手回答：

- 这个知识到底在回答什么核心问题？
- 哪些是不可再拆的底层零件？
- 这些零件如何生成最终结论？
- 哪些概念依赖哪些概念？
- 哪里有反馈闭环，哪里只是开环？
- 怎样证明学习者真的会用？

## License / 许可证

MIT License. See [LICENSE](LICENSE).
