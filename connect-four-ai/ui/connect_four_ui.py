import tkinter as tk
from tkinter import messagebox

from game.environment import ConnectFourEnv
from agents.random_agent import random_agent
from agents.think1_agent import think1_agent
from agents.think2_agent import think2_agent
from agents.think3_agent import think3_agent


ROWS = 6
COLS = 7

CELL_SIZE = 82
PIECE_PADDING = 9


class ConnectFourUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Connect Four AI")
        self.root.geometry("1450x900")
        self.root.minsize(1200, 780)

        # ----------------------------
        # Theme
        # ----------------------------

        self.bg = "#081426"
        self.panel = "#0f1e33"
        self.panel_hover = "#172a45"

        self.text = "#f5f7fb"
        self.muted = "#91a0b8"

        self.blue = "#0878f9"
        self.board_blue = "#0767d7"

        self.red = "#ef2638"
        self.yellow = "#ffc01e"

        self.empty = "#07162a"

        self.root.configure(bg=self.bg)

        # ----------------------------
        # Game state
        # ----------------------------

        self.env = ConnectFourEnv()

        self.game_mode = tk.StringVar(
            value="Human vs AI"
        )

        self.ai_level = tk.StringVar(
            value="Think 3"
        )

        self.move_history = []

        self.game_over = False
        self.ai_running = False

        # ----------------------------
        # Build UI
        # ----------------------------

        self.build_header()
        self.build_main_layout()

        self.new_game()

    # ==================================================
    # HEADER
    # ==================================================

    def build_header(self):

        header = tk.Frame(
            self.root,
            bg="#09182b",
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        logo = tk.Label(
            header,
            text="🔴 CONNECT FOUR 🟡",
            font=("Segoe UI", 25, "bold"),
            fg=self.text,
            bg="#09182b"
        )

        logo.pack(
            side="left",
            padx=35
        )

        nav = tk.Frame(
            header,
            bg="#09182b"
        )

        nav.pack(
            side="right",
            padx=30
        )

        self.create_nav_button(
            nav,
            "🎮  Play",
            True
        )

        self.create_nav_button(
            nav,
            "⚙  Settings"
        )

        self.create_nav_button(
            nav,
            "📊  Statistics"
        )

        self.create_nav_button(
            nav,
            "ⓘ  About"
        )

    def create_nav_button(
        self,
        parent,
        text,
        active=False
    ):

        bg = self.blue if active else "#09182b"

        button = tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 12),
            fg=self.text,
            bg=bg,
            padx=18,
            pady=10,
            cursor="hand2"
        )

        button.pack(
            side="left",
            padx=5
        )

    # ==================================================
    # MAIN LAYOUT
    # ==================================================

    def build_main_layout(self):

        container = tk.Frame(
            self.root,
            bg=self.bg
        )

        container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # Left sidebar

        self.left_panel = tk.Frame(
            container,
            bg=self.bg,
            width=280
        )

        self.left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 20)
        )

        self.left_panel.pack_propagate(False)

        # Center

        self.center_panel = tk.Frame(
            container,
            bg=self.bg
        )

        self.center_panel.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Right sidebar

        self.right_panel = tk.Frame(
            container,
            bg=self.bg,
            width=300
        )

        self.right_panel.pack(
            side="right",
            fill="y",
            padx=(20, 0)
        )

        self.right_panel.pack_propagate(False)

        self.build_left_panel()
        self.build_center_panel()
        self.build_right_panel()

    # ==================================================
    # LEFT
    # ==================================================

    def build_left_panel(self):

        self.create_section_title(
            self.left_panel,
            "Game Mode"
        )

        modes = [
            "Human vs AI",
            "Human vs Human",
            "AI vs AI"
        ]

        for mode in modes:

            rb = tk.Radiobutton(
                self.left_panel,
                text=mode,
                variable=self.game_mode,
                value=mode,
                command=self.new_game,
                indicatoron=False,
                bg=self.panel,
                fg=self.text,
                selectcolor=self.blue,
                activebackground=self.panel_hover,
                activeforeground=self.text,
                font=("Segoe UI", 11),
                anchor="w",
                padx=15,
                pady=12
            )

            rb.pack(
                fill="x",
                pady=3
            )

        self.create_section_title(
            self.left_panel,
            "AI Difficulty",
            top=25
        )

        levels = [
            ("Random", "Random moves"),
            ("Think 1", "Win if possible"),
            ("Think 2", "Block opponent"),
            ("Think 3", "Look ahead 3 moves")
        ]

        for name, description in levels:

            text = f"🤖  {name}\n      {description}"

            rb = tk.Radiobutton(
                self.left_panel,
                text=text,
                variable=self.ai_level,
                value=name,
                command=self.new_game,
                indicatoron=False,
                justify="left",
                anchor="w",
                bg=self.panel,
                fg=self.text,
                selectcolor=self.blue,
                activebackground=self.panel_hover,
                activeforeground=self.text,
                font=("Segoe UI", 10),
                padx=12,
                pady=8
            )

            rb.pack(
                fill="x",
                pady=2
            )

    def create_section_title(
        self,
        parent,
        text,
        top=0
    ):

        label = tk.Label(
            parent,
            text=text,
            bg=self.bg,
            fg=self.text,
            font=("Segoe UI", 15, "bold"),
            anchor="w"
        )

        label.pack(
            fill="x",
            pady=(top, 10)
        )

    # ==================================================
    # CENTER
    # ==================================================

    def build_center_panel(self):

        self.status_frame = tk.Frame(
            self.center_panel,
            bg=self.panel,
            height=80
        )

        self.status_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        self.status_frame.pack_propagate(False)

        self.player_label = tk.Label(
            self.status_frame,
            text="🔴 You (Red)",
            font=("Segoe UI", 16, "bold"),
            fg=self.text,
            bg=self.panel
        )

        self.player_label.pack(
            side="left",
            padx=25
        )

        vs = tk.Label(
            self.status_frame,
            text="VS",
            font=("Segoe UI", 14, "bold"),
            fg=self.muted,
            bg=self.panel
        )

        vs.pack(
            side="left",
            expand=True
        )

        self.opponent_label = tk.Label(
            self.status_frame,
            text="Think 3 AI 🟡",
            font=("Segoe UI", 16, "bold"),
            fg=self.text,
            bg=self.panel
        )

        self.opponent_label.pack(
            side="right",
            padx=25
        )

        # Board

        board_width = COLS * CELL_SIZE
        board_height = ROWS * CELL_SIZE

        self.canvas = tk.Canvas(
            self.center_panel,
            width=board_width,
            height=board_height,
            bg=self.board_blue,
            highlightthickness=0,
            cursor="hand2"
        )

        self.canvas.pack(
            pady=10
        )

        self.canvas.bind(
            "<Button-1>",
            self.on_board_click
        )

        # Column numbers

        numbers = tk.Frame(
            self.center_panel,
            bg=self.bg
        )

        numbers.pack()

        for col in range(COLS):

            label = tk.Label(
                numbers,
                text=str(col + 1),
                width=7,
                bg=self.bg,
                fg=self.text,
                font=("Segoe UI", 11, "bold")
            )

            label.pack(
                side="left"
            )

        # Turn status

        self.turn_label = tk.Label(
            self.center_panel,
            text="🔴 Your turn",
            bg=self.panel,
            fg=self.text,
            font=("Segoe UI", 15, "bold"),
            pady=15
        )

        self.turn_label.pack(
            fill="x",
            pady=(20, 0)
        )

    # ==================================================
    # RIGHT
    # ==================================================

    def build_right_panel(self):

        self.create_right_title(
            "Game Information"
        )

        self.info_label = tk.Label(
            self.right_panel,
            text="",
            justify="left",
            anchor="nw",
            bg=self.panel,
            fg=self.text,
            font=("Segoe UI", 11),
            padx=18,
            pady=15
        )

        self.info_label.pack(
            fill="x"
        )

        self.create_right_title(
            "Game Controls"
        )

        new_game = tk.Button(
            self.right_panel,
            text="⟳  New Game",
            command=self.new_game,
            bg=self.blue,
            fg="white",
            activebackground="#1687ff",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            pady=12,
            cursor="hand2"
        )

        new_game.pack(
            fill="x",
            pady=5
        )

        control_row = tk.Frame(
            self.right_panel,
            bg=self.bg
        )

        control_row.pack(
            fill="x",
            pady=5
        )

        undo = tk.Button(
            control_row,
            text="↶ Undo",
            command=self.undo_move,
            bg=self.panel,
            fg=self.text,
            relief="flat",
            font=("Segoe UI", 10),
            pady=10,
            cursor="hand2"
        )

        undo.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 3)
        )

        resign = tk.Button(
            control_row,
            text="✕ Resign",
            command=self.resign,
            bg=self.panel,
            fg=self.text,
            relief="flat",
            font=("Segoe UI", 10),
            pady=10,
            cursor="hand2"
        )

        resign.pack(
            side="right",
            fill="x",
            expand=True,
            padx=(3, 0)
        )

        self.create_right_title(
            "Move History"
        )

        self.history_box = tk.Listbox(
            self.right_panel,
            bg=self.panel,
            fg=self.text,
            selectbackground=self.blue,
            borderwidth=0,
            highlightthickness=0,
            font=("Consolas", 10),
            height=15
        )

        self.history_box.pack(
            fill="both",
            expand=True
        )

    def create_right_title(
        self,
        text
    ):

        label = tk.Label(
            self.right_panel,
            text=text,
            bg=self.bg,
            fg=self.text,
            font=("Segoe UI", 14, "bold"),
            anchor="w"
        )

        label.pack(
            fill="x",
            pady=(5, 10)
        )

    # ==================================================
    # GAME LOGIC
    # ==================================================

    def get_ai(self):

        agents = {
            "Random": random_agent,
            "Think 1": think1_agent,
            "Think 2": think2_agent,
            "Think 3": think3_agent
        }

        return agents[self.ai_level.get()]

    def new_game(self):

        self.env.reset()

        self.move_history = []

        self.game_over = False
        self.ai_running = False

        if hasattr(self, "history_box"):
            self.history_box.delete(0, tk.END)

        self.update_information()
        self.draw_board()
        self.update_status()

        if self.game_mode.get() == "AI vs AI":
            self.root.after(
                700,
                self.ai_vs_ai_turn
            )

    # ==================================================
    # BOARD INPUT
    # ==================================================

    def on_board_click(self, event):

        if self.game_over:
            return

        if self.ai_running:
            return

        mode = self.game_mode.get()

        if mode == "AI vs AI":
            return

        column = event.x // CELL_SIZE

        if column not in self.env.valid_moves:
            return

        self.make_move(column)

        if self.game_over:
            return

        if mode == "Human vs AI":

            self.ai_running = True

            self.turn_label.config(
                text="🤖 AI is thinking..."
            )

            self.root.after(
                450,
                self.ai_turn
            )

    # ==================================================
    # MOVE
    # ==================================================

    def make_move(self, column):

        player = self.env.current_player

        _, reward, done, _ = self.env.step(
            column
        )

        self.move_history.append(
            (player, column)
        )

        self.update_history()
        self.draw_board()

        if done:

            self.game_over = True

            if reward == 1:

                winner = (
                    "Red"
                    if player == 1
                    else "Yellow"
                )

                self.turn_label.config(
                    text=f"🏆 {winner} wins!"
                )

                messagebox.showinfo(
                    "Game Over",
                    f"{winner} wins!"
                )

            else:

                self.turn_label.config(
                    text="Draw!"
                )

                messagebox.showinfo(
                    "Game Over",
                    "The game is a draw."
                )

            return

        self.update_status()

    # ==================================================
    # AI
    # ==================================================

    def ai_turn(self):

        if self.game_over:
            self.ai_running = False
            return

        agent = self.get_ai()

        move = agent(self.env)

        self.make_move(move)

        self.ai_running = False

    def ai_vs_ai_turn(self):

        if self.game_over:
            return

        agent = self.get_ai()

        move = agent(self.env)

        self.make_move(move)

        if not self.game_over:

            self.root.after(
                500,
                self.ai_vs_ai_turn
            )

    # ==================================================
    # DRAW BOARD
    # ==================================================

    def draw_board(self):

        self.canvas.delete("all")

        state = self.env.state

        for row in range(ROWS):

            for col in range(COLS):

                x1 = col * CELL_SIZE + PIECE_PADDING
                y1 = row * CELL_SIZE + PIECE_PADDING

                x2 = (
                    (col + 1) * CELL_SIZE
                    - PIECE_PADDING
                )

                y2 = (
                    (row + 1) * CELL_SIZE
                    - PIECE_PADDING
                )

                value = state[row][col]

                if value == 1:
                    color = self.red

                elif value == -1:
                    color = self.yellow

                else:
                    color = self.empty

                self.canvas.create_oval(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="#153f70",
                    width=3
                )

    # ==================================================
    # STATUS
    # ==================================================

    def update_status(self):

        if self.game_over:
            return

        if self.env.current_player == 1:

            self.turn_label.config(
                text="🔴 Red's turn"
            )

        else:

            self.turn_label.config(
                text="🟡 Yellow's turn"
            )

    def update_information(self):

        mode = self.game_mode.get()
        level = self.ai_level.get()

        text = (
            f"🎮 Mode       {mode}\n\n"
            f"🤖 AI         {level}\n\n"
            f"🔴 Player 1   Red (R)\n\n"
            f"🟡 Player 2   Yellow (Y)\n\n"
            f"▦ Board      6 × 7"
        )

        self.info_label.config(
            text=text
        )

        if mode == "Human vs AI":

            self.player_label.config(
                text="🔴 You (Red)"
            )

            self.opponent_label.config(
                text=f"{level} AI 🟡"
            )

        elif mode == "Human vs Human":

            self.player_label.config(
                text="🔴 Player 1"
            )

            self.opponent_label.config(
                text="Player 2 🟡"
            )

        else:

            self.player_label.config(
                text=f"🔴 {level} AI"
            )

            self.opponent_label.config(
                text=f"{level} AI 🟡"
            )

    # ==================================================
    # HISTORY
    # ==================================================

    def update_history(self):

        self.history_box.delete(
            0,
            tk.END
        )

        for index, (player, column) in enumerate(
            self.move_history,
            start=1
        ):

            player_name = (
                "Red"
                if player == 1
                else "Yellow"
            )

            self.history_box.insert(
                tk.END,
                f"{index:>2}. {player_name:<7} Column {column + 1}"
            )

        self.history_box.yview(
            tk.END
        )

    # ==================================================
    # UNDO
    # ==================================================

    def undo_move(self):

        if not self.move_history:
            return

        mode = self.game_mode.get()

        remove_count = 1

        # Human vs AI:
        # undo cả Human + AI nếu có thể
        if (
            mode == "Human vs AI"
            and len(self.move_history) >= 2
        ):
            remove_count = 2

        remaining_moves = (
            self.move_history[:-remove_count]
        )

        self.env.reset()

        self.move_history = []

        self.game_over = False

        for _, column in remaining_moves:

            player = self.env.current_player

            self.env.step(column)

            self.move_history.append(
                (player, column)
            )

        self.update_history()
        self.draw_board()
        self.update_status()

    # ==================================================
    # RESIGN
    # ==================================================

    def resign(self):

        if self.game_over:
            return

        answer = messagebox.askyesno(
            "Resign",
            "Are you sure you want to resign?"
        )

        if not answer:
            return

        self.game_over = True

        self.turn_label.config(
            text="Game resigned"
        )