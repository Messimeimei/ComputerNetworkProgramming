# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/13 13:23

"""服务器端"""
import socket
import os
import threading

HEADER = 64 # 指定接受的数据报的首部长度
FORMAT = 'utf-8'    # 数据解码的格式
DISCONNECTED = 'DISCONNECTED!'  # 当接受到这个消息时，服务器就断开连接
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    """
    处理客户端传来的数据报(由首部和数据部分两部分组成)
    :param conn: 与客户端建立的连接
    :param adrr: 建立的连接的信息，包括客户端的ip地址和端口
    :return:
    """
    print(f"[NEW CONNECTION]    {addr[0]}:{addr[1]} 已连接上服务器!")

    is_connected = True
    while is_connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # 有数据才执行下列操作
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED:
                is_connected = False
            print(f"[{addr[0]}:{addr[1]}]    发送的数据：{msg}")

            # 服务器回复收到
            recv_msg = '服务器已经收到消息!'
            byte_recv_msg = str(len(recv_msg)).encode(FORMAT)
            conn.send(byte_recv_msg + b' ' * (HEADER - len(byte_recv_msg))) # 先发送首部数据
            conn.send(recv_msg.encode(FORMAT))

    conn.close()    # 断开连接


def start():
    """启动服务器"""
    print(f"[LISTENING] 服务器正在 {SERVER} 上监听")

    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))   # 每一个客户端对应一个服务器的线程
        thread.start()

        # 进程数-1表示已连接的客户端个数，-1表示自身进程不算
        print(f"[CONNECTION NUMBER]    已连接客户端个数：{threading.activeCount() - 1}")


if __name__ == '__main__':
    print('[START]  服务器已启动...')
    start()

