# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2022/12/15 21:55

"""主程序"""
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='templates')


@app.route("/")
def index():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    count = request.form.get('count')
    name = request.form.get('pwd')
    if count == 'wjr' and name == '0106':
        return "登录成功"
    else:
        return render_template('login.html', msg='登录失败')


if __name__ == '__main__':
    app.run(debug=True)
