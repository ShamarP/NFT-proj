from flask import Flask, render_template, url_for, request

app = Flask(__name__)

headings = ("NFT","Entry Price", "Exit Price", "Profit","Hold Duration")

data = [("Bored Ape", "2", "3","1","1 week")]
@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        user_address = request.form['address']
        return table(user_address)
    else:
        return render_template("homepage.html")

@app.route('/<id>')
def table(id):
    return render_template("table.html", headings = headings, data=data, user_id = id)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)