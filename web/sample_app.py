from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from bson import ObjectId
from pymongo import MongoClient
import os

sample = Flask(__name__)

mongo_uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
mydb = client[db_name]
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


interface_status = mydb["interface_status"]


@sample.route("/router/<ip>", methods=["GET"])
def router_detail(ip):
    docs = mydb.interface_status.find({"router_ip": ip})\
        .sort("timestamp", -1).limit(3)
    return render_template("router_detail.html",\
                            router_ip=ip, interface_data=docs)


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
