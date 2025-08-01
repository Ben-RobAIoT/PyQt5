# QLabel
## Introduction
A QLabel object acts as a placeholder to display non-editable text or image, or a movie of animated GIF. It can also be used as a mnemonic key for other widgets. Plain text, hyperlink or rich text can be displayed on the label.

## QLabel classes
linkActivated:	If the label containing embedded hyperlink is clicked, the URL will open. setOpenExternalLinks feature must be set to true.
linkHovered:	Slot method associated with this signal will be called when the label having embedded hyperlinked is hovered by the mouse.

~~~python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

def hovered(link):  # Hover: Lơ lửng, có nghĩa là: Hiển thị trực tiếp trên Terminal giao diện lập trình luôn
    print("hovering on:", link)

def clicked(link): # Click: Nhấn, có nghĩa là: Khi nhấn vào label thì sẽ được điều hướng tới trang khác được gán đường dẫn
    print("clicked:", link)

def window(): # Giao diện cửa sổ làm việc và hiển thị
    app = QApplication(sys.argv)
    win = QWidget() 

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    # Label 1: văn bản đơn giản
    l1.setText("Hello World")
    l1.setAlignment(Qt.AlignCenter)
    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)

    # Label 2: chứa liên kết HTML
    l2.setText('<a href="https://python.org">Welcome to Python GUI Programming</a>')
    l2.setAlignment(Qt.AlignCenter)
    l2.setOpenExternalLinks(True)  # Không mở browser, dùng connect
    l2.linkHovered.connect(hovered)

    # Label 3: hình ảnh
    pixmap = QPixmap("python.png") # Lưu ý, phải tải một file ảnh với định dạng (png, jpg,...) về (Đặt chung thư mục) hoặc (Có đường dẫn rõ ràng)
    resized_pixmap = pixmap.scaled(200, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    l3.setPixmap(resized_pixmap)
    l3.setAlignment(Qt.AlignCenter)

    # Label 4: liên kết khác
    l4.setText('<a href="https://tutorialspoint.com">TutorialsPoint</a>')
    l4.setAlignment(Qt.AlignCenter)
    l4.setOpenExternalLinks(True)
    l4.linkActivated.connect(clicked)

    # Layout
    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    win.setLayout(vbox)
    win.setWindowTitle("QLabel Demo")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
~~~

# QLineEdit
## Introduction
QLineEdit object is the most commonly used input field. It provides a box in which one line of text can be entered. In order to enter multi-line text

## Method
1. setAlignment()

## Sample code
~~~python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   e1 = QLineEdit()
   e1.setValidator(QIntValidator())
   e1.setMaxLength(4)
   e1.setAlignment(Qt.AlignRight)
   e1.setFont(QFont("Arial",20))
	
   e2 = QLineEdit()
   e2.setValidator(QDoubleValidator(0.99,99.99,2))
	
   flo = QFormLayout()
   flo.addRow("integer validator", e1)
   flo.addRow("Double validator",e2)
	
   e3 = QLineEdit()
   e3.setInputMask('+99_9999_999999')
   flo.addRow("Input Mask",e3)
	
   e4 = QLineEdit()
   e4.textChanged.connect(textchanged)
   flo.addRow("Text changed",e4)
	
   e5 = QLineEdit()
   e5.setEchoMode(QLineEdit.Password)
   flo.addRow("Password",e5)
	
   e6 = QLineEdit("Hello Python")
   e6.setReadOnly(True)
   flo.addRow("Read Only",e6)
	
   e5.editingFinished.connect(enterPress)
   win.setLayout(flo)
   win.setWindowTitle("PyQt")
   win.show()
	
   sys.exit(app.exec_())

def textchanged(text):
   print ("contents of text box: " + text)
	
def enterPress():
   print ("edited")

if __name__ == '__main__':
   window()
~~~
