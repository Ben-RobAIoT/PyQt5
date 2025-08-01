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

