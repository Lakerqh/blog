from blueblog import app, db
from flask import Blueprint, flash, redirect, url_for, render_template, request, json, jsonify
from blueblog.models import User, Menu
from sqlalchemy import and_, or_

admin_bp = Blueprint('admin', __name__)

# 用户登录
@admin_bp.route('/login', methods=['GET', 'POST'])
def user():
    # user_info = request.form.to_dict()
    # username = user_info.get('username')
    # password = user_info.get('password')
    user_info = request.json
    username = user_info.get('username')
    password = user_info.get('password')
    user = User.query.filter(and_(User.username == username,User.password_hash == password)).first()
    print(user)
    if user:
        user1 = User.query.filter(and_(User.username == username,User.password_hash == password, User.power == 1)).first()
        if user1:
            result = {
                'code': 1,
                'msg': '验证通过'
            }
            return result
        else:
            result = {
                'code': 2,
                'msg': '账号审核中'
            }
            return result

    else:
        result = {
            'code': 0,
            'msg': '账号或密码错误，请重新输入'
        }
        return result

# 用户注册
@admin_bp.route('/register', methods=['GET', 'POST'])
def register():
    user_info = request.json
    username = user_info.get('username')
    password = user_info.get('password')
    user = User(username=username, password_hash=password)
    db.session.add(user)
    db.session.commit()
    result = {
        'code': 1,
        'msg': '注册成功，请等待审核'
    }
    return result

# 管理员审核注册账号申请
@admin_bp.route('/check', methods=['GET','POST'])
def check():
    user_info = request.json
    id = user_info.get('id')
    user = User.query.get(id)
    user.power = '1'
    db.session.commit()
    return '审核通过'

# 菜单列表
@admin_bp.route('/getmenu', methods=['GET', 'POST'])
def getmenu():
    menu = Menu.query.all()
    list = model_to_dict(menu)
    menulist = list_to_tree(list)
    return jsonify({"list": menulist, 'code': 200})

# 模型转字典结构
def model_to_dict(result):
    from collections import Iterable
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')

# 数组转树结构
def list_to_tree(data):
    res = {}
    for v in data:
        # v["parent_id"] = v["parent_id"] if v["parent_id"] else 0
        # 以id为key，存储当前元素数据
        res.setdefault(v["id"], v).update(v)  # .update(v) 解决先添加parent_id，后添加id的情况。
        # 这里默认的关联关系，v的内存地址是一致的，所以后续修改之后，关联的结构数据也会变化。
        res.setdefault(v["parent_id"], {}).setdefault("children", []).append(v)
    return res[0]["children"]