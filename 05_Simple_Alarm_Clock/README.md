# ⏰ Console-Based Alarm Clock in Python

A simple yet powerful terminal-based alarm clock built with Python. This project supports multiple alarms, background time-checking using threads, and interactive user input for managing alarms in real-time.

---

### 🚀 Features

- ✅ Set alarms in **HH:MM** (24-hour) format
- ✅ Trigger alert with **sound notification and message**
- ✅ Support for **multiple alarms**
- ✅ **Threaded time-checking** – alarm system runs in background
- ✅ **Edit / Cancel** alarms before they trigger
- ✅ Cross-platform support (Windows, Linux, macOS)

---

### 🛠 Requirements

- Python 3.6+
- No external libraries required

*Optional:*  
- `winsound` for sound on Windows  
- Bell sound (`\a`) support on Unix/Linux terminals

---

### 📋 How to Use
After launching the program, you'll see a simple menu:

```mathematica
===== Alarm Clock Menu =====
1. Set Alarm
2. Remove Alarm
3. View Alarms
4. Exit
```

#### 🕐 Set Alarm
- Choose option 1
- Enter time in HH:MM 24-hour format (e.g. 06:30 or 18:45)
- Alarm will trigger at the exact minute and alert with a message and sound

#### ❌ Remove Alarm
- Choose option 2
- Select the alarm number from the list to remove

#### 👀 View Alarms
- Choose option 3 to see all active alarms

#### 🛑 Exit
- Choose option 4 to stop the alarm clock and safely exit the program

---

### 🔔 Alarm Notification
- When an alarm is triggered, a message will print in the terminal
- A beep sound will play if supported by your system

---

### 📌 Notes
- The program automatically removes alarms after they trigger.
- The alarm-checking loop runs in a background thread, so you can continue interacting with the menu in real-time.

---

### 🧠 Future Improvements
- ⏰ Snooze option
- 🔁 Recurring daily alarms
- 🏷️ Alarm labels (e.g. “Meeting at 9AM”)
- 📅 Calendar-based alarm setting
- 💾 Persistent storage (save alarms between runs)