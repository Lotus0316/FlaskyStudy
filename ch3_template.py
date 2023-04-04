from flask import Flask,render_template # 还要导入一个render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

hello = Flask('Hello')

bootstrap = Bootstrap(hello)# 初始化Bootstrap对象
moment = Moment(hello)# 同样初始化Moment

@hello.route('/') # 装饰器，把根目录映射到了index()视图函数上，定义了一个静态路由
def index():
    return render_template('name.html',name='World',current_time=datetime.utcnow())
# 其实这里已经有了用二级模板的思维了，将name的导航栏拉出来作为base即可

@hello.route('/name/<user>')
def name(user):# 这里要调用name模板了
    return render_template('name.html',name=user,current_time=datetime.utcnow())

@hello.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
# 这里参数通常为e（Exception）,其可以访问该异常对象，同时别忘了return404状态码
