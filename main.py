import os

LINE = "Hey \u2014 press B4 and let my coils drop something sweet for you. I've been humming here all day, and you're the exact change I needed."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
