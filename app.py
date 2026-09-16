from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/board")
def board():

    with open("information.json", "r") as file:
            comments = json.load(file)

    return render_template("board.html", comments = comments)

@app.route("/post", methods=['POST'])
def post():
    idnumber = request.form.get("idnumber")
    emailaddress = request.form.get("emailaddress")
    phonenumber = request.form.get("phonenumber")
    comment = request.form.get("comment")

    with open("information.json", "r") as file:
        comments = json.load(file)

    comments.append(
         {
              "idnumber": f"{idnumber}",
              "emailaddress": f"{emailaddress}",
              "phonenumber": f"{phonenumber}",
              "comment": f"{comment}"
         }
    )

    with open("information.json", "a") as file:
        json.dump(comments, file, indent=4)

    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')