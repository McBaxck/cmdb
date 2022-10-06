
from flask import Flask, request
import json
import sys
import os
from pathlib import Path
from classes.database.server.server_database import ServerDatabase
from classes.database.stockage.hard_disk_database import DisqueDurDatabase
from classes.database.stockage.partition_database import PartitionDatabase
from classes.server.config.interface_reseau import InterfaceReseau
from classes.server.config.ip_table_rules import IpTableRules
from classes.database.interfaces.ip_table_rules_database import IpTableRulesDatabase
from classes.database.interfaces.interface_reseau_database import InterfaceReseauDatabase
from classes.database.interfaces.interface_reseau_route_database import InterfaceReseauRouteDatabase


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
    print(server.selectById(id=id))
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


@app.route(f'{BASE_URI}/server/<int:id>/disk/<id_disk>')
def server_single_disk(id, id_disk):
    disk: DisqueDurDatabase = DisqueDurDatabase()
    try:
        return disk.selectById(id=id_disk)
    except (TypeError, Exception):
        return '- No result -'


@app.route(f'{BASE_URI}/partitions')
def get_partitions():
    partition: PartitionDatabase = PartitionDatabase()
    try:
        return partition.selectAll()
    except (Exception) as NoResult:
        return '- No partitions -'


@app.route(f'{BASE_URI}/disk/<int:id_disk>/partitions')
def server_disk_partitions(id_disk):
    partition: PartitionDatabase = PartitionDatabase()
    try:
        return partition.selectByIdDisk(id=id_disk)
    except Exception as NoResult:
        return '- No result -'


@app.route(f'{BASE_URI}/server/<int:id>/partitions')
def server_partitions(id):
    partition: PartitionDatabase = PartitionDatabase()
    try:
        return partition.selectById(id=id)
    except (Exception) as NoResult:
        return '- No result -'


@app.route(f'{BASE_URI}/create/server', methods=['PUT'])
def create_server():
    _datas: bytes = request.data
    new_server_datas: dict = json.loads(_datas.decode())
    server: ServerDatabase = ServerDatabase()
    return server.create(id_server=new_server_datas.get('id_serveur'), label=new_server_datas.get('label'), hostname=new_server_datas.get(
        'hostname'), serveur_type=new_server_datas.get('serveur_type'), cpu=new_server_datas.get('cpu'), gpu=new_server_datas.get('gpu'))


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
    return disk.create(label=new_disk_datas.get('label'), espace_libre=new_disk_datas.get('espace_libre'),
                       espace_utilise=new_disk_datas.get('espace_utilise'), format_disque=new_disk_datas.get('format_disque'),
                       id_serveur=new_disk_datas.get('id_serveur'))


@app.route(f'{BASE_URI}/create/partition', methods=['PUT'])
def create_partition():
    _datas: bytes = request.data
    new_partition_datas: dict = json.loads(_datas.decode())
    partition: PartitionDatabase = PartitionDatabase()
    return partition.create(id_partition=new_partition_datas.get('id_partition'), label=new_partition_datas.get('label'),
                            espace_libre=new_partition_datas.get('espace_libre'), espace_utilise=new_partition_datas.get('espace_utilise'),
                            id_disque_dur=new_partition_datas.get('id_disque_dur'))


@app.route(f'{BASE_URI}/delete/disk/<int:id>', methods=['DELETE'])
def delete_disk(id):
    disk: DisqueDurDatabase = DisqueDurDatabase()
    print(disk.delete(id_disque_dur=id))
    try:
        return disk.delete(id_disque_dur=id)
    except (TypeError, Exception):
        return '- Unable to delete the disk, maybe not register -'


@app.route(f'{BASE_URI}/set/server/<int:id_server>/field/<field>/<value>', methods=['PUT'])
def set_hostname(id_server, field, value):
    server: ServerDatabase = ServerDatabase()
    return server.tailored_update(id_serveur=id_server, field=field, value=value)


@app.route(f'{BASE_URI}/set/partition/<int:id_partition>/field/<field>/<value>', methods=['PUT'])
def set_partition(id_partition, field, value):
    partition: PartitionDatabase = PartitionDatabase()
    return partition.tailored_update(id_partition=id_partition, field=field, value=value)


@app.route(f'{BASE_URI}/delete/partition/<int:id_partition>', methods=['DELETE'])
def delete_partition(id_partition):
    partition: PartitionDatabase = PartitionDatabase()
    return partition.delete(id_partition=id_partition)


@app.route(f'{BASE_URI}/interfaces/reseau', methods=['GET'])
def get_inets():
    interface_reseau_db: InterfaceReseauDatabase = InterfaceReseauDatabase()
    try:
        return interface_reseau_db.selectAll()
    except (Exception) as NoResult:
        return '- No result -'


@app.route(f'{BASE_URI}/server/<int:id>/interfaces/reseau', methods=['GET'])
def get_inets_from_server(id):
    interface_reseau_db: InterfaceReseauDatabase = InterfaceReseauDatabase()
    try:
        return interface_reseau_db.selectByServeur(serverId=id)
    except (Exception) as NoResult:
        return '- No result -'


@app.route(f'{BASE_URI}/create/interface/reseau/<int:id_serveur>', methods=['PUT'])
def add_inet(id_serveur):
    _datas: bytes = request.data
    new_inet_datas: dict = json.loads(_datas.decode())
    interface_reseau_db: InterfaceReseauDatabase = InterfaceReseauDatabase()
    _inet: InterfaceReseau = InterfaceReseau(_idInterfaceReseau=new_inet_datas.get('id_interface_reseau'), _ipSource=new_inet_datas.get('ip_source'),
                                             _port=new_inet_datas.get('port'), _passerelle=new_inet_datas.get('passerelle'),
                                             _interface_reseau_route=[])
    return interface_reseau_db.create(_inet, id_serveur)


@app.route(f'{BASE_URI}/delete/interface/reseau/<int:id_interface>', methods=['DELETE'])
def delete_network_interface(id_interface):
    interface_reseau_db: InterfaceReseauDatabase = InterfaceReseauDatabase()
    return interface_reseau_db.delete(id_interface_reseau=id_interface)


@app.route(f'{BASE_URI}/create/itr/<int:id_itr>', methods=['PUT'])
def add_itr(id_itr):
    _datas: bytes = request.data
    new_itr_datas: dict = json.loads(_datas.decode())
    ip_table_rules_db: IpTableRulesDatabase = IpTableRulesDatabase()
    return ip_table_rules_db.create(IpTableRules(_id=new_itr_datas.get('id'), _ip_source=new_itr_datas.get('ip_source'),
                                                 _ip_destination=new_itr_datas.get('ip_destination'), _port=new_itr_datas.get('port'),
                                                 _protocol=new_itr_datas.get('protocol'), _option=new_itr_datas.get('options'),
                                                 _iptable_policy=new_itr_datas.get('policy')), id_itr)


@app.route(f'{BASE_URI}/delete/itr/<int:id_iptablerules>/', methods=['DELETE'])
def delete_itr(id_iptablerules):
    ip_table_rules_db: IpTableRulesDatabase = IpTableRulesDatabase()
    return ip_table_rules_db.delete(id_iptablerules)


if __name__ == '__main__':
    app.run(host=NAME, port=PORT)
