common_spells = ('Crucio', 'Avadakedavra', 'Imperio', 'sheild')
harry_spells = ('Reducto', 'Friend fyre', 'Nebulus')
Voldmort_spells = ('Taboo', 'Expulso', 'Confringo')
value_of_spells = {'Crucio': 40, 'AvadaKedavra': 100, 'Imperio': 20, 'sheild': 0, 'Reducto': 60,
                   'Friendfyre': 50, 'Nebulus': 40, 'Taboo': 80, 'Expulso': 60, 'Confringo': 55}

#####################################################
class Wizard:                 ## parent class contain the common functions
    def __init__(self, health, energy, num_shield):
        self.health = health
        self.energy = energy
        self.num_shield = num_shield

    def compare(self, h_s, v_s):    ## function compare value of spells and return the difference
        self.h_s = h_s
        self.v_s = v_s
        if value_of_spells[h_s] > value_of_spells[v_s]:
            value = value_of_spells[h_s] - value_of_spells[v_s]

        else:
            value = value_of_spells[v_s] - value_of_spells[h_s]
        return value

    def crucio(self):                    ## function minus crucio energy

        self.energy -= value_of_spells['Crucio']
        return self.energy

    def AvadaKedavra(self):             ## function minus AvadaKedavra energy

        self.energy -= value_of_spells['AvadaKedavra']
        return self.energy

    def Imperio(self):                     ## function minus Imperio energy

        self.energy -= value_of_spells['Imperio']
        return self.energy

    def sheild(self):            #### function check number of sheilds
        if  self.num_shield > 0:
            self.num_shield -= 1  ## minus one every time we use it
            return 1
        else:
            return 0
####################################################
class Harry(Wizard):     ## class harry contain special function and common
    def Reducto(self):
        self.energy -= value_of_spells['Reducto']
        return self.energy
    def Friend_fyre(self):
        self.energy -= value_of_spells['Friendfyre']
        return self.energy
    def Nebulus(self):
        self.energy -= value_of_spells['Nebulus']
        return self.energy

        ######################################
class Voldmort(Wizard):                  ## class Voldmort contain special function and common
    def Taboo(self):
        self.energy -= value_of_spells['Taboo']
        return self.energy
    def Expulso(self):
        self.energy -= value_of_spells['Expulso']
        return self.energy
    def Confringo(self):
        self.energy -= value_of_spells['Confringo']
        return self.energy

        #################################
harry = Harry(100, 500, 3)       ### object from class Harry // health=100//energy =500//number of sheilds =3
vold = Voldmort(100, 500, 3)          ### object from class Voldmort // health=100//energy =500//number of sheilds =3

############################
while harry.health > 0 and vold.health > 0:   ## if harry and voldmort still alive
    print("Enter the two spells (harry then voldemort) ")
    spell_H ,spell_V = input().split()
    x = harry.compare(spell_H, spell_V)
    print("\t" " Harry "  "\t"  " voldmort ")
################################################
    if spell_H == "Crucio":
        if harry.energy >= 40:
            harry_energy = harry.crucio()
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x

            else:
                harry.health -= x
        else:
            print(" you cant use this try another one harry ")

  #######################################################
    elif spell_H == "AvadaKedavra":
        if harry.energy >= 100:
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x

            else:
                harry.health -= x
            harry_energy = harry.AvadaKedavra()
        else:
            print(" you cant use this try another one harry  ")

            #######################################################
    elif spell_H == "Imperio":
        if harry.energy >= 20:
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x

            else:
                harry.health -= x
            harry_energy = harry.Imperio()
        else:
            print(" you cant use this try another one harry  ")

            ################################################
    elif spell_H == "Reducto":
        if harry.energy >= 60:
            harry_energy = harry.Reducto()
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x
            else:
                harry.health -= x
        else:
            print(" you cant use this try another one harry  ")

            ##################################################
    elif spell_H == "Friendfyre":
        if harry.energy >= 50:
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x
            else:
                harry.health -= x
            harry_energy = harry.Friend_fyre()
        else:
            print(" you cant use this try another one harry  ")

######################################################
    elif spell_H == "Nebulus":
        if harry.energy >= 40:
            if value_of_spells[spell_V] == 0:
                flag_v = vold.sheild()
                if flag_v == 0:
                    vold.health -= x
            elif value_of_spells[spell_H] > value_of_spells[spell_V]:
                vold.health -= x
            else:
                harry.health -= x
            harry_energy = harry.Nebulus()

        else:
            print(" you cant use this try another one harry  ")

    ######################################################
    if spell_V == "Crucio":
        if vold.energy >= 40:
            vold_energy = vold.crucio()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort ")

            ########################################
    elif spell_V == "AvadaKedavra":
        if vold.energy >= 100:
            vold_energy = vold.AvadaKedavra()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort  ")

            #####################################
    elif spell_V == "Imperio":
        if vold.energy >= 20:
            vold_energy = vold.Imperio()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort  ")

            ###############################################
    elif spell_V == "Taboo":
        if vold.energy >= 80:
            vold_energy = vold.Taboo()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort  ")

            #############################
    elif spell_V == "Expulso":
        if vold.energy >= 60:
            vold_energy = vold.Expulso()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort  ")

            ###################################
    elif spell_V == "Confringo":
        if vold.energy >= 55:
            vold_energy = vold.Confringo()
            if value_of_spells[spell_H] == 0:
                flag_h = harry.sheild()
                if flag_h == 0:
                    harry.health -= x
        else:
            print(" you cant use this try another one Voldemort  ")

            #############################################
    print("Health : {} \t {}".format(harry.health, vold.health))
    print("Energy : {} \t {}".format(harry.energy, vold.energy))
if harry.health == 0:
    print("Voldmort is the winner")
elif vold.health == 0:
    print("Harry is the winner")
