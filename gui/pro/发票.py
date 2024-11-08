# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/11/8 23:06 
@本段代码的视频说明     ：
'''
import json
import os
import sys
import traceback

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, \
    QSpacerItem, QSizePolicy, QMessageBox, QGridLayout, QLineEdit, QFileDialog, QTextEdit, QProgressBar

import poocr


class MainWindow(QWidget):
    process_status_signal = pyqtSignal(int, str)

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.initUI()

    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):  # 是否Bundle Resource
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()
        # lg.info(f"basepath：{base_path}")
        return os.path.join(base_path, relative_path)

    def updateJson(self, jsonFile, key, value):
        try:
            with open(jsonFile, 'r', encoding="utf-8") as fr:  # 文件路径自己改成完整的
                # print(key,value)
                json_all = json.load(fr)
                json_all[key] = value
            with open(jsonFile, 'w+', encoding="utf-8") as fw:
                json.dump(json_all, fw, ensure_ascii=False, indent=4)
        except:
            error = traceback.format_exc()
            print(error)

    def initUI(self):
        '''
        (1)
        创建主垂直布局
        '''
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # 设置布局的四个间距都为0
        self.resize(600, 400)

        '''
        (2)
        创建第一个QWidget，背景色为绿色，固定高度为60
        '''
        top_widget = QWidget()
        top_widget.setStyleSheet("background-color:#6495ED;")
        top_widget.setFixedHeight(60)
        # 创建一个横向布局
        h_layout = QHBoxLayout()

        # 创建图片标签并添加到横向布局
        image_label = QLabel()
        # 假设你有一个图片路径
        # 加载图片并调整其大小为64x64
        pixmap = QPixmap('title.png')
        scaled_pixmap = pixmap.scaled(120, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        h_layout.addWidget(image_label)
        h_layout.setSpacing(20)

        # 创建文本标签并添加到横向布局
        text_label = QLabel("欢迎使用提取电子发票数据到Excel工具！")
        text_label.setStyleSheet("QLabel { color: white; }")
        h_layout.addWidget(text_label)

        # 创建一个压缩空间控件并添加到横向布局
        # 使用QSizePolicy.Expanding作为策略可以使空间尽可能地被压缩
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(spacer_item)

        # 将横向布局设置为top_widget的布局
        top_widget.setLayout(h_layout)
        # 添加到主布局
        main_layout.addWidget(top_widget)

        '''
        创建第二个QWidget，用于包含win1和win2的QHBoxLayout
        '''
        second_widget = QWidget()
        second_layout = QHBoxLayout(second_widget)

        # 创建win1，固定宽度为60
        win1 = QWidget()
        win1.setFixedWidth(160)
        win1.setStyleSheet("background-color: #6495ED;")
        # 创建两个按钮
        button1 = QPushButton("操作界面", win1)
        button2 = QPushButton("配置设置", win1)
        # 设置字体样式
        font = QFont('微软雅黑', 12, QFont.Bold)  # 字体名称、大小、加粗
        button1.setFont(font)
        button2.setFont(font)
        text_label.setFont(font)
        button1.setStyleSheet("QPushButton { color: #6495ED;border-radius:5px;background-color:white; }")
        button2.setStyleSheet("QPushButton { color: #6495ED; border-radius:5px;background-color:white;}")
        spacer_item2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # 垂直布局用于放置按钮
        button_layout = QVBoxLayout(win1)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addItem(spacer_item2)
        button_layout.setSpacing(40)
        # 将win1添加到水平布局
        second_layout.addWidget(win1)

        # 创建win2的QStackedWidget
        win2 = QStackedWidget()
        # win2.setStyleSheet("background-color: #ffffff;")
        '''
        创建两个界面
        1、第一个界面
        '''
        firstWg = QWidget()
        firstLayout = QGridLayout(firstWg)
        pdfLabel1 = QLabel("电子发票目录", firstWg)
        self.pdfText1 = QLineEdit()
        self.pdfText1.setText(self.config.get("pdfPath"))
        self.pdfBtn = QPushButton("选择", firstWg)
        self.pdfBtn.clicked.connect(self.btnProcess)

        firstLayout.addWidget(pdfLabel1, 0, 0)
        firstLayout.addWidget(self.pdfText1, 0, 1)
        firstLayout.addWidget(self.pdfBtn, 0, 2)

        resLabel1 = QLabel("结果目录", firstWg)
        self.resText1 = QLineEdit()
        self.resText1.setText(self.config.get("resPath"))
        self.resBtn = QPushButton("选择", firstWg)
        self.resBtn.clicked.connect(self.btnProcess)

        firstLayout.addWidget(resLabel1, 1, 0)
        firstLayout.addWidget(self.resText1, 1, 1)
        firstLayout.addWidget(self.resBtn, 1, 2)

        self.progLbl = QLabel("运行日志", firstWg)
        self.progLbl.setAlignment(Qt.AlignRight)
        firstLayout.addWidget(self.progLbl, 2, 0)
        self.progressText = QTextEdit(self)
        self.progressText.setObjectName("progressText")
        firstLayout.addWidget(self.progressText, 2, 1, 1, 2)
        self.progLbl2 = QLabel("运行进度", firstWg)
        self.progressBar = QProgressBar(firstWg)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        firstLayout.addWidget(self.progLbl2, 3, 0)
        firstLayout.addWidget(self.progressBar, 3, 1, 1, 2)

        self.submitBtn1 = QPushButton("提交", firstWg)
        self.openBtn1 = QPushButton("结果目录", firstWg)
        self.closeBtn = QPushButton("关闭", firstWg)
        self.submitBtn1.clicked.connect(self.btnProcess)
        self.openBtn1.clicked.connect(self.btnProcess)
        self.closeBtn.clicked.connect(self.close)
        firstLayout.addWidget(self.submitBtn1, 4, 0)
        firstLayout.addWidget(self.openBtn1, 4, 1)
        firstLayout.addWidget(self.closeBtn, 4, 2)
        spacer_item2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        firstLayout.addItem(spacer_item2, 5, 0)
        firstLayout.addItem(spacer_item2, 5, 1)

        '''
        2、第二个界面内容
        '''
        secondWg = QWidget()
        secondLayout = QGridLayout(secondWg)

        label2 = QLabel("腾讯云SecretId：", secondWg)
        self.text2 = QLineEdit()
        self.text2.setText(self.config.get("id"))
        secondLayout.addWidget(label2, 0, 0)
        secondLayout.addWidget(self.text2, 0, 1)

        label3 = QLabel("腾讯云SecretKey：", secondWg)
        self.text3 = QLineEdit()
        self.text3.setText(self.config.get("key"))
        secondLayout.addWidget(label3, 1, 0)
        secondLayout.addWidget(self.text3, 1, 1)

        self.saveBtn2 = QPushButton("保存", secondWg)
        self.saveBtn2.clicked.connect(self.btnProcess)

        secondLayout.addWidget(self.saveBtn2, 2, 0)
        spacer_item2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        secondLayout.addItem(spacer_item2, 3, 0)
        secondLayout.addItem(spacer_item2, 3, 1)
        # 将界面添加到堆叠控件
        win2.addWidget(firstWg)
        win2.addWidget(secondWg)

        # 将win2添加到水平布局
        second_layout.addWidget(win2)

        # 将第二个QWidget添加到主布局
        main_layout.addWidget(second_widget)

        # 连接按钮信号到槽函数
        button1.clicked.connect(lambda: win2.setCurrentIndex(0))
        button2.clicked.connect(lambda: win2.setCurrentIndex(1))
        main_layout.setSpacing(0)
        second_layout.setSpacing(0)
        second_layout.setContentsMargins(0, 0, 0, 0)
        # 设置窗口属性
        self.setWindowIcon(QIcon(self.resource_path("logo.ico")))
        self.setWindowTitle('电子发票数据自动提取到Excel')
        self.show()

    '''
        浏览点击事件
    '''

    def btnProcess(self):
        try:
            button = self.sender()
            if button == self.pdfBtn:
                dirPath = QFileDialog.getExistingDirectory(self, '选择发票文件目录',
                                                           os.path.join(os.getcwd(), "发票目录"))
                self.pdfText1.setText(dirPath)
                self.updateJson(os.path.join(os.getcwd(), "配置信息/sysConfig.json"), "pdfPath", dirPath)
            elif button == self.resBtn:
                dirPath = QFileDialog.getExistingDirectory(self, '选择结果目录',
                                                           os.path.join(os.getcwd(), "结果"))
                self.resText1.setText(dirPath)
                self.updateJson(os.path.join(os.getcwd(), "配置信息/sysConfig.json"), "resPath", dirPath)


            elif button == self.saveBtn2:
                ID = self.text2.text()
                pwd = self.text3.text()
                self.updateJson(os.path.join(os.getcwd(), '配置信息/sysConfig.json'), "id", ID)
                self.updateJson(os.path.join(os.getcwd(), '配置信息/sysConfig.json'), "key", pwd)
                self.config["id"] = ID
                self.config["key"] = pwd
                reply = QMessageBox.warning(self, "成功", "保存成功！")
                if reply:
                    return
            elif button == self.openBtn1:
                path = self.resText1.text()
                path = path.replace("/", "\\")
                os.system(f"start explorer {path}")

            elif button == self.submitBtn1:
                '''
                判断输入框的内容是否为空
                '''
                srcPath = self.pdfText1.text()
                if srcPath == "":
                    reply = QMessageBox.warning(self, "警告", "电子发票目录未设置！")
                    if reply:
                        return

                resultPath = self.resText1.text()
                if resultPath == "":
                    reply = QMessageBox.warning(self, "警告", "结果目录未选择！")
                    if reply:
                        return

                id = self.config.get("id")
                key = self.config.get("key")
                if not id and not key:
                    reply = QMessageBox.warning(self, "警告", "配置信息未配置！")
                    if reply:
                        return

                self.submitBtn1.setEnabled(False)
                self.openBtn1.setEnabled(False)
                self.closeBtn.setEnabled(False)
                self.progressText.setText("")
                self.progressBar.setValue(0)
                self.config["pdfPath"] = srcPath
                self.config["resPath"] = resultPath

                os.system('taskkill /IM EXCEL.exe /F')
                # os.system('taskkill /IM WINWORD.exe /F')
                os.system('taskkill /IM WPS.exe /F')
                '''
                开始转换
                '''
                self.progTxt = ""
                self.process_thread = transferThread(self.config)
                self.process_thread.start()
                self.process_thread.start_process_signal.connect(self.processStatus)
                self.process_thread.exec_()

        except Exception as e:
            e = traceback.format_exc()
            print(f"error:{e}")
            self.create.setEnabled(True)
            self.openDir.setEnabled(True)
            self.closeBtn.setEnabled(True)

    '''
    处理子线程信号函数
    '''

    def processStatus(self, value1, str1):
        self.progTxt = f"{self.progTxt}\n{str1}"
        if str1 == "":
            self.progressBar.setMaximum(int(value1))
            self.max_value = int(value1)
        else:
            self.progressBar.setValue(int(value1))
            self.progressText.setText(self.progTxt)
            if str1.find("Error") >= 0:
                reply = QMessageBox.warning(self, "错误", f"错误：{str1}！")
                if reply:
                    self.submitBtn1.setEnabled(True)
                    self.openBtn1.setEnabled(True)
                    self.closeBtn.setEnabled(True)
                    return
            elif int(value1) == self.max_value and str1.find("全部已完成") >= 0:
                reply = QMessageBox.warning(self, "成功", "处理已完成！")
                if reply:
                    self.submitBtn1.setEnabled(True)
                    self.openBtn1.setEnabled(True)
                    self.closeBtn.setEnabled(True)
                    return


'''
子线程类，实现转换
'''


class transferThread(QThread):
    '''
    创建信号 接受字符串（这里用于主线程向子线程传递信息）
    '''
    start_process_signal = pyqtSignal(int, str)

    def __init__(self, args):
        super(transferThread, self).__init__()
        self.args = args
        print(f"self.args:{self.args}")

    '''
    子线程主处理函数
    '''

    def run(self):
        try:
            self.start_process_signal.emit(3, "")
            pdfPath = self.args.get("pdfPath")
            resPath = self.args.get("resPath")
            id = self.args.get("id")
            key = self.args.get("key")
            resFile = "发票结果.xlsx"
            self.start_process_signal.emit(1, "配置数据获取完成，开始转换")
            print(f"{pdfPath},{resPath},{id},{key}")
            poocr.ocr2excel.VatInvoiceOCR2Excel(pdfPath, resPath, resFile, id=id, key=key)
            self.start_process_signal.emit(2, "转换已完成！")
            self.start_process_signal.emit(3, "处理全部已完成！")

        except:
            msg = traceback.format_exc()
            print(f"erorMsg:{msg}")
            self.start_process_signal.emit(1, f"Error:{msg}")


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    config = {}
    if os.path.exists(os.path.join(os.getcwd(), "配置信息/sysConfig.json")):
        with open(os.path.join(os.getcwd(), "配置信息/sysConfig.json"), encoding="utf-8") as f:
            configStr = f.read()
        config = json.loads(configStr)

    ex = MainWindow(config)
    sys.exit(app.exec_())
