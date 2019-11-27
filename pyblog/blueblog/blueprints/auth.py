from blueblog import app, db
from flask import Blueprint, flash, redirect, url_for, render_template, request, json, jsonify
from blueblog.models import Article,Note,Message

auth_bp = Blueprint('auth', __name__)

#格式化数据库数据
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
# 数组转树机构
# data = [
# 	{'id': 1, 'parent_id': 0, 'name': "A"},
# 	{'id': 2, 'parent_id': 0, 'name': "AA"},
# 	{'id': 3, 'parent_id': 1, 'name': "AB"},
# 	{'id': 4, 'parent_id': 3, 'name': "ABA"},
# 	{'id': 5, 'parent_id': 3, 'name': "ABB"},
# 	{'id': 6, 'parent_id': 3, 'name': "ABC"},
# 	{'id': 7, 'parent_id': 1, 'name': "AC"},
# 	{'id': 8, 'parent_id': 7, 'name': "ACA"},
# 	{'id': 9, 'parent_id': 8, 'name': "ACAA"},
# 	{'id': 10,'parent_id': 8, 'name': "ACAB"},
# ]
def list_to_tree(data):
    res = {}
    for v in data:
        # v["parent_id"] = v["parent_id"] if v["parent_id"] else 0
        # 以id为key，存储当前元素数据
        res.setdefault(v["id"], v).update(v)  # .update(v) 解决先添加parent_id，后添加id的情况。
        # 这里默认的关联关系，v的内存地址是一致的，所以后续修改之后，关联的结构数据也会变化。
        res.setdefault(v["parent_id"], {}).setdefault("children", []).append(v)
    return res[0]["children"]

@auth_bp.route('/login')
def login():
    return 'login'

@auth_bp.route('/logout')
def logout():
    return 'logout'

# 提交会话
@app.route('/addMessage',methods=['POST'])
def addmessage():
    user_info = request.form.to_dict()
    name = user_info.get('name')
    body = user_info.get('body')
    message = Message(name=name, body=body)
    db.session.add(message)
    db.session.commit()
    return 'ok'
#查询全部会话
@app.route('/getMessage',methods=['GET'])
def getmessage():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    list = model_to_dict(messages)
    print(list)

    return jsonify({"list": list, 'code': 200})
#增
@app.route('/addnote',methods=['GET'])
def addnote():
    note1 = Note(body="remenber")
    db.session.add(note1)
    db.session.commit()
    return '12'
#查
@app.route('/getnote')
def getnote():
    allnote = Note.query.all()
    print(allnote[0].body)
    return 'a'
#改
@app.route('/updatenote')
def updatenote():
    note = Note.query.get(5)
    note.body = '修改后的文本'
    db.session.commit()
    return '修改成功'
#删
@app.route('/deletenote')
def deletenote():
    note = Note.query.get(6)
    db.session.delete(note)
    db.session.commit()
    return '删除成功'