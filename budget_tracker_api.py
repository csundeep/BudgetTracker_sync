from flask import Flask

app = Flask(__name__)


@app.route('/items/all', methods=['GET'])
def get_items():
    return 'This is call to get items'


@app.route('/item/save', methods=['POST'])
def save_item():
    return 'This is call to save item'


@app.route('/item/edit', methods=['POST'])
def edit_item():
    return 'This is call to edit item'


@app.route('/item/delete', methods=['DELETE'])
def delete_item():
    return 'This is call to delete item'





@app.route('/users/all', methods=['GET'])
def get_users():
    return 'This is call to get users'


@app.route('/user/save', methods=['POST'])
def save_user():
    return 'This is call to save user'


@app.route('/user/edit', methods=['POST'])
def edit_user():
    return 'This is call to edit user'


@app.route('/user/delete', methods=['DELETE'])
def delete_user():
    return 'This is call to delete user'


@app.route('/budgets/all', methods=['GET'])
def get_budgets():
    return 'This is call to get budgets'


@app.route('/budget/save', methods=['POST'])
def save_budget():
    return 'This is call to save budget'


@app.route('/budget/edit', methods=['POST'])
def edit_budget():
    return 'This is call to edit budget'


@app.route('/budget/delete', methods=['DELETE'])
def delete_budget():
    return 'This is call to delete budget'


@app.route('/expenses/all', methods=['GET'])
def get_expenses():
    return 'This is call to get expenses'


@app.route('/expense/save', methods=['POST'])
def save_expense():
    return 'This is call to save expense'


@app.route('/expense/edit', methods=['POST'])
def edit_expense():
    return 'This is call to edit expense'


@app.route('/expense/delete', methods=['DELETE'])
def delete_expense():
    return 'This is call to delete expense'


if __name__ == '__main__':
    app.run(host="localhost", port="8080")
