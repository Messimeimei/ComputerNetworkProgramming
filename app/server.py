# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/13 13:23

"""服务器端"""
import socket
import os
import threading

HEADER = 64 # 与客户端约定好的，第一条信息(会告知数据的总长)的长度
FORMAT = 'utf-8'    # 数据解码的格式
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_txt(conn, addr, store_path='../store'):
    """
    处理客户端传来的数据报(由首部和数据部分两部分组成)
    :param conn: 与客户端建立的连接
    :param adrr: 建立的连接的信息，包括客户端的ip地址和端口
    :param store_path: 写入本地文件夹的地址
    :return:
    """
    print(f"[TXT HANDLER]    {addr[0]}:{addr[1]} has already connected to the server!")

    msg_length = conn.recv(HEADER).decode(FORMAT)   # 接收数据的总长度,字符型
    # 有数据才执行下列操作
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)  # 接收文件数据
        # 写入本地文件夹中
        filename = conn.recv(HEADER).decode(FORMAT) # 接收文件名
        with open(os.path.join(store_path, filename), 'w', encoding='utf-8') as f:
            f.write(msg)

        print(f"[FILE_NAME] {filename}")
        print(f"[RECEIVED DATA] {msg}")

def handle_img(conn, addr, store_path='../store'):
    """
    处理客户端传来的数据报(由首部和数据部分两部分组成)
    :param conn: 与客户端建立的连接
    :param adrr: 建立的连接的信息，包括客户端的ip地址和端口
    :param store_path: 写入本地文件夹的地址
    :return:
    """
    print(f"[IMAGE HANDLER]    {addr[0]}:{addr[1]} has already connected to the server!")

    msg_length = conn.recv(HEADER).decode(FORMAT)   # 接收数据的总长度,字符型
    # 有数据才执行下列操作
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length)  # 接收文件数据
        # 写入本地文件夹中
        filename = conn.recv(HEADER).decode(FORMAT) # 接收文件名
        with open(os.path.join(store_path, filename), 'wb') as f:
            f.write(msg)

        print(f"[IMAGE_NAME] {filename}")

def handle_video(conn, addr, store_path='../store'):
    """
    处理客户端传来的数据报(由首部和数据部分两部分组成)
    :param conn: 与客户端建立的连接
    :param adrr: 建立的连接的信息，包括客户端的ip地址和端口
    :param store_path: 写入本地文件夹的地址
    :return:
    """
    print(f"[VIDEO HANDLER]    {addr[0]}:{addr[1]} has already connected to the server!")

    msg_length = conn.recv(HEADER).decode(FORMAT)   # 接收数据的总长度,字符型
    # 有数据才执行下列操作
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length)  # 接收文件数据
        # 写入本地文件夹中
        filename = conn.recv(HEADER).decode(FORMAT) # 接收文件名
        with open(os.path.join(store_path, filename), 'wb') as f:
            f.write(msg)

        print(f"[VIDEO_NAME] {filename}")


def start():
    """启动服务器"""
    print(f"[LISTENING] Listinging on {SERVER}")

    server.listen()
    while True:
        conn, addr = server.accept()
        handle_img(conn, addr)
        break
    while True:
        handle_txt(conn, addr)
        break
    while True:
        handle_video(conn, addr)
        break


if __name__ == '__main__':
    print('[START]  Server is running...')
    start()

