from flask import Flask,render_template,session,redirect,url_for,flash
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment # 添加时间戳
from flask_wtf import FlaskForm # 表单类
from wtforms import StringField, SubmitField# 添加两个表单属性类
from wtforms.validators import DataRequired# 添加验证器

app = Flask(__name__)

bootstrap = Bootstrap(app)# 初始化Bootstrap对象
moment = Moment(app)# 同样初始化Moment
app.config['SECRET_KEY']='123456yhy'# 这个最好不要写在源码里

# 定义一个表单对象
class NameForm(FlaskForm):
    name = StringField('Whats u name ?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST']) # 装饰器，把根目录映射到了index()视图函数上，定义了一个静态路由
def index():
    form = NameForm()
    if form.validate_on_submit():# 这里是接受验证器的反馈
        old_name = session.get('name')
        new_name = form.name.data
        if old_name is not None and old_name != new_name:
            flash('you have changed your name!')
        session['name'] = new_name 
        return redirect(url_for('name',user=session.get('name')))# 重定向到name视图
    return render_template('name.html',current_time=datetime.utcnow(),form=form)# 这里就不用再传入name了
# 其实这里已经有了用二级模板的思维了，将name的导航栏拉出来作为base即可

@app.route('/name/<user>')
def name(user):# 这里要调用name模板了
    return render_template('name.html',name=user,current_time=datetime.utcnow())
# 先 通过if form来保留这个url的可用性

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
# 这里参数通常为e（Exception）,其可以访问该异常对象，同时别忘了return404状态码

if __name__=="__main__":# 这个__main__是这个py文档的__main__，与Flask(__main__)无关
    app.run()