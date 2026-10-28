<!--
  这是 https://github.com/sxh313 展示的个人主页。
  merged-prs 与 activity 标记之间的内容由 .github/workflows/refresh.yml 自动更新；
  如需调整这些区域的文字，请同步修改 .github/scripts/render_merged_prs.py。
-->

<div align="center">

# sxh313

### AI Agent Engineering · Agent Harness · Runtime

<p>
  系统学习和实践 AI Agent 工程，关注可运行、可评估、可恢复、可生产化的智能体系统。<br/>
  将原理、源码、工程、项目和面试内容重新组织成一套可以在线阅读、动手验证和反复复习的中文知识体系。
</p>

<p>
  <a href="https://sxh313.github.io/engineering-map/ai/"><b>🤖 AI Agent 学习中心</b></a>
  ·
  <a href="https://sxh313.github.io/engineering-map/ai/handbook"><b>📖 融合学习手册</b></a>
  ·
  <a href="https://sxh313.github.io/engineering-map/ai/roadmap"><b>🧪 实践路线</b></a>
  ·
  <a href="#-开源贡献"><b>🌍 开源贡献</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/AI_Agent-Engineering-8250DF?style=flat-square" alt="AI Agent Engineering" />
  <img src="https://img.shields.io/badge/Harness_%26_Runtime-Systems-0969DA?style=flat-square" alt="Harness 与 Runtime" />
  <img src="https://img.shields.io/badge/Open_Source-Contributor-1F883D?style=flat-square&logo=github&logoColor=white" alt="Open Source Contributor" />
</p>

</div>

## 🤖 AI Agent 综合知识体系

这不是两个开源仓库的链接集合，而是一套围绕 **Agent 怎样理解目标、组织上下文、调用工具、保存状态、评估结果并持续改进** 重新编排的学习体系。

### 原理体系 · AI Agent Book

用于建立 Agent 的整体认知框架，覆盖 Agent 基本原理、上下文工程、Memory 与 RAG、Tool Calling、Coding Agent、多模态交互、评估、训练、多 Agent 和持续进化。

[阅读 AI Agent Book 站内版 →](https://sxh313.github.io/engineering-map/ai/library/ai-agent-book/)

### 工程体系 · zero2Agent

用于理解 Agent 如何从概念变成真实系统，覆盖 Agent Loop、Context Engineering、Tool Calling、Runtime、Agent Infra、Coding Agent、SDK 与框架、训练评估、生产项目和面试专题。

[阅读 zero2Agent 站内版 →](https://sxh313.github.io/engineering-map/ai/library/zero2agent/)

### 运行体系 · Agent Harness

Harness 是承载 Agent 运行所需能力的工程外壳：它把模型、指令、工具、上下文、权限和执行环境装配在一起，并处理 Session、Transcript、沙箱、状态持久化、中断恢复、人工确认和可观测性。

[阅读 Coding Agent 与 Harness 专题 →](https://sxh313.github.io/engineering-map/ai/handbook#appendix-harnesses)

### 实践与复习体系

每个主题继续连接分阶段学习、动手实践、完成标准、自测问题、面试表达、项目拆解、失败分析以及评估回归，目标是把“读过”推进到“能够实现、验证和解释”。

[进入实践路线 →](https://sxh313.github.io/engineering-map/ai/roadmap) · [进入 Agent 面试专题 →](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/)

> **融合关系：**AI Agent Book 偏原理，zero2Agent 偏工程；[融合学习手册](https://sxh313.github.io/engineering-map/ai/handbook)负责把两套资料按同一条 Agent 工程主线重新组织。

> **来源边界：**本站在遵守原项目署名和许可证要求的前提下进行站内整理与学习路径重组。AI Agent Book 使用 Apache License 2.0；zero2Agent 主体使用 MIT License；其面试部分使用 CC BY-NC-SA 4.0。

## 🧭 AI Agent 学习主线

1. **Agent 基本闭环**：理解模型、动作、观察和停止条件怎样组成最小 Agent Loop。
2. **上下文工程**：决定当前任务真正需要哪些指令、历史、知识和环境信息。
3. **Memory 与 RAG**：区分会话状态、长期记忆和外部知识检索的职责。
4. **Tool / MCP / Skill**：理解工具能力、协议连接和可复用操作规范之间的边界。
5. **Harness 与 Runtime**：装配运行环境，并管理状态、Session、调度、持久化和恢复。
6. **Coding Agent**：让 Agent 安全地使用文件、终端、代码搜索、沙箱和异步任务。
7. **评估与可观测性**：通过 Trace、数据集、失败分类和回归测试判断系统是否变好。
8. **训练与行为优化**：理解预训练、SFT、RL 和推理期优化分别解决什么问题。
9. **持续进化**：让知识、指令、程序和模型参数通过反馈闭环持续更新。
10. **Multi-Agent 与生产项目**：处理任务拆分、协作边界、共享状态、交接和验收。

[按照 10 个阶段阅读完整手册 →](https://sxh313.github.io/engineering-map/ai/handbook)

## ⚙️ Harness、Runtime 与 Agent Loop

```text
用户目标
  ↓
Agent Harness
  模型 · 指令 · 工具 · 上下文 · 权限 · 执行环境
  ↓
Agent Runtime
  状态 · Session · 调度 · 持久化 · 中断恢复
  ↓
Agent Loop
  推理 → 调用工具 → 获得观察 → 更新状态 → 判断是否继续
  ↓
评估与持续改进
```

Harness 不只是某个框架的名称。它负责为 Agent 准备并约束运行条件；Runtime 管理任务执行过程；Agent Loop 则在这些条件内不断推理、行动和观察。

## 📚 站内学习入口

- [AI Agent 学习首页](https://sxh313.github.io/engineering-map/ai/)：先了解整套知识体系及推荐学习顺序。
- [AI Agent 融合手册](https://sxh313.github.io/engineering-map/ai/handbook)：按 10 个阶段学习原理、工程控制点和面试表达。
- [AI Agent 全部内容目录](https://sxh313.github.io/engineering-map/ai/atlas)：查看两套来源内容到站内课程的完整映射。
- [AI Agent 实践路线](https://sxh313.github.io/engineering-map/ai/roadmap)：通过练习、验收标准和复盘完成实践闭环。
- [AI Agent Book 站内版](https://sxh313.github.io/engineering-map/ai/library/ai-agent-book/)：完整阅读原理章节和配套图表。
- [zero2Agent 站内版](https://sxh313.github.io/engineering-map/ai/library/zero2agent/)：完整阅读工程课程、项目和专题内容。
- [Agent Harness 专题](https://sxh313.github.io/engineering-map/ai/handbook#appendix-harnesses)：理解 Coding Agent 的运行外壳和工程控制点。
- [Agent 面试复习](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/)：按工程主题复习高频问题和追问。

主要学习正文均部署在自己的 GitHub Pages 站内，可以直接在线阅读。

## 🧠 AI Agent 工程关注方向

- **Harness 与 Runtime**：能力装配、任务生命周期、状态持久化、中断恢复和并行调度。
- **Context / Memory / RAG**：上下文选择、压缩、检索、长期记忆和知识更新。
- **Tool / MCP / Skill**：工具描述、参数校验、协议连接、权限边界和错误恢复。
- **Coding Agent**：文件、终端、代码搜索、沙箱、Session Transcript 和人机协作。
- **Evaluation**：Trace、测试集、失败分类、回归评估、成本与延迟控制。
- **Multi-Agent**：任务拆分、角色边界、共享状态、交接协议和结果验收。

## 🌍 开源贡献

通过真实开源项目检验 Agent 工程理解，关注源码阅读、问题定位、最小改动、测试验证和上游协作。下面只展示已经合并 PR 的项目级统计，不将合并数量描述为项目主导经验。

<!-- merged-prs:start -->
<p align="center">
  <img src="https://img.shields.io/badge/%E5%B7%B2%E5%90%88%E5%B9%B6%20PR-68-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="68 已合并 pr" />
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E9%A1%B9%E7%9B%AE-18-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="18 贡献项目" />
  <img src="https://img.shields.io/badge/%E4%B8%8A%E6%B8%B8%E9%A1%B9%E7%9B%AE%20Stars-944.4k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="944.4k 上游项目 stars" />
</p>

| 贡献项目 | ★ | 主要语言 | 已合并 |
| :-- | --: | :-- | --: |
| <img src="https://github.com/openclaw.png?size=48" width="24" height="24" alt="" />&nbsp;[`openclaw/openclaw`](https://github.com/openclaw/openclaw)<br><sub>可以在任意操作系统和平台上执行真实任务的开源 AI 助手。</sub> | 393.2k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 11 |
| <img src="https://github.com/bytedance.png?size=48" width="24" height="24" alt="" />&nbsp;[`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)<br><sub>面向深度研究、代码生成与内容创作的长程智能体框架。</sub> | 84.5k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 12 |
| <img src="https://github.com/agentscope-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`agentscope-ai/agentscope`](https://github.com/agentscope-ai/agentscope)<br><sub>用于构建、运行与观测可信智能体的开发框架。</sub> | 34.5k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 8 |
| <img src="https://github.com/QwenLM.png?size=48" width="24" height="24" alt="" />&nbsp;[`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code)<br><sub>运行在终端中的开源 AI 编程智能体。</sub> | 28.8k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 2 |
| <img src="https://github.com/TencentCloud.png?size=48" width="24" height="24" alt="" />&nbsp;[`TencentCloud/Octop`](https://github.com/TencentCloud/Octop)<br><sub>支持多用户、多智能体协作的自托管 AI 助手。</sub> | 11.2k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 10 |
| <details><summary><sub>展开其余 13 个项目</sub></summary><br><img src="https://github.com/cheaper-inference.png?size=48" width="24" height="24" alt="" />&nbsp;[`cheaper-inference/OmniRoute`](https://github.com/cheaper-inference/OmniRoute) &middot; 81.9k &middot; 3<br><img src="https://github.com/headroomlabs-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`headroomlabs-ai/headroom`](https://github.com/headroomlabs-ai/headroom) &middot; 78.1k &middot; 3<br><img src="https://github.com/MemPalace.png?size=48" width="24" height="24" alt="" />&nbsp;[`MemPalace/mempalace`](https://github.com/MemPalace/mempalace) &middot; 59.8k &middot; 1<br><img src="https://github.com/TriliumNext.png?size=48" width="24" height="24" alt="" />&nbsp;[`TriliumNext/Trilium`](https://github.com/TriliumNext/Trilium) &middot; 38.6k &middot; 3<br><img src="https://github.com/oraios.png?size=48" width="24" height="24" alt="" />&nbsp;[`oraios/serena`](https://github.com/oraios/serena) &middot; 30.8k &middot; 1<br><img src="https://github.com/yamadashy.png?size=48" width="24" height="24" alt="" />&nbsp;[`yamadashy/repomix`](https://github.com/yamadashy/repomix) &middot; 29.0k &middot; 4<br><img src="https://github.com/livekit.png?size=48" width="24" height="24" alt="" />&nbsp;[`livekit/agents`](https://github.com/livekit/agents) &middot; 15.0k &middot; 3<br><img src="https://github.com/microsoft.png?size=48" width="24" height="24" alt="" />&nbsp;[`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) &middot; 14.3k &middot; 1<br><img src="https://github.com/mrexodia.png?size=48" width="24" height="24" alt="" />&nbsp;[`mrexodia/ida-pro-mcp`](https://github.com/mrexodia/ida-pro-mcp) &middot; 13.2k &middot; 2<br><img src="https://github.com/CursorTouch.png?size=48" width="24" height="24" alt="" />&nbsp;[`CursorTouch/Windows-MCP`](https://github.com/CursorTouch/Windows-MCP) &middot; 10.5k &middot; 1<br><img src="https://github.com/mobile-next.png?size=48" width="24" height="24" alt="" />&nbsp;[`mobile-next/mobile-mcp`](https://github.com/mobile-next/mobile-mcp) &middot; 10.1k &middot; 1<br><img src="https://github.com/strands-agents.png?size=48" width="24" height="24" alt="" />&nbsp;[`strands-agents/harness-sdk`](https://github.com/strands-agents/harness-sdk) &middot; 9.0k &middot; 1<br><img src="https://github.com/timescale.png?size=48" width="24" height="24" alt="" />&nbsp;[`timescale/pg-aiguide`](https://github.com/timescale/pg-aiguide) &middot; 1.9k &middot; 1</details> | 392.2k | — | 25 |

<sub>仅统计 Stars 不低于 1,000 的项目及其中已合并的 PR。表格展示 5 个代表项目，其余项目可在最后一行展开。数据由 [.github/workflows/refresh.yml](.github/workflows/refresh.yml) 自动更新；最后更新于 2026-10-28 01:49 UTC。</sub>
<!-- merged-prs:end -->

## 🧱 AI 全栈能力底座

Agent 最终需要接入真实界面、业务服务、数据库和部署环境。TypeScript、Python、Go 与数据工程因此是 Agent 落地的能力底座，而不是与 Agent 主线平行的独立方向。

```text
前端交互
  ↓
后端服务
  ↓
数据存储
  ↓
Python 能力服务
  ↓
Agent 系统
```

<p>
  <img src="https://skillicons.dev/icons?i=go,python,ts,mysql,redis,docker,git,github&theme=dark" alt="Go、Python、TypeScript、MySQL、Redis、Docker、Git 与 GitHub" />
</p>

- **前端与交互**：TypeScript、React、Next.js，以及 Agent 任务状态和结果展示。
- **后端服务**：Go、Gin、GORM、gRPC、Node.js、API 设计和任务接口。
- **数据与检索**：MySQL、PostgreSQL、Redis、向量检索、混合检索和 RAG。
- **能力服务**：Python、FastAPI、模型接入、数据处理和 Agent 工具服务。
- **工程交付**：Docker、测试、自动化、文档、代码审查和可观测性。

后端八股、源码笔记和工程知识也整理在[在线学习地图](https://sxh313.github.io/engineering-map/)中，用于查询、复习和项目实践。

## 🛤️ 配套成长路线：前端 → 全栈 → Agent

这条路线用于为 AI Agent 应用开发补齐前端、后端、数据库和 Python 服务能力，适合从 Vibe Coding 继续走向“能够读懂、修改和验证完整项目”的学习阶段。

覆盖内容包括：

- JavaScript / TypeScript
- React / Next.js
- Node.js / Express
- PostgreSQL / SQL
- Python / FastAPI
- Agent 工程与完整项目
- 八股复习与模拟面试

[查看飞书外部学习路线 →](https://bcnbltoq3sjn.feishu.cn/docx/EpEPd9agzoh0tpxdp4mc7cmMnfe)

> 这是配套的外部飞书文档，不属于 GitHub Pages 站内 AI Agent 知识库正文。

## 👋 关于我

- 当前主线是 **AI Agent 工程与 AI 全栈应用开发**。
- 正在通过原理学习、源码阅读、项目实践和评估复盘理解 Agent 系统。
- 将零散资料整理为有顺序、有实践任务、有完成标准的中文学习路径。
- 通过开源协作检验理解：阅读源码、定位问题、完成最小改动并跟踪上游反馈。

## 📈 GitHub 活跃度

<!-- activity:start -->
最近 3 个月，数据来自 GitHub 贡献图。

<p align="center">
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E6%95%B0-9.8k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="9.8k 贡献数" />
  <img src="https://img.shields.io/badge/%E6%8F%90%E4%BA%A4%E6%95%B0-9.2k-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="9.2k 提交数" />
  <img src="https://img.shields.io/badge/%E6%B6%89%E5%8F%8A%E4%BB%93%E5%BA%93-56-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="56 涉及仓库" />
</p>
<!-- activity:end -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" />
    <img alt="GitHub 贡献图动态贪吃蛇" src="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" width="100%" />
  </picture>
</p>
