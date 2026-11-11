<!--
  这是 https://github.com/sxh313 展示的个人主页。
  merged-prs 与 activity 标记之间的内容由 .github/workflows/refresh.yml 自动更新；
  如需调整这些区域的文字，请同步修改 .github/scripts/render_merged_prs.py。
-->

<div align="center">

# sxh313

### AI Agent 工程 · 产品实践 · 开源协作

<p>
  通过个人项目与真实开源协作，持续实践<br/>
  Agent Runtime、Tool Calling、Memory / RAG 与 Evaluation。
</p>

<p>
  <a href="#-开源贡献"><b>开源贡献</b></a>
  ·
  <a href="https://sxh313.github.io/engineering-map/ai/"><b>学习地图</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/AI_Agent-Engineering-8250DF?style=flat-square" alt="AI Agent Engineering" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Open_Source-1F883D?style=flat-square&logo=github&logoColor=white" alt="Open Source" />
</p>

</div>

## 🌍 开源贡献

通过真实开源项目检验 Agent 工程理解，关注源码阅读、问题定位、最小改动、测试验证和上游协作。下面只展示已经合并 PR 的项目级统计，不将合并数量描述为项目主导经验。

<!-- merged-prs:start -->
<p align="center">
  <img src="https://img.shields.io/badge/%E5%B7%B2%E5%90%88%E5%B9%B6%20PR-70-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="70 已合并 pr" />
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E9%A1%B9%E7%9B%AE-18-8250DF?style=for-the-badge&logo=box&logoColor=white" alt="18 贡献项目" />
  <img src="https://img.shields.io/badge/%E4%B8%8A%E6%B8%B8%E9%A1%B9%E7%9B%AE%20Stars-959.0k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="959.0k 上游项目 stars" />
</p>

| 贡献项目 | ★ | 主要语言 | 已合并 |
| :-- | --: | :-- | --: |
| <img src="https://github.com/openclaw.png?size=48" width="24" height="24" alt="" />&nbsp;[`openclaw/openclaw`](https://github.com/openclaw/openclaw)<br><sub>可以在任意操作系统和平台上执行真实任务的开源 AI 助手。</sub> | 394.4k | ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) | 11 |
| <img src="https://github.com/bytedance.png?size=48" width="24" height="24" alt="" />&nbsp;[`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)<br><sub>面向深度研究、代码生成与内容创作的长程智能体框架。</sub> | 85.3k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 12 |
| <img src="https://github.com/agentscope-ai.png?size=48" width="24" height="24" alt="" />&nbsp;[`agentscope-ai/agentscope`](https://github.com/agentscope-ai/agentscope)<br><sub>用于构建、运行与观测可信智能体的开发框架。</sub> | 35.8k | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | 9 |

<sub>仅统计 Stars 不低于 1,000 的项目及其中已合并的 PR。表格仅展示 openclaw/openclaw、bytedance/deer-flow 和 agentscope-ai/agentscope。数据由 [.github/workflows/refresh.yml](.github/workflows/refresh.yml) 自动更新；最后更新于 2026-11-11 23:37 UTC。</sub>
<!-- merged-prs:end -->

## 🧠 工程关注

- **Harness / Runtime**：任务生命周期、状态持久化、调度、中断与恢复。
- **Tool / MCP / Skill**：能力描述、协议连接、权限边界与调用可靠性。
- **Context / Memory / RAG**：上下文选择、长期记忆、检索与知识更新。
- **Evaluation**：Trace、失败分类、回归测试，以及成本与延迟权衡。
- **Multi-Agent**：任务拆分、共享状态、交接协议与结果验收。

TypeScript、Python、Go、数据库与部署能力，作为这些 Agent 系统落地的工程支撑。

## 📚 学习与整理

<details>
<summary><b>展开查看 AI Agent 学习资料</b></summary>

<br/>

- [AI Agent 学习首页](https://sxh313.github.io/engineering-map/ai/)：主题索引与阅读入口。
- [AI Agent 融合手册](https://sxh313.github.io/engineering-map/ai/handbook)：按统一工程主线组织原理与实践。
- [AI Agent 实践路线](https://sxh313.github.io/engineering-map/ai/roadmap)：从最小闭环走向可运行、可评估、可恢复的系统。
- [Agent 面试复习](https://sxh313.github.io/engineering-map/ai/library/zero2agent/learn-agent-interview/)：项目拆解、失败分析与面试表达。

资料整理参考 [AI Agent Book](https://sxh313.github.io/engineering-map/ai/library/ai-agent-book/) 与 [zero2Agent](https://sxh313.github.io/engineering-map/ai/library/zero2agent/)。AI Agent Book 使用 Apache License 2.0；zero2Agent 主体使用 MIT License，面试部分使用 CC BY-NC-SA 4.0。本站保留来源与许可边界，不将整理内容表述为个人原创教材。

</details>

## 👋 关于我

- 目前专注于 **AI Agent 工程与产品实践**。
- 通过源码阅读、个人项目和评估复盘理解 Agent 系统的真实边界。
- 通过开源协作练习问题定位、最小改动、测试验证和上游沟通。

<details>
<summary><b>📈 查看 GitHub 活跃度</b></summary>

<br/>

<!-- activity:start -->
最近 3 个月，数据来自 GitHub 贡献图。

<p align="center">
  <img src="https://img.shields.io/badge/%E8%B4%A1%E7%8C%AE%E6%95%B0-9.5k-8250DF?style=for-the-badge&logo=github&logoColor=white" alt="9.5k 贡献数" />
  <img src="https://img.shields.io/badge/%E6%8F%90%E4%BA%A4%E6%95%B0-8.9k-8250DF?style=for-the-badge&logo=git&logoColor=white" alt="8.9k 提交数" />
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
