# # pip install pywin32
# # import akshare
# from win32api import *  #windows应用程序接口
# from win32gui import *  #windows图形界面接口
# from win32con import *  #windows控制接口
# from time import sleep  #延时!
#
# qq_wnd = FindWindow('TXGuiFoundation', 'QQ') #晚上好 Have data nice day!
#
# while True
#     SetForegroundWindow(qq_wnd)
#
#     #打开一个分组
#     # TAB           #进入联系人
#     # TAB           #进入好友/群聊
#     kebd_event(VK_TAB, 0, 0, 0)
#     sleep(0.03)
#     kebd_event(VK_TAB, 0, 2, 0)
#     sleep(0.03)
#     kebd_event(VK_TAB, 0, 0, 0)
#     sleep(0.03)
#     kebd_event(VK_TAB, 0, 2, 0)
#     sleep(0.03)
#
#
#     # DOWN RETURN   #一直按 直到打开一个对话框
#     while True:
#         keybd_event(VK_DOWN,0,0,0)
#         sleep(0.03)
#         keybd_event(VK_DOWN,0,2,0)
#         sleep(0.03)
#         keybd_event(VK_RETURN,0,0,0)
#         sleep(0.03)
#         keybd_event(VK_RETURN,0,2,0)
#         sleep(0.03)
#         if GetForegroundWindow() != qq_wnd:
#             break
#
#     # CONTROL + V   #粘贴
#     kebd_event(VK_CONTROL, 0, 0, 0)
#     sleep(0.03)
#     kebd_event(ord('V'), 0, 0, 0)
#     sleep(0.03)
#     kebd_event(ord('V'), 0, 2, 0)
#     sleep(0.03)
#     kebd_event(VK_CONTROL, 0, 2, 0)
#     sleep(0.03)
#
#     # RETURN        #发送
#     kebd_event(VK_RETURN, 0, 0, 0)
#     sleep(0.03)
#     kebd_event(VK_RETURN, 0, 2, 0)
#     sleep(0.03)
#     # ESC           #关闭对话框
#     kebd_event(VK_ESCAPE, 0, 0, 0)
#     sleep(0.03)
#     kebd_event(VK_ESCAPE, 0, 2, 0)
#     sleep(0.03)
#
#
#
# # 窗口识别 Microsoft Spy++
# # 多少窗口 窗口ID/窗口句柄
# windId = FindWindow('TXGuiFoundation', 'QQ') #'QQ'->'何奇'
# print(windId)
#
# #置顶窗口
# SetForegroundWindow(windId)
# #获取最前的窗口ID
# id = GetForegroundWindow()
#
#
# #发送（给窗口）消息（指令）
# for i in range(500):
#     SendMessage(windId, WM_PASTE, 0,0) #你吃饭了吗？
#     SendMessage(windId, WM_KEYDOWN, VK_RETURN,0) #回车发送
#
#
# # 按键模拟 键盘事件
# keybd_event()
#
# #按下一个TAB
# kebd_event(VK_TAB, 0, 0, 0) # TAB按下去
# sleep(0.05)
# kebd_event(VK_TAB, 0, 2, 0) # TAB弹起来
# sleep(0.05)
# keybd_event(ord('C'), 0, 0, 0)
# sleep(0.05)
# keybd_event(ord('C'), 0, 2, 0)
# sleep(0.05)
#
# # shift + A
# # ctrl + C
# kebd_event(VK_CONTROL, 0, 0, 0)
# sleep(0.02)
# kebd_event(ord('C'), 0, 0, 0)
# sleep(0.02)
# kebd_event(ord('C'), 0, 2, 0)
# sleep(0.02)
# kebd_event(VK_CONTROL, 0, 2, 0)
# sleep(0.02)
#
#
# #按键模拟 控制什么按键！
# #1、控制同一个程序 正常写就可以了！
# #2、一定要加时间间隔!
#
#
# # 模拟按键！
# # 需要4个参数！
# # 1、你要模拟什么键？功能键：VK_TAB VK_SPACE VK_RETURN VK_SHIFT VK_CONTROL VK_MENU
# #    数字键+字母键 ord('1') ord('D') shift + 5 = %
# # 2、0  不要管
# # 3、你要模拟按下还是弹起。按下去0 弹起来2
# # 4、0 不要管
#
#
# # 鼠标模拟
# SetCursorPos((1663,65))
# mouse_event(MOUSEEVENTF_LEFTDOWN, 1663, 65, 0, 0)
# mouse_event(MOUSEEVENTF_LEFTUP, 1663, 65, 0, 0)
