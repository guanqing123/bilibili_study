# coding:utf-8
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import wx


class YsjClient(wx.Frame):
    def __init__(self, client_name):
        # 调用父类的初始化方法
        # None: 没有父级窗口
        # id: 表示当前窗口的一个编号
        # pos: 窗体的打开位置
        # size: 窗体的大小, 单位是像素, 400宽,450高
        wx.Frame.__init__(self, None, id=1001, title=client_name + '的客户端界面', pos=wx.DefaultPosition,
                          size=wx.Size(400, 450))
        # 创建面板对象
        panel = wx.Panel(self)
        # 在面板中放上盒子
        box = wx.BoxSizer(wx.VERTICAL)  # 垂直方向布局
        # 可伸缩的网格布局
        grid = wx.FlexGridSizer(wx.HSCROLL)  # 水平方法布局

        # 创建两个按钮
        con_btn = wx.Button(panel, size=wx.Size(200, 40), label='连接')
        dis_con_btn = wx.Button(panel, size=wx.Size(200, 40), label='断开')

        # 把两个按钮放到可伸缩的网格布局中
        grid.Add(con_btn, 1, wx.TOP | wx.LEFT)
        grid.Add(dis_con_btn, 1, wx.TOP | wx.RIGHT)
        # (可伸缩的网格布局)添加到box中
        box.Add(grid, 1, wx.ALIGN_CENTRE)

        # 只读文本框,显示聊天内容 (TE_MULTILINE:多行,TE_READONLY:只读)
        self.show_text = wx.TextCtrl(panel, size=wx.Size(400, 210), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTRE)

        # 创建聊天内容的文本框
        self.chat_text = wx.TextCtrl(panel, size=wx.Size(400, 120), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.chat_text, 1, wx.ALIGN_CENTRE)

        # 可伸缩的网格布局
        grid2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方法布局
        # 创建两个按钮
        reset_btn = wx.Button(panel, size=wx.Size(200, 40), label='重置')
        send_btn = wx.Button(panel, size=wx.Size(200, 40), label='发送')
        grid2.Add(reset_btn, 1, wx.TOP | wx.LEFT)
        grid2.Add(send_btn, 1, wx.TOP | wx.RIGHT)

        box.Add(grid2, 1, wx.ALIGN_CENTRE)
        # 将盒子放到面板中
        panel.SetSizer(box)

        '''--------------------以上代码是客户端界面的绘制--------------------'''
        self.Bind(wx.EVT_BUTTON, self.connect_to_server, con_btn)
        # 实例属性的设置
        self.client_name = client_name
        self.isConnected = False  # 存储客户端连接服务器的状态,默认为False,没连
        self.client_socket = None  # 设置客户端的socket对象为空

    def connect_to_server(self, event):
        print(f'客户端{self.client_name}连接服务器成功')
        # 如果客户端没有连接服务器,则开始连接
        if not self.isConnected:  # 等价于 self.isConnected == False:
            # TCP编程的步骤
            server_host_port = ('127.0.0.1', 8888)
            # 创建socket对象
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            # 发送连接请求
            self.client_socket.connect(server_host_port)
            # 只要连接成功,发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))
            # 启动一个线程,客户端的线程与服务器的会话线程进行会话
            client_thread = Thread(target=self.recv_data)
            # 设置成守护线程，窗体关掉，子线程也结束了
            client_thread.daemon = True
            # 修改一下连接状态
            self.isConnected = True
            # 启动线程
            client_thread.start()

    def recv_data(self):
        pass


if __name__ == '__main__':
    # 初始化App()
    app = wx.App()
    # 创建自己的客户端界面对象
    client = YsjClient('Python娟子姐')
    client.Show()  # 可以改成 YsjClient('Python娟子姐').Show()

    # 循环刷新显示
    app.MainLoop()
