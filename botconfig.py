#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {}

# global configuration 
config["nickname"] = "Lorelei"
config["servername"] = "irc.quakenet.org"
config["serverport"] = 6667
config["serverpass"] = None
config["realname"] = "Gather Bot"
config["username"] = "kgb"
config["channels"] = ["#kag2d.ru"]
config["color1"] = 8
config["color2"] = 6

# server configuration
config["servers"] = [
		{
			"name": "Baal",
			"ip": "192.168.1.1",
			"port": 1234,
			"password": "baal",
			"trigger": "!baal"
		}
	]
# game modes
config["modes"] = [
		{
			"name": "Normal",
			"authed": False,
			"voiced": False,
			"maxplayers": 5,
			"create": "!on",
			"add": "!add",
			"off": "!off",
			"color1": 7,
			"color2": 3,
			"balance": True,
			"servers": ["Baal"]
		},
		{
			"name": "Gold",
			"authed": False,
			"voiced": True,
			"maxplayers": 4,
			"create": "!on+",
			"add": "!add+",
			"off": "!off+",
			"color1": 3,
			"color2": 4,
			"balance": False,
			"servers": ["Baal"]
			}
#		},
#		{
#			"name": "Sub",
#			"authed": False,
#			"voiced": False,
#			"maxplayers": 1,
#			"create": "!sub",
#			"add": "!sadd",
#			"color1": 9,
#			"color2": 1
#		},
#		{
#			"name": "GoldSub",
#			"authed": False,
#			"voiced": True,
#			"maxplayers": 1,
#			"create": "!sub+",
#			"add": "!sadd+",
#			"color1": 6,
#			"color2": 4
#		}
	]

if __name__ == "__main__":
	pass
