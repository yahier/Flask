# coding: UTF-8

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort, redirect, url_for

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login_post"
    else:
        return "do_the_login_get"



#Flask 会在 templates 文件夹里寻找模板
# 在模板里，你也可以访问 request 、 session 和 g [1] 对象， 以及 get_flashed_messages() 函数。
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


#读取 cookies:
@app.route('/getCookie')
def index():
    username = request.cookies.get('username')
    return username
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.


#存储 cookies:
@app.route('/setCookie')
def setcookie():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'yahier')
    return resp


#重定向  和  日志系统
@app.route('/a')
def a():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return redirect(url_for('yahier'))


if __name__ == '__main__':
    app.run()

