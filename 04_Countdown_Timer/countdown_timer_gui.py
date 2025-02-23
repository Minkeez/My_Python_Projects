import sys
import time
import threading
import winsound # Windows only (for sound alerts)
from plyer import notification # Cross-platform notifications
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit
from PyQt6.QtCore import QTimer

class CountdownTimer(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    self.timer = QTimer()
    self.timer.timeout.connect(self.update_timer)
    self.remaining_time = 0
    self.is_paused = False

  def initUI(self):
    self.setWindowTitle("Countdown Timer")
    self.setGeometry(200, 200, 400, 300)

    self.label = QLabel("Enter time in seconds:", self)
    self.input_time = QLineEdit(self)

    self.start_button = QPushButton("Start", self)
    self.pause_button = QPushButton("Pause", self)
    self.reset_button = QPushButton("Reset", self)
    self.pause_button.setEnabled(False)
    self.reset_button.setEnabled(False)

    self.timer_display = QLabel("00:00", self)
    self.history_log = QTextEdit(self)
    self.history_log.setReadOnly(True)

    layout = QVBoxLayout()
    layout.addWidget(self.label)
    layout.addWidget(self.input_time)
    layout.addWidget(self.start_button)
    layout.addWidget(self.pause_button)
    layout.addWidget(self.reset_button)
    layout.addWidget(self.timer_display)
    layout.addWidget(self.history_log)

    self.setLayout(layout)

    self.start_button.clicked.connect(self.start_timer)
    self.pause_button.clicked.connect(self.pause_resume_timer)
    self.reset_button.clicked.connect(self.reset_timer)
  
  def start_timer(self):
    try:
      self.remaining_time = int(self.input_time.text())
      if self.remaining_time <= 0:
        self.history_log.append("Invalid time. Please enter a positive number.")
        return
      
      self.timer.start(1000)
      self.start_button.setEnabled(False)
      self.pause_button.setEnabled(True)
      self.reset_button.setEnabled(True)
      self.update_timer_display()
    except ValueError:
      self.history_log.append("Invalid input! Please enter a valid number.")

  def pause_resume_timer(self):
    if self.is_paused:
      self.timer.start(1000)
      self.pause_button.setText("Pause")
    else:
      self.timer.stop()
      self.pause_button.setText("Resume")
    self.is_paused = not self.is_paused

  def reset_timer(self):
    self.timer.stop()
    self.remaining_time = 0
    self.timer_display.setText("00:00")
    self.start_button.setEnabled(True)
    self.pause_button.setEnabled(False)
    self.reset_button.setEnabled(False)
  
  def update_timer(self):
    if self.remaining_time > 0:
      self.remaining_time -= 1
      self.update_timer_display()
    else:
      self.timer.stop()
      self.timer_display.setText("Time's up!")
      self.history_log.append("Countdown finished!")
      self.send_notification()
      self.play_alarm()
      self.start_button.setEnabled(True)
      self.pause_button.setEnabled(False)
      self.reset_button.setEnabled(False)
  
  def update_timer_display(self):
    mins, secs = divmod(self.remaining_time, 60)
    self.timer_display.setText(f"{mins:02}:{secs:02}")

  def send_notification(self):
    notification.notify(
      title="Countdown Timer",
      message="Time is up!",
      timeout=5
    )

  def play_alarm(self):
    try:
      for _ in range(3): # Beep 3 times
        winsound.Beep(1000, 500) # 1000 Hz frequency, 500ms duration
        time.sleep(0.5)
    except:
      pass # Ignore errors (for non-Windows systems)
  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = CountdownTimer()
  window.show()
  sys.exit(app.exec())