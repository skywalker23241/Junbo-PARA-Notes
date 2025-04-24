# How to Integrate MCP with GitHub Copilot in VS Code

## What is MCP?

**The Model Context Protocol (MCP)** is an **open standard developed by Anthropic** to simplify and standardize how large language models (LLMs) integrate with external tools, databases, and APIs. Think of MCP as the *“USB-C port”* for AI models: just as USB-C unified device connectivity, MCP aims to create a universal interface for AI-to-tool interaction.

Originally built to enhance **Claude’s** ability to interact with external systems, MCP was **open-sourced in early 2024** to promote industry-wide adoption. By making the protocol public, Anthropic’s goal was to establish a shared infrastructure for tool communication that minimizes the need for custom integrations while boosting **modularity**, **interoperability**, and **developer productivity** in AI applications.

Through MCP, language models can:

- Dynamically invoke APIs and fetch real-time data
- Interact with databases and third-party tools using a consistent format
- Avoid hardcoded logic, making model behavior more flexible and maintainable

In short, **MCP is reshaping how AI models plug into the real world**, shifting from isolated, monolithic systems to flexible, tool-aware agents that can reason, retrieve, and act using standardized methods.

## Prerequisites

Before you begin, ensure you have the following:

- **Visual Studio Code (VS Code)**: Updated to the latest version.
- **GitHub Account**: With access to GitHub Copilot (Free, Pro, Business, or Enterprise plan).
- **GitHub Copilot Extensions**: Both GitHub Copilot and GitHub Copilot Chat extensions installed and enabled in VS Code.
- **Node.js**: Latest LTS version installed (check with `node -v` in your terminal). Download from the [official Node.js website](https://nodejs.org/) if needed.
- **Python**: Installed for PIP packages (optional, depending on the MCP server). Download from the [official Python website](https://www.python.org/) if needed.
- **Git**: Installed for version control and repository management.

## Step 1: Setting Up the Environment

1. **Update VS Code**:

   - Open VS Code and check for updates via the Help > Check for Updates menu.
   - Ensure you’re running the latest stable or Insiders version to support MCP integration.
2. **Sign in to GitHub**:

   - In VS Code, go to the Accounts menu in the Activity Bar.
   - Select “Sign in with GitHub to use GitHub Copilot” and follow the prompts to authenticate using your GitHub account. If you don’t have a Copilot subscription, you’ll be signed up for the Copilot Free plan with limited completions and chat interactions.
3. **Install Node.js and Python**:

   - Verify Node.js installation by running `node -v` in your terminal. Install the latest LTS version if not present.
   - Verify Python installation by running `python --version` or `python3 --version`. Install Python if needed for PIP-based MCP servers.
   - MCP supports multiple languages and packages (e.g., TypeScript, Docker, C#), but this guide focuses on Node.js for NPX packages and Python for PIP packages.
4. **Install GitHub Copilot Extensions**:

   - In VS Code, go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).
   - Search for “GitHub Copilot” and install both the **GitHub Copilot** and **GitHub Copilot Chat** extensions.
   - Restart VS Code after installation.

## Step 2: Configuring MCP in VS Code

MCP servers enhance GitHub Copilot’s Agent Mode by providing tools for tasks like repository management, file operations, or API calls. Here’s how to configure an MCP server in VS Code:

1. **Choose an MCP Server**:

   - Visit the [MCP documentation](https://docs.anthropic.com/) or [GitHub’s MCP server repository](https://github.com/modelcontextprotocol/servers) for a list of supported servers (e.g., GitHub MCP server, Microsoft Playwright MCP server).
   - For this guide, we’ll use the **GitHub MCP Server** for repository-related actions like creating issues or comparing files.
2. **Install the MCP Server**:

   - Open a terminal in VS Code (`Ctrl+`` or `Cmd+`` on macOS).
   - For the GitHub MCP server, follow the setup instructions from the official repository (e.g., `npm install @github/copilot-language-server` for Node.js-based servers).
   - Alternatively, use the VS Code interface:
     - Open the GitHub Copilot Chat view (`Ctrl+Alt+I` or `Cmd+Alt+I`).
     - Select **Agent Mode** from the chat mode dropdown.
     - Click the “Install MCP Server” button if prompted (e.g., for Azure MCP Server or GitHub MCP Server).
3. **Configure MCP in Workspace Settings**:

   - Create a `.vscode/mcp.json` file in your workspace folder to define MCP server settings. Example:
     ```json
     {
       "servers": [
         {
           "name": "GitHub MCP Server",
           "transport": "stdio",
           "command": ["node", "./node_modules/@github/copilot-language-server/dist/language-server.js", "--stdio", "true"]
         }
       ]
     }
     ```
   - Alternatively, add MCP server settings to your user settings (`Ctrl+,` or `Cmd+,` > Search for “MCP”):
     ```json
     {
       "mcp.servers": [
         {
           "name": "GitHub MCP Server",
           "transport": "stdio",
           "command": ["node", "./node_modules/@github/copilot-language-server/dist/language-server.js", "--stdio", "true"]
         }
       ]
     }
     ```
   - Ensure the `command` points to the correct path for your MCP server executable.
4. **Enable MCP Tools**:

   - In the Copilot Chat view, switch to **Agent Mode**.
   - Click the **Tools** button and refresh the tools list. The installed MCP server (e.g., “GitHub MCP Server”) should appear. Toggle it on if needed.

## Step 3: Writing and Testing MCP Code

MCP enables Copilot to perform actions like creating GitHub issues or comparing files. Here’s how to write and test MCP-related interactions:

1. **Writing MCP Prompts**:

   - In the Copilot Chat view, ensure **Agent Mode** is selected.
   - Use natural language prompts with context variables. Examples:
     - **Prompt**: “Create a GitHub issue for adding a new feature to my repository.”
     - **Prompt**: “Compare my `ServerConfig.json` with similar public GitHub repository configurations and suggest improvements. #file:ServerConfig.json”
   - Add context using the **Add Context** button or variables like `#file` or `#codebase`.
2. **Testing MCP Interactions**:

   - Enter the prompt in the Copilot Chat input field and press Enter.
   - Copilot will invoke the MCP server’s tools (e.g., GitHub API for creating issues) and display results in the Chat view.
   - Review the output (e.g., a new issue created in your repository or a diff of file comparisons).
   - Accept changes by selecting **Keep** or **Accept** in the Chat view, or reject them if they’re incorrect.
3. **Example Node.js Code for MCP Interaction**:

   - If developing a custom MCP server, use the MCP SDK. Below is a basic Node.js example to create a tool for listing repository files:
     ```javascript
     const { MCPServer } = require('@anthropic/mcp-sdk');

     const server = new MCPServer({
       transport: 'stdio',
       tools: [
         {
           name: 'list_repository_files',
           description: 'Lists files in a GitHub repository',
           execute: async (params) => {
             const { repo } = params;
             // Simulated GitHub API call
             return ['index.js', 'package.json', 'README.md'];
           },
         },
       ],
     });

     server.start();
     ```
   - Save this as `mcp-server.js` and run it with `node mcp-server.js`. Configure VS Code to use this server as shown in Step 2.[](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
4. **Example Python Code for MCP Interaction**:

   - For Python-based MCP servers, use the Python MCP SDK:
     ```python
     from mcp_sdk import MCPServer

     server = MCPServer(
         transport="stdio",
         tools=[
             {
                 "name": "create_github_issue",
                 "description": "Creates a GitHub issue in a repository",
                 "execute": lambda params: f"Issue created in {params['repo']} with title: {params['title']}",
             }
         ],
     )

     server.start()
     ```
   - Save as `mcp_server.py` and run with `python mcp_server.py`. Update the `.vscode/mcp.json` file to point to this script.

## Step 4: Advanced Features and Customization

1. **Custom Instructions**:

   - Create a `.github/copilot-instructions.md` file to provide project-specific context (e.g., coding standards, preferred libraries). Example:
     ```markdown
     # Copilot Instructions
     This project is a web application built with Node.js and Express.
     - Use camelCase for variable names.
     - Prefer async/await over callbacks.
     - Use the GitHub MCP server for repository actions.
     ```
   - Copilot automatically applies these instructions in Agent Mode.
2. **Dynamic Tool Updates**:

   - MCP servers can dynamically update tools using list-changed events. Modify your MCP server code to emit updates when new tools are added.
3. **Remote MCP Servers**:

   - Host MCP servers on platforms like Azure Container Apps for remote access. Configure VS Code to connect via server-sent events (SSE) instead of stdio.
4. **Prompt Engineering**:

   - Use specific prompts for better results. Example: “Generate a Node.js function to fetch data from an API using the GitHub MCP server. #file:api.js”

## Step 5: Troubleshooting and Best Practices

1. **Troubleshooting**:

   - **MCP Server Not Detected**: Check the `.vscode/mcp.json` file for correct command paths. Run `MCP: List Servers` from the Command Palette to verify.
   - **No Suggestions**: Ensure Agent Mode is active and the MCP server is toggled on in the Tools menu.
   - **Errors in Chat View**: Select the error notification and choose “Show Output” to view server logs.
   - **Authentication Issues**: Re-authenticate your GitHub account via the Accounts menu if Copilot fails to connect.
2. **Best Practices**:

   - **Use Trusted MCP Servers**: Only install servers from verified sources to avoid security risks.
   - **Keep Prompts Specific**: Break tasks into smaller, clear prompts (e.g., “Generate a function” instead of “Build an app”).
   - **Version Control Instructions**: Store `.github/copilot-instructions.md` in your repository to share with your team.
   - **Test Changes**: Always review and test Copilot’s suggestions before accepting, as MCP actions may modify files or repositories.

## Conclusion

Integrating the Model Context Protocol (MCP) with GitHub Copilot in VS Code unlocks powerful AI-driven capabilities, enabling seamless interaction with GitHub repositories, APIs, and external tools. By following this guide, you’ve learned how to set up your environment, configure MCP servers, write and test MCP interactions, and leverage advanced features like custom instructions. With MCP’s standardized interface, you can extend Copilot’s Agent Mode to suit your project’s needs, boosting productivity and modularity.

For further exploration, check these resources:

- [MCP Documentation](https://docs.anthropic.com/)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code MCP Guide](https://code.visualstudio.com/docs/copilot/mcp-servers)
- GitHub’s [Awesome-MCP-ZH](https://github.com/awesome-mcp-zh) for Chinese-language MCP resources

Experiment with different MCP servers and prompts to tailor Copilot to your workflow, and share your feedback with the community to help shape the future of AI-driven development!
