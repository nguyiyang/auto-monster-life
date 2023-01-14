from pymem import Pymem
from pymem.ptypes import RemotePointer

pm = Pymem("Maplestory.exe")
game_module = pm.base_address

def get_ptr_addr(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset

def read_waru_value():
    try:
        state = pm.read_int(get_ptr_addr(game_module + 0x05C9B8D0, [0x30, 0x78]))
        return state
    except: return -1