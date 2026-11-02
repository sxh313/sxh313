<!--
  这是 https://github.com/sxh313 展示的个人主页。
  merged-prs 与 activity 标记之间的内容由 .github/workflows/refresh.yml 自动更新；
  如需调整这些区域的文字，请同步修改 .github/scripts/render_merged_prs.py。
-->

<div align="center">

# sxh313

### AI Agent 工程 · Agent Harness · AI 全栈能力底座

<p>
  欢迎来到我的工程学习主页。<br/>
  我正在围绕 Agent Harness、Runtime、上下文、记忆、工具调用、评估与生产化，<br/>
  整理一套可以在线阅读、实践和复习的 AI Agent 中文学习体系。
</p>

<p>
  <a href="https://sxh313.github.io/engineering-map/ai/"><b>🤖 AI Agent 学习中心</b></a><br/>
  <a href="https://sxh313.github.io/engineering-map/ai/handbook"><b>📖 融合学习手册</b></a><br/>
  <a href="https://sxh313.github.io/engineering-map/ai/roadmap"><b>🧪 AI Agent 实践路线</b></a><br/>
  <a href="#-开源贡献"><b>🌍 开源贡献</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/AI_Agent-Engineering-8250DF?style=flat-square" alt="AI Agent Engineering" />
  <img src="https://img.shields.io/badge/Harness_%26_Runtime-Systems-0969DA?style=flat-square" alt="Harness 与 Runtime" />
  <img src="https://img.shields.io/badge/Open_Source-Contributor-1F883D?style=flat-square&logo=github&logoColor=white" alt="Open Source Contributor" />
</p>

</div>

## 🤖 AI Agent 综合知识体系

这里不是简单收集链接，而是把原理资料、工程资料、运行机制、实践任务和面试复习，重新编排成一条 Agent 工程主线：理解 Agent 如何组织上下文、调用工具、保存状态、完成任务，并通过评估持续改进。

### 1. 原理体系：AI Agent Book

偏向建立整体认知，覆盖 Agent 基本原理、上下文工程、Memory 与 RAG、Tool Calling、Coding Agent、多模态交互、评估、训练、多 Agent 和持续进化。

[阅读 AI Agent Book 站内版 →](https://sxh313.github.io/engineering-map/ai/library/ai-agent-book/)

### 2. 工程体系：zero2Agent

偏向理解真实系统，覆盖 Agent Loop、Context Engineering、Tool Calling、Runtime、Agent Infra、Coding Agent、SDK 与框架、训练评估、生产项目和 Agent 面试专题。

[阅读 zero2Agent 站内版 →](https://sxh313.github.io/engineering-map/ai/library/zero2agent/)

### 3. 运行体系：Agent Harness

Harness 是承载 Agent 运行所需能力的工程外壳，负责把模型、指令、工具、上下文、权限和执行环境装配起来，并约束它们如何协作。

它重点处理：

- Agent Loop 的运行控制
- Session、Transcript 与状态持久化
- 工具权限、调用边界和人工确认
- 沙箱、终端、文件与代码搜索能力
- 中断恢复、可观测性和 Coding Agent 的执行环境

[阅读 Agent Harness 专题 →](https://sxh313.github.io/engineering-map/ai/handbook#appendix-harnesses)

### 4. 实践与复习体系

通过分阶段学习、动手实践、完成标准、自测问题、项目拆解、失败分析、面试表达和评估回归，把“读过”推进到“能够实现、验证和解释”。

[进入 AI Agent 实践路线 →](https://sxh313.github.io/engineering-map/ai/roadmap) · [进入 Agent 面试专题 →](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/)

> **融合关系**
>
> - **AI Agent Book**：偏原理，帮助建立 Agent 的整体认知框架。
> - **zero2Agent**：偏工程，帮助理解 Agent 如何落地为真实系统。
> - **融合学习手册**：将两套资料按同一条 Agent 工程主线重新组织。
>
> **来源与许可**
>
> - AI Agent Book：Apache License 2.0
> - zero2Agent 主体：MIT License
> - zero2Agent 面试部分：CC BY-NC-SA 4.0
> - 本站遵守原项目署名和许可证要求，进行站内整理与学习路径重组，不将相关资料表述为个人原创教材。

## 🧭 AI Agent 学习路线

按下面的顺序，从最小闭环逐步走向可运行、可评估、可恢复的 Agent 系统：

1. **Agent 基本闭环**：理解模型、动作、观察和停止条件如何组成最小 Agent Loop。
2. **Context Engineering**：选择当前任务真正需要的指令、历史、知识和环境信息。
3. **Memory 与 RAG**：区分会话状态、长期记忆和外部知识检索的职责。
4. **Tool / MCP / Skill**：理解工具能力、协议连接和可复用操作规范的边界。
5. **Harness 与 Runtime**：装配运行环境，管理状态、Session、调度、持久化和恢复。
6. **Coding Agent**：让 Agent 安全使用文件、终端、代码搜索、沙箱和异步任务。
7. **评估与可观测性**：用 Trace、数据集、失败分类和回归测试判断系统是否变好。
8. **训练与行为优化**：理解预训练、SFT、RL 和推理期优化分别解决什么问题。
9. **持续进化**：让知识、指令、程序和模型参数通过反馈闭环持续更新。
10. **Multi-Agent 与生产项目**：处理任务拆分、协作边界、共享状态、交接和验收。

[按照 10 个阶段阅读完整融合手册 →](https://sxh313.github.io/engineering-map/ai/handbook)

## ⚙️ Agent Harness 与 Runtime

Harness 不是某个普通框架名称，而是为 Agent 准备并约束运行条件的工程外壳；Runtime 管理任务执行过程；Agent Loop 在这些条件内持续推理、行动和观察。

```text
用户目标
  ↓
Agent Harness
  模型 · 指令 · 工具 · 上下文 · 权限 · 执行环境
  ↓
Agent Runtime
  Session · 状态 · 调度 · 持久化 · 中断恢复
  ↓
Agent Loop
  推理 → 工具调用 → 观察 → 更新状态 → 继续或结束
  ↓
评估与持续改进
```

## 📚 站内学习入口

核心内容优先指向自己的 GitHub Pages，外部来源仅作为原始资料和配套路线说明：

- [AI Agent 学习首页](https://sxh313.github.io/engineering-map/ai/)
- [AI Agent 融合手册](https://sxh313.github.io/engineering-map/ai/handbook)
- [AI Agent 全部内容目录](https://sxh313.github.io/engineering-map/ai/atlas)
- [AI Agent 实践路线](https://sxh313.github.io/engineering-map/ai/roadmap)
- [AI Agent Book 站内版](https://sxh313.github.io/engineering-map/ai/library/ai-agent-book/)
- [zero2Agent 站内版](https://sxh313.github.io/engineering-map/ai/library/zero2agent/)
- [Agent Harness 专题](https://sxh313.github.io/engineering-map/ai/handbook#appendix-harnesses)
- [Agent 面试复习](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/)

## 🧠 AI Agent 工程关注方向

- **Harness 与 Runtime**：能力装配、任务生命周期、状态持久化、中断恢复和调度。
- **Context / Memory / RAG**：上下文选择、压缩、检索、长期记忆和知识更新。
- **Tool / MCP / Skill**：工具描述、参数校验、协议连接、权限边界和错误恢复。
- **Coding Agent**：文件、终端、代码搜索、沙箱、Session Transcript 和人机协作。
- **Evaluation**：Trace、测试集、失败分类、回归评估、成本与延迟控制。
- **Multi-Agent**：任务拆分、角色边界、共享状态、交接协议和结果验收。

## 🌍 开源贡献

通过真实开源项目检验 Agent 工程理解，关注源码阅读、问题定位、最小改动、测试验证和上游协作。下面只展示已经合并 PR 的项目级统计，不将合并数量描述为项目主导经验。

<!-- merged-prs:start -->
<p align="center">
  <img src="https://img.shields.io/badge/%E5%B7%B2%E5%90%88%E5%B9%B6%20PR-69-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="69 已合并 pr" />
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E9%A1%B9%E7%9B%AE-18-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="18 贡献项目" />
  <img src="https://img.shields.io/badge/%E4%B8%8A%E6%B8%B8%E9%A1%B9%E7%9B%AE%20Stars-951.1k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="951.1k 上游项目 stars" />
</p>

| 贡献项目 | ★ | 主要语言 | 已合并 |
| :-- | --: | :-- | --: |
| <img src="https://github.com/openclaw.png?size=48" width="24" height="24" alt="" />&nbsp;[`openclaw/openclaw`](https://github.com/openclaw/openclaw)<br><sub>可以在任意操作系统和平台上执行真实任务的开源 AI 助手。</sub> | 393.8k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 11 |
| <img src="https://github.com/bytedance.png?size=48" width="24" height="24" alt="" />&nbsp;[`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)<br><sub>面向深度研究、代码生成与内容创作的长程智能体框架。</sub> | 84.9k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 12 |
| <img src="https://github.com/agentscope-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`agentscope-ai/agentscope`](https://github.com/agentscope-ai/agentscope)<br><sub>用于构建、运行与观测可信智能体的开发框架。</sub> | 35.2k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 8 |

<sub>仅统计 Stars 不低于 1,000 的项目及其中已合并的 PR。表格仅展示 openclaw/openclaw、bytedance/deer-flow 和 agentscope-ai/agentscope。数据由 [.github/workflows/refresh.yml](.github/workflows/refresh.yml) 自动更新；最后更新于 2026-11-02 23:57 UTC。</sub>
<!-- merged-prs:end -->

## 🧱 AI 全栈能力底座

Agent 最终需要接入真实界面、业务服务、数据库和部署环境。TypeScript、Python、Go 与数据工程是 Agent 落地的能力底座，而不是与 Agent 主线平行的独立方向。

```text
前端交互
  ↓
Node.js / Go 后端服务
  ↓
数据库与检索
  ↓
Python 能力服务
  ↓
Agent 系统
```

- **前端与交互**：TypeScript、React、Next.js，以及 Agent 任务状态和结果展示。
- **后端服务**：Go、Gin、GORM、gRPC、Node.js、API 设计和任务接口。
- **数据与检索**：MySQL、PostgreSQL、Redis、向量检索、混合检索和 RAG。
- **能力服务**：Python、FastAPI、模型接入、数据处理和 Agent 工具服务。
- **工程交付**：Docker、测试、自动化、文档、代码审查和可观测性。

[在线学习地图 →](https://sxh313.github.io/engineering-map/)

## 🛤️ 配套成长路线：前端 → 全栈 → Agent

这是一条外部配套路线，用来补齐 AI Agent 应用开发所需的前端、后端、数据库和 Python 服务能力：

- JavaScript / TypeScript
- React / Next.js
- Node.js / Express
- PostgreSQL / SQL
- Python / FastAPI
- Agent 工程与完整项目
- 八股复习与模拟面试

前端交互 → Node.js 后端 → 数据库 → Python 能力服务 → Agent 系统。

[查看飞书外部学习路线 →](https://bcnbltoq3sjn.feishu.cn/docx/EpEPd9agzoh0tpxdp4mc7cmMnfe)

> 这是外部飞书文档，不属于 GitHub Pages 站内 AI Agent 知识库正文。

## 👋 关于我

- 当前主线是 **AI Agent 工程与 AI 全栈应用开发**。
- 正在通过原理学习、源码阅读、项目实践和评估复盘理解 Agent 系统。
- 将零散资料整理为有顺序、有实践任务、有完成标准的中文学习路径。
- 通过开源协作检验理解：阅读源码、定位问题、完成最小改动并跟踪上游反馈。

<details>
<summary><b>📈 查看 GitHub 活跃度</b></summary>

<br/>

<!-- activity:start -->
最近 3 个月，数据来自 GitHub 贡献图。

<p align="center">
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E6%95%B0-9.8k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="9.8k 贡献数" />
  <img src="https://img.shields.io/badge/%E6%8F%90%E4%BA%A4%E6%95%B0-9.2k-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="9.2k 提交数" />
  <img src="https://img.shields.io/badge/%E6%B6%89%E5%8F%8A%E4%BB%93%E5%BA%93-55-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="55 涉及仓库" />
</p>
<!-- activity:end -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" />
    <img alt="GitHub 贡献图动态贪吃蛇" src="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" width="100%" />
  </picture>
</p>

</details>
