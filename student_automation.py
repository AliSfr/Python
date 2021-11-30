from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import os

con = sqlite3.connect("stundent.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student(Name TEXT,Surname TEXT,Class TEXT,Number INT)")
con.commit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 529)
        Form.setBaseSize(QtCore.QSize(50, 50))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 181, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.add = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.add.setContentsMargins(0, 0, 0, 0)
        self.add.setObjectName("add")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.add.addWidget(self.name)
        self.surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.surname.setObjectName("surname")
        self.add.addWidget(self.surname)
        self.Class = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Class.setObjectName("Class")
        self.add.addWidget(self.Class)
        self.number = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.number.setObjectName("number")
        self.add.addWidget(self.number)
        self.add_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.add.addWidget(self.add_button)
        self.label = QtWidgets.QLabel("")
        self.add.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 290, 181, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.delete_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.delete_2.setContentsMargins(0, 0, 0, 0)
        self.delete_2.setObjectName("delete_2")
        self.del_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.del_name.setObjectName("del_name")
        self.delete_2.addWidget(self.del_name)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delete_button.setObjectName("delete_button")
        self.delete_2.addWidget(self.delete_button)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(200, 10, 411, 511))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Show = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Show.setContentsMargins(0, 0, 0, 0)
        self.Show.setObjectName("Show")
        self.Show_Text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.Show_Text.setObjectName("Show_Text")
        self.Show.addWidget(self.Show_Text)
        self.Show_button = QtWidgets.QPushButton(Form)
        self.Show_button.setGeometry(QtCore.QRect(50, 460, 101, 41))
        self.Show_button.setObjectName("Show_button")
        self.add_button.clicked.connect(self.ekle)
        self.delete_button.clicked.connect(self.sil)
        self.Show_button.clicked.connect(self.goster)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "Name"))
        self.surname.setText(_translate("Form", "Surname"))
        self.Class.setText(_translate("Form", "Class"))
        self.number.setText(_translate("Form", "Number"))
        self.add_button.setText(_translate("Form", "Add"))
        self.del_name.setText(_translate("Form", "Number"))
        self.delete_button.setText(_translate("Form", "Delete"))
        self.Show_Text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Show_button.setText(_translate("Form", "Show"))

    def ekle(self):
        self.label.setText("")
        name = self.name.text()
        surname = self.surname.text()
        Class = self.Class.text()
        number = int(self.number.text())
        cursor.execute("SELECT * FROM Student WHERE Number = ?",(number,))
        liste = cursor.fetchall()
        if(len(liste) == 0):
            cursor.execute("INSERT INTO Student VALUES(?,?,?,?)",(name,surname,Class,number))
            con.commit()
            self.label.setText("")
        else:
            self.label.setText("Such a student already exists")

    def sil(self):
        self.label.setText("")
        number = int(self.del_name.text())
        cursor.execute("SELECT * FROM Student WHERE Number = ?",(number,))
        liste = cursor.fetchall()
        if (len(liste) == 0):
            self.label.setText("No such number was found")
        else:
            cursor.execute("DELETE FROM Student WHERE Number = ?",(number,))
            con.commit()
            self.label.setText("")

    def goster(self):
        self.label.setText("")
        cursor.execute("SELECT * FROM Student")
        liste = cursor.fetchall()
        if (len(liste) == 0):
            self.label.setText("No data to display")
        else:
            self.label.setText("")
            with open("ogr.txt","w",encoding = "utf-8", errors = "ignore") as file:
                for i in liste:
                    file.write("-------------------------------------------------------")
                    for a in i:
                        file.write(str(a) + "\n")
            with open("ogr.txt","r",encoding = "utf-8", errors = "ignore") as file2:
                self.Show_Text.setText(file2.read())
            os.remove("ogr.txt")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
