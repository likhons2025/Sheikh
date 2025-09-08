# Sheikh
Sheikh - tackles bugs, small feature requests, and other software engineering tasks

The future of coding isn’t tied to a desk anymore. After exploring mobile development possibilities for years, I’ve built something that transforms smartphones into autonomous development environments where AI agents handle the heavy lifting while you focus on creativity and problem-solving, even get a tan!
Meet agent-loop [repo]: a CLI system that brings AI-assisted coding directly to your smartphone or tablet, complete with automated package installation.
This isn’t just another mobile dev tool — it’s a rethink of when and where software gets built.
🧠 Why This Matters
The breakthrough isn’t just technical — it’s practical.
Imagine brainstorming a new app idea during your morning commute and having a working prototype by the time you reach the office. Or fixing a critical production bug while waiting at the airport. Mobile AI development enables a level of agility that desktop-bound workflows simply can’t match.
🦾 The Architecture
Agent-loop also runs on desktop and is built around what I call the Agentic Execution Pattern: a structured loop where AI agents receive tasks, execute tool calls, process results, and iterate until completion (or request human input).
Press enter or click to view image in full size

🔌 The real game-changer is Model Context Protocol (MCP) integration — Anthropic’s standardized interface (but you can use it with OpenAI too) that enables seamless tool connectivity. Agent-loop leverages MCP to compose development workflows from different servers into unified autonomous processes.
Here’s how the MCP ecosystem works in practice:
Press enter or click to view image in full size

This architecture becomes particularly powerful on mobile devices because MCP’s lightweight communication protocol minimizes resource overhead while maximizing capability exposure. Agent-loop can discover available tools dynamically, adapt to different Android configurations, and compose complex workflows without requiring extensive local processing.
Mobile Development Superpowers: Agility Unleashed
The real magic happens when you realize what mobile AI development enables that traditional setups cannot.
🛠️ Rapid Prototyping Anywhere: The ability to go from idea to working prototype in minutes, regardless of location, fundamentally changes how we approach development. Waiting for a train? Perfect time to prototype that API integration you’ve been thinking about.
🚨 Critical Bug Resolution On-The-Go: Production down at 2 AM while you’re away from your desk? Pull out your phone, clone the repo, and let agent-loop analyze logs and suggest fixes. Deploy the patch directly from your device. This level of operational agility can mean the difference between minutes and hours of downtime.
⏳ Utility Development in Dead Time: Those small automation scripts and utilities that make life easier but never seem worth firing up the laptop for? Perfect mobile development tasks. Transform your commute into productive coding time by building those quick tools you always mean to create.
🧠💡 Brainstorming with Immediate Validation: The most powerful aspect might be the shortest feedback loop between idea and implementation. Sketch out an API design in your head, voice it to your phone, and watch agent-loop generate a working mock server with sample data. This immediate validation cycle accelerates creativity in ways desktop development cannot match Key Features

User-Friendly Setup: Simply choose your username and follow the on-screen prompts.
Storage Requirements: Approximately 4GB of storage space is required. Note that additional applications will consume more space.
Detailed Documentation: Please review the full README for comprehensive information about this setup.
Installation

To install, execute the following command in Termux:

curl -sL https://raw.githubusercontent.com/phoenixbyrd/Termux_XFCE/main/install_xfce_native.sh -o install.sh && bash install.sh
Support and Community

For questions, assistance, or suggestions, join our Discord community:
Discord Invite Link

Screenshots

Desktop Screenshot

Use Case

This setup is optimized for use on devices like the Samsung Galaxy Fold 3, functioning as a PC/laptop replacement when connected to a monitor, keyboard, and mouse. It is designed for daily use and serves as a personal daily driver.

Samsung Galaxy Fold 3 - Dex Setup

Starting the Desktop

To start the desktop, use the following command:

start
This command initiates a Termux-X11 session, starts the XFCE4 desktop, and opens the Termux-X11 app directly into the desktop.

To access the Debian proot environment from the terminal, use:

debian
Note: The display is pre-configured in the Debian proot environment, allowing you to launch GUI applications directly from the terminal.

Hardware Acceleration & Proot

Several aliases are provided to simplify launching applications:

Termux XFCE:

prun: Execute commands from the Debian proot environment directly in the Termux terminal without entering the proot shell.
zrun: Launch applications in Debian proot with hardware acceleration.
zrunhud: Launch applications with hardware acceleration and FPS HUD.
Debian Proot:

debian To enter the Debian proot environment, from there, you can install additional software using sudo apt.

Additional Utilities

cp2menu: Copy .desktop files from Debian proot to the Termux XFCE menu for easy access.
app-installer: Easy to use GUI app to manage installing additional apps not available in Termux or Debian repositories.
Troubleshooting

Process Completed (Signal 9) - Press Enter

Install LADB from the Play Store or download it from here.
Connect to Wi-Fi.
Enable wireless debugging in Developer Settings and note the port number and pairing code.
Enter these values in LADB.
Once connected, run the following command:
adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"
You can also run adb shell directly 
