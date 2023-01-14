INTERMEDIATE_MOBS = ['nine_tailed_fox', 'victor', 'snow_giant', 'ifrit', 'griffey', 'manon', 'king_slime']

def convert_monster_name(monster_name):
        monster_name = monster_name.replace(' ', '_')
        monster_name = monster_name.replace('-', '_')
        monster_name = monster_name.replace('&', 'and')
        monster_name = monster_name.replace('.', '')
        monster_name = monster_name.replace('(', '')
        monster_name = monster_name.replace(')', '')
        monster_name = monster_name.lower()
        return monster_name

def contains(item, ls):
    res = False
    for i in ls:
        if i.get() == item:
            res = True
            break
    return res

def paste_string(autohotpy):
    autohotpy.LEFT_CTRL.down()
    autohotpy.sleep()
    autohotpy.V.down()
    autohotpy.sleep()
    autohotpy.LEFT_CTRL.up()
    autohotpy.sleep()
    autohotpy.V.up()
    autohotpy.sleep()