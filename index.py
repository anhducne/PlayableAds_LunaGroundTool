import os
import sys
import tkinter as tk
from tkinter import ttk
import Root.Utility.GlobalVarible as var_Global
import Root.main as mainIndex


def openStockFolder():
    os.startfile(var_Global.stockPath_Now)

def openTargetFolder():
    os.startfile(var_Global.targetPath_Now)

def changeTargetImageSize():
    mainIndex.changeTargetImageSize(selected_size, label_toolStatus2, label_toolStatus)

def buildAds():
    mainIndex.buildAds(label_toolStatus)

def on_close():
        try: 
            sys.exit() 
        except Exception as e:
            print(e)


root = tk.Tk()
root.title("Luna Crack: One Click Irounsouce for All")
root.geometry("870x450") # size cửa sổ mặc đinh
root.resizable(True,True) # cho người dùng resize cửa sổ ko 
root.protocol("WM_DELETE_WINDOW", on_close)
# Tạo và định vị các widget
label_tittle = ttk.Label(root, text="One Click Irounsouce for all by DuxBee - Ver 0.1" ,foreground="violet", font=("Arial",17,"bold"))
label_tittle.grid(column=1, row=0, sticky=tk.EW, padx=0, pady=5)
#1
label_tittle_2 = ttk.Label(root, text="#1: CẤU HÌNH", foreground="green", font=("bold"))
label_tittle_2.grid(column=0, row=1, sticky=tk.EW, padx=0, pady=5)
label_toolStatus = ttk.Label(root, text="TOOL_STATUS:", foreground="red", font=("bold"))
label_toolStatus.grid(column=1, row=1, sticky=tk.EW, padx=0, pady=5)
#3 - stock folder 
label_stockFolder = ttk.Label(root, text="Thư mục gốc (StockFolder): ")
label_stockFolder.grid(column=0, row=3, sticky=tk.EW, padx=0, pady=5)
stockFolder_Path = tk.Text(root, height=1, width=30)
stockFolder_Path.grid(column=1, row=3, sticky=tk.EW, padx=0, pady=5)
opend_stockFolder = ttk.Button(root, text="Mở Thư mục gốc", command=openStockFolder)
opend_stockFolder.grid(column=2, row=3, sticky=tk.EW, padx=0, pady=5)
#4 - targetFolder 
label_targetFolder = ttk.Label(root, text="Thư mục đích (TargetFolder):")
label_targetFolder.grid(column=0, row=4, sticky=tk.EW, padx=0, pady=5)
targetFolder_Path = tk.Text(root, height=1, width=30)
targetFolder_Path.grid(column=1, row=4, sticky=tk.EW, padx=0, pady=5)
opend_targetFolder = ttk.Button(root, text="Mở Thư mục đích", command=openTargetFolder)
opend_targetFolder.grid(column=2, row=4, sticky=tk.EW, padx=0, pady=5)
#5 - Dropdown list hiển thị các size ảnh từ file JSON
label_dropdown = ttk.Label(root, text="Mạng cần convert: ")
label_dropdown.grid(column=0, row=5, sticky=tk.EW, padx=0, pady=5)
selected_size = tk.StringVar()
size_dropdown = ttk.Combobox(root, textvariable=selected_size)
size_dropdown.grid(column=1, row=5, sticky=tk.EW, padx=0, pady=5)
Choose_ImageSize = ttk.Button(root, text="Chọn", command=changeTargetImageSize)
Choose_ImageSize.grid(column=2, row=5, sticky=tk.EW,padx=10, pady=5)
#7 - Chooseimage Zone
label_ConvertImgNow = ttk.Label(root, text="#2: Build", foreground="Blue", font=("bold"))
label_ConvertImgNow.grid(column=0, row=6, sticky=tk.EW, padx=0, pady=5)
label_toolStatus2 = ttk.Label(root, text="MẠNG ĐÍCH:", foreground="blue", font=("bold"))
label_toolStatus2.grid(column=1, row=6, sticky=tk.EW, padx=0, pady=5)
button_Build = ttk.Button(root, text="Build", command=buildAds)
button_Build.grid(column=2, row=6, sticky=tk.EW, padx=0, pady=5)
# 7
label_ConvertImgNow2 = ttk.Label(root, text="#3: Guide", foreground="black", font=("bold"))
label_ConvertImgNow2.grid(column=0, row=7, sticky=tk.EW, padx=0, pady=5)
label_toolStatus3 = ttk.Label(root, text="B1: Đổi tên file html thành index.html \nB2: Cho folder data đối với mạng MTG vào folder import\nđể chạy tự động đổi luôn scripts.js nhớ đổi tên folder thành asset\nB3: Mạng GG chưa làm build folder asset nên vẫn theo cách cũ\nB4:Cách dùng: chọn mạng cần convert, sau đó bấm chọn\nsau đó bấm build, chương trình sẽ tự chạy\nB5: Mỗi khi build mạng MTG thì hãy bỏ lại folder asset vào\nbấm build đi build lại nhiều lần sẽ tăng dung lượng file scripts.js", foreground="black", font=("bold"))
label_toolStatus3.grid(column=1, row=7, sticky=tk.EW, padx=0, pady=5)

def Init_UI():
    mainIndex.init_StockFolder(var_Global.stockPath_Now ,stockFolder_Path, label_toolStatus)
    mainIndex.init_TargetFolder(var_Global.targetPath_Now, targetFolder_Path, label_toolStatus)
    mainIndex.init_ResolutionSize(selected_size, size_dropdown)


def Init_Main():
    mainIndex.Init_Main()

if __name__ == "__main__":
  Init_Main()
  Init_UI()

root.mainloop()