# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/15 21:55

"""主程序"""
import os.path

from utilis.pagination import Pagination
from flask import Flask, render_template, request, flash, redirect, url_for
import pymysql
import traceback

app = Flask(__name__)
app.secret_key = 'secret key'


def show():
    """展示数据库中的文件"""
    db = pymysql.connect(host='localhost', port=3306, user='root', password="20040616wldnrr", db='networkprogramming')
    cursor = db.cursor()
    sql = 'select * from files'
    cursor.execute(sql)
    results = cursor.fetchall()
    items = []
    for result in results:
        item = []
        for i in range(len(result)):
            if i == 2:
                path = result[2].split(os.path.sep)
                path = os.path.join("./static/", path[-3], path[-2], path[-1])
                a = os.path.join(path)
                item.append(a)
            else:
                item.append(result[i])
        items.append(item)
    number = len(items)
    db.commit()
    db.close()
    return items, number


def store(name, type, path):
    """数据存储到数据库"""
    db = pymysql.connect(host='localhost', port=3306, user='root', password="20040616wldnrr", db='networkprogramming')
    cursor = db.cursor()
    sql = 'insert into files(filename,filetype,filepath) values(%s,%s,%s)'
    data = (name, type, path)
    cursor.execute(sql, data)
    db.commit()
    db.close()


@app.route('/', methods=["GET", "POST"])
def index():
    # 获取提交的账号密码
    count = request.form.get('count')
    pwd = request.form.get('pwd')
    # 连接数据库
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', password="20040616wldnrr", db='networkprogramming')
        cursor = db.cursor()
        sql = 'select * from users'
        cursor.execute(sql)
        result = cursor.fetchall()
        # 登录验证
        flag = False
        for info in result:
            if count == info[0] and pwd == info[1]:
                flag = True
                break
        if flag:
            print("登录成功!")
            db.commit()
            return redirect(url_for("upload"))
        else:
            print("登录失败!")
            return render_template("login.html")
    except pymysql.Error as e:
        print(f"发生错误:{str(e)}")
        traceback.print_exc()
        db.rollback()
        db.close()
        return render_template('login.html', msg='数据库连接失败!请重新登录')


@app.route("/upload", methods=['POST', "GET"])
def upload():
    results, number = show()
    li = []
    for i in range(1, number + 1):
        li.append(i)
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args,
                           per_page_count=10)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('uplode.html', results=results, index_list=index_list, html=html)


@app.route('/process', methods=['POST'])
def process():
    # 接收上传来的文件并保存
    if request.method == 'POST':
        img = request.files['img']
        if img:
            img_name = img.filename  # 接收图片名称
            img_type = img_name.split('.')[-1]  # 图片类型
            img_path = os.path.join(r'E:\PycharmProjects\Web项目\ComputerNetworkProgramming\app\static\store\img',
                                    img_name)
            store(img_name, img_type, img_path)  # 存到数据库
            img.save(img_path)
            print(f'{img_name}已保存至数据库!')
    if request.method == 'POST':
        video = request.files['video']
        if video:
            video_name = video.filename  # 接收图片名称
            video_type = video_name.split('.')[-1]
            video_path = os.path.join(r'E:\PycharmProjects\Web项目\ComputerNetworkProgramming\app\static\store\video',
                                      video_name)
            store(video_name, video_type, video_path)
            video.save(video_path)
            print(f"{video_name}已保存至数据库!")
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_name = file.filename  # 接收图片名称
            file_type = file_name.split('.')[-1]
            file_path = os.path.join(r'E:\PycharmProjects\Web项目\ComputerNetworkProgramming\app\static\store\file',
                                     file_name)
            store(file_name, file_type, file_path)
            file.save(file_path)
            print(file_name)

    return '成功上传!'
    # 启动服务器
    # Server = Receiver()
    # Server.start()
    # # 启动客户端
    # Client = SendMessage()


if __name__ == '__main__':
    app.run(debug=True)
