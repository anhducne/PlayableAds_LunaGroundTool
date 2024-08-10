import re
import os
from bs4 import BeautifulSoup
from Root.Utility import GlobalVarible


# if(not os.path.isdir('Applovin')):
#     os.mkdir(GlobalVarible.targetPath_Now + 'Applovin')
#     print('Tao thanh con thu muc Applovin')

# RootDir = os.getcwd()
# print(RootDir)

# htmlPath = RootDir + '/00PutFileIndexHere/index.html'
# htmlPathAfterBuild = RootDir + '/Applovin/index.html'


# ////////////////////////////////////////////////////////////////////////////ENDSolutionIDEA//////////////////////////////////////////////////////////////////////////////////////////
def simpleImSoLazy(html_file_name, html_target):
    with open(html_file_name, "r") as f:
        html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")

        scripts = soup.find_all("script")

        stringPLC0 = r'resourceConfig'  #ok
        stringPLC1 = r'window.pi.apply' #ok
        stringPLC5 = r'dapi.removeEventListener'
        stringPLC8 = r'NUC is not defined'
        stringPLC9 = r'NUC is not defined'

        # Ket quả cần thay đổi 
        strTarget0 = r'window.$environment={baseUrl:"./",resourceConfig:{json:"inline",image:"inline",video:"inline",sound:"compress",blob:"compress"},packageConfig:Object.assign({inlineScripts:!0,inlineJsons:!0,inlineBlobs:!0,inlineImages:!0,inlineSounds:!0,inlineVideos:!0,applicationName:"",iosLink:"",androidLink:"https://play.google.com/store/apps/details?id=com.ps.badmoms.good.mom.momrun",orientation:"unspecified",languages:["en","en"]},window.LUNA_PLAYGROUND_PACKAGE_CONFIG||{}),playerPrefs:!0,usingWebWorkers:"off",targetPlatform:"applovin",runtimeAnalysisModules:["physics3d","physics2d","particle_system","reflection","prefabs","mecanim-wasm"]}'
        strTarget1 = r'window.pi.apply(window,["applovin",123144,5159547,"d0cf3fa323b7c27f70113bc27beb7c964187cda86bb860e071da1c5edd071c47","https://collector.lunalabs.io/api/v1/stats/collect",null,3000,500,null,"https://collector.lunalabs.io/api/v1/stats/errors/collect"]||[])'

        strTarget5 = r'!function(){var n=!1,e=!1;function t(){return mraid.isViewable()&&"hidden"!==mraid.getState()}function a(){n?t()&&e?(window.dispatchEvent(new Event("luna:resume")),e=!1):t()||e||(window.dispatchEvent(new Event("luna:pause")),e=!0):t()&&(window.dispatchEvent(new Event("luna:start")),n=!0)}function i(){}function d(n){window.dispatchEvent(new Event(n?"luna:unsafe:unmute":"luna:unsafe:mute"))}var r=function(){"undefined"!=typeof mraid?(mraid.removeEventListener("ready",r),mraid.addEventListener("viewableChange",a),mraid.addEventListener("stateChange",a),mraid.addEventListener("orientationchange",i),mraid.addEventListener("audioVolumeChange",d),console.log("a legend who was here, Hanoi_27/02/2024, sign: DucBee, fb: https://www.facebook.com/toilachogaugaugau") ,a()):window.dispatchEvent(new Event("luna:start"))};window.addEventListener("luna:build",(function(){window.pi.logLoaded(),"undefined"!=typeof mraid?"loading"===mraid.getState()?mraid.addEventListener("ready",r):r():window.dispatchEvent(new Event("luna:start"))}))}()'
        
        # strTarget5 = r'!function(){var n=!1,e=!1;function t(){return mraid.isViewable()&&"hidden"!==mraid.getState()}function a(){n?t()&&e?(window.dispatchEvent(new Event("luna:resume")),e=!1):t()||e||(window.dispatchEvent(new Event("luna:pause")),e=!0):t()&&(window.dispatchEvent(new Event("luna:start")),n=!0)}function i(){}function d(n){window.dispatchEvent(new Event(n?"luna:unsafe:unmute":"luna:unsafe:mute"))}var r=function(){"undefined"!=typeof mraid?(mraid.removeEventListener("ready",r),mraid.addEventListener("viewableChange",a),mraid.addEventListener("stateChange",a),mraid.addEventListener("orientationchange",i),mraid.addEventListener("audioVolumeChange",d),a()):window.dispatchEvent(new Event("luna:start"))};window.addEventListener("luna:build",(function(){window.pi.logLoaded(),"undefined"!=typeof mraid?"loading"===mraid.getState()?mraid.addEventListener("ready",r):r():window.dispatchEvent(new Event("luna:start"))}))}()'


        strTarget8 = r'window.addEventListener("luna:build",(function(){Bridge.ready((function(){Luna.Unity.Playable.InstallFullGame=function(n,i){window.pi.logCta(),n=n||window.$environment.packageConfig.iosLink,i=i||window.$environment.packageConfig.androidLink;const o=/iphone|ipad|ipod|macintosh/i.test(window.navigator.userAgent.toLowerCase())?n:i;"undefined"!=typeof mraid?mraid.open(o):(console.warn("Mraid is not defined"),window.open(o,"_blank"))}}))}))'
        strTarget9 = r'!function(){let e=window.innerWidth,n=window.innerHeight;window.addEventListener("resize",(()=>{e=window.innerWidth,n=window.innerHeight})),setInterval((()=>{e===window.innerWidth&&n===window.innerHeight||window.dispatchEvent(new Event("resize"))}),300)}(),window.addEventListener("luna:starting",(()=>{window.audioVolumeToggle(!0)})),window.addEventListener("luna:started",(()=>{const e=function(){document.body.removeEventListener("mousemove",e),document.body.removeEventListener("scroll",e),document.body.removeEventListener("keydown",e),document.body.removeEventListener("click",e),document.body.removeEventListener("touchstart",e),document.body.removeEventListener("pointerdown",e),window.dispatchEvent(new Event("luna:unsafe:unmute"))};document.body.addEventListener("mousemove",e),document.body.addEventListener("scroll",e),document.body.addEventListener("keydown",e),document.body.addEventListener("click",e),document.body.addEventListener("touchstart",e),document.body.addEventListener("pointerdown",e)}))'

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

# solution4 - Add some scripts
        for script in scripts:
            script_content = script.text.strip()
            if re.search(stringPLC9, script_content):
                new_script = soup.new_tag("script")
                new_script.string = strTarget9
                script.insert_after(new_script)
                print("Solution4.4 Match !====")
            else:
                print("Solution4.4 Not Match !")

 
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
    if(not os.path.isdir(GlobalVarible.targetPath_Now + '/Applovin')):
        os.mkdir(GlobalVarible.targetPath_Now + '/Applovin')
        print('Tao thanh con thu muc Applovin')

def main():
    htmlPath = GlobalVarible.stockPath_Now + '/index.html'
    htmlPathAfterBuild = GlobalVarible.targetPath_Now + '/Applovin/index.html'
    makeAdsFolder()
    simpleImSoLazy(htmlPath, htmlPathAfterBuild)
    reFixMetaTagMeta1(htmlPathAfterBuild)
    reFixMetaTagMeta2(htmlPathAfterBuild)
    os.startfile(GlobalVarible.targetPath_Now + '/Applovin')


# if __name__ == "__main__":
#   main()



# os.system("pause")