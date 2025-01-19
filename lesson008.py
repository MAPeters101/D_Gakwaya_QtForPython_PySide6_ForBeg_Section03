from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens
def button_clicked():
  print("You clicked the button, didn't you!")

app = QApplication()
button = QPushButton("Press Me")

# Clicked is a signal of QPushButton. It's emitted when you click
# on the button
# You can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)

button.show()
app.exec()