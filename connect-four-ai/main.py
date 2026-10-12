import tkinter as tk

from ui.connect_four_ui import ConnectFourUI


def main():
    root = tk.Tk()

    ConnectFourUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()