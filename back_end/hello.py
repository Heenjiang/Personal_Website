from flask import Flask, jsonify, render_template, request
import random, hashlib

app = Flask(__name__, 
            template_folder="./front_end/react_front_end/build",
            static_folder='front_end/react_front_end/build',
            static_url_path="/")

# 生成MD5
def genearteMD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
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
            userRegisteredDate = request.json['registeredDate']
        except KeyError as ke:
            return jsonify({
                "error" : "Pls input email and password!"
            })
        salt = '-'.join(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
        userPwdMd5 = genearteMD5(salt.join(userPwdFromClient))
        
        return jsonify({
            "username": username,
            "userpassword": userPwdMd5,
            "userSalt": salt
        })

@app.route('/api/hello')
def api():
  return {
        "username": 'Nicole',
        "theme": 'Blue',
    }  

if __name__ == '__main__':
    app.run(debug=True)