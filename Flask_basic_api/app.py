from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "id":1, "name":"Abhinav Prakash", "email":"abhinavprakash@gmail.com"
    },
    {
        "id":2, "name":"Aman Kumar", "email":"aman@gmail.com"
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users),200

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = next((u for u in users if u['id']==id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': "User not found"}), 404

@app.route('/user', methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users)+1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/user/<int:id>', methods=["PUT"])
def update_user(id):
    user = next((u for u in users if u['id']==id),None)
    if user : 
        updated_data = request.get_json()
        user.update(updated_data)
        return jsonify(user),200
    return jsonify({'error':"User not found"}),404

@app.route('/user/<int:id>', methods=["DELETE"])
def delete_user(id):
    global users
    users = [u for u in users if u['id']!=id]
    return jsonify({'message':"User get deleted Successfully"})

if __name__ =='__main__':
    app.run(debug=True)