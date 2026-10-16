# liuliu-chat-style

致敬一位神明

## 使用方法

### 作为 Skill 使用

将 `liuliu-chat-style` 文件夹安装到所用工具的技能目录。

在 Codex 中可直接调用：

```text
使用 $liuliu-chat-style，按六六的口吻回复下面这段聊天：
……
```

也可以让它改写消息、模拟多轮对话，或检查回复是否符合角色口吻。

### 接入其他模型或聊天机器人

将 `assets/六六系统提示词.txt` 的内容放入模型的系统提示词。

每次调用时提供当前消息和必要的近期上下文。不同私聊、群聊分别保存，避免串话。提示词文件可以启动时读取，无需每条消息重新读文件。

## 文件说明

- `SKILL.md`：技能入口与使用范围。
- `references/口吻规则.md`：完整角色、词汇和场景规则。
- `references/QQ接入约定.md`：聊天触发、生图和资料修改协议。
- `references/场景验证.md`：虚构测试场景。
- `assets/六六系统提示词.txt`：合并后的运行提示词。

修改规则后，重新生成提示词：

```bash
python3 scripts/build_runtime.py
```

检查生成内容是否同步：

```bash
python3 scripts/build_runtime.py --check
```

## 说明

本项目提供聊天口吻方案，不包含 QQ 登录或机器人程序。识图、生图、修改资料等功能，需要接入程序实际支持。

模型可能偶发复读或偏离口吻，测试情况与限制见 `references/验证记录.md`。
