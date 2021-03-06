# !/usr/bin/env python
# -*- coding: utf-8 -*-
from blueblog import db
from datetime import datetime

# 读者注册
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    gender = db.Column(db.String(2))
    role_id = db.Column(db.Integer)

# 菜单
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    parent_id = db.Column(db.Integer)
    role_type = db.Column(db.Integer)

#  角色类型
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(20))
    menulist = db.Column(db.String(500))

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)

# # 管理员模型
# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20))
#     password_hash = db.Column(db.String(128))
#     blog_title = db.Column(db.String(60))
#     blog_sub_title = db.Column(db.String(100))
#     name = db.Column(db.String(30))
#     about = db.Column(db.Text)

# # 分类-用于存储文章分类
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True)
#     posts = db.relationship('Post',back_populates='category')

# # 文章
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(60))
#     body = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     category = db.relationship('Category',back_populates='posts')
#     comments = db.relationship('Comment',back_populates='post', cascade='all,delete-orphan')

# # 评论
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String(30))
#     email = db.Column(db.String(254))
#     site = db.Column(db.String(255))
#     body = db.Column(db.Text)
#     from_admin = db.Column(db.Boolean, default=False)
#     reviewed = db.Column(db.Boolean, default=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     post = db.relationship('Post',back_populates='comments')
#     replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
#     replied = db.relationship('Comment',back_populates='replies', remote_side=[id])
#     replies = db.relationship('Comment',back_populates='replied', cascade='all')

db.create_all()