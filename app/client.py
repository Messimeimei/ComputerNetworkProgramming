# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/13 13:46

"""客户端"""

import socket

client = socket.socket()


class SendMessage(object):
    """所有发送消息的基类"""

    def __init__(self):
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.client = client
        client.connect(self.ADDR)

    def send_txt(self, txt_path):
        """
        发送txt文本文件,步骤：
        1. 发送数据总长
        2. 发送文件数据
        3. 发送文件名
        :param txt_path:文本文件的路径
        """
        txt_name = txt_path.split('/')[-1]
        with open(txt_path, 'r', encoding=self.FORMAT) as f:
            content = f.read().encode(self.FORMAT)
        msg_length = str(len(content)).encode(self.FORMAT)  # 数据总长
        msg_length += b' ' * (self.HEADER - len(msg_length))
        self.client.send(msg_length)
        self.client.send(content)
        self.client.send(txt_name.encode(self.FORMAT))

    def send_img(self, img_path):
        """
        发送图片，步骤：
        1. 发送数据总长
        2. 发送图片数据
        3. 发送图片名
        :param img_path: 图片所在路径
        """
        imgname = img_path.split('/')[-1]
        with open(img_path, 'rb') as f:
            content = f.read()
        msg_length = str(len(content)).encode(self.FORMAT)  # 数据总长
        msg_length += b' ' * (self.HEADER - len(msg_length))
        self.client.send(msg_length)
        self.client.send(content)
        self.client.send(imgname.encode(self.FORMAT))

    def send_video(self, video_path):
        """
        发送视频，步骤：
        1. 发送数据总长
        2. 发送视频数据
        3. 发送视频名
        :param video_path: 视频所在路径
        """
        videoname = video_path.split('/')[-1]
        with open(video_path, 'rb') as f:
            content = f.read()
        msg_length = str(len(content)).encode(self.FORMAT)  # 数据总长
        msg_length += b' ' * (self.HEADER - len(msg_length))
        self.client.send(msg_length)
        self.client.send(content)
        self.client.send(videoname.encode(self.FORMAT))

if __name__ == '__main__':
    sender = SendMessage()
    sender.send_img('../test-files/莫德里奇.jpg')
    sender.send_txt('../test-files/xt.txt')
    sender.send_video('../test-files/mp4.mp4')