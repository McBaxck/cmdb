from flask import Flask
import json

PORT = 8081
NAME = 'localhost'
LINKED_DB = 'test.db'
BASE_URI = '/api/v1'

test: dict = {1: 'heho', 2: 'ouho', 3: ['suu', 'siii']}
app: Flask = Flask(__name__)
# Route 1) ------------


@app.route(f'{BASE_URI}')
def home():
    return json.dumps(test)


@app.route(f'{BASE_URI}/servers')
def servers():
    return '/servers location'


@app.route(f'{BASE_URI}/server/<int:id>')
def server(id):
    return f'/server/{id} location'


@app.route(f'{BASE_URI}/server/<int:id>/disks')
def server_disks(id):
    return f'server {id}: disks'


@app.route(f'{BASE_URI}/create/server', methods=['PUT'])
def create_server():
    return 'put /create/server/'


@app.route(f'{BASE_URI}/create/disk/<int:id>', methods=['PUT'])
def create_disk(id):
    return 'put /create/disk'


if __name__ == '__main__':
    app.run(host=NAME, port=PORT)
