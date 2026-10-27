<!--
  这是 https://github.com/sxh313 展示的个人主页。
  merged-prs 与 activity 标记之间的内容由 .github/workflows/refresh.yml 自动更新；
  如需调整这些区域的文字，请同步修改 .github/scripts/render_merged_prs.py。
-->

<div align="center">

# 你好，我是 sxh313 👋

### AI Agent 工程 · AI 全栈 · 开源贡献

<p>
  关注 Agent Harness、Runtime、工具调用、上下文与记忆、评估及生产化落地。<br/>
  我把学习、实践和开源协作沉淀成一套可以在线阅读、持续复习的中文知识库。
</p>

<p>
  <a href="https://sxh313.github.io/engineering-map/ai/"><b>🤖 AI Agent 学习中心</b></a>
  ·
  <a href="https://sxh313.github.io/engineering-map/ai/handbook"><b>📖 融合学习手册</b></a>
  ·
  <a href="#-开源贡献"><b>🌍 开源贡献</b></a>
  ·
  <a href="https://github.com/sxh313?tab=repositories"><b>🧩 项目仓库</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/AI_Agent-Harness_%26_Runtime-8250DF?style=flat-square" alt="AI Agent Harness 与 Runtime" />
  <img src="https://img.shields.io/badge/Python-Agent_Engineering-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Agent Engineering" />
  <img src="https://img.shields.io/badge/Go-Backend_Foundation-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go Backend Foundation" />
</p>

</div>

## 🤖 AI Agent 学习与实践

我正在沿着一条完整的工程链路学习 Agent：不只关注 Prompt 和框架调用，也关注一个 Agent 怎样获得上下文、执行工具、保存状态、定位失败，并在评估之后持续改进。

```text
用户目标 → Harness 装配（模型 / 指令 / 工具 / 上下文）
                       ↓
          推理与规划 → 工具执行 → 环境反馈
              ↑                       ↓
              └── 状态 / 记忆 / 评估 ──┘
```

| 从这里开始 | 适合什么时候看 | 站内入口 |
| :-- | :-- | :-- |
| **AI Agent 综合路线** | 第一次进入，先了解完整学习结构 | [进入学习中心 →](https://sxh313.github.io/engineering-map/ai/) |
| **10 阶段融合手册** | 系统学习原理、工程控制点与面试表达 | [开始系统学习 →](https://sxh313.github.io/engineering-map/ai/handbook) |
| **Coding Agent 与 Harness** | 理解 Agent 的运行外壳、Session、工具环境与恢复机制 | [阅读 Harness 专题 →](https://sxh313.github.io/engineering-map/ai/handbook#appendix-harnesses) |
| **全部内容目录** | 查找 AI Agent Book 与 zero2Agent 的完整站内内容 | [查看完整目录 →](https://sxh313.github.io/engineering-map/ai/atlas) |
| **实践学习契约** | 从“看懂”走向“做出、验证、复盘” | [进入实践路线 →](https://sxh313.github.io/engineering-map/ai/roadmap) |
| **Agent 面试专题** | 按工具、RAG、Runtime 等主题集中复习 | [进入面试复习 →](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/) |

> 所有主要学习正文都部署在自己的 GitHub Pages 站内，可以直接在线阅读；手机端也按单列阅读和无横向滚动进行了适配。

> 🛤️ **配套成长路线：前端 → 全栈 → Agent**
>
> 面向刚完成 Vibe Coding、希望进一步读懂和改造真实项目的学习者，依次补齐 TypeScript、React / Next.js、Node.js、PostgreSQL、Python / FastAPI 与 Agent 工程，并为每一阶段设置练习和完成标准。
>
> [查看完整飞书学习路线 →](https://bcnbltoq3sjn.feishu.cn/docx/EpEPd9agzoh0tpxdp4mc7cmMnfe)

## 🧠 我关注的 Agent 工程问题

- **Agent Loop 与 Runtime：** 状态流转、任务生命周期、中断恢复、并行执行与可观测性。
- **Agent Harness：** 模型、指令、工具、上下文和执行环境的装配，以及 Session、权限、隔离与恢复机制。
- **Tool / MCP / Skill：** 工具描述、参数校验、权限边界、错误恢复与协议协作。
- **Context / Memory / RAG：** 上下文选择、压缩、检索、长期记忆及知识更新。
- **Coding Agent：** 文件、终端、代码搜索、沙箱、会话记录与人机协作。
- **Eval 与生产化：** Trace、数据集、失败分类、回归评估、成本和延迟控制。
- **Multi-Agent：** 任务拆分、角色边界、共享状态、交接协议与结果验收。

## 🌍 开源贡献

这里展示已有 PR 被合并的上游项目。统计区块会自动更新，只展示项目级信息，不逐条罗列 PR。

<!-- merged-prs:start -->
<p align="center">
  <img src="https://img.shields.io/badge/%E5%B7%B2%E5%90%88%E5%B9%B6%20PR-68-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="68 已合并 pr" />
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E9%A1%B9%E7%9B%AE-18-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="18 贡献项目" />
  <img src="https://img.shields.io/badge/%E4%B8%8A%E6%B8%B8%E9%A1%B9%E7%9B%AE%20Stars-944.2k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="944.2k 上游项目 stars" />
</p>

| 贡献项目 | ★ | 主要语言 | 已合并 |
| :-- | --: | :-- | --: |
| <img src="https://github.com/openclaw.png?size=48" width="24" height="24" alt="" />&nbsp;[`openclaw/openclaw`](https://github.com/openclaw/openclaw)<br><sub>可以在任意操作系统和平台上执行真实任务的开源 AI 助手。</sub> | 393.2k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 11 |
| <img src="https://github.com/bytedance.png?size=48" width="24" height="24" alt="" />&nbsp;[`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)<br><sub>面向深度研究、代码生成与内容创作的长程智能体框架。</sub> | 84.5k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 12 |
| <img src="https://github.com/agentscope-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`agentscope-ai/agentscope`](https://github.com/agentscope-ai/agentscope)<br><sub>用于构建、运行与观测可信智能体的开发框架。</sub> | 34.4k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 8 |
| <img src="https://github.com/QwenLM.png?size=48" width="24" height="24" alt="" />&nbsp;[`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code)<br><sub>运行在终端中的开源 AI 编程智能体。</sub> | 28.8k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 2 |
| <img src="https://github.com/TencentCloud.png?size=48" width="24" height="24" alt="" />&nbsp;[`TencentCloud/Octop`](https://github.com/TencentCloud/Octop)<br><sub>支持多用户、多智能体协作的自托管 AI 助手。</sub> | 11.2k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 10 |
| <details><summary><sub>展开其余 13 个项目</sub></summary><br><img src="https://github.com/cheaper-inference.png?size=48" width="24" height="24" alt="" />&nbsp;[`cheaper-inference/OmniRoute`](https://github.com/cheaper-inference/OmniRoute) &middot; 81.9k &middot; 3<br><img src="https://github.com/headroomlabs-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`headroomlabs-ai/headroom`](https://github.com/headroomlabs-ai/headroom) &middot; 78.0k &middot; 3<br><img src="https://github.com/MemPalace.png?size=48" width="24" height="24" alt="" />&nbsp;[`MemPalace/mempalace`](https://github.com/MemPalace/mempalace) &middot; 59.8k &middot; 1<br><img src="https://github.com/TriliumNext.png?size=48" width="24" height="24" alt="" />&nbsp;[`TriliumNext/Trilium`](https://github.com/TriliumNext/Trilium) &middot; 38.6k &middot; 3<br><img src="https://github.com/oraios.png?size=48" width="24" height="24" alt="" />&nbsp;[`oraios/serena`](https://github.com/oraios/serena) &middot; 30.8k &middot; 1<br><img src="https://github.com/yamadashy.png?size=48" width="24" height="24" alt="" />&nbsp;[`yamadashy/repomix`](https://github.com/yamadashy/repomix) &middot; 29.0k &middot; 4<br><img src="https://github.com/livekit.png?size=48" width="24" height="24" alt="" />&nbsp;[`livekit/agents`](https://github.com/livekit/agents) &middot; 15.0k &middot; 3<br><img src="https://github.com/microsoft.png?size=48" width="24" height="24" alt="" />&nbsp;[`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) &middot; 14.3k &middot; 1<br><img src="https://github.com/mrexodia.png?size=48" width="24" height="24" alt="" />&nbsp;[`mrexodia/ida-pro-mcp`](https://github.com/mrexodia/ida-pro-mcp) &middot; 13.2k &middot; 2<br><img src="https://github.com/CursorTouch.png?size=48" width="24" height="24" alt="" />&nbsp;[`CursorTouch/Windows-MCP`](https://github.com/CursorTouch/Windows-MCP) &middot; 10.5k &middot; 1<br><img src="https://github.com/mobile-next.png?size=48" width="24" height="24" alt="" />&nbsp;[`mobile-next/mobile-mcp`](https://github.com/mobile-next/mobile-mcp) &middot; 10.1k &middot; 1<br><img src="https://github.com/strands-agents.png?size=48" width="24" height="24" alt="" />&nbsp;[`strands-agents/harness-sdk`](https://github.com/strands-agents/harness-sdk) &middot; 9.0k &middot; 1<br><img src="https://github.com/timescale.png?size=48" width="24" height="24" alt="" />&nbsp;[`timescale/pg-aiguide`](https://github.com/timescale/pg-aiguide) &middot; 1.9k &middot; 1</details> | 392.1k | — | 25 |

<sub>仅统计 Stars 不低于 1,000 的项目及其中已合并的 PR。表格展示 5 个代表项目，其余项目可在最后一行展开。数据由 [.github/workflows/refresh.yml](.github/workflows/refresh.yml) 自动更新；最后更新于 2026-10-27 22:52 UTC。</sub>
<!-- merged-prs:end -->

## 🧱 AI 全栈能力底座

Agent 最终要运行在真实系统里，因此我也持续补齐后端、数据、部署和工程协作能力。

学习顺序不是孤立地堆技术栈，而是沿着 **前端交互 → 后端服务 → 数据存储 → Python 能力服务 → Agent 系统** 逐步形成完整的数据链路和工程视角。

<p>
  <img src="https://skillicons.dev/icons?i=go,python,ts,mysql,redis,docker,git,github&theme=dark" alt="Go、Python、TypeScript、MySQL、Redis、Docker、Git 与 GitHub" />
</p>

| 能力方向 | 学习与实践内容 |
| :-- | :-- |
| 后端服务 | Go、Gin、GORM、gRPC、API 设计与服务治理 |
| 数据与检索 | MySQL、Redis、向量检索、混合检索与 RAG |
| Agent 应用 | Python、TypeScript、模型接入、工作流与交互界面 |
| 工程交付 | Docker、测试、自动化、文档、代码审查与可观测性 |

后端八股、源码笔记和工程知识也整理在[在线学习地图](https://sxh313.github.io/engineering-map/)中，用于查询、复习和项目实践。

## 👋 关于我

- 当前主线是 **AI Agent 工程与 AI 全栈应用开发**，Go 后端是重要的工程基础。
- 喜欢把零散资料重新组织成有顺序、有实践、有验收标准的学习路径。
- 通过真实项目和开源协作检验理解：阅读源码、定位问题、提交改动、跟踪反馈。
- 持续整理学习过程，希望每一个知识点最后都能被解释、实现和验证。

## 📈 GitHub 活跃度

<!-- activity:start -->
最近 3 个月，数据来自 GitHub 贡献图。

<p align="center">
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E6%95%B0-9.8k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="9.8k 贡献数" />
  <img src="https://img.shields.io/badge/%E6%8F%90%E4%BA%A4%E6%95%B0-9.2k-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="9.2k 提交数" />
  <img src="https://img.shields.io/badge/%E6%B6%89%E5%8F%8A%E4%BB%93%E5%BA%93-57-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="57 涉及仓库" />
</p>
<!-- activity:end -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" />
    <img alt="GitHub 贡献图动态贪吃蛇" src="https://raw.githubusercontent.com/sxh313/sxh313/github-snake/github-snake.svg" width="100%" />
  </picture>
</p>
