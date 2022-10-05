
from flask import Flask, request
import json
import sys
import os
from pathlib import Path
from classes.database.server.server_database import ServerDatabase
from classes.database.stockage.hard_disk_database import DisqueDurDatabase
from classes.database.stockage.partition_database import PartitionDatabase

PORT = 8081
NAME = 'localhost'
LINKED_DB = 'test.db'
BASE_URI = '/api/v1'

test: dict = {1: 'heho', 2: 'ouho', 3: ['suu', 'siii']}
app: Flask = Flask(__name__)
# Route 1) ------------


@app.route(f'{BASE_URI}')
def home():
    return "CMDB API - State [online]"


@app.route(f'{BASE_URI}/servers')
def servers():
    server: ServerDatabase = ServerDatabase()
    try:
        return server.selectAll()
    except (TypeError, Exception):
        return '- No result -'


@app.route(f'{BASE_URI}/server/<int:id>')
def server(id):
    server: ServerDatabase = ServerDatabase()
    try:
        return server.selectById(id=id)
    except (TypeError, Exception):
        return '- No result -'


@app.route(f'{BASE_URI}/server/<int:id>/disks')
def server_disks(id):
    disk: DisqueDurDatabase = DisqueDurDatabase()
    try:
        return disk.selectAll(id_serveur=id)
    except (TypeError, Exception):
        return '- No result -'


@app.route(f'{BASE_URI}/create/server', methods=['PUT'])
def create_server():
    _datas: bytes = request.data
    new_server_datas: dict = json.loads(_datas.decode())
    server: ServerDatabase = ServerDatabase()
    try:
        return server.create(id_server=new_server_datas.get('id_serveur'), label=new_server_datas.get('label'), hostname=new_server_datas.get(
            'hostname'), serveur_type=new_server_datas.get('serveur_type'), cpu=new_server_datas.get('cpu'), gpu=new_server_datas.get('gpu'))
    except (TypeError, Exception):
        return '- No result -'


@app.route(f'{BASE_URI}/delete/server/<id>', methods=['DELETE'])
def delete_server(id):
    server: ServerDatabase = ServerDatabase()
    try:
        return server.delete(id_server=id)
    except (TypeError, Exception):
        return '- No server registered -'


@app.route(f'{BASE_URI}/create/disk', methods=['PUT'])
def create_disk():
    _datas: bytes = request.data
    new_disk_datas: dict = json.loads(_datas.decode())
    disk: DisqueDurDatabase = DisqueDurDatabase()
    return disk.create(label=new_disk_datas.get('label'), espace_libre=new_disk_datas.get('espace_libre'), espace_utilise=new_disk_datas.get('espace_utilise'), id_serveur=new_disk_datas.get('id_serveur'))


@app.route(f'{BASE_URI}/delete/disk/<int:id>', methods=['DELETE'])
def delete_disk(id):
    disk: DisqueDurDatabase = DisqueDurDatabase()
    print(disk.selectAll())
    try:
        return disk.delete(id_disque_dur=id)
    except (TypeError, Exception):
        return '- Unable to delete the disk, maybe not register -'


@app.route(f'{BASE_URI}/set/<int:id_server>/<field>/<value>', methods=['PUT'])
def set_hostname(id_server, field, hostname):
    server: ServerDatabase = ServerDatabase()
    print(server.single_update(field=field,
          value=value, id_serveur=id_server))
    return 'put /set_hostname/'


@app.route(f'{BASE_URI}/set_partition/<server>/<partition_name>', methods=['PUT'])
def set_partition(server, partition_name):
    partition: PartitionDatabase = PartitionDatabase()

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
