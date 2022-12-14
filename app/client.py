# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/13 13:46

"""客户端"""

import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECTED = 'DISCONNECTED!'
PORT = 5050
SERVER = '192.168.2.132'  # 要连接的服务器的ip地址
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)  # 客户端连接服务端


def send(msg):
    """
    发送数据
    :param msg:
    :return:
    """
    message = msg.encode(FORMAT)  # 对发送的数据按照服务器解码的格式进行编码
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)  # 首部数据(二进制)
    send_length += b' ' * (HEADER - len(send_length))  # 对首部数据填充为64字节(对应服务器接受时的要求)
    client.send(send_length)  # 发送首部数据
    client.send(message)  # 发送数据部分

    # 客户端打印收到回复的消息
    recv_mag = client.recv(HEADER).decode(FORMAT)
    if recv_mag:
        print(client.recv(len(recv_mag)).decode(FORMAT))


text = """
    当你看到这封情书时，可以告诉你的是，我已经喜欢你很久了。至于为什么喜欢你，这个问题我沉思了很久，最终我也想不清楚。

　　回想我是从什么时候开始喜欢你的呢？

　　也许是那一刻你的回眸一笑，也许是与你擦身而过时无意间嗅到的你的芳香，也许是你优雅且淑女的气质，也许就是那一刻的心动，于是，我便喜欢上你了。

　　请原谅我的表白来得晚一些，但总算是没有迟到，当我经过越来越多的痛楚，那一次次的思念，我知道，我已经爱你爱得无法自控了。

　　“夜很深了，此刻的你还好吗？总似有千言万语，又不知从何说起，心里好想你！今夜有梦吗？”

　　多少个夜晚，望着天际的星星，默默想着远方的某人某事，多少个夜晚，手拿着一支笔想为你写点什么，淡淡的苦涩，反而成为了清醒头脑的一种动力。年轻的天空永远美丽，隐没的故事重现脑际，多少有些无言，多少有些惆怅，喜欢你的笑容，喜欢静静地看着你。只要见到你，我那美好的青春就在心中奋发。

　　我想告诉你：我爱你。就像一位诗人说的，明月装饰了你的窗，而你装饰了我的梦。悄然间，你已经成为了我心灵里一道靓丽的风景，一生中不可或缺的旅伴。

　　有的人喜欢海誓山盟的惊心动魄，有的人喜欢王子公主般的浪漫童话。而我只愿和你拥有那执子之手，与子偕老的恬淡幸福。愿得一心人，白首不相离。

　　可我知道，你喜欢浪漫，喜欢我在朦胧的月光下拉着你的手在湖边漫步，或者是坐在柳树下的长椅诉说着对你的爱，向自然界的万物证明我爱你是爱得那样的深沉、热烈。在生活上，我们像是无话不说的知心好友，在工作上，我们像是并肩作战的同志。

　　只是，当你累了时，请回到我身边。我会为你抚平心中的创伤，把你紧紧地抱在怀里、吻你，而我的肩膀也永远是你最温暖的港湾。我爱你，所以才会想给你一个承诺。也许某天事情太多忽视了你，请原谅我的粗心大意，也请你知道，在我心中那最温暖的角落，你一直在。

　　我爱你，所以珍惜你，所以会在意，所以会说你傻，所以会为你的错误发脾气。可是有时我也只是个男生，会犯傻，会误解，会错过，请包容我那颗偶尔会幼稚的心。

　　我爱你，所以会不自觉的关心你，请忽略我关心你的借口，我们是好朋友，这只是我的敷衍。爱你，所以会知道你喜欢酸酸甜甜的味道；爱你，所以会在你需要时出现；爱你，于是我的电话对你永远没有不在服务区，也正是因为爱你，所以会在你身边默默做你最可信赖的人。

　　“一个依靠，一个拥抱，为你祈祷，为你牵挂，缘份让我们走在一起，两颗心不再有隔阂。”

　　是否，你还记得那个日子，当我在舞台上唱着张国荣的《倩女幽魂》。那刻，你专注地看着我，然后致以我的鼓掌，那一刻，对于我来说，它已经定格为永恒。是否，你还记得那个日子，一个寒冷的冬天，我在图书馆复习，你递上的一杯温馨的豆浆。

　　如今，我想告诉你，我爱你。爱你的笑，爱你的哭，爱你的任性，爱你的撒娇，爱你的调皮，爱你的一切。请给我个机会，让我继续爱你，直到永远？
"""
send("111666")
send("DISCONNECTED!")
