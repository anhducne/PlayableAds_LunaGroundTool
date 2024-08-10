import os
import re
from Root.Utility import GlobalVarible
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import Root.dataManager as data
import Root.model_Applovin as C_applovin
import Root.model_Google as C_google
import Root.model_Mintengal as C_mintengal

def notiToolStatus4(label_toolStatus, value1, value2):
    GlobalVarible.ToolStatus = value1
    label_toolStatus.config(text=f"MẠNG ĐÍCH: {GlobalVarible.ToolStatus} {value2}")

def notiToolStatus(label_toolStatus, value1, value2):
    GlobalVarible.ToolStatus = value1
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus} {value2}")

def notiToolStatus2(label_toolStatus, value1):
    GlobalVarible.ToolStatus = value1
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus}")

def notiToolStatus3(label_toolStatus):
    label_toolStatus.config(text=f"TOOL_STATUS: {GlobalVarible.ToolStatus}")


def init_StockFolder(f_path, stockFolder_Path, label_toolStatus):
    try:
        stockFolder_Path.delete("1.0", tk.END)
        stockFolder_Path.insert(tk.END, f_path)
        notiToolStatus2(label_toolStatus,"Đang kiểm tra các thông số")  
    except Exception as e:   
        print(e)
        notiToolStatus2(label_toolStatus,"Lỗi Tạo folder Import")  

def init_TargetFolder(f_path,targetFolder_Path, label_toolStatus):
    try:
        targetFolder_Path.delete("1.0", tk.END)
        targetFolder_Path.insert(tk.END, f_path)
        notiToolStatus2(label_toolStatus,"Đang kiểm tra các thông số")  
    except Exception as e:  
        print(e)
        notiToolStatus2(label_toolStatus,"Lỗi Tạo folder Export")   

def init_ResolutionSize(selected_size, size_dropdown):
    selected_size.set(GlobalVarible.ads_Now)
    # cleaned_string = var_Global.resolution_All.replace("'", "").replace(",", "").replace("]", "").replace("[", "") // cái ni là cho chuỗi string
    size_dropdown['values'] = GlobalVarible.ads_all

def changeTargetImageSize(selected_size, label_toolStatus2, label_toolStatus):
    selectedSizeTemp = selected_size.get()
    if selectedSizeTemp != GlobalVarible.ads_Now :
        # data.update_json(jsType.resolutionNowChange, selectedSizeTemp)
        GlobalVarible.ads_Now = selectedSizeTemp
        selected_size.set(GlobalVarible.ads_Now)
        notiToolStatus2(label_toolStatus,"Đã thay đổi mạng đầu ra")  
        notiToolStatus4(label_toolStatus2, "X", GlobalVarible.ads_Now)  
    else:
        notiToolStatus4(label_toolStatus2, "Error", GlobalVarible.ads_Now)  


def buildAds(label_toolStatus):
    if GlobalVarible.ads_Now == "Applovin":
        try:
            C_applovin.main()
            notiToolStatus2(label_toolStatus,"Convert thành công sang Applovin")  
        except Exception as e:
            print(e)
            notiToolStatus2(label_toolStatus,"Lỗi: Check lại html đầu vào !")  
    elif GlobalVarible.ads_Now == "Google":
        try:
            C_google.main()
            notiToolStatus2(label_toolStatus,"Convert thành công sang Google")  
        except Exception as e:
            print(e)
            notiToolStatus2(label_toolStatus,"Lỗi: Check lại html đầu vào !")  
    elif GlobalVarible.ads_Now == "Mintengal":
        try:
            C_mintengal.main()
            notiToolStatus2(label_toolStatus,"Convert thành công sang Mintengal")  
        except Exception as e:
            print(e)
            notiToolStatus2(label_toolStatus,"Lỗi: Check lại html đầu vào !")  


def Init_Main():
    data.Init_Data()
