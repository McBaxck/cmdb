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


@app.route(f'{BASE_URI}/delete/server', methods=['PUT'])
def del_server():
    return 'put /delete/server/'


@app.route(f'{BASE_URI}/create/disk/<int:id>', methods=['PUT'])
def create_disk(id):
    return 'put /create/disk'


@app.route(f'{BASE_URI}/delete/disk/<int:id>', methods=['PUT'])
def delete_disk(id):
    return 'put /delete/disk'


@app.route(f'{BASE_URI}/set_hostname/<server>/<hostname>', methods=['PUT'])
def set_hostname(server, hostname):
    return 'put /set_hostname/'


@app.route(f'{BASE_URI}/set_partition/<server>/<partition_name>', methods=['PUT'])
def set_partition(server, partition_name):
    return 'put /set_partition/'


@app.route(f'{BASE_URI}/delete_partition/<server>/<partition_name>', methods=['PUT'])
def delete_partition(server, partition_name):
    return 'put /delete_partition/'


@app.route(f'{BASE_URI}/create_raid/<raid_name>', methods=['DELETE'])
def create_raid(raid_name):
    return 'put /create_raid/'


@app.route(f'{BASE_URI}/delete_raid/<raid_name>', methods=['DELETE'])
def delete_raid(raid_name):
    return 'put /delete_raid/'


@app.route(f'{BASE_URI}/add_raid/<raid_name>/<disk>', methods=['PUT'])
def add_raid(raid_name, disk):
    return 'put /add_raid/'


@app.route(f'{BASE_URI}/delete_raid/<raid_name>/<disk>', methods=['DELETE'])
def delete_raid_from_disk(raid_name, disk):
    return 'put /delete_raid/'


@app.route(f'{BASE_URI}/add_network_interface/<server>/<ip_adress>/<default_gateway>/<routing_table>/<interface_name>', methods=['PUT'])
def add_network_interface(server, ip_adress, default_gateway, routing_table, interface_name):
    return 'put /add_network_interface/'


@app.route(f'{BASE_URI}/del_network_interface/<interface_name>', methods=['DELETE'])
def delete_network_interface(interface_name):
    return 'put /del_network_interface/'


@app.route(f'{BASE_URI}/set_ip_rules/<interface_name>/<firewall_ip>', methods=['PUT'])
def set_ip_rules(interface_name, firewall_ip):
    return 'put /del_network_interface/'


@app.route(f'{BASE_URI}/del_ip_rules/<interface_name>/', methods=['DELETE'])
def del_ip_rules(interface_name):
    return 'put /del_network_interface/'


if __name__ == '__main__':
    app.run(host=NAME, port=PORT)
