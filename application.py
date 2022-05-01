from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import scrapping

app = Flask(__name__)
CORS(app)
api = Api(app)

class All_syntaxes(Resource):
    def get(self, word):
        return scrapping.all_syntaxes_(word)

class Noun_search(Resource):
    def get(self, word):
        return scrapping.noun_search_(word)

class Verb_search(Resource):
    def get(self, word):
        return scrapping.verb_search_(word)

class Adjective_search(Resource):
    def get(self, word):
        return scrapping.adjective_search_(word)

api.add_resource(All_syntaxes, "/all-syntaxes/<string:word>")
api.add_resource(Noun_search, "/noun-search/<string:word>")
api.add_resource(Verb_search, "/verb-search/<string:word>")
api.add_resource(Adjective_search, "/adjective-search/<string:word>")

if __name__ == "__main__":
    app.run()