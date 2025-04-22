# 什么是MCP?

MCP(Model Context Protocol) 是一个通过专用服务器处理工具和资源调用的简单协议。

**Model Context Protocol（MCP）是由 Anthropic 推出的开放标准，旨在简化大型语言模型（LLM）与外部工具和数据源的集成方式。可以将 MCP 想象成 AI 应用的“USB-C 接口”：就像 USB-C 统一了设备之间的连接方式，MCP 也为 AI 模型提供了标准化的方式来访问各种数据和工具。**

The Model Context Protocol (MCP) is an open standard that enables large language models to interact dynamically with external tools, databases, and APIs through a standardized interface.模型上下文协议 (MCP) 是一种开放标准，它使大型语言模型能够通过标准化接口与外部工具、数据库和 API 动态交互。

The Model Context Protocol (MCP) is an open standard developed by Anthropic to enable easy and standardized integration between AI models and external tools. It acts as a universal connector, allowing large language models (LLMs) to interact dynamically with APIs, databases, and business applications.

模型上下文协议 (MCP) 是由 Anthropic 开发的一项开放标准，旨在实现 AI 模型与外部工具之间轻松且标准化的集成。它充当通用连接器，允许大型语言模型 (MCP) 与 API、数据库和业务应用动态交互。

Originally built to improve Claude’s ability to interact with external systems, Anthropic decided to [open-source MCP in early 2024](https://www.anthropic.com/news/model-context-protocol) to encourage industry-wide adoption. By making MCP publicly available,they aimed to create a standardized framework for AI-to-tool
communication, reducing reliance on proprietary integrations andenabling greater modularity and interoperability across AI applications.

Anthropic最初是为了提升 Claude 与外部系统交互的能力而构建的，后来决定在 2024 年初将 MCP 开源， 以推动整个行业的采用。通过公开 MCP，他们的目标是创建一个标准化的 AI 与工具通信框架，减少对专有集成的依赖，并提高 AI 应用之间的模块化和互操作性。

> *这里就可以把它理解为一个模块,用来给ai提供具体的上下文.*
