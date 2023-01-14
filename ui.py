import tkinter as tk
from tkinter import ttk
from AutoHotPy import AutoHotPy
from backend import *
import pyperclip as pc
import math
import pyautogui
from common import *
from WindowMgr import *
import time

class App(tk.Tk):
    def __init__(self, autohotpy):
        super().__init__()
        self.autohotpy = autohotpy  #Initialize the library

        self.geometry('1800x500+50+50')

        # form with checkboxes for each monster and a submit button to collect all the monster names to fuse
        self.monster_recipe = {
            "Oberon": ("Dunas", "Spirit Of Light"), 
            "Reinforced Beryl": ("Beryl", "Aufheben"), 
            "Master Jackson": ("Captain Black Slime", "Dodo"),

            "Awakened Rock Spirit": ("Spirit Of Rock", "Spirit Of Disharmony"),
            "Master Margana": ("Asmodian Black Magician", "Halloween Knight"),
            "Master Relic": ("Asmodian Chaser", "Guwaru's Vestige"),
            "Master Hisop ": ("Asmodian Predator", "Ergoth"),
            "Master Red Nirg ": ("Asmodian History", "Prison Guard Ani"),
            "Grown-up Mir": ("Growing Mir", "Growing Mir"),
            "Petite Lania": ("Petite Luminous (Equilibrium)", "Petite Cygnus"),

            "Typhon": ("Xerxes", "Freezer"),
            "Ephenia": ("Pixiemom", "Ancient Slime"),
            "Mu Gong's Shadow": ("Master Dummy", "Tae Roon"),
            "Mir": ("Manon", "Lupin Pig"),
            "Petite Luminous (Dark)": ("King Slime", "Papulatus' Watch"),
            "Shadow of Black Mage": ("Petite Luminous (Dark)", "Master Omen"),
            "Petite Luminous (Equilibrium)": ("Petite Luminous (Light)", "Petite Luminous (Dark)"),

            "Petite Hilla": ("Riche", "Elite Bloodfang"),
            "Romancist KS": ("King Slime", "Yeti Couple"),
            "Petite Horntail": ("Leviathan", "Snow Witch"),
            "Petite Phantom": ("Moon Bunny Thief", "Romancist KS"),
            "Lazuli": ("Eye of Time", "Petite Hilla"),
            "Black Viking": ("Viking Legion", "Sober Viking"),
            "Petite Cygnus": ("shinsoo", "oberon"),

            "Scarecrow": ("Thief Crow", "Petite Arkarium"),
            "Petite Von Leon": ("Lilynouch", "Toy Black Knight"),
            "Lil Moonbeam": ("Nine-Tailed Fox", "Petite Orchid"),
            "Pierre": ("Jr Balrog", "Targa"),
            "Petite Magnus": ("Crimson Balrog", "Apsu"),
            "Lapis" : ("Eye of Time", "Ifrit"),
            "Tin Woodman": ("Inner Rage", "Victor"),

            "Jr. Balrog": ("Mini Bean", "Reaper Specter"),
            "Crimson Balrog": ("Jack-O-Lantern", "Pirate King Barbosa"),
            "Pharaoh Yeti": ("Yeti and Pepe", "Pharaoh Mummy"),
            "Twin Halloween Bunnies": ("Moon Bunny", "Couple Mushrooms Celebrating Their 100th Day Together"),
            "Aufheben": ("MT-09", "Iruvata"),
            "Petite Orchid": ("Snow Giant", "Twin Halloween Bunnies"),
            "Petite Mercedes": ("Reinforced Beryl", "Ephenia"),

            "Moon Bunny Thief": ("Moon Bunny", "Moonlight Thief"),
            "Petite Arkarium": ("Timer", "Nether Monk"),
            "Von Bon": ("Pink Bean", "Griffey"),
            "Commander Will": ("Giant Spider", "Big Operator Balloon"),
            "Yeti Couple": ("Gold Yeti and King Pepe", "Panda Bear In Love"),
            "Bully Jack": ("Giant", "Halloween Pumpkin"),
            "Big Operator's Balloon": ("Small Operator Balloon", "Small Operator Balloon"),

            "Petite Eunwol": ("Petite Luminous (Light)", "Petite Phantom"),
            "Giant Dark Soul": ("Giant", "Dark Soul"),
            "King Castle Golem": ("Giant", "Castle Golem"),
            "Inner Rage": ("Spirit of Rock", "Strange Monsters"),
            "Small Operator Balloon": ("Pierre", "Prime Minister"),
        }

        self.monster_list = list(self.monster_recipe.keys())

        lt = list(self.monster_recipe.values())
        self.monster_ingredient_list = [item for t in lt for item in t]

        self.selected_monster_list = []
        for i in range(len(self.monster_list)):
            self.selected_monster_list.append(tk.StringVar())

        self.selected_monster_ingredient_list = []
        for i in range(len(self.monster_ingredient_list)):
            self.selected_monster_ingredient_list.append(tk.StringVar())


        self.monster_list_label = ttk.Label(self, text="Monsters to fuse:").grid(row=0)
        # Define a Checkbox
        for x in range(len(self.monster_list)):
            self.l = ttk.Checkbutton(self, text=self.monster_list[x], variable=self.selected_monster_list[x], onvalue=self.monster_list[x], offvalue="", compound=tk.LEFT).grid(row=x%10 + 1,column=math.floor(x/10))

        self.monster_ingredient_list_label = ttk.Label(self, text="Monsters owned:").grid(row=15)
        for x in range(len(self.monster_ingredient_list)):
            self.l = ttk.Checkbutton(self, text=self.monster_ingredient_list[x], variable=self.selected_monster_ingredient_list[x], onvalue=self.monster_ingredient_list[x], offvalue="", compound=tk.LEFT).grid(row=x%10 + 20,column=math.floor(x/10))
        
        self.submit = ttk.Button(self, text="Fuse", command=self.start).grid(row=50)

    def go_to_farm(self, autohotpy, str):
        pc.copy(str)
        x, y = pyautogui.locateCenterOnScreen('images/view_friends_list.png', confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.1)
        x, y = pyautogui.locateCenterOnScreen('images/enter_farm_name.png', confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.1)
        paste_string(autohotpy)
        x, y = pyautogui.locateCenterOnScreen('images/tick.png', confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(4)

    def find_monster(self, monster_to_fuse_with):
        print("Looking for monster..")
        # look for monster
        found = False
        count = 0
        x_next, y_next = pyautogui.locateCenterOnScreen('images/next.png', confidence=0.7)
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('images/{monster_name}.png'.format(monster_name=monster_to_fuse_with), confidence=0.9)
                time.sleep(1)
                print("Monster found..")
                found = True
                break
            except:
                if count == 20:
                    break
                else:
                    pyautogui.click(x_next, y_next)
                    time.sleep(0.1)
                    count += 1
        
        return found

    def fuse_monster(self, monster_name):
        print("Fusing monster..")
        # fuse
        pyautogui.rightClick(x, y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('images/fuse.png', confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.5)
        self.autohotpy.ENTER.press()
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('images/{monster_name}.png'.format(monster_name=monster_name), confidence=0.7)
        pyautogui.click(x, y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('images/combine.png', confidence=0.7)
        pyautogui.click(x, y)
        time.sleep(0.5)
        self.autohotpy.ENTER.press()
        time.sleep(0.5)
        self.autohotpy.ENTER.press()
        time.sleep(5)

    def is_ss_monster(self):
        is_ss = False
        try:
            x, y = pyautogui.locateCenterOnScreen('images/ok.png', confidence=0.5)
            pyautogui.click(x, y)
            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen('images/release.png', confidence=0.7)
            pyautogui.click(x, y)
            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen('images/tick.png', confidence=0.7)
            pyautogui.click(x, y)
            time.sleep(0.5)
            self.autohotpy.ENTER.press()
            time.sleep(0.5)
        except:
            is_ss = True
        time.sleep(3)
        return is_ss

    def is_special_monster(self, target_monster):
        is_special = False
        # if fuse success, break
        try:
            time.sleep(2)
            x, y = pyautogui.locateCenterOnScreen('images/special.png', confidence=0.7)
            time.sleep(1)
            print("{monster_name} successfully fused".format(monster_name=target_monster.get()))
            x, y = pyautogui.locateCenterOnScreen('images/save_to_farm.png', confidence=0.7)
            pyautogui.click(x, y)
            time.sleep(0.5)
            self.autohotpy.ENTER.press()
            time.sleep(0.5)
            is_special = True
        except Exception as e:
            print(e)
            print("Fuse unsuccessful, finding another farm")
            time.sleep(3)
            # release
            x, y = pyautogui.locateCenterOnScreen('images/release.png', confidence=0.7)
            pyautogui.click(x, y)
            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen('images/tick.png', confidence=0.7)
            pyautogui.click(x, y)
            time.sleep(0.5)
            self.autohotpy.ENTER.press()
            time.sleep(0.5)
        return is_special


    def start(self):
        # Open MapleStory window
        w = WindowMgr()
        w.find_window_wildcard(".*MapleStory.*")
        w.set_foreground()

        for selected_monster in self.selected_monster_list:
            if selected_monster.get() != "":
                print(selected_monster.get())
                # fuse monster
                # get list of farms
                ingredients = self.monster_recipe.get(selected_monster.get())
                res = None
                monster_to_fuse_with = None
                my_monster = None
                if contains(ingredients[0], self.selected_monster_ingredient_list):
                    my_monster = convert_monster_name(ingredients[0])
                    monster_to_fuse_with = convert_monster_name(ingredients[1])
                    res = get_farm_list(monster_to_fuse_with)
                elif contains(ingredients[1], self.selected_monster_ingredient_list):
                    my_monster = convert_monster_name(ingredients[1])
                    monster_to_fuse_with = convert_monster_name(ingredients[0])
                    res = get_farm_list(monster_to_fuse_with)
                else:
                    print("You don't have the monsters to fuse for {monster_name}".format(monster_name=selected_monster.get()))
                
                print(res)
                    
                # if monster is owned
                if res != None:
                    for i in res:
                        print(i[0])
                        if i[0] == "":
                            continue
                        # visit farm
                        self.go_to_farm(self.autohotpy, i[0])

                        is_found = self.find_monster(monster_to_fuse_with)

                        if is_found:

                            self.fuse_monster(my_monster)

                            is_ss = self.is_ss_monster()
                            if not is_ss:
                                continue
                            
                            is_special = self.is_special_monster(selected_monster)
                            if is_special:
                                break
                            
