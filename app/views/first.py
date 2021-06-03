from flask import Blueprint
from app.ext import db
from flask import redirect,url_for,request
from app.models import Userok


first=Blueprint("first",__name__)

@first.route("/")
def index():
    return "我是首页,,,hello world"




@first.route("/createdb/")
def createdb():
    db.create_all()
    return "建表成功"


@first.route("/reto")
def reto():
    #如果是蓝图注册的,必须调用  蓝图.方法名来生成url
    return redirect(url_for("first.index"))

#这里<string:name>的name必须和下面name的名字一样
@first.route("/tk/<string:name>")
def tk(name):
    print(name)
    print(type(name))
    # request.args.get用来获取 xxx?user=kk&age=77中问号后面的变量
    print(request.args.get("user"))
    return "请到控制台查看详情"


@first.route("/adduser/")
def adduser():
    user=Userok()
    user.user="myzi"
    user.addr="henan"
    user.age="77"
    user.save()
    return "添加用户成功"