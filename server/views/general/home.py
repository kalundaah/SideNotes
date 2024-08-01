from . import general


@general.route('/', methods=['GET'])
def home():
    return "Home page", 200


