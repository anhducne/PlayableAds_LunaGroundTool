import re
import os
import shutil
from bs4 import BeautifulSoup
from Root.Utility import GlobalVarible


# if(not os.path.isdir('Mintengal')):
#     os.mkdir('Mintengal')
#     print('Tao thanh con thu muc Mintengal')

# RootDir = os.getcwd()
# print(RootDir)

# htmlPath = RootDir + '/00PutFileIndexHere/index.html'
# htmlPathAfterBuild = RootDir + '/Mintengal/index.html'

# ////////////////////////////////////////////////////////////////////////////ENDSolutionIDEA//////////////////////////////////////////////////////////////////////////////////////////
def simpleImSoLazy(html_file_name, html_target):
    with open(html_file_name, "r") as f:
        html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")

        scripts = soup.find_all("script")

        mystring1 = r'insertYourRemoteDebuggingTokenHere'
        mystring2 = r'window._compressedAssets = window._compressedAssets'
        mystring3 = r'RECEIVE_MSG_PREFIX="DAPI_SERVICE:"'

        stringPLC0 = r'resourceConfig'
        stringPLC1 = r'window.pi.apply'
        stringPLC2 = r'const unbrotli = makeBrotliDecode'
        stringPLC3 = r'const unbrotli = makeBrotliDecode'
        stringPLC4 = r'const unbrotli = makeBrotliDecode'
        stringPLC5 = r'dapi.removeEventListener'
        stringPLC6 = r'NUC is not defined'
        stringPLC7 = r'base64ToArrayBuffer'
        stringPLC8 = r'Luna.Unity.LifeCycle.OnMute'
        


        # Ket quả cần thay đổi 
        strTarget0 = r'window.$environment={baseUrl:"./",resourceConfig:{json:"inline",image:"inline",video:"inline",sound:"compress",blob:"compress"},packageConfig:Object.assign({inlineScripts:!1,inlineJsons:!1,inlineBlobs:!1,inlineImages:!0,inlineSounds:!0,inlineVideos:!0,applicationName:"",iosLink:"",androidLink:"",orientation:"unspecified",languages:["en","en"]},window.LUNA_PLAYGROUND_PACKAGE_CONFIG||{}),playerPrefs:!0,usingWebWorkers:"off",targetPlatform:"mintegral",runtimeAnalysisModules:["physics3d","physics2d","particle_system","reflection","prefabs","mecanim-wasm"]}'
        strTarget1 = r'window.pi.apply(window,[]||[])'
        strTarget2 = r'assets/scripts.js' #x
        strTarget3 = r'assets/jsons.js' #x
        strTarget4 = r'assets/blobs.js' #x

        strTarget5 = r'window.gameClose=function(){window.dispatchEvent(new Event("luna:pause"))},window.addEventListener("luna:build",(()=>{Bridge.ready((()=>{Luna.Unity.Playable.InstallFullGame=function(){window.pi.logCta(),window.install&&window.install()}}))})),window.addEventListener("luna:ended",(()=>{window.gameEnd&&window.gameEnd()}))'
        strTarget6 = r'window.addEventListener("luna:build",(()=>{window.pi.logLoaded(),window.dispatchEvent(new Event("luna:unsafe:pause")),window.dispatchEvent(new Event("luna:start"))})),window.addEventListener("luna:started",(()=>{window.gameReady&&window.gameReady()})),window.gameStart=function(){window.dispatchEvent(new Event("luna:unsafe:resume")), console.log("a legend who was here, Hanoi_27/02/2024, sign: DucBee, fb: https://www.facebook.com/toilachogaugaugau")}'
        
        strTarget7 = r'function _base64ToArrayBuffer(e){for(var r=window.atob(e),n=r.length,o=new Uint8Array(n),t=0;t<n;t++)o[t]=r.charCodeAt(t);return o}function _initParallelDecompression(){window._usingWebWorkers=!0;const e=`\n              const makeBrotliDecode = ${window.makeBrotliDecodeStr};\n              const unbrotli = makeBrotliDecode();\n              self.onmessage = ( e ) => {\n                  const { buffer, length } = e.data;\n                  const result = unbrotli( new Uint8Array( buffer, 0, length ) ).buffer;\n                  postMessage( { result }, [ result ] );\n              }\n          `,r=new Blob([e],{type:"application/javascript"});window._workerBlobUrl=URL.createObjectURL(r);const n=Math.max(Math.min(navigator.hardwareConcurrency||2,4),2);for(let e=0;e<n;e++)window._freeWorkers.push(new Worker(window._workerBlobUrl))}function _initSyncDecompression(){window._usingWebWorkers=!1,Function(`"use strict"; window.unbrotli = (${window.makeBrotliDecodeStr})()`)()}function _fetchFreeWorker(){return new Promise((e=>{0!==window._freeWorkers.length?e(window._freeWorkers.pop()):window._workerWaitingList.push(e)}))}function _freeWorker(e){0!==window._workerWaitingList.length?window._workerWaitingList.pop()(e):window._freeWorkers.push(e)}window.sharedBase122Buffer=null,(()=>{let e=0,r=0,n=0;const o=[0,10,13,34,38,92];function t(o,t){e|=(o<<=1)>>>r,r+=7,r>=8&&(t[n++]=e,r-=8,e=o<<7-r&255)}window._base122ToArrayBuffer=(s,i=!1)=>{const w=1.75*s.length|0;let a=null;i?((!window.sharedBase122Buffer||window.sharedBase122Buffer.length<w)&&(window.sharedBase122Buffer=new Uint8Array(w)),a=window.sharedBase122Buffer):a=new Uint8Array(w),e=0,r=0,n=0;for(let e=0;e<s.length;e++){const r=s.charCodeAt(e);if(r>127){const e=r>>>8&7;7!==e&&t(o[e],a),t(127&r,a)}else t(r,a)}return new Uint8Array(a.buffer,0,n)}})(),window._usingWebWorkers=!1,window._freeWorkers=[],window._workerWaitingList=[],window._workerBlobUrl=null,(()=>{const e=window.$environment&&window.$environment.usingWebWorkers||"off";let r=!0;"off"===e?r=!1:"test"===e&&(r=murmurhash3_32_gc(window.pi.env.sessionId)%3==0);try{r?_initParallelDecompression():_initSyncDecompression()}catch(e){console.error(e),_initSyncDecompression()}finally{delete window.makeBrotliDecodeStr}})();const decompressUsingWebWorkers=function(e,r){return new Promise((n=>{_fetchFreeWorker().then((o=>{const t=r?_base122ToArrayBuffer(e):_base64ToArrayBuffer(e),s=t.buffer;o.postMessage({buffer:s,length:t.length},[s]);const i=e=>{o.removeEventListener("message",i),_freeWorker(o),n(new Uint8Array(e.data.result))};o.addEventListener("message",i)}))}))},decompressInTheSameThread=function(e,r){return new Promise((n=>{n(r?unbrotli(_base122ToArrayBuffer(e,!0)):unbrotli(_base64ToArrayBuffer(e)))}))},decompress=function(e,r){return window.lunaStartup&&(window.lunaStartup.timestamps.decompressionStarted=window.lunaStartup.timestamps.decompressionStarted||performance.now()),window._usingWebWorkers?decompressUsingWebWorkers(e,r):decompressInTheSameThread(e,r)},decompressArrayBuffer=function(e,r){return new Promise((n=>{decompress(e,r).then((({buffer:e})=>{n(e)})).catch((e=>console.error(e)))}))},decompressString=function(e,r){return new Promise((n=>{decompress(e,r).then((e=>{const r=new TextDecoder("utf-8").decode(e);n(r)})).catch((e=>console.error(e)))}))};window.addEventListener("luna:ready",(function(){Promise.all(window._compressedAssets).then((function(){window.lunaStartup&&(window.lunaStartup.timestamps.decompressionFinished=performance.now()),window._compressedAssets=null,window.unbrotli=null;for(const e of window._freeWorkers)e.terminate();window._freeWorkers=null,window._workerWaitingList=null,URL.revokeObjectURL(window._workerBlobUrl),window._workerBlobUrl=null,window.sharedBase122Buffer=null,window.dispatchEvent(new Event("luna:build"))})).catch((e=>console.error(e)))}))'
        strTarget8 = r'!function(){var n=!1;window.audioVolumeToggle=function(e){e!==n&&(n=e,e?(Luna.Unity.LifeCycle.OnMute(),window.app.app.muteAudio()):(Luna.Unity.LifeCycle.OnUnmute(),window.app.app.unmuteAudio()),window.app&&window.app.AudioManager&&window.app.AudioManager.TriggerMasterVolumeChange(n?0:1))},window.addEventListener("luna:unmute",(function(){window.audioVolumeToggle(!1)})),window.addEventListener("luna:mute",(function(){window.audioVolumeToggle(!0)})),window.addEventListener("luna:pause",(function(){window.app&&window.app.app&&(Luna.Unity.LifeCycle.OnPause(),window.app.app.pause())})),window.addEventListener("luna:resume",(function(){window.app&&window.app.app&&(Luna.Unity.LifeCycle.OnResume(),window.app.app.resume())}))}() '


# solution1 - Delete
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text
            if re.search(mystring1, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution1.1 Match !====")
                script.extract()
            else:
                print("Solution1.1 Not Match !")  
# solution1 - Delete
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(mystring2, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution1.2 Match !====")
                script.extract()
            else:
                print("Solution1.2 Not Match !")  
# solution1 - Delete
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(mystring3, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution1.3 Match !====")
                script.extract()
            else:
                print("Solution1.3 Not Match !")  

# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC0, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.1 Match !====")
                script.string = strTarget0
            else:
                print("Solution3.1 Not Match !")

# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC1, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.2 Match !====")
                script.string = strTarget1
            else:
                print("Solution3.2 Not Match !")

# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC5, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.3 Match !====")
                script.string = strTarget5
            else:
                print("Solution3.3 Not Match !")

# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC6, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.4 Match !====")
                script.string = strTarget6
            else:
                print("Solution3.4 Not Match !")
# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC8, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.6 Match !====")
                script.string = strTarget8
            else:
                print("Solution3.6 Not Match !")


# solution4 - Add some scripts
        for script in scripts:
            script_content = script.text.strip()
            if re.search(stringPLC2, script_content):
                new_script = soup.new_tag("script")
                new_script["src"] = strTarget2
                new_script["defer"] = ""
                script.insert_after(new_script)
                print("Solution4.1 Match !====")
            else:
                print("Solution4.1 Not Match !")
# solution4 - Add some scripts
        for script in scripts:
            script_content = script.text.strip()
            if re.search(stringPLC3, script_content):
                new_script = soup.new_tag("script")
                new_script["src"] = strTarget3
                new_script["defer"] = ""
                script.insert_after(new_script)
                print("Solution4.2 Match !====")
            else:
                print("Solution4.2 Not Match !")
# solution4 - Add some scripts
        for script in scripts:
            script_content = script.text.strip()
            if re.search(stringPLC4, script_content):
                new_script = soup.new_tag("script")
                new_script["src"] = strTarget4
                new_script["defer"] = ""
                script.insert_after(new_script)
                print("Solution4.3 Match !====")
            else:
                print("Solution4.3 Not Match !")                

# solution3 - Replace same scripts
        for script in scripts:
            # Lấy nội dung của thẻ script
            script_content = script.text.strip()
            if re.search(stringPLC7, script_content):
            # Thay thế nội dung của thẻ script
                print("Solution3.5 Match !====")
                script.string = strTarget7
            else:
                print("Solution3.5 Not Match !")

    with open(html_target, "w") as f:
        # f.write(str(soup))
        f.write(str(soup.prettify()))


def reFixMetaTagMeta1(html_file_name):
    with open(html_file_name, "r") as f:
        html_content = f.read()
        mystring5 = r'<meta content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no" name="viewport"/>'
        mystring51 = r'<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">'    
        html_content1 = re.sub(mystring5, mystring51, html_content)
    with open(html_file_name, "w") as f:
        f.write(str(html_content1))

def reFixMetaTagMeta2(html_file_name):
    with open(html_file_name, "r") as f:
        html_content = f.read()
        mystring4 = r'<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>' 
        mystring41 = r'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
        html_content1 = re.sub(mystring4, mystring41, html_content)
    with open(html_file_name, "w") as f:
        f.write(str(html_content1))


def makeAdsFolder():
    if(not os.path.isdir(GlobalVarible.targetPath_Now + '/Mintengal')):
        os.mkdir(GlobalVarible.targetPath_Now + '/Mintengal')
        print('Tao thanh con thu muc Mintengal')


def readJsAsset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    # Bước 2: Tìm vị trí bắt đầu của đoạn code cần sao chép
    start_code = 'window.sounds = window.sounds || {}; window._compressedAssets = window._compressedAssets || [];window._compressedAssets.push'
    start_index = None
    for index, line in enumerate(content):
        if start_code in line:
            start_index = index
            break
    # Kiểm tra nếu tìm thấy vị trí bắt đầu
    if start_index is not None:
        # Sao chép từ vị trí bắt đầu đến hết file
        content_to_copy = ''.join(content[start_index:])  # Kết hợp các dòng thành một chuỗi
        # Bước 3: Xóa nội dung từ đầu đến 'function():'
        content_to_copy = content_to_copy[content_to_copy.index(start_code):]
        # Bước 4: Dán nội dung đã sao chép vào cuối file
        content.append(content_to_copy)
        # Bước 5: Ghi lại nội dung đã cập nhật vào file JS
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(content)
        print("Đã sao chép và dán thành công!")
    else:
        print("Không tìm thấy đoạn code cần sao chép.")

def moveFolder(stockPath, targetPath):
    if os.path.exists(stockPath):
        # Bước 2: Sao chép thư mục
        shutil.copytree(stockPath, targetPath)
        print("Đã sao chép thư mục thành công!")
    else:
        print("Thư mục nguồn không tồn tại.")
        

def main():
    htmlPath = GlobalVarible.stockPath_Now + '/index.html'
    htmlPathAfterBuild = GlobalVarible.targetPath_Now + '/Mintengal/index.html'
    file_path_JS = GlobalVarible.stockPath_Now + '/assets/scripts.js'
    makeAdsFolder()
    simpleImSoLazy(htmlPath, htmlPathAfterBuild)
    reFixMetaTagMeta1(htmlPathAfterBuild)
    reFixMetaTagMeta2(htmlPathAfterBuild)

    readJsAsset(file_path_JS) # modyfi js file
    moveFolder(GlobalVarible.stockPath_Now + '/assets', GlobalVarible.targetPath_Now + '/Mintengal/assets')
    
    os.startfile(GlobalVarible.targetPath_Now + '/Mintengal')
    

# if __name__ == "__main__":
#   main()


# os.system("pause")