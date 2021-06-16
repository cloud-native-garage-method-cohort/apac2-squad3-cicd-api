from flask import Flask,jsonify,request
import model

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    name = 'worldkk'
    if 'name' in request.args:
        name = request.args['name']
    data={'data': 'hello ' + name}
    return jsonify(data)

@app.route('/users',methods=['GET'])
def get_users():
    mod = model.Model()
    sql = "SELECT * FROM users"
    res = mod._exec(sql)
    print(res)
    ret = []
    for item in res:
        d = {}
        d["username"] = item[1]
        d["password"] = item[2]
        ret.append(d)
    return {"data": ret}

@app.route('/login',methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    mod = model.Model()
    sql = "SELECT * FROM users where username='{}' and password='{}'".format(username, password)
    print(sql)
    res = mod._exec(sql)
    print(res)
    if len(res) == 0:
        return {"result": False}
    return {"result": True}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
