from flask import Flask, jsonify, render_template

app = Flask(__name__, 
            template_folder="./front_end/react_front_end/build",
            static_folder='front_end/react_front_end/build',
            static_url_path="/")

@app.route('/')
def hello_world():
   return render_template('index.html')  # 渲染打包好的React App的页面

@app.route('/api/hello')
def api():
   return {
        "username": 'Nicole',
        "theme": 'Blue',
    }  

if __name__ == '__main__':
    app.run(debug=True)