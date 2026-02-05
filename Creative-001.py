from datetime import datetime

with open("myfile.txt", "a") as f:
    while True:
        text = input("Write something (type 'stop' to end): ")

        if text.lower() == "stop":
            break

        # Current date and time
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Write to file
        f.write(f"[{time_stamp}] {text}\n")

print("All text saved with date & time!")
