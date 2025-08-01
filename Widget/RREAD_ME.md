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

def hovered(link):
    print("hovering on:", link)

def clicked(link):
    print("clicked:", link)

def window():
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
