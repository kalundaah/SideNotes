#dependencies
from flask import Blueprint

# create test blueprint
test = Blueprint("test",__name__)

@test.route('home',methods=["GET"])
def home():
    return "HOME PAGE",200