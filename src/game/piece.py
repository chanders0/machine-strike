class Piece:
    def __init__(self, name, machine_type, health, attack_power, attack_range, movement, armor, weaknesses, points, skill, rarity, x = None, y = None):
        self.name = name
        self.type = machine_type
        self.health = health
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.movement = movement
        self.armor = armor
        self.weaknesses = weaknesses
        self.points = points
        self.skill = skill
        self.rarity = rarity
        self.x = x
        self.y = y

    def is_alive(self):
        return self.health > 0
    
    def combat_power(self, tile_height):
        return self.attack_power + tile_height
    
    # machines
    def Behemoth():
        return Piece("Behemoth","Gunner",10,3,2,2,["Front"],["Left","Right"],5,"Shield","Rare",None,None)
    
    def Bellowback():
        return Piece("Bellowback","Gunner",7,3,2,2,["Front"],["Back","Left","Right"],3,"Spray","Uncommon",None,None)
    
    def Bilegut():
        return Piece("Bilegut","Pull",9,3,3,2,["Left","Right"],["Front"],5,"Alter Terrain","Rare",None,None)
    
    def Bristleback():
        return Piece("Bristleback","Ram",4,2,1,3,["Front"],["Back"],2,"Spray","Uncommon",None,None)
    
    def Burrower():
        return Piece("Burrower","Melee",4,2,1,2,["Front"],["Back"],1,"None","Common",None,None)
    
    def TrackerBurrower():
        return Piece("Tracker Burrower","Melee",4,2,1,2,["Front"],["Back"],2,"Alter Terrain","Common",None,None)
    
    def Charger():
        return Piece("Charger","Dash",4,2,2,3,["Front"],["Back"],2,"Gallop","Uncommon",None,None)
    
    def Clamberjaw():
        return Piece("Clamberjaw","Melee",8,3,1,3,["Front"],["Back"],4,"Stalk","Rare",None,None)
    
    def Clawstrider():
        return Piece("Clawstrider","Melee",8,3,2,2,["Front"],["Back"],3,"None","Uncommon",None,None)
    
    def ElementalClawstrider():
        return Piece("Elemental Clawstrider","Gunner",8,3,2,2,["Front"],["Back"],4,"Burn","Rare",None,None)
    
    def ApexClawstrider():
        return Piece("Apex Clawstrider","Melee",8,3,1,2,["Front","Left","Right"],["Back"],5,"Retaliate","Uncommon",None,None)
    
    def Dreadwing():
        return Piece("Dreadwing","Swoop",9,3,3,2,["Front"],["Back"],5,"Whiplash","Rare",None,None)
    
    def Fanghorn():
        return Piece("Fanghorn","Ram",5,2,2,2,["Front"],["Left","Right"],32,"High Ground","Uncommon",None,None)
    
    def Fireclaw():
        return Piece("Fireclaw","Melee",10,4,2,3,["Front"],["Back"],7,"Burn","Legendary",None,None)
    
    def Frostclaw():
        return Piece("Frostclaw","Melee",10,4,2,2,["Left","Right"],["Front"],7,"Freeze","Rare",None,None)
    
    def Glinthawk():
        return Piece("Glinthawk","Swoop",5,2,3,3,["Back"],["Front"],2,"None","Uncommon",None,None)
    
    def Grazer():
        return Piece("Grazer","Ram",4,1,1,2,["Front"],["Left","Right"],1,"Gallop","Common",None,None)
    
    def Lancehorn():
        return Piece("Lancehorn","Ram",5,2,2,2,["Front"],["Left","Right"],2,"Climb","Uncommon",None,None)
    
    def Leaplasher():
        return Piece("Leaplasher","Melee",3,1,1,4,["Front"],["Back"],1,"Empower","Common",None,None)
    
    def Longleg():
        return Piece("Longleg","Gunner",6,1,2,4,["Front"],["Back"],2,"Empower","Uncommon",None,None)
    
    def Plowhorn():
        return Piece("Plowhorn","Ram",5,2,1,2,["Front"],["Back"],1,"Growth","Uncommon",None,None)
    
    def Ravager():
        return Piece("Ravager","Gunner",9,2,2,2,["Front"],["Back"],4,"Sweep","Uncommon",None,None)
    
    def RedeyeWatcher():
        return Piece("Redeye Watcher","Gunner",5,2,2,2,["Left","Right"],["Front"],3,"Blind","Uncommon",None,None)
    
    def Rockbreaker():
        return Piece("Rockbreaker","Gunner",9,3,2,3,["Left","Right"],["Back"],6,"Alter Terrain","Rare",None,None)
    
    def Rollerback():
        return Piece("Rollerback","Melee",5,3,2,3,["Front","Left","Right"],["Back"],4,"Retaliate","Rare",None,None)
    
    def Scorcher():
        return Piece("Scorcher","Dash",12,4,2,2,["Front"],["Back"],8,"Burn","Rare",None,None)
    
    def Scrapper():
        return Piece("Scrapper","Gunner",5,3,2,2,["Front"],["Back"],2,"None","Common",None,None)
    
    def Scrounger():
        return Piece("Scrounger","Melee",4,2,1,3,["Front"],["Back"],1,"None","Common",None,None)
    
    def ShellWalker():
        return Piece("Shell Walker","Melee",7,2,1,2,["Front","Right"],["Back"],3,"Shield","Uncommon",None,None)
    
    def Shellsnapper():
        return Piece("Shellsnapper","Pull",10,3,3,2,["Back","Left","Right"],["Front"],6,"None","Rare",None,None)
    
    def Skydrifter():
        return Piece("Skydrifter","Swoop",6,2,3,2,["Front"],["Back"],2,"None","Uncommon",None,None)
    
    def Slaughterspine():
        return Piece("Slaughterspine","Melee",15,4,1,2,["Front"],["Left","Right"],10,"Spray","Legendary",None,None)
    
    def Slitherfang():
        return Piece("Slitherfang","Dash",12,4,3,2,["Front"],["Back"],9,"Alter Terrain","Rare",None,None)
    
    def Snapmaw():
        return Piece("Snapmaw","Pull",7,3,3,2,["Front"],["Back"],3,"None","Uncommon",None,None)
    
    def Spikesnout():
        return Piece("Spikesnout","Melee",5,2,1,2,["Front"],["Back"],1,"None","Common",None,None)
    
    def Stalker():
        return Piece("Stalker","Melee",5,4,2,3,["Front"],["Back"],4,"Stalk","Rare",None,None)
    
    def Stormbird():
        return Piece("Stormbird","Swoop",9,3,3,3,["Back"],["Front"],6,"Sweep","Rare",None,None)
    
    def Sunwing():
        return Piece("Sunwing","Swoop",7,3,2,3,["Back"],["Front"],3,"None","Uncommon",None,None)
    
    def Thunderjaw():
        return Piece("Thunderjaw","Dash",10,3,2,3,["Front","Back"],["Left","Right"],6,"Sweep","Rare",None,None)
    
    def Tideripper():
        return Piece("Tideripper","Pull",10,4,3,2,["Left","Right"],["Back"],6,"None","Rare",None,None)
    
    def Tremortusk():
        return Piece("Tremortusk","Dash",10,3,2,2,["Front"],["Back"],5,"Sweep","Rare",None,None)
    
    def Waterwing():
        return Piece("Waterwing","Pull",8,2,2,3,["Back"],["Front"],4,"Whiplash","Rare",None,None)
    
    def Widemaw():
        return Piece("Widemaw","Pull",7,3,2,2,["Front"],["Back"],3,"None","Uncommon",None,None)
    