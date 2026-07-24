# 学习者状态 Schema

本 reference 规定如何记录一次学习中的可观察状态。除非用户明确同意，不要把它当作跨会话个人记忆保存。

## 最小状态

```yaml
learning_object: "当前学习对象"
goal: explain | use | derive | critique | create | retain
scope: "本次覆盖范围"
assumptions:
  - "关于前置知识或目标的明确假设"
prerequisites:
  known: []
  unknown_or_untested: []
observed_state:
  "概念或能力": unknown | fragile | misconception | prompted | independent | transferable | retained
evidence:
  - type: explanation | prediction | application | derivation | implementation | counterexample | delayed_retrieval
    observation: "学习者实际做了什么"
    interpretation: source-backed | observed | inferred | uncertain
misconceptions: []
tested_representations: []
current_hypotheses: []
next_probe: []
user_confirmed_preferences: []
retention_plan: []
```

## 状态判定

```text
unknown       尚未测试，不等于不会
fragile       在提示或熟悉表面条件下可以完成
misconception 存在可观察的错误模型
prompted      需要提示才能完成
independent   新任务中可以独立完成
transferable  改变表面条件后仍能完成
retained      延迟后仍能回忆并应用
```

不要因为一次流畅复述就从 `prompted` 跳到 `retained`。每次状态提升都应指出对应证据。

## 证据优先级

对“是否掌握”的判断，通常优先考虑：

```text
延迟迁移/独立实现
  > 新条件下的独立应用
  > 反例和错误诊断
  > 不看原文的解释或预测
  > 看着原文复述
  > 熟悉感和主观自信
```

这不是绝对排序；具体学科的 domain adapter 可以覆盖它。

## 隐私与持久化

- 当前会话内可以使用状态来调整下一步教学；
- 跨会话保存前应得到用户同意；
- 保存可验证的学习事实，不保存未经证实的人格标签；
- 每条长期偏好最好带来源、时间和最近验证情况；
- 用户要求删除或更正时，应以用户指令为准。

## 学习收据

一次深度学习结束时，可生成简洁收据：

```markdown
## 学习收据
- 学习对象：
- 目标：
- 已验证能力：
- 脆弱或错误部分：
- 尚未测试：
- 下一个迁移任务：
- 建议的延迟检索：
- 本次证据：
```

不要把收据写成泛泛的学习感想；每项都应尽量对应一个可观察证据。
