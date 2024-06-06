import tkinter as tk
from datetime import datetime

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.elapsed_time = 0
        self.is_running = False

        self.time_label = tk.Label(master, text="00:00:00", font=("Times New Roman", 30))
        self.time_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_stop)
        self.start_button.grid(row=1, column=0, padx=5)
        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.grid(row=1, column=1, padx=5)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.grid(row=1, column=2, padx=5)
        

    def start_stop(self):
        if not self.is_running:
            self.start_time = datetime.now()
            self.is_running = True
            self.update_time()
            self.start_button.config(text="Stop")
        else:
            self.is_running = False
            self.start_button.config(text="Start")

    def pause(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(text="Start")

    def update_time(self):
        if self.is_running:
            self.elapsed_time = datetime.now() - self.start_time
            self.time_label.config(text=str(self.elapsed_time).split('.')[0])
            self.master.after(100, self.update_time)

    def reset(self):
        self.is_running = False
        self.start_button.config(text="Start")
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

