#use this one
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from bson import ObjectId
from pymongo import MongoClient

sample = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
mydb = client["routers"]
mycol = mydb["my_routers_collection"]


@sample.route("/")
def main():
    items = list(mycol.find({}))
    return render_template("index.html", items=items)

@sample.route("/add", methods=["POST"])
def add_comment():

    ip = request.form.get("ip")
    user = request.form.get("user")
    password = request.form.get("password")
    if ip and user and password:
        mycol.insert_one({"ip": ip, "user": user, "password": password})
    return redirect(url_for("main"))

@sample.route("/delete", methods=["POST"])
def delete_comment():
    rid = request.form.get("id")
    try:
        mycol.delete_one({"_id": ObjectId(rid)})
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
