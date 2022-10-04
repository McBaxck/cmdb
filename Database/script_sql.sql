CREATE TABLE Serveur(
   id_serveur INTEGER,
   label TEXT NOT NULL,
   hostname TEXT NOT NULL,
   type TEXT NOT NULL,
   cpu TEXT NOT NULL,
   gpu TEXT NOT NULL,
   PRIMARY KEY(id_serveur)
);

CREATE TABLE Disque_Dur(
   id_disque_dur INTEGER,
   label TEXT NOT NULL,
   espace_libre INTEGER NOT NULL,
   espace_utilise INTEGER NOT NULL,
   id_serveur INTEGER NOT NULL,
   PRIMARY KEY(id_disque_dur),
   FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur)
);

CREATE TABLE Partition_DD(
   id_partition INTEGER,
   label TEXT NOT NULL,
   espace_libre INTEGER NOT NULL,
   espace_utilise INTEGER NOT NULL,
   id_disque_dur INTEGER NOT NULL,
   PRIMARY KEY(id_partition),
   FOREIGN KEY(id_disque_dur) REFERENCES Disque_Dur(id_disque_dur)
);

CREATE TABLE Securite(
   id_securite INTEGER,
   ip_firewall TEXT NOT NULL,
   PRIMARY KEY(id_securite)
);

CREATE TABLE IPTable_Rules(
   id_iptable_rules INTEGER,
   ip_destination TEXT NOT NULL,
   port INTEGER NOT NULL,
   protocole TEXT NOT NULL,
   policy TEXT NOT NULL,
   id_securite INTEGER NOT NULL,
   PRIMARY KEY(id_iptable_rules),
   FOREIGN KEY(id_securite) REFERENCES Securite(id_securite)
);

CREATE TABLE IPTable_Rules_Option(
   id_iptables_rules_option INTEGER,
   option TEXT NOT NULL,
   PRIMARY KEY(id_iptables_rules_option)
);

CREATE TABLE Interface_Reseau(
   id_interface_firewall INTEGER,
   ip_source TEXT NOT NULL,
   port INTEGER NOT NULL,
   ip_passerelle TEXT NOT NULL,
   id_serveur INTEGER NOT NULL,
   PRIMARY KEY(id_interface_firewall),
   FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur)
);

CREATE TABLE Route(
   id_route INTEGER,
   ip_destination TEXT NOT NULL,
   masque_reseau TEXT NOT NULL,
   ip_interface TEXT NOT NULL,
   ttl INTEGER,
   id_interface_firewall INTEGER NOT NULL,
   PRIMARY KEY(id_route),
   FOREIGN KEY(id_interface_firewall) REFERENCES Interface_Reseau(id_interface_firewall)
);

CREATE TABLE RAID(
   id_raid INTEGER,
   label TEXT NOT NULL,
   PRIMARY KEY(id_raid)
);

CREATE TABLE iptable_options(
   id_iptable_rules INTEGER,
   id_iptables_rules_option INTEGER,
   PRIMARY KEY(id_iptable_rules, id_iptables_rules_option),
   FOREIGN KEY(id_iptable_rules) REFERENCES IPTable_Rules(id_iptable_rules),
   FOREIGN KEY(id_iptables_rules_option) REFERENCES IPTable_Rules_Option(id_iptables_rules_option)
);

CREATE TABLE serveur_securite(
   id_serveur INTEGER,
   id_securite INTEGER,
   PRIMARY KEY(id_serveur, id_securite),
   FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur),
   FOREIGN KEY(id_securite) REFERENCES Securite(id_securite)
);

CREATE TABLE serveur_raid(
   id_serveur INTEGER,
   id_raid INTEGER,
   PRIMARY KEY(id_serveur, id_raid),
   FOREIGN KEY(id_serveur) REFERENCES Serveur(id_serveur),
   FOREIGN KEY(id_raid) REFERENCES RAID(id_raid)
);
