import PySimpleGUI as sg
import invoiceOCR

# 设置窗口图标
sg.set_global_icon("./image.ico")

# 设置主题
sg.theme("LightBlue2")
background_color = "#FFD39B"
button_color = "#F4A460"  # 228B22
sg.theme_text_element_background_color(background_color)
sg.theme_background_color(background_color)
sg.theme_button_color(button_color)
# 窗口布局
layout = [
    [sg.T("选择文件夹:", size=(11, 1), font=("楷体", 15), pad=((20, 20), 5)),
     sg.In(key="-dir_path-", tooltip="请输入文件夹路径", font=("楷体", 14), size=(27, 1)),
     sg.FolderBrowse("选择路径", target="-dir_path-", pad=((15, 10), 1), size=(10, 1), font=("楷体", 13))],

    [sg.T("选择输出路径:", size=(13, 1), font=("楷体", 15), pad=((20, 0), 5)),
     sg.In(key="-out_put-", tooltip="请输入文件夹路径", font=("楷体", 14), size=(27, 1)),
     sg.FolderBrowse("选择路径", target="-out_put-", pad=((15, 10), 1), size=(10, 1), font=("楷体", 13),
                     initial_folder="./Desktop")],

    [sg.T("发票文件格式:只支持JPG, JPEG, PNG 和 PDF格式", size=(44, 1), font=("楷体", 13), pad=((20, 30), 5)),
     sg.B("发票识别", key="-start-", pad=((2, 10), 1), size=(10, 1), font=("楷体", 13))],

    [sg.ML(key="-ml-", size=(55, 12), reroute_cprint=True, disabled=True, font=("楷体", 14))],
    [sg.T("作者:婳灬染    B站UID:215000730", size=(35, 1), font=("楷体", 10), pad=((330, 0), 5))]
]

window = sg.Window("发票识别", layout, alpha_channel=0.9)  # , size=(600, 365)
while True:
    event, values = window.read()
    if event == "-start-":
        # 清屏
        window['-ml-'].update(value="")

        # 禁用确认按钮
        window['-start-'].update(disabled=True)

        # 弹出窗口,用于防止误操作
        pop_result = sg.PopupOKCancel('请确认是否继续执行', grab_anywhere=True, keep_on_top=True,
                                      modal=True, font=('楷体', 12))

        # 判断弹窗返回值,'OK'执行,其他关闭程序
        if pop_result == 'OK':

            # 获取输入框中的值
            dir_path = values["-dir_path-"]
            out_put = values["-out_put-"]

            # 调用合并函数
            if dir_path and out_put:
                invoiceOCR.InvoiceInfo(dir_path, out_put).InvoiceInfo()

            else:
                sg.cprint("文件路径或输出路径不能为空!!!")

            # 清空输入框
            window["-dir_path-"].update(value="")
            window["-out_put-"].update(value="")
        window['-start-'].update(disabled=False)

    if event in (None, "Cancel"):
        break
window.close()

