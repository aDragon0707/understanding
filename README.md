# Lijie Skill / 理解 Skill

Lijie is a Codex skill for turning unfamiliar material into learnable structure.
It helps an AI assistant explain concepts from first principles, run a Feynman-style teach-back, and map relationships between ideas instead of only producing a short summary.

`lijie` 是一个用于“真正理解”的 Codex skill。它会把陌生概念、文章、课程、论文、工作流或知识体系拆成可学习的结构：先用第一性原理找到底层零件，再用费曼解释讲清楚，最后把概念之间的顺序、层级、依赖、网络和反馈闭环标出来。

## What It Does / 它的作用

- Explains a topic in plain language first, then with precise terminology.
- Separates primitives, assumptions, mechanisms, constraints, consequences, and examples.
- Maps knowledge relations such as sequence, hierarchy, dependency, one-to-many, many-to-one, and feedback loops.
- Turns summaries into reusable learning artifacts: concept maps, study notes, mastery checks, teach-back prompts, and learning paths.
- Marks uncertain or inferred claims instead of hiding them inside fluent prose.

- 先讲人话，再讲精确版本。
- 区分事实、假设、底层概念、机制、限制条件、结果和例子。
- 显式标注知识关系：1-2-3 顺序、1/2/3 并列、层级、依赖、一对多、多对一、网络、闭环和开环。
- 把“看起来懂了”的摘要，变成能复习、能迁移、能自测的学习材料。
- 对推断、不确定、高风险或需要验证的内容做标记，不把它们伪装成确定结论。

## When To Use / 什么时候使用

Use `lijie` when you want to understand, teach, summarize, or internalize:

- a concept, book, paper, article, video, course, or documentation page
- a technical system, product workflow, business model, mental model, or research domain
- a dense note that needs structure rather than compression
- relationships between ideas, especially dependencies, loops, tradeoffs, and hidden prerequisites

当你想学习、解释、总结或内化以下内容时，可以使用 `lijie`：

- 概念、书籍、论文、文章、视频、课程或文档
- 技术系统、产品流程、商业模型、思维模型或研究领域
- 信息很密但结构不清的笔记
- 概念之间的关系，尤其是依赖、闭环、开环、权衡和隐藏前置知识

## Example Prompts / 示例提示词

```text
Use $lijie to explain reinforcement learning from first principles.
```

```text
Use $lijie to summarize this article, then map the knowledge structure and open loops.
```

```text
用 $lijie 解释这篇论文：先给我费曼解释，再拆第一性原理，最后列出掌握检查题。
```

```text
用 $lijie 把这个商业模式拆成：底层假设、关键机制、依赖关系、反馈闭环和失败模式。
```

## Output Shape / 输出形态

The skill adapts to the request, but commonly produces:

- Core question
- Feynman explanation
- First-principles decomposition
- Knowledge structure map
- Examples, failure modes, and edge cases
- Mastery checks or teach-back prompts

它会根据任务自动调整输出，但常见结构包括：

- 核心问题
- 费曼解释
- 第一性原理拆解
- 知识结构图
- 例子、失败模式和边界情况
- 掌握检查题或复述提示

## Repository Structure / 仓库结构

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   `-- structure-framework.md
|-- docs/
|   |-- INTRO.en.md
|   `-- INTRO.zh-CN.md
|-- .gitignore
`-- README.md
```

## Installation / 安装

Clone this repository, enter the repo root, then copy its contents into your Codex skills directory:

```powershell
New-Item -ItemType Directory -Force C:\Users\<you>\.codex\skills\lijie
Copy-Item -Recurse .\* C:\Users\<you>\.codex\skills\lijie
```

Or keep the repository elsewhere and sync the repository contents into your skills directory.

克隆这个仓库，进入仓库根目录，然后把内容复制到 Codex skills 目录：

```powershell
New-Item -ItemType Directory -Force C:\Users\<you>\.codex\skills\lijie
Copy-Item -Recurse .\* C:\Users\<you>\.codex\skills\lijie
```

也可以把 repo 放在别处，只把仓库内容同步到你的 skills 目录。

## Design Philosophy / 设计理念

Good learning is not just shorter text. It is structure, mechanism, feedback, and recall.

好的学习不是把文字变短，而是把知识变成结构、机制、反馈和可回忆的能力。

`lijie` therefore pushes the assistant to answer:

- What is the core question?
- What are the irreducible pieces?
- How do the pieces generate the result?
- What depends on what?
- Where is the feedback loop?
- How do we know the learner can use it?

所以 `lijie` 会推动助手回答：

- 这个知识到底在回答什么核心问题？
- 哪些是不可再拆的底层零件？
- 这些零件如何生成最终结论？
- 哪些概念依赖哪些概念？
- 哪里有反馈闭环，哪里只是开环？
- 怎样证明学习者真的会用？

## License / 许可证

Add a license that matches your publishing preference before public release.

公开发布前，请根据你的发布意图补充合适的许可证。
