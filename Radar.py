import pymem
import pymem.process
import time
from pointers import *

pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle, "client.dll")


while True:
    time.sleep(0.01)
    for i in range(1, 64):
            entity = pm.read_int(client.lpBaseOfDll + dwEntityList + i * 0x10)
            if entity:
                pm.write_int(entity + m_bSpotted, 1)