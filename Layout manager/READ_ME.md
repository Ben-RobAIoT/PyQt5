# Modify the parameter to see the differences of xpos, ypos, width, height
## Sample code
~~~python
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
)

class ConfigWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Configurator")

        # Tạo các thành phần
        self.label_x = QLabel("X Position:")
        self.input_x = QLineEdit("100")

        self.label_y = QLabel("Y Position:")
        self.input_y = QLineEdit("100")

        self.label_w = QLabel("Width:")
        self.input_w = QLineEdit("400")

        self.label_h = QLabel("Height:")
        self.input_h = QLineEdit("300")

        self.button = QPushButton("Create Window")
        self.button.clicked.connect(self.create_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_x)
        layout.addWidget(self.input_x)
        layout.addWidget(self.label_y)
        layout.addWidget(self.input_y)
        layout.addWidget(self.label_w)
        layout.addWidget(self.input_w)
        layout.addWidget(self.label_h)
        layout.addWidget(self.input_h)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def create_window(self):
        try:
            xpos = int(self.input_x.text())
            ypos = int(self.input_y.text())
            width = int(self.input_w.text())
            height = int(self.input_h.text())

            self.dialog = QDialog()
            self.dialog.setGeometry(xpos, ypos, width, height)
            self.dialog.setWindowTitle("Custom Window")

            btn = QPushButton("Close", self.dialog)
            btn.move(20, 20)
            btn.clicked.connect(self.dialog.close)

            self.dialog.show()

        except ValueError:
            print("Please enter valid integers.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConfigWindow()
    window.show()
    sys.exit(app.exec_())
~~~
# How to allign the window position screen in the middle of the main screen (Auto allignment)
<table>
  <tr>
    <th>Solution 1: Using equation</th>
    <th>Solution 2: Using method()</th>
  </tr>
  <tr>
    <td>
      <pre><code>
import sys
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QDialog()

    width = 500
    height = 500

    # Lấy độ phân giải màn hình hiện tại
    screen = QDesktopWidget().screenGeometry()
    screen_width = screen.width()
    screen_height = screen.height()

    # Tính vị trí để căn giữa
    xpos = (screen_width - width) // 2
    ypos = (screen_height - height) // 2

    b1 = QPushButton("Button1", win)
    b1.move(50, 20)

    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("PyQt5 - Cách của bạn, nhưng đúng")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
      </code></pre>
    </td>
    <td>
      <pre><code>
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QDesktopWidget

def window():
    app = QApplication(sys.argv)
    win = QDialog()
    win.resize(500, 500)  # Kích thước cửa sổ

    # Nút bấm
    b1 = QPushButton("Button1", win)
    b1.move(50, 20)

    # Căn giữa cửa sổ
    qr = win.frameGeometry()  # Lấy khung hình của cửa sổ
    cp = QDesktopWidget().availableGeometry().center()  # Tâm của màn hình
    qr.moveCenter(cp)
    win.move(qr.topLeft())  # Di chuyển cửa sổ đến vị trí mới

    win.setWindowTitle("PyQt5 - Centered Window")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
      </code></pre>
    </td>
  </tr>
</table>
