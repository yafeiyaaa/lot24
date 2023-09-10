from flask import Flask, render_template, request
from flask import redirect, url_for
from defs import *
app = Flask(__name__)
app.secret_key = b'e8896925b5cf99fbeae289fc187d047e391b536f8224e37a8859b64e6'

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('POST')
        # 处理用户点击事件
        button_index = request.form.get("button")
        deal_post(int(button_index))
       
    
    return render_template('game.html', session = session)


@app.route('/login_in', methods = ['GET', 'POST'])
def login_in():
    if request.method == 'POST':
        subject = request.form.get('subject')
        # 创建记录被试的文件夹
        create_recording(subject=subject)
        # 初始化session
        session_init(subject)
        # 重定向
        return redirect(url_for('index'))
    return render_template('login.html')





if __name__ == '__main__':
    #print(Flask.secret_key )
    app.run(host='0.0.0.0',debug=True)