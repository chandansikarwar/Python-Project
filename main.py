import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.running = False
        self.time = 0

        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=20)

        self.start_btn = tk.Button(root, text="Start", command=self.start)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop)
        self.stop_btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.running:
            self.time += 1
            mins, secs = divmod(self.time, 60)
            hrs, mins = divmod(mins, 60)
            self.label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")


root = tk.Tk()
app = Stopwatch(root)
root.mainloop()


