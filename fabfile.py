#!/usr/bin/env python
# coding=utf-8

from fabric.api import env,local,cd,run
from fabric.context_managers import prefix

def build():
    '''
    设置build环境
    '''
    env.hosts = ["root@60.205.190.223"]
    env.password ="Jax@gmail.com"
def prepare():
    '''
    提交本地代码,准备部署,remote 和 branch更据自己需求修改
    '''
    local("git pull webapp master")
    local("pip freeze > requirements.txt")
    local("git add . -A && git commit")
    local("git push webapp master")

def update():
    '''
    服务器上更新代码
    '''
    with cd("/home/jax/python/awesome-python-webapp"):
        run("git pull")
        run("pip install -r requirements.txt")
        run("supervisorctl restart awesome")

def deploy():
    build()
    prepare()
    update()
