#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {}

# global configuration 
config["nickname"] = "KAGGatherBot"
config["servername"] = "irc.quakenet.org"
config["serverport"] = 6667
config["serverpass"] = None
config["realname"] = "Gather Bot"
config["username"] = "kgb"
config["channels"] = ["#kag2d.ru"]

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
			"maxplayers": 10,
			"create": "!on",
			"add": "!add"
		},
		{
			"name": "Gold",
			"authed": False,
			"voided": True,
			"maxplayers": 10,
			"create": "!on+",
			"add": "!add+"
		},
		{
			"name": "Sub",
			"authed": False,
			"Voiced": False,
			"maxplayers": 1,
			"create": "!sub",
			"add": "!sadd"
		},
		{
			"name": "GoldSub",
			"authed": False,
			"Voiced": True,
			"maxplayers": 1,
			"create": "!sub+",
			"add": "!sadd+"
		}
	]

if __name__ == "__main__":
	pass