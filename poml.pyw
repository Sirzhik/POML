import os

from tkinter import *

w = 400
h = 100
server = '' #server IP

try:
    nick_file = open('C:/nick.txt', 'r')
    nick_file.close()
except FileNotFoundError:
    file_f = open('C:/nick.txt', 'w')
    file_f.write('')
    file_f.close()
except PermissionError:
    pass

def _Win():
    _win = Tk()
    _win.geometry(f'{w}x{h}+100+110')
    _win.title('Launcher')
    _win["bg"] = "gray22"
    _win.resizable(False, False)
    _l = Label(_win, text='Username:',
                              font=('Arial', 15),
                              bg = 'gray20',
                                     fg = 'green')
    _l.grid(row=0, column=0)
    _e = Entry(_win)
    _e.grid(row=0, column=1)
    _b = Button(_win, text='Start', command=lambda:saveNick(_e.get(), _win),
                              font=('Arial', 15),
                              bg = 'green',
                              activebackground = 'red',
                              fg = 'white')
    _b.grid(row=1, column=0)
    _win.mainloop()

def saveNick(nick, _):
    _.destroy()
    _nick = open('C:/nick.txt', 'w')
    _nick.write(nick)
    _nick.close()
    runWin(nick)
    
def runWin(nick):
    win = Tk()
    win.geometry(f'{w}x{h}+100+110')
    win.title('Launcher')
    win["bg"] = "gray22"
    win.resizable(False, False)

    def start():
        os.system(fr'"%AppData%\.minecraft\runtime\jre-legacy\windows\jre-legacy\bin\javaw.exe -Dos.name="Windows 10" -Dos.version=10.0 -Djava.library.path="%AppData%\.minecraft\versions\ForgeOptiFine 1.12.2\natives" -cp "%AppData%\.minecraft\libraries\net\minecraftforge\forge\1.12.2-14.23.5.2860\forge-1.12.2-14.23.5.2860.jar;%AppData%\.minecraft\libraries\org\ow2\asm\asm-debug-all\5.2\asm-debug-all-5.2.jar;%AppData%\.minecraft\libraries\net\minecraft\launchwrapper\1.12\launchwrapper-1.12.jar;%AppData%\.minecraft\libraries\org\jline\jline\3.5.1\jline-3.5.1.jar;%AppData%\.minecraft\libraries\com\typesafe\akka\akka-actor_2.11\2.3.3\akka-actor_2.11-2.3.3.jar;%AppData%\.minecraft\libraries\com\typesafe\config\1.2.1\config-1.2.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-actors-migration_2.11\1.1.0\scala-actors-migration_2.11-1.1.0.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-compiler\2.11.1\scala-compiler-2.11.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\plugins\scala-continuations-library_2.11\1.0.2_mc\scala-continuations-library_2.11-1.0.2_mc.jar;%AppData%\.minecraft\libraries\org\scala-lang\plugins\scala-continuations-plugin_2.11.1\1.0.2_mc\scala-continuations-plugin_2.11.1-1.0.2_mc.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-library\2.11.1\scala-library-2.11.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-parser-combinators_2.11\1.0.1\scala-parser-combinators_2.11-1.0.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-reflect\2.11.1\scala-reflect-2.11.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-swing_2.11\1.0.1\scala-swing_2.11-1.0.1.jar;%AppData%\.minecraft\libraries\org\scala-lang\scala-xml_2.11\1.0.2\scala-xml_2.11-1.0.2.jar;%AppData%\.minecraft\libraries\lzma\lzma\0.0.1\lzma-0.0.1.jar;%AppData%\.minecraft\libraries\java3d\vecmath\1.5.2\vecmath-1.5.2.jar;%AppData%\.minecraft\libraries\net\sf\trove4j\trove4j\3.0.3\trove4j-3.0.3.jar;%AppData%\.minecraft\libraries\org\apache\maven\maven-artifact\3.5.3\maven-artifact-3.5.3.jar;%AppData%\.minecraft\libraries\net\sf\jopt-simple\jopt-simple\5.0.3\jopt-simple-5.0.3.jar;%AppData%\.minecraft\libraries\org\apache\logging\log4j\log4j-api\2.15.0\log4j-api-2.15.0.jar;%AppData%\.minecraft\libraries\org\apache\logging\log4j\log4j-core\2.15.0\log4j-core-2.15.0.jar;%AppData%\.minecraft\libraries\org\tlauncher\patchy\1.3.9\patchy-1.3.9.jar;%AppData%\.minecraft\libraries\oshi-project\oshi-core\1.1\oshi-core-1.1.jar;%AppData%\.minecraft\libraries\net\java\dev\jna\jna\4.4.0\jna-4.4.0.jar;%AppData%\.minecraft\libraries\net\java\dev\jna\platform\3.4.0\platform-3.4.0.jar;%AppData%\.minecraft\libraries\com\ibm\icu\icu4j-core-mojang\51.2\icu4j-core-mojang-51.2.jar;%AppData%\.minecraft\libraries\net\sf\jopt-simple\jopt-simple\5.0.3\jopt-simple-5.0.3.jar;%AppData%\.minecraft\libraries\com\paulscode\codecjorbis\20101023\codecjorbis-20101023.jar;%AppData%\.minecraft\libraries\com\paulscode\codecwav\20101023\codecwav-20101023.jar;%AppData%\.minecraft\libraries\com\paulscode\libraryjavasound\20101123\libraryjavasound-20101123.jar;%AppData%\.minecraft\libraries\com\paulscode\librarylwjglopenal\20100824\librarylwjglopenal-20100824.jar;%AppData%\.minecraft\libraries\com\paulscode\soundsystem\20120107\soundsystem-20120107.jar;%AppData%\.minecraft\libraries\io\netty\netty-all\4.1.9.Final\netty-all-4.1.9.Final.jar;%AppData%\.minecraft\libraries\com\google\guava\guava\21.0\guava-21.0.jar;%AppData%\.minecraft\libraries\org\apache\commons\commons-lang3\3.5\commons-lang3-3.5.jar;%AppData%\.minecraft\libraries\commons-io\commons-io\2.5\commons-io-2.5.jar;%AppData%\.minecraft\libraries\commons-codec\commons-codec\1.10\commons-codec-1.10.jar;%AppData%\.minecraft\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;%AppData%\.minecraft\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0.jar;%AppData%\.minecraft\libraries\com\google\code\gson\gson\2.8.0\gson-2.8.0.jar;%AppData%\.minecraft\libraries\org\tlauncher\authlib\1.6.251\authlib-1.6.251.jar;%AppData%\.minecraft\libraries\com\mojang\realms\1.10.22\realms-1.10.22.jar;%AppData%\.minecraft\libraries\org\apache\commons\commons-compress\1.8.1\commons-compress-1.8.1.jar;%AppData%\.minecraft\libraries\org\apache\httpcomponents\httpclient\4.3.3\httpclient-4.3.3.jar;%AppData%\.minecraft\libraries\commons-logging\commons-logging\1.1.3\commons-logging-1.1.3.jar;%AppData%\.minecraft\libraries\org\apache\httpcomponents\httpcore\4.3.2\httpcore-4.3.2.jar;%AppData%\.minecraft\libraries\it\unimi\dsi\fastutil\7.1.0\fastutil-7.1.0.jar;%AppData%\.minecraft\libraries\org\apache\logging\log4j\log4j-api\2.8.1\log4j-api-2.8.1.jar;%AppData%\.minecraft\libraries\org\apache\logging\log4j\log4j-core\2.8.1\log4j-core-2.8.1.jar;%AppData%\.minecraft\libraries\org\lwjgl\lwjgl\lwjgl\2.9.4-nightly-20150209\lwjgl-2.9.4-nightly-20150209.jar;%AppData%\.minecraft\libraries\org\lwjgl\lwjgl\lwjgl_util\2.9.4-nightly-20150209\lwjgl_util-2.9.4-nightly-20150209.jar;%AppData%\.minecraft\libraries\com\mojang\text2speech\1.10.3\text2speech-1.10.3.jar;%AppData%\.minecraft\versions\ForgeOptiFine 1.12.2\ForgeOptiFine 1.12.2.jar" -Xmx3000M -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.net.preferIPv4Stack=true -Dminecraft.applet.TargetDirectory="%AppData%\.minecraft" -Dlog4j.configurationFile="%AppData%\.minecraft\assets\log_configs\client-1.12.xml" net.minecraft.launchwrapper.Launch --username {nick} --version "ForgeOptiFine 1.12.2" --gameDir "%AppData%\.minecraft" --assetsDir "%AppData%\.minecraft\assets" --assetIndex 1.12 --accessToken null --userType mojang --tweakClass net.minecraftforge.fml.common.launcher.FMLTweaker --versionType Forge --width 925 --height 530 --server {server}"')
        win.destroy()
    
    l = Label(win, text='Python Open Minecraft Launcher',
    bg = 'gray22',
    fg = 'white',
    font=('Arial', 15))
    l.pack()
    btn_start = Button(win, text='Play', command=start,
                  font=('Arial', 15),
                  bg = 'green',
                  activebackground = 'red',
                  fg = 'white')
    btn_start.pack()
    win.mainloop()

if os.path.getsize('C:/nick.txt') == 0:
        _Win()
else:
    fNick = open('C:/nick.txt', 'r')
    runWin(fNick.read())

