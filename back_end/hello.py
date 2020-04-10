from flask import Flask, jsonify, render_template, request
import random, hashlib
from src.objects.User import User
import time
from src.apis.signupApi import SignUp 

app = Flask(__name__, 
            template_folder="./front_end/react_front_end/build",
            static_folder='front_end/react_front_end/build',
            static_url_path="/")

# 生成MD5
def genearteMD5(timeStamp):
    timeStampStr = str(timeStamp)
    hl = hashlib.md5()
    hl.update(timeStampStr.encode(encoding='utf-8'))
    return hl.hexdigest()

@app.route('/')
def hello_world():
   return render_template('index.html')  # 渲染打包好的React App的页面

@app.route('/user/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.json['username']
            userPwdFromClient = request.json['userpassword']
        except KeyError as ke:
            return jsonify({
                "error" : "Pls input email and password!"
            })
        userRegisteredDate = int(time.time())
        strTimeStamp = str(userRegisteredDate)
        # 用timeStamp和客户端传过来的密码（也是email和password的加密码）再次编码
        userPwdMd5 = genearteMD5(strTimeStamp.join(userPwdFromClient))
        # 创建User instance
        register = User(username, userPwdMd5, userRegisteredDate)
        # 创建注册对象
        registerProxcy = SignUp(register)
        
        registerFlag = registerProxcy.signup()

        if registerFlag == None:
             return jsonify({
                "validation error" : "This emali has already been registered!"
            })    
        else:
             return jsonify({
                "message" : str(registerFlag)
            })   
        

@app.route('/api/hello')
def api():
  return {
        "username": 'Nicole',
        "theme": 'Blue',
    }  

if __name__ == '__main__':
    app.run(debug=True)