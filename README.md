# AI Virtual Assistant

This project is an intelligent virtual assistant designed to streamline daily tasks through natural language interaction. It leverages advanced AI capabilities to understand user intent, respond conversationally, and execute a wide range of actions, from managing music playback to controlling the computer and accessing information online.

## Project Description

The AI Virtual Assistant aims to provide a seamless and intuitive user experience by acting as a proactive and helpful digital companion. It addresses the need for efficient task management and information retrieval in a hands-free or minimally interactive manner. The assistant can:

*   **Understand and Respond:** Engages in natural language conversations, understanding user intent, emotions, and context, even when not explicitly stated.
*   **Automate Tasks:** Executes a variety of actions autonomously, such as playing music, setting timers, managing computer tasks, and interacting with applications.
*   **Access Real-time Information:** Retrieves up-to-date information from the internet for weather, news, current times, and other real-world data.
*   **Provide Assistance:** Offers guidance and support based on user context or even by analyzing screenshots for troubleshooting or task execution.
*   **Personalize Experience:** Adapts to user moods and preferences, offering comforting music, suggesting breaks, or initiating shutdown sequences when appropriate.

## Installation

To get started with the AI Virtual Assistant, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ashu-choudhury/ai-assistant.git
    ```

2.  **Navigate to the Project Directory:**
    ```bash
    cd ai-assistant
    ```

### 3. Set up the Python environment

This project uses **[UV](https://github.com/astral-sh/uv)** for Python version and dependency management.  
You don’t need to manually create a virtual environment or install dependencies.

### 4. Running the Assistant

Once the repository is cloned, simply run:

```bash
uv run jarvis.py
```

6.  **Configure Environment Variables:**
    The project requires a Google API key for accessing generative AI models.
    *   Create a `.env` file in the root of the project directory.
    *   Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=your_real_api_key_here
        ```
    *   Ensure the `.env` file is added to your `.gitignore` to avoid committing sensitive information.

## Usage

The AI Virtual Assistant can be launched and interacted with in several ways:

### Launching the Assistant

The assistant can be started directly from the command line:

```bash
python jarvis.py
```

### Interacting with the Assistant

*   **Voice Commands:** The assistant is always listening for its wake word. Once activated, you can issue commands or ask questions naturally.
*   **Keyboard Shortcuts:**
    *   `Ctrl+Alt+I`: Opens the graphical user interface (GUI) for chat interactions.
    *   `Ctrl+Alt+V`: Triggers a voice interaction, allowing you to speak your command.
    *   `Ctrl+Alt+Q`: Quits the application. A confirmation dialog will appear.
    *   `Ctrl+Alt+X`: Captures a screenshot and sends it to the AI for analysis.
    *   `Ctrl+Shift`: Interrupts the current AI processing or speech output.

### GUI Interaction

The graphical user interface (GUI) provides an alternative way to interact with the assistant:

1.  **Launch the GUI:** Press `Ctrl+Alt+I` or run the script in a way that brings up the GUI.
2.  **Send Messages:** Type your message into the input box and press Enter or click the "Send" button.
3.  **View Chat History:** All interactions will be displayed in the chat history pane.
4.  **Settings:** Access settings by clicking the "Settings" button to configure:
    *   **AI Name:** Customize the name used by the AI.
    *   **Mute Mic:** Toggle microphone input (useful for silent operations or testing).
    *   **Save/Cancel:** Save or discard changes made in the settings.

### Function Calling

The assistant can leverage various built-in functions to perform specific tasks. These functions are automatically invoked by the AI when a user's request maps to a function's capabilities. Examples include:

*   **Music Playback:**
    *   `playMusic(musicName="Bohemian Rhapsody", musicVolume=75)`: Plays a specific song at a given volume.
    *   `stopMusic()`: Stops the currently playing music.
    *   `pauseMusic()`: Pauses the music.
    *   `resumeMusic()`: Resumes paused music.
    *   `setMusicVolume(volume=40)`: Adjusts the music volume.
    *   `changeMusic(musicName="Hotel California")`: Changes the current track.

*   **System Commands:**
    *   `shel(command="dir")`: Executes a Windows shell command and returns its output.

*   **Information Retrieval:**
    *   `searchGoogle(q="current weather in London")`: Retrieves real-time information from Google.
    *   `searchYoutube(q="how to play guitar", limit=1)`: Searches YouTube for videos.

*   **Utilities:**
    *   `setTimer(Time=15, Name="Break Timer", Content="Time to take a break!")`: Sets a timer with a name and announcement content.
    *   `mouse(x=100, y=200, doubleClick=False, button=1)`: Controls the mouse cursor to move and click.
    *   `type(text="This is typed text", speed=0.1)`: Types text on the keyboard with adjustable speed.
    *   `change_voice(name="en-US-JennyNeural")`: Changes the TTS voice.
    *   `gettts(text="Hello, this is text to speech.")`: Converts text to speech.

## Key Features

*   **Natural Language Understanding:** Advanced AI for comprehending context, intent, and emotion.
*   **Proactive Assistance:** Can act on user moods or vague statements without explicit commands.
*   **Multi-modal Interaction:** Supports voice commands, keyboard shortcuts, and a graphical user interface.
*   **Extensive Functionality:** Integrates various tools for music, web search, system commands, and more.
*   **Screenshot Analysis:** Ability to process screenshots for context-aware assistance.
*   **Customizable TTS:** Supports changing the Text-to-Speech voice for personalized output.
*   **Intuitive Mouse and Keyboard Control:** Automates user interface interactions.
*   **Error Handling:** Gracefully handles potential issues and provides informative feedback.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

We welcome contributions to the AI Virtual Assistant project! Whether you're interested in adding new features, improving existing ones, fixing bugs, or enhancing the documentation, your input is valuable.

The vibe of this project is collaborative and welcoming. We believe in building a powerful and user-friendly assistant together. You'll enjoy contributing if you appreciate:

*   Working with cutting-edge AI and natural language processing.
*   Developing tools that genuinely simplify everyday tasks.
*   A supportive community that values your efforts.

To contribute, please fork the repository, make your changes, and submit a pull request. We encourage you to open an issue first to discuss your proposed changes.

## Developer Notes

*   The `.env.example` file should be copied to `.env` and populated with your `GOOGLE_API_KEY`.
*   The `keys.json` file stores hotkeys for various actions. You can customize these to your preference.
*   The assistant's core AI logic is managed by `gemini.py`, which utilizes the Google Generative AI API. Ensure your API key is correctly set up.
*   The `functions.py` file lists all available tools (functions) that the AI can call.
*   The `tts.py` and `stt.py` modules handle Text-to-Speech and Speech-to-Text functionalities, respectively.
*   The `gui.py` module manages the graphical user interface using `wxPython`.
*   The `jarvis.py` script is the main entry point for running the assistant.
*   The `.gitattributes` file might contain configurations for line endings or other Git-related settings, crucial for cross-platform compatibility.
*   Ensure your environment is set up with the correct Python version as specified in dependency files like `pyproject.toml` or `uv.lock`. The project specifies Python 3.12+.