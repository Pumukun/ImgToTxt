import cv2
import pytesseract
from ui import Ui_MainWindow as MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import easygui
import sys

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
filetypes = ['*.ras', '*.xwd', '*.bmp', '*.jpe', '*.jpg', '*.jpeg',
             '*.xpm', '*.ief', '*.pbm', '*.tif', '*.gif', '*.ppm',
             '*.xbm', '*.tiff', '*.rgb', '*.pgm', '*.png', '*.pnm']


class ImgToTxt(QtWidgets.QMainWindow):
    def __init__(self):
        super(ImgToTxt, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.convert_button.clicked.connect(self.img_load)
        self.ui.load_img_button.clicked.connect(self.img_load_button)

    def init_UI(self):
        self.setWindowTitle('ImgToTxtApp')
        self.setWindowIcon(QIcon('imgtotxt.png'))

    def img_load_button(self):
        input_file = easygui.fileopenbox(filetypes=filetypes)
        self.ui.img_loc_edit.setText(input_file)

    def img_load(self):
        img_loc = self.ui.img_loc_edit.displayText()
        if img_loc == '' or self.location_correct(img_loc) == False:
            self.ui.output_text.setText('*Something went wrong.*')
        else:
            img = cv2.imread(img_loc)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            res = pytesseract.image_to_string(img, self.language_change())
            self.ui.output_text.setText(res)

    def language_change(self):
        lang = self.ui.language_cbox.currentIndex()
        if lang == 0:
            return 'eng'
        if lang == 1:
            return 'rus'

    @staticmethod
    def location_correct(location):
        fl = False
        for i in filetypes:
            if location[-(len(i) - 1):] == i[1::]:
                fl = True
        return fl


app = QtWidgets.QApplication([])
application = ImgToTxt()
application.show()

sys.exit(app.exec())
