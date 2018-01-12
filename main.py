import graphene
import json
from flask import Flask, request
app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"), age=graphene.Int())

    def resolve_hello(self, info, name, age):
        return 'hello, my name is {} and I am {} years old'.format(name, age)

schema = graphene.Schema(query=Query)


@app.route('/', methods=['POST'])
def hello():
    # result = schema.execute('{ hello(name: "charlie", age:21) }')
    data = json.loads(request.data)
    result = schema.execute(data["query"]).data
    return json.dumps(result)

if __name__ == '__main__':
    app.run()

# print(result.data['hello']) # "Hello stranger"
