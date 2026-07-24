# Lijie A/B Test: micrograd — 2026-07-24

## 测试边界

官方 Karpathy `micrograd` 仓库不在本地，且当前环境连接 GitHub 失败。因此本次使用按 micrograd 标量 `Value`、计算图和反向传播语义编写的最小 fixture。

这是真实 Python 执行的 micrograd 语义测试，但不是官方仓库版本回归测试。

## 固定代码任务

> 真正理解 micrograd 的 `Value.backward()`：为什么反向传播需要按拓扑逆序执行，为什么多个分支汇聚到同一节点时必须用 `+=` 累加梯度？先预测 `x=3; z=x*x+x` 的 `x.grad`，再用一个改变计算图结构的任务验证。

固定学习者回答：

> 我觉得梯度是 6，因为 `x*x` 的导数是 `2x`；我不确定最后那个 `+x` 的梯度会不会自动合进去。

## 执行证据

本地 fixture：

- `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\micrograd-ab-test\micrograd_fixture.py`
- `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\micrograd-ab-test\test_engine.py`

实际结果：

```text
CORRECT z=12.0 x.grad=7.0
OVERWRITE_MUTANT z=12.0 x.grad=3.0
TRANSFER z=18.0 x.grad=12.0
MICROGRAD_SEMANTIC_TESTS=3 FAILED=0
```

## A 组：旧版全局 `lijie`

### 代表性响应

```text
z=x*x+x 有两条从 x 到 z 的路径：
1. x→乘法→z，贡献 2x=6；
2. x→加法→z，贡献 1。
所以总梯度是 6+1=7。

必须用 +=，因为同一节点可能从多个下游节点收到梯度贡献。
拓扑逆序保证一个节点先收齐下游梯度，再继续传播给它的父节点。
```

### 行为评价

旧版能给出正确的 Feynman explanation、计算图关系和检查问题。它也能说明 `+=`，但运行、mutation test 和状态诊断不是代码任务的明确结束标准，容易停在“解释正确”。

## B 组：R2 draft + code adapter

### 学习契约

目标为 `explain + diagnose + perform + transfer`。成功标准：

1. 预测 `x.grad=7`；
2. 沿计算图逐边说明局部梯度；
3. 把 `+=` 改为 `=` 后能预测并运行出错误；
4. 在结构变化后的图中再次得到正确梯度。

### 对固定回答的诊断

学习者知道 `x*x` 的局部导数，但遗漏了 `x→加法→z` 路径。可观察状态为：

```text
chain rule on one path: prompted/fragile
gradient accumulation across branches: misconception
topological execution: unknown
```

### 代表性响应

```text
先把 data 和 grad 分开：前向值 z=12 不受梯度覆盖 bug 影响。

反向时：
z.grad=1
├─ 加法左支给 (x*x).grad += 1
└─ 加法右支给 x.grad += 1

乘法节点随后传播：
x.grad += x.data * (x*x).grad，执行两次，共增加 6。
因此 x.grad=1+6=7。

把 += 改成 = 后，分支贡献会互相覆盖。实际 mutation test 得到 x.grad=3，
而 z.data 仍是 12；这把“前向正确”和“反向正确”区分开了。
```

### 迁移

改变图结构：

```python
x = Value(3.0)
y = x * x
z = y + y
z.backward()
```

正确结果为 `x.grad=12`。这不仅复用了输入 `x`，还让中间节点 `y` 被两个分支复用，检查梯度是否在中间节点先汇聚再向后传播。

## 评分

评分尺度：`0` = 未体现，`1` = 部分体现，`2` = 明确且可执行。单任务人工评分，不是独立 benchmark。

| 维度 | A 旧版 | B R2 | 观察 |
|---|---:|---:|---|
| 目标与成功标准 | 2 | 2 | 两者都理解任务目标 |
| 执行/状态轨迹 | 1 | 2 | R2 code adapter 明确追踪 `data`、`grad` 和节点顺序 |
| 错误模型诊断 | 1 | 2 | R2 把遗漏分支识别为具体 misconception |
| 运行与 mutation evidence | 1 | 2 | R2 将真实运行和覆盖突变纳入结束标准 |
| 结构迁移 | 1 | 2 | R2 用 `y+y` 改变图结构，而不只是改数字 |
| 交互负担 | 2 | 1 | 旧版更轻，R2 验证步骤更多 |
| **合计** | **8/12** | **11/12** | R2 证据链更强，旧版更快速 |

## 结论

这个任务暴露了 R2 的实际价值：它要求把“我理解 `+=`”落到预测、执行轨迹、失败 mutation、测试和结构迁移上。旧版可以解释正确，但不强制得到可执行证据。

R2 仍有开销风险。对只问“micrograd 为什么用 `+=`”的一次性问题，应选择 `Light + One-shot + Informal`，不应输出学习状态和完整测试协议。

## 限制与下一步

- 不是官方仓库回归测试；网络失败使这一项目前不可验证。
- A/B 输出由同一模型按两份协议生成，存在自评偏差。
- 下一步若能获得官方源码，应对真实 `micrograd/engine.py` 和它的 tests 运行同一 mutation test。
