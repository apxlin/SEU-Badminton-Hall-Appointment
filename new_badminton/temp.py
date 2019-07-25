#coding=utf-8
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import requests
import PicProcess
from io import BytesIO
from PIL import Image
import datetime
import time
from threading import Timer
class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(MainWindow)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 9, 401, 161))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.widget_5)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget_5)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.login = QtWidgets.QPushButton(self.widget_5)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 2, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(30, 180, 371, 141))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.friendid = QtWidgets.QLineEdit(self.widget_6)
        self.friendid.setObjectName("friendid")
        self.gridLayout_3.addWidget(self.friendid, 1, 1, 1, 1)
        self.friendadd = QtWidgets.QPushButton(self.widget_6)
        self.friendadd.setObjectName("friendadd")
        self.gridLayout_3.addWidget(self.friendadd, 2, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget.raise_()
        self.widget_6.raise_()
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 360, 381, 141))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.time1 = QtWidgets.QLineEdit(self.widget_7)
        self.time1.setObjectName("time1")
        self.gridLayout_4.addWidget(self.time1, 1, 1, 1, 1)
        self.date = QtWidgets.QLineEdit(self.widget_7)
        self.date.setObjectName("date")
        self.gridLayout_4.addWidget(self.date, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.start = QtWidgets.QPushButton(self.widget_7)
        self.start.setObjectName("start")
        self.gridLayout_4.addWidget(self.start, 2, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(500, 10, 281, 511))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text = QtWidgets.QTextEdit(self.widget_4)
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.login.clicked.connect(self.loginfun) 
        self.friendadd.clicked.connect(self.friendfun)
        self.start.clicked.connect(self.startfun)
        
        self.ssion = requests.session()
        self.headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
		 }
        self.islogin = False
        self.friend='75496'
        self.usr='220173080'
        self.pas='01234567891234567890123456789'
        self.strend='2018-09-14'
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "东南大学羽毛球预约软件"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.login.setText(_translate("MainWindow", "登陆"))
        self.label_4.setText(_translate("MainWindow", "添加用户ID"))
        self.friendadd.setText(_translate("MainWindow", "添加确认"))
        self.label_5.setText(_translate("MainWindow", "预约日期"))
        self.label_6.setText(_translate("MainWindow", "预约时间"))
        self.start.setText(_translate("MainWindow", "开始预约"))
    

		
		
   
    def loginfun(self):
        strus=self.username.text()
        strps=self.password.text()
        
        data = {"username": strus,"password":strps}
        self.ssion.post("https://selfservice.seu.edu.cn/selfservice/campus_login.php", data = data)
        response = self.ssion.get("http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1")
        if len(response.text)>9080:
            self.text.setText("login success\n")
            self.usr=strus
            self.pas=strps
            
        
    def friendfun(self):
        strid=self.friendid.text()
        data2 = {"cardNo": strid}
        req=self.ssion.post("http://yuyue.seu.edu.cn/eduplus/order/order/order/order/searchUser.do?sclId=1", data = data2)
        name=req.json()[0]['nameDepartment']
        self.text.setText(name)
        self.friend=str(req.json()[0]['userId'])

    def threadsleep(self):
        while(self.islogin==False):
            data = {"username": self.usr,"password":self.pas}

            self.ssion.post("https://selfservice.seu.edu.cn/selfservice/campus_login.php", data = data)

            req=self.ssion.get("http://yuyue.seu.edu.cn:80/eduplus/control/validateimage")

            f = BytesIO(req.content)
            im = Image.open(f)
            validateNum = PicProcess.getResutlFromStr(im)
            data2 = {"orderVO.useTime": self.strend,"orderVO.itemId":"10","orderVO.useMode":"2","useUserIds":self.friend,"orderVO.phone":"12345678901","orderVO.remark":"","validateCode":validateNum}
            req=self.ssion.post("http://yuyue.seu.edu.cn/eduplus/order/order/order/insertOredr.do?sclId=1",data=data2)
            if req.text == 'success':
                self.islogin = True
            
        return
            
        
        
        
    def startfun(self): 
        self.text.setText("start......")
        strdata=self.date.text()
        strtime=self.time1.text()
        self.strend=strdata+' '+strtime
        
        now = datetime.datetime.now()
        nextDay = now + datetime.timedelta(days=1)
        loginTime = datetime.datetime(nextDay.year, nextDay.month, nextDay.day , 8, 0, 10)	
      #  exitTime = datetime.datetime(nextDay.year, nextDay.month, nextDay.day , 8, 1,0)
        a=(loginTime-now).seconds
        t = Timer(a,self.threadsleep)
        t.start()
        t.join()
        if self.islogin==True:
            self.text.setText("success")
        return
        
        
        
        
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
