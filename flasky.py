# coding: UTF-8

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World.yahier write this in 广州!'


#这两种情况访问的时候。末尾带不带/是不同的
@app.route('/yahier')
def yahier():
    return '你好啊 yahier'


@app.route('/bingo/')
def bingo():
    return 'bingo'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'hi %s' % username

#方法遭遇错误
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login_post"
    else:
        return "do_the_login_get"



#Flask 会在 templates 文件夹里寻找模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()

