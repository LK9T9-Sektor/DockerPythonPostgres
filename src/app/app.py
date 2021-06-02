import psycopg2
import pprint

from sqlalchemy import create_engine
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql import text

# DB Connection data
db_user = 'username'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'
db_name = 'genshin'

# Connect to the database
db_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
# Access the DB Engine
engine = create_engine(db_string, echo=True)

# Create database if it does not exist.
if not database_exists(engine.url):
    print("Database doesnt exists")
    create_database(engine.url)
else:
    print("Database already exists")
    # Connect the database if exists.
    engine.connect()

# Column names
name = 'name'
rarity = 'rarity'
atk = 'atk'
substat = 'substat'

Base = declarative_base()

# Create a metadata instance
metadata = MetaData(engine)

# Tables
tables = {Table('sword', metadata,
                    Column(name, String),
                    Column(rarity, Integer),
                    Column(atk, Integer),
                    Column(substat, String)):
                    [{"name": "Dull Blade", "rarity": 1, "atk": 23, "substat": "none"},
	{"name": "Silver Sword", "rarity": 2, "atk": 33, "substat": "none"},
    {"name": "Traveler's Handy Sword", "rarity": 3, "atk": 40, "substat": "DEF"},
    {"name": "Skyrider Sword", "rarity": 3, "atk": 38, "substat": "DEF"},
    {"name": "Fillet Blade", "rarity": 3, "atk": 39, "substat": "ATK"},
    {"name": "Dark Iron Sword", "rarity": 3, "atk": 39, "substat": "Elemental Mastery"},
    {"name": "Harbinger of Dawn", "rarity": 3, "atk": 39, "substat": "CRIT DMG"},
    {"name": "Cool Steel", "rarity": 3, "atk": 39, "substat": "ATK"},
    {"name": "Favonius Sword", "rarity": 4, "atk": 41, "substat": "Energy Recharge"},
    {"name": "The Black Sword", "rarity": 4, "atk": 42, "substat": "CRIT Rate"},
    {"name": "Iron Sting", "rarity": 4, "atk": 42, "substat": "Elemental Mastery"},
    {"name": "Sword of Descension", "rarity": 4, "atk": 39, "substat": "ATK"},
    {"name": "Festering Desire", "rarity": 4, "atk": 42, "substat": "Energy Recharge"},
    {"name": "The Flute", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "Sacrificial Sword", "rarity": 4, "atk": 41, "substat": "Energy Recharge"},
    {"name": "Royal Longsword", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "Prototype Rancour", "rarity": 4, "atk": 44, "substat": "Physical DMG Bonus"},
    {"name": "Lion's Roar", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "The Alley Flash", "rarity": 4, "atk": 45, "substat": "Elemental Mastery"},
    {"name": "Blackcliff Longsword", "rarity": 4, "atk": 44, "substat": "CRIT DMG"},
    {"name": "Skyward Blade", "rarity": 5, "atk": 46, "substat": "Energy Recharge"},
    {"name": "Summit Shaper", "rarity": 5, "atk": 46, "substat": "ATK"},
    {"name": "Primordial Jade Cutter", "rarity": 5, "atk": 44, "substat": "CRIT Rate"},
    {"name": "Aquila Favonia", "rarity": 5, "atk": 48, "substat": "Physical DMG Bonus"}],
        Table('claymore', metadata,
                Column(name, String),
                Column(rarity, Integer),
                Column(atk, Integer),
                Column(substat, String)):
                [{"name": "Waster Greatsword", "rarity": 1, "atk": 23, "substat": "none"},
    {"name": "Old Merc's Pal", "rarity": 2, "atk": 33, "substat": "none"},
    {"name": "Bloodtainted Greatsword", "rarity": 3, "atk": 38, "substat": "Elemental Mastery"},
    {"name": "Debate Club", "rarity": 3, "atk": 39, "substat": "ATK"},
    {"name": "Ferrous Shadow", "rarity": 3, "atk": 39, "substat": "HP"},
    {"name": "Quartz", "rarity": 3, "atk": 40, "substat": "Elemental Mastery"},
    {"name": "Skyrider Greatsword", "rarity": 3, "atk": 39, "substat": "Physical DMG Bonus"},
    {"name": "White Iron Greatsword", "rarity": 3, "atk": 39, "substat": "DEF"},
    {"name": "Favonius Greatsword", "rarity": 4, "atk": 41, "substat": "Energy Recharge"},
    {"name": "Prototype Archaic", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "Rainslasher", "rarity": 4, "atk": 42, "substat": "Elemental Mastery"},
    {"name": "Royal Greatsword", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "The Bell", "rarity": 4, "atk": 42, "substat": "HP"},
    {"name": "Whiteblind", "rarity": 4, "atk": 42, "substat": "DEF"},
    {"name": "Serpent Spine", "rarity": 4, "atk": 42, "substat": "CRIT Rate"},
    {"name": "Lithic Blade", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "Sacrificial Greatsword", "rarity": 4, "atk": 44, "substat": "Energy Recharge"},
    {"name": "Snow-Tombed Starsilver", "rarity": 4, "atk": 44, "substat": "Physical DMG Bonus"},
    {"name": "Blackcliff Slasher", "rarity": 4, "atk": 42, "substat": "CRIT DMG"},
    {"name": "Wolf's Gravestone", "rarity": 5, "atk": 46, "substat": "ATK"},
    {"name": "The Unforged", "rarity": 5, "atk": 46, "substat": "ATK"},
    {"name": "Skyward Pride", "rarity": 5, "atk": 48, "substat": "Energy Recharge"},
    {"name": "Song of Broken Pines", "rarity": 5, "atk": 49, "substat": "Physical DMG Bonus"}],
        Table('polearm', metadata,
                Column(name, String),
                Column(rarity, Integer),
                Column(atk, Integer),
                Column(substat, String)):
                [{"name": "Beginner's Protector", "rarity": 1, "atk": 23, "substat": "none"},
    {"name": "Iron Point", "rarity": 2, "atk": 33, "substat": "none"},
    {"name": "Black Tassel", "rarity": 3, "atk": 38, "substat": "HP"},
    {"name": "Halberd", "rarity": 3, "atk": 40, "substat": "ATK"},
    {"name": "White Tassel", "rarity": 3, "atk": 39, "substat": "CRIT Rate"},
    {"name": "Deathmatch", "rarity": 4, "atk": 41, "substat": "CRIT Rate"},
    {"name": "Blackcliff Pole", "rarity": 4, "atk": 42, "substat": "CRIT DMG"},
    {"name": "Dragon's Bane", "rarity": 4, "atk": 41, "substat": "Elemental Mastery"},
    {"name": "Prototype Starglitter", "rarity": 4, "atk": 42, "substat": "Energy Recharge"},
    {"name": "Crescent Pike", "rarity": 4, "atk": 44, "substat": "Physical DMG Bonus"},
    {"name": "Favonius Lance", "rarity": 4, "atk": 44, "substat": "Energy Recharge"},
    {"name": "Royal Spear", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "Dragonspine Spear", "rarity": 4, "atk": 41, "substat": "Physical DMG Bonus"},
    {"name": "Lithic Spear", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "Primordial Jade Winged-Spear", "rarity": 5, "atk": 48, "substat": "CRIT Rate"},
    {"name": "Skyward Spine", "rarity": 5, "atk": 48, "substat": "Energy Recharge"},
    {"name": "Vortex Vanquisher", "rarity": 5, "atk": 46, "substat": "ATK"},
    {"name": "Staff of Homa", "rarity": 5, "atk": 46, "substat": "CRIT DMG"}],
        Table('bow', metadata,
                Column(name, String),
                Column(rarity, Integer),
                Column(atk, Integer),
                Column(substat, String)):
                [{"name": "Hunter's Bow", "rarity": 1, "atk": 23, "substat": "none"},
    {"name": "Seasoned Hunter's Bow", "rarity": 2, "atk": 33, "substat": "none"},
    {"name": "Ebony Bow", "rarity": 3, "atk": 40, "substat": "ATK"},
    {"name": "Raven Bow", "rarity": 3, "atk": 40, "substat": "Elemental Mastery"},
    {"name": "Sharpshooter's Oath", "rarity": 3, "atk": 39, "substat": "CRIT DMG"},
    {"name": "Recurve Bow", "rarity": 3, "atk": 38, "substat": "HP"},
    {"name": "Messenger", "rarity": 3, "atk": 40, "substat": "CRIT DMG"},
    {"name": "Slingshot", "rarity": 3, "atk": 38, "substat": "CRIT Rate"},
    {"name": "Royal Bow", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "Rust", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "The Stringless", "rarity": 4, "atk": 42, "substat": "Elemental Mastery"},
    {"name": "Sacrificial Bow", "rarity": 4, "atk": 44, "substat": "Energy Recharge"},
    {"name": "Prototype Crescent", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "The Viridescent Hunt", "rarity": 4, "atk": 42, "substat": "CRIT Rate"},
    {"name": "Blackcliff Warbow", "rarity": 4, "atk": 44, "substat": "CRIT Rate"},
    {"name": "Alley Hunter", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "Windblume Ode", "rarity": 4, "atk": 42, "substat": "Elemental Mastery"},
    {"name": "Favonius Warbow", "rarity": 4, "atk": 41, "substat": "Energy Recharge"},
    {"name": "Compound Bow", "rarity": 4, "atk": 41, "substat": "Physical DMG Bonus"},
    {"name": "Skyward Harp", "rarity": 5, "atk": 48, "substat": "CRIT Rate"},
    {"name": "Elegy for the End", "rarity": 5, "atk": 46, "substat": "Energy Recharge"},
    {"name": "Amos' Bow", "rarity": 5, "atk": 46, "substat": "ATK"}],
        Table('catalyst', metadata,
                Column(name, String),
                Column(rarity, Integer),
                Column(atk, Integer),
                Column(substat, String)):      
    [{"name": "Apprentice's Notes", "rarity": 1, "atk": 23, "substat": "none"},
    {"name": "Pocket Grimoire", "rarity": 2, "atk": 33, "substat": "none"},
    {"name": "Emerald Orb", "rarity": 3, "atk": 40, "substat": "Elemental Mastery"},
    {"name": "Otherworldly Story", "rarity": 3, "atk": 39, "substat": "Energy Recharge"},
    {"name": "Twin Nephrite", "rarity": 3, "atk": 40, "substat": "CRIT Rate"},
    {"name": "Thrilling Tales of Dragon Slayers", "rarity": 3, "atk": 39, "substat": "HP"},
    {"name": "Magic Guide", "rarity": 3, "atk": 38, "substat": "Elemental Mastery"},
    {"name": "Amber Catalyst", "rarity": 3, "atk": 40, "substat": "Elemental Mastery"},
    {"name": "Blackcliff Agate", "rarity": 4, "atk": 42, "substat": "CRIT DMG"},
    {"name": "Favonius Codex", "rarity": 4, "atk": 42, "substat": "Energy Recharge"},
    {"name": "Mappa Mare", "rarity": 4, "atk": 44, "substat": "Elemental Mastery"},
    {"name": "Prototype Amber", "rarity": 4, "atk": 42, "substat": "HP"},
    {"name": "Royal Grimoire", "rarity": 4, "atk": 44, "substat": "ATK"},
    {"name": "Sacrificial Fragments", "rarity": 4, "atk": 41, "substat": "Elemental Mastery"},
    {"name": "Solar Pearl", "rarity": 4, "atk": 42, "substat": "CRIT Rate"},
    {"name": "Eye of Perception", "rarity": 4, "atk": 41, "substat": "ATK"},
    {"name": "Frostbearer", "rarity": 4, "atk": 42, "substat": "ATK"},
    {"name": "Wine and Song", "rarity": 4, "atk": 44, "substat": "Energy Recharge"},
    {"name": "The Widsith", "rarity": 4, "atk": 42, "substat": "CRIT DMG"},
    {"name": "Skyward Atlas", "rarity": 5, "atk": 48, "substat": "ATK"},
    {"name": "Memory of Dust", "rarity": 5, "atk": 46, "substat": "ATK"}, 
    {"name": "Lost Prayer to the Sacred Winds", "rarity": 5, "atk": 46, "substat": "CRIT Rate"}]
}

for k, v in tables.items():
    # If table don't exist, Create.
    if not engine.dialect.has_table(engine.connect(), k):
        print("Creating table: ", k)
        # Create table
        k.create()

        conn = engine.connect()

        print(v)
        # insert multiple data
        conn.execute(k.insert(), v)
    else:
        print("Table already exists: ", k)

# check table exists
ins = inspect(engine)
for _t in ins.get_table_names():
    print("TableName: " + _t)
