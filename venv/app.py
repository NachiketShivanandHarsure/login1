from  flask import Flask  ,request, jsonify

app = Flask(_name_)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if _name_ == 'main':
    app.run(debug=True)