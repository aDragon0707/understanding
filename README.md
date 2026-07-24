# Understanding / `lijie`

`lijie` 是一个面向 Codex 的证据驱动学习 skill。它不把学习等同于“得到一段更短的解释”，而是帮助学习者把陌生材料变成可以解释、推导、应用、迁移和复查的能力。

> `lijie` turns unfamiliar knowledge into explainable, usable, testable, and transferable structure.

当前公开版本为 **R2**。

## 它解决什么问题

很多学习材料的问题不是信息太少，而是结构没有被显式化：

- 哪些是对象、原语和前置条件？
- 哪些是机制、步骤、约束和结果？
- 哪些概念存在依赖、分支、汇聚或反馈？
- “我看懂了”是否真的能被独立解释、预测、执行或迁移验证？

`lijie` 把学习组织成一个可检查的闭环：

```text
目标 -> 校准 -> 学科拆解 -> 构造最小模型 -> 主动生成
     -> 检验 -> 定向修复 -> 迁移 -> 延迟复习
```

## R2 的核心变化

R2 将 skill 分成稳定核心协议、学科适配器、学习状态和证据记录四层：

1. **学习契约**：先明确学习对象、目标能力、范围和成功标准。
2. **最小校准**：用少量预测、解释或微型应用题观察真实起点，不猜测学习者的隐藏心理状态。
3. **学科拆解**：按学科的对象、原语、操作、表示、假设、不变量、机制、约束、失败模式和验证方式展开。
4. **主动生成与检验**：通过 explain、predict、apply、compare、diagnose、counterexample、perform、transfer 等任务判断掌握程度。
5. **可控演化**：学习偏好和跨会话状态只能在用户同意、证据支持和回归测试之后升级。

## 快速安装

Windows：

```powershell
git clone https://github.com/aDragon0707/understanding.git
cd understanding
Copy-Item -Recurse -Force .\skill\lijie C:\Users\<YOU>\.codex\skills\
```

macOS / Linux：

```bash
git clone https://github.com/aDragon0707/understanding.git
cd understanding
cp -R skill/lijie ~/.codex/skills/
```

安装后，在 Codex 中使用 `$lijie`：

```text
用 $lijie 学习这个概念：先建立最小模型，再给我一个预测题、一个应用题和一个迁移题。
```

## 适合怎么用

### 学习代码 / 软件系统

```text
Use $lijie to teach me micrograd from first principles.
Start with the smallest runnable mechanism, trace the forward and backward passes,
then give me a debugging task and a transfer task.
```

代码适配器会优先关注：对象与状态、输入输出、调用链、执行轨迹、不变量、边界条件、失败模式、测试和可运行实现。

### 学习数学

```text
用 $lijie 学习这个定理：先说明它要解决什么问题，
再拆定义、假设、不变量和推导来源，最后给我证明骨架、反例和变体题。
```

数学适配器会优先关注：对象、定义、量词、假设、表示变换、推导、证明义务、反例、边界条件和迁移。

### 学习其他领域

```text
用 $lijie 学习这个陌生领域。先列出它的对象、基本原语、核心操作、
约束和验证方式，再构造一个最小可用模型，不要直接套用代码或数学模板。
```

## 三个独立维度

不要把输出长度、互动方式和严谨程度混成一个维度：

| 维度 | 选项 | 适用场景 |
|---|---|---|
| 深度 | `Light` / `Deep` | 快速定位 vs. 真正掌握 |
| 互动 | `One-shot` / `Interactive` / `Coaching` | 成品交付 vs. 主动生成 vs. 长期辅导 |
| 验证 | `Informal` / `Rigorous` / `Source-backed` | 普通理解 vs. 严格推导 vs. 需要来源核验 |

例如：短摘要可以是 `Light + One-shot`；学习 micrograd 可以是 `Deep + Interactive`；研究论文可以是 `Deep + Source-backed`。

## 证据与边界

`lijie` 区分以下证据状态：

```text
source-backed  来源直接支持
observed       在学习者回答或任务结果中观察到
inferred       基于证据的模型推断
uncertain      当前证据不足
uncovered      尚未检查
```

它不会假装能直接读取人的隐含上下文，也不会因为一次“听起来顺畅”就宣称掌握。学习者的解释、预测、执行、反例、迁移和延迟复习结果，才是调整讲解方式的依据。

它也不是以下工具：

- 单纯翻译、改写、校对或回答一个事实问题时的强制长模板；
- 人格诊断或固定的“学习类型”分类器；
- 未经用户同意就写入长期记忆的个人偏好系统。

## 仓库结构

```text
.
|-- README.md
|-- CHANGELOG.md
|-- LICENSE
|-- docs/
|   |-- INTRO.en.md
|   |-- INTRO.zh-CN.md
|   |-- R2-design-spec.zh-CN.md
|   |-- evaluation/
|   |   |-- AB-test-2026-07-24.md
|   |   `-- AB-test-micrograd-2026-07-24.md
|   `-- evolution/
|       `-- lijie-evolution-log.md
`-- skill/
    `-- lijie/
        |-- SKILL.md
        |-- agents/
        |   `-- openai.yaml
        `-- references/
            |-- code-learning.md
            |-- domain-adapter-template.md
            |-- learner-state-schema.md
            |-- math-learning.md
            `-- structure-framework.md
```

`skill/lijie/` 是可安装包；`docs/` 保存设计、评估和演化记录。旧版保护快照不放入公开包，而是保留在维护者本地作为回滚材料。

## 验证记录

R2 的公开验证记录位于 [`docs/evaluation/`](docs/evaluation/)：

- skill quick validation：通过；
- 数学 A/B 测试：R2 为 `13/14`，旧版为 `8/14`；
- micrograd 语义测试：`3/3` 通过。

这些结果说明 R2 在本轮测试任务上表现更好，但不代表对所有学科、所有学习者或长期记忆都已经完成充分评估。后续修改应继续经过回归测试，而不是只依据一次对话的主观流畅度。

## 文档导航

- [中文介绍](docs/INTRO.zh-CN.md)
- [English introduction](docs/INTRO.en.md)
- [R2 设计规格](docs/R2-design-spec.zh-CN.md)
- [A/B 测试记录](docs/evaluation/AB-test-2026-07-24.md)
- [micrograd 测试记录](docs/evaluation/AB-test-micrograd-2026-07-24.md)
- [演化日志](docs/evolution/lijie-evolution-log.md)

## 许可证

MIT License，见 [LICENSE](LICENSE)。
