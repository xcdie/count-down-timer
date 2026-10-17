import time
import tkinter as tk
from tkinter import messagebox
import threading

def start_countdown():
    try:
        total_seconds = int(hour_var.get()) * 3600 + int(minute_var.get()) * 60 + int(second_var.get())
        if total_seconds <= 0:
            messagebox.showerror("Error", "Please enter a time greater than 0.")
            return
        
        def run_timer():
            nonlocal total_seconds
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                hours, mins = divmod(mins, 60)
                timer_var.set(f"{hours:02d}:{mins:02d}:{secs:02d}")
                time.sleep(1)
                total_seconds -= 1
            
            timer_var.set("00:00:00")
            root.bell()
            messagebox.showinfo("Time's Up!", "⏰ Countdown finished!")

        threading.Thread(target=run_timer, daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for time.")

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x240")
root.config(bg="#f4f4f9")

tk.Label(root, text=" Countdown Timer", font=("Arial", 14, "bold"), bg="#f4f4f9").pack(pady=10)

input_frame = tk.Frame(root, bg="#f4f4f9")
input_frame.pack(pady=5)

hour_var = tk.StringVar(value="00")
minute_var = tk.StringVar(value="05")
second_var = tk.StringVar(value="00")

tk.Entry(input_frame, textvariable=hour_var, width=3, font=("Arial", 14), justify="center").pack(side=tk.LEFT, padx=3)
tk.Label(input_frame, text=":", font=("Arial", 14), bg="#f4f4f9").pack(side=tk.LEFT)
tk.Entry(input_frame, textvariable=minute_var, width=3, font=("Arial", 14), justify="center").pack(side=tk.LEFT, padx=3)
tk.Label(input_frame, text=":", font=("Arial", 14), bg="#f4f4f9").pack(side=tk.LEFT)
tk.Entry(input_frame, textvariable=second_var, width=3, font=("Arial", 14), justify="center").pack(side=tk.LEFT, padx=3)

start_btn = tk.Button(root, text="Start Timer", command=start_countdown, bg="#28a745", fg="white", font=("Arial", 11, "bold"), width=15)
start_btn.pack(pady=10)

timer_var = tk.StringVar(value="00:05:00")
timer_label = tk.Label(root, textvariable=timer_var, font=("Arial", 28, "bold"), bg="#f4f4f9", fg="#333")
timer_label.pack(pady=5)

root.mainloop()