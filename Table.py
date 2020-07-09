import pymem
import pymem.process
import time
from tabulate import tabulate
import os
from pointers import *


pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle, "client.dll")
clear = lambda: os.system('cls')

def AllPlayers():
    players = 1
    for i in range(1, 64):
        entity = pm.read_int(client.lpBaseOfDll + dwEntityList + i * 0x10)
        if entity:
            players = players + 1
    return players

def Name(i):
    try:
        radar_base = pm.read_int(client.lpBaseOfDll + dwRadarBase)
        radar = pm.read_int(radar_base + 0x74)
        name = pm.read_string(radar + 0x300 + (0x174 * (i - 1)))
        return name
    except:
        return "???"

def Team(i):
    entity = pm.read_int(client.lpBaseOfDll + dwEntityList + (i - 1) * 0x10)
    if entity:
        entity_team_id = pm.read_int(entity + m_iTeamNum)
        if(entity_team_id == 2):
            return "Terrorist"
        elif(entity_team_id == 3):
            return "Counter-terrorist"
        else:
            return "???"
    else:
        return "???"

def Health(i):
    entity = pm.read_int(client.lpBaseOfDll + dwEntityList + (i - 1) * 0x10)
    if entity:
        return pm.read_int(entity + m_iHealth)
    return "???"

def Table():
    clear()
    cont = [(i, Team(i), Name(i), Health(i), pm.read_int(client.lpBaseOfDll + dwEntityList + (i - 1) * 0x10)) for i in range(1, AllPlayers() + 1)]
    print(tabulate(cont, headers=["Index", "Team", "Name", "Health", "ID"], tablefmt="grid"))

while True:
    time.sleep(1)
    Table()




            