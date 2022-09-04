import sys
from resizeImage import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class ImageResizer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.chooseFile.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resizer)
        self.btnSave.clicked.connect(self.save)
        self.resized = False
    
    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open image',
            r'C:\Users\55119\Documents\Estudos\Python\PyQT5'
        )

        self.inputOpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.imageLabel.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))
    
    def resizer(self):
        width = int(self.inputWidth.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.imageLabel.setPixmap(self.new_img)
        self.inputWidth.setText(str(self.new_img.width()))
        self.inputHeight.setText(str(self.new_img.height()))
        self.resized = True
    
    def save(self):
        if not self.resized == False:
            image, _ = QFileDialog.getSaveFileName(
                self.centralwidget,
                'Save image',
                r'C:\Users\55119\Documents\Estudos\Python\PyQT5'
            )

            self.new_img.save(image, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resizer = ImageResizer()
    resizer.show()
    qt.exec_()