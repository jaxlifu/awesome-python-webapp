#!/usr/bin/env python
# coding=utf-8

from fabric.api import env, local, cd, run
from fabric.context_managers import prefix


def build():
    '''
    设置build环境
    '''
    env.user = 'root'
    env.hosts = ['60.205.190.223']
    env.password = "Jax@gmail.com"


def prepare():
    '''
    提交本地代码,准备部署,remote 和 branch更据自己需求修改
    '''
    pull = local("git pull webapp master")
    print("pull result ==> %s" % pull)
    freeze = local("pip freeze > requirements.txt")
    print("freeze result ==> %s" % freeze)
    commit = local("git add . -A && git commit")
    print("commit result ==> %s" % commit)
    push = local("git push webapp master")
    print("push result ==> %s" % push)


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
