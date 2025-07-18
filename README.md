# Experimental Steam Idler

**Experimental Steam Idler** is a desktop application written in Python that simulates activity in Steam games to accumulate playtime. It is designed to run in the background with minimal resource usage.

---

## Features

- Graphical interface using `tkinter` and `ttk` (dark mode).
- Automatic game launching via Steam AppID.
- Game window minimization and off-screen repositioning.
- Low priority setting to reduce CPU usage.
- Optional timer to automatically close the game.
- Support for the following games:
    - Left 4 Dead 2
    - Portal 2
    - Half-Life 2
    - Team Fortress 2

---

## Requirements

- Python 3.12 or higher.
- Windows operating system.
- Steam installed and configured.

---

## Installation

1. Clone this repository or download the necessary files:

```bash
git clone https://github.com/fakefountain548/Experimental-Steam-Idler.git
cd experimental-steam-idler
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```
Contents of `requirements.txt`:

```txt
psutil
pywin32
```

3. Run the main script:

```bash
python bot.py
```

---

## Usage

1. Select the game from the dropdown menu.

2. (Optional) Set the idle duration in minutes. If set to 0, the game will remain open until manually closed.

3. Toggle low-priority mode on or off.

4. Press the start button. The application will:
    - Launch the game using the `steam://run/{AppID}` protocol
    - Minimize and move the game window off-screen
    - Lower the game's process priority

5. The game will automatically close when the timer ends or when the stop button is pressed.

---

## Notes
    - This project only supports Windows, as it uses libraries like pywin32.
    - Steam may or may not register playtime depending on its policies and updates.
    - Use this tool at your own risk.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


