CREATE TABLE serveurs (
	id_serveur	INTEGER NOT NULL PRIMARY KEY,
	label 		TXT NOT NULL,
	hostname 	TXT NOT NULL,
	type		TEXT NOT NULL, -- must be 'virtual' or 'physical'
	cpu 		TXT NOT NULL,
	gpu 		TXT NOT NULL
);

CREATE TABLE serveur_raids (
	FOREIGN KEY(id_serveur) REFERENCES serveurs(id),
	FOREIGN KEY(id_raid) REFERENCES raids(id)
);

CREATE TABLE raids (
	id_raid 		INTEGER NOT NULL PRIMARY KEY,
	label	TXT NOT NULL -- must be 0, 1, 5 or 6
);

CREATE TABLE disks (
	id_disk 		INTEGER NOT NULL PRIMARY KEY,
	label			TXT NOT NULL,
	espace_libre	INTEGER NOT NULL,
	espace_utilise	INTEGER NOT NULL,
	FOREIGN KEY(id_serveur) REFERENCES serveurs(id),
);

CREATE TABLE partition_DD (
	id_partition	INTEGER NOT NULL PRIMARY KEY,
	label			TXT NOT NULL,
	espace_libre	INTEGER NOT NULL,
	espace_utilise	INTEGER NOT NULL,
	FOREIGN KEY(id_disk) REFERENCES disks(id),
);

CREATE TABLE interface_reseau (
	id_interface	INTEGER NOT NULL PRIMARY KEY,
	ip_source		TXT NOT NULL,
	port			INTEGER NOT NULL,
	ip_passerelle	TXT NOT NULL,
	FOREIGN KEY(id_serveur) REFERENCES serveurs(id)
);

CREATE TABLE serveur_securite (
	FOREIGN KEY(id_serveur) REFERENCES serveurs(id),
	FOREIGN KEY(id_securite) REFERENCES securite(id)
);

CREATE TABLE securite (
	id_securite		INTEGER NOT NULL PRIMARY KEY,
	ip_firewall		TXT NOT NULL
);

CREATE TABLE route (
	ip_route		INTEGER NOT NULL PRIMARY KEY,
	ip_destination 	TXT NOT NULL,
	masque_reseau	TXT NOT NULL,
	ip_interface	TXT NOT NULL,
	ttl				INTEGER NOT NULL,
	FOREIGN KEY(id_interface) REFERENCES interface_reseau(id)
);

CREATE TABLE ip_table_options (
	FOREIGN KEY(id_iptable_rule) REFERENCES ip_table_rules(id),
	FOREIGN KEY(id_iptable_rule_option) REFERENCES ip_table_rules_option(id)
);

CREATE TABLE ip_table_rules (
	id_iptable_rule INTEGER NOT NULL PRIMARY KEY,
	ip_destination 	TXT NOT NULL,
	port			INTEGER NOT NULL,
	protcole		TXT NOT NULL,
	policy 			TXT NOT NULL,
	FOREIGN KEY(id_securite) REFERENCES securite(id)
);

CREATE TABLE ip_table_rules_option (
	id_iptable_rule_option	INTEGER NOT NULL PRIMARY KEY,
	option					TXT NOT NULL
);