from app.bean.secretkey import Secretkey
from app.db import User
from flask import request
import hashlib

def dologin():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    u = User.query.filter_by(UserPhone=UserPhone).first()
    print (UserPhone)
    if u is None:
        msg = '用户不存在'
        state = '0'
        SecretKey = None
        UserPhoto = None
    else:
        m = PassWord.encode('utf-8')
        password = hashlib.md5()
        password.update(m)
        psw = password.hexdigest()
        print (psw)
        print (u.PassWord)
        if psw == u.PassWord:
            state = '1'
            msg = '登陆成功'
            S = Secretkey()
            SecretKey = S.GetSecretKey()
            u.SecretKey = SecretKey
        else:
            msg = '账号或密码错误'
            state = '0'
            SecretKey = None
            UserPhoto = None
    array = {
    'msg': msg,
    'state' : state,
    'SecretKey': SecretKey,
    }
    return array