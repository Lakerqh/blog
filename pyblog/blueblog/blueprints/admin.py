from blueblog import app, db
from flask import Blueprint, flash, redirect, url_for, render_template, request, json, jsonify
from blueblog.models import User
from sqlalchemy import and_, or_

admin_bp = Blueprint('admin', __name__)

# 用户登录
@admin_bp.route('/user', methods=['GET','POST'])
def user():
    print(request.json)

    # user_info = request.form.to_dict()
    # username = user_info.get('username')
    # password = user_info.get('password')

    user_info = request.json
    username = user_info.get('username')
    password = user_info.get('password')
    user = User.query.filter(and_(User.username == username, User.password_hash == password)).first()
    if user:
        return 'True'
    else:
        return 'False'