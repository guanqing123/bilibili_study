"""
    第三方库Pyinstaller可以在Windows操作系统中将Python源文件打包成.exe的可执行文件.
    还可以在Linux和Mac OS操作系统中对源文件进行打包操作.
    打包的语法结构为:
        pyinstaller -F 源文件文件名
        pyinstaller --icon=C:\python\music.ico -F music.py

        在 Windows 上，文件路径中的反斜杠 \ 需要进行转义，或使用正斜杠 /。例如：
        icon='C:\\path\\to\\your_icon.ico'
        # 或
        icon='C:/path/to/your_icon.ico'

        pyinstaller your_script.spec

        pyinstaller --hidden-import=requests music.py
"""