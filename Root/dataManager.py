import os
import json
from datetime import datetime
from Root.Utility import GlobalFunction
from Root.Utility import GlobalVarible 

RootDir = os.getcwd()
JsonPath = RootDir + "\Root\Data\Data.json"
dataPath = RootDir + '\Root\Data'

dataParentPath = RootDir + '\Root'
new_folder_name = "Data"

stock_target_Path = RootDir

new_Stockfolder_name = "1_Folder_Import"
new_Targetfolder_name = "2_Folder_Export"

stockPath = "\Folder_Import"
target_PATH = "\Folder_Export"
adsNow = "Applovin"
adsAll =  ['Applovin','Google', 'Mintengal']

# Json Time CRUD by Bee

# Hàm check có tồn tại jsonFile không 
def check_json_file(file_path):
  return os.path.exists(file_path)

# Nếu không tồn tại Json/ Tạo Json Default
def create_json(JsonPathPara):
    now = datetime.now()
    current_time = now.isoformat()
    data = {
    "tittle": "Json Create by beeJsonDefault",
    "time_Create": current_time,
    "stock_PATH": RootDir + stockPath,
    "target_PATH": RootDir + target_PATH,
    "ads_Now": adsNow,
    "ads_All": adsAll,
    }
    # Ghi dữ liệu vào file JSON
    GlobalFunction.tool_status("Json Update Done !")
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(JsonPathPara, 'w', encoding='utf-8') as f:
       f.write(json_data)

# Nếu có Json thì đọc dữ liệu có sẵn và lưu vào biến global 
def read_json(JsonPath):
    with open(JsonPath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Tittle
    GlobalVarible.title_Now = data.get("tittle")
    # Trích xuất thời gian hiện tại từ dữ liệu
    timestamp = data.get("time_Create")
    # Chuyển đổi chuỗi thời gian sang đối tượng datetime
    time_obj = datetime.fromisoformat(timestamp)
    # Gán giá trị// thời điểm chạy ban đầu
    GlobalVarible.timeCreate_Now = str(time_obj)
    GlobalVarible.stockPath_Now = data.get("stock_PATH")
    GlobalVarible.targetPath_Now = data.get("target_PATH")
    GlobalVarible.ads_Now = str(data.get("adsNow"))
    GlobalVarible.ads_all = data.get("ads_All")

def checkData_Json(JsonPathPara):
    if check_json_file(JsonPathPara):
        GlobalFunction.tool_status("Tồn tại Data.json")
        read_json(JsonPathPara)
    else:
        GlobalFunction.tool_status("Không có Data.json")
        create_json(JsonPathPara)
        read_json(JsonPathPara)   

# Hàm check Data chạy vào đầu khi khởi động chương trình 
def checkData_Folder(JsonPathPara):
    try:
        if  os.path.exists(dataPath):
            checkData_Json(JsonPathPara)
        else:
            new_folder_path = os.path.join(dataParentPath, new_folder_name)
            os.makedirs(new_folder_path)
            checkData_Json(JsonPathPara)
    except Exception as e:
            print(e)


# Hàm check đã tồn tại folder đích với gốc chưa, chưa thì tạo default rồi gán lại giá trị
def checkStock_Folder(data):
    # GlobalVarible.stockPath_Now = data.get("stock_PATH")
    try:
        if  os.path.exists(data.get("stock_PATH")):
            # print("stockPath_Availiable")
            print(".......")
        
        elif os.path.exists(os.path.join(stock_target_Path, new_Stockfolder_name)):
            print("case cak")
            new_folder_path = os.path.join(stock_target_Path, new_Stockfolder_name)
            data["stock_PATH"] = new_folder_path
            GlobalVarible.stockPath_Now = data.get("stock_PATH")
        else:
            # print("stockPath_NotAvailiable")
            print(".......")
            new_folder_path = os.path.join(stock_target_Path, new_Stockfolder_name)
            os.makedirs(new_folder_path)
            #cập nhật lại data về default
            data["stock_PATH"] = new_folder_path
            GlobalVarible.stockPath_Now = data.get("stock_PATH")
    except Exception as e:
            print(e)

def checkTarget_Folder(data):
    try:
        if  os.path.exists(data.get("target_PATH")):
            # print("targetPath_Availiable")
            print(".....")
        elif os.path.exists(os.path.join(stock_target_Path, new_Targetfolder_name)):
            print(".....")
            new_folder_path = os.path.join(stock_target_Path, new_Targetfolder_name)
            data["target_PATH"] = new_folder_path
            GlobalVarible.targetPath_Now = data.get("stock_PATH")
        else:
            # print("targetPath_NotAvailiable")
            print(".......")
            new_folder_path = os.path.join(stock_target_Path, new_Targetfolder_name)
            os.makedirs(new_folder_path)
            data["target_PATH"] = new_folder_path 
            GlobalVarible.targetPath_Now = data.get("target_PATH")
    except Exception as e:
            print(e)

def check_target_stock_available():
    with open(JsonPath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    checkStock_Folder(data)
    checkTarget_Folder(data)
    with open(JsonPath, 'w') as file:
        json.dump(data, file, indent=4)




def Init_Data():
    checkData_Folder(JsonPath)
    check_target_stock_available()