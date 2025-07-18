import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import time
from modules import set_low_resource_usage, minimize_window_by_title, move_window_offscreen, config
import os

GAMES = config.GAMES

set_low_resource_usage = set_low_resource_usage.set_low_resource_usage
minimize_window_by_title = minimize_window_by_title.minimize_window_by_title
move_window_offscreen = move_window_offscreen.move_window_offscreen

process = None
close_timer = None


def idle_game(app_id, duration, low_priority, game_name):
    global process, close_timer
    try:
        process = subprocess.Popen(f'start steam://run/{app_id}', shell=True)
        time.sleep(10)

        if low_priority:
            set_low_resource_usage(game_name)

        minimize_window_by_title(game_name)
        move_window_offscreen(game_name)

        status_label.config(text=f"{game_name} starting in idle mode.")
        start_button.config(text="Stop Idle", command=stop_idle)

        if duration > 0:
            close_timer = threading.Timer(duration * 60, stop_idle)
            close_timer.start()

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error starting game.")


def stop_idle():
    global close_timer
    for exe in ["hl2.exe", "left4dead2.exe", "portal2.exe", "tf2.exe"]:
        os.system(f"taskkill /f /im {exe} >nul 2>&1")
    status_label.config(text="Idle stopped.")
    start_button.config(text="Start Idle", command=on_start)
    if close_timer:
        close_timer.cancel()


def on_start():
    selected_game = game_var.get()
    app_id = GAMES[selected_game]
    try:
        duration = int(duration_entry.get())
    except ValueError:
        duration = 0
    low_priority = priority_var.get()
    threading.Thread(
        target=idle_game,
        args=(app_id, duration, low_priority, selected_game),
        daemon=True
    ).start()

root = tk.Tk()
root.title("Steam Idler")
root.geometry("420x350")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

dark_gray = "#1e1e1e"
mid_gray = "#2e2e2e"
light_gray = "#d3d3d3"

style.configure(".", background=dark_gray, foreground=light_gray)
style.configure("Dark.TLabel", background=dark_gray, foreground=light_gray)
style.configure("Dark.TEntry",
                fieldbackground=mid_gray,
                background=mid_gray,
                foreground=light_gray)
style.configure("Dark.TCombobox",
                fieldbackground=mid_gray,
                background=mid_gray,
                foreground=light_gray,
                arrowcolor=light_gray)
style.map("Dark.TCombobox",
                fieldbackground=[('readonly', mid_gray)],
                background=[('readonly', mid_gray)],
                foreground=[('readonly', light_gray)])
style.configure("Dark.TButton",
                background=mid_gray,
                foreground=light_gray,
                font=('Segoe UI', 10, 'bold'),
                borderwidth=0)
style.map("Dark.TButton",
                background=[('active', mid_gray)],
                foreground=[('active', light_gray)])
style.configure("Dark.TLabelframe",
                background=dark_gray,
                foreground=light_gray)
style.configure("Dark.TLabelframe.Label",
                background=dark_gray,
                foreground=light_gray)

ttk.Label(root, text="Select a game to choose an idle mode:",
        font=("Segoe UI", 12, "bold"), style="Dark.TLabel").pack(pady=10)

game_var = tk.StringVar(value=list(GAMES.keys())[0])
game_selector = ttk.Combobox(
    root,
    textvariable=game_var,
    values=list(GAMES.keys()),
    state="readonly",
    style="Dark.TCombobox"
)
game_selector.pack(pady=5)

options_frame = ttk.LabelFrame(
    root,
    text="Options",
    style="Dark.TLabelframe"
)
options_frame.pack(pady=10, padx=10, fill="x")

priority_var = tk.BooleanVar(value=True)
tk.Checkbutton(
    options_frame,
    text="Use low priority",
    variable=priority_var,
    bg=dark_gray,
    fg=light_gray,
    selectcolor=dark_gray,
    activebackground=dark_gray,
    activeforeground=light_gray,
    highlightthickness=0,
    bd=0
).pack(anchor="w", padx=10, pady=2)

ttk.Label(
    options_frame,
    text="Duration (minutes, 0 = infinite):",
    style="Dark.TLabel"
).pack(anchor="w", padx=10, pady=(10, 2))

duration_entry = ttk.Entry(options_frame, style="Dark.TEntry")
duration_entry.insert(0, "60")
duration_entry.pack(padx=10, fill="x")

start_button = ttk.Button(
    root,
    text="Start Idle",
    command=on_start,
    style="Dark.TButton"
)
start_button.pack(pady=15)

status_label = ttk.Label(
    root,
    text="Waiting for action...",
    style="Dark.TLabel"
)
status_label.pack(pady=10)

root.mainloop()