#made by Sankeerthikan Nimalathas


#search for the element and know the name, symbol, atomic number, atomic mass, Neutrons, Protons, Electrons of it . 
#able to do some basic conversion to check their work such as converting from mols to atoms, mols to grams, or grams to atoms,and grams to mol.


def my_lists():
    # below are lists that are made globally accessible to all functions in the program 
    global elements
       #list of elements in order by atomic number
    elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
    global symbols    
        #list of symbols in order by atomic number 
    symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
    global atomic_numbers 
        #atomic numbers to 118 since the symbols and elements are in order by atomic number
    atomic_numbers = [x for x in range(1,119)] 
    global atomic_mass_numbers 
        #list of atomic mass numbers in order by atomic number, last 10-20 numbers may not be accurate since different websites have different values. some websites used(https://mccord.cm.utexas.edu/chembook/page-nonav.php?chnum=1&sect=5, https://www.webelements.com)
    atomic_mass_numbers = [1.00797,4.00260,6.941,9.01218,10.81,12.011,14.0067,15.9994,18.998403,20.179,22.98977,24.305,26.98154,28.0855,30.97376,32.06,35.453,39.0983,39.948,40.08,44.9559,47.90,50.9415,51.996,54.9380,55.847,58.70,58.9332,63.546,65.38,69.72,72.59,74.9216,78.96,79.904,83.80,85.4678,87.62,88.9059,91.22,92.9064,95.94,98,101.07,102.9055,106.4,107.868,112.41,114.82,118.69,121.75,126.9045,127.60,131.30,132.9054,137.33,138.9055,140.12,140.9077,144.24,145,150.4,151.96,157.25,158.9254,162.50,164.9304,167.26,168.9342,173.04,174.967,178.49,180.9479,183.85,186.207,190.2,192.22,195.09,196.9665,200.59,204.37,207.2,208.9804,209,210,222,223,226.0254,227.0278,231.0359,232.0381,237.0482,238.029,242,243,247,247,250,251,252,255,256,257,258,260,261,262,269,264,269,278,281,282,285,286,289,289 ,293,294,294]
        # rounds the atomic mass numbers to 3 decimal places if it has more decimals
    atomic_mass_numbers = [round(x, 3) for x in atomic_mass_numbers]

def menu():
     # displays the instructions
        print('''
              NAME SEARCH: Find atomic number, name, and symbol
              PROPERTY SEARCH: Find mass number, protons, electrons
              CONVERSION: Find the number of mols, grams, or atoms
              TABLE: shows the periodic table again
              '''+ '\n')    
           
# This function is a graphic of the periodic table 
def periodic_table():
    # to make underline '_'
    class under_line:
        end = '\033[0m' # end of underline
        start = '\033[4m' # start of underline
    # when underlining, the underline will be under the entire length of the string, so i had to seperate each row and print them individually
    a1 = under_line.start +'|H |    '+ under_line.end
    a2 = under_line.start +'___________________| He|'+under_line.end
    b1 = under_line.start +'|Li| Be|'+under_line.end
    b2 = under_line.start +'| B | C | N | O | F | Ne|'+under_line.end
    c1 = under_line.start +'|Na| Mg|                                       | Al| Si| P | S | Cl| Ar|'+under_line.end
    d = under_line.start +'|K | Ca| Sc| Ti| V | Cr| Mn| Fe| Co| Ni| Cu| Zn| Ga| Ge| As| Se| Br| Kr|'+under_line.end
    e = under_line.start +'|Rb| Sr| Y | Zr| Nb| Mo| Tc| Ru| Rh| Pd| Ag| Cd| In| Sn| Sb| Te| I | Xe|'+under_line.end
    f = under_line.start +'|Cs| Ba| La| Hf| Ta| W | Re| Os| Ir| Pt| Au| Hg| Tl| Pb| Bi| Po| At| Rn|'+under_line.end
    g = under_line.start +'|Fr| Ra| Ac| Rf| Db| Sg| Bh| Hs| Mt| Ds| Rg| Cn| Nh| Fl| Mc| Lv| Ts| Og|'+under_line.end
    print('\n'+ "___                "+under_line.start + "Periodic Table of Elements"+under_line.end)
    print (a1 + "                                        " + a2)
    print (b1 + "                                       " + b2)
    print(c1)
    print(d)
    print(e)
    print(f)
    print(g)
    print("       " + under_line.start +'|Ce| Pr| Nd| Pm| Sm| Eu| Gd| Tb |Dy | Ho| Er| Tm| Yb| Lu|'+ under_line.end)
    print("       " + under_line.start +'|Th| Pa| U | Np| Pu| Am| Cm| Bk | Cf| Es| Fm| Md| No| Lr|'+ under_line.end+ '\n')

 # This function called name provides the atomic number, name, symbol and mass   
def name():
    # if the user inputs the name of the element that is in the list elements, print the symbol, number and mass
    if input_element in elements:
        # since the list of symbols were all capitalized to prevent case sensitivity, to print them as usual (first letter capital and second lowercase), we use .capitalize()
        print("Symbol: "+  symbols[elements.index(input_element)].capitalize())
        # find the value of the atomic number in the list by indexing 
        print("Atomic Number:" + str(atomic_numbers[elements.index(input_element)]))
        # find the value of the atomic mass in the list by indexing
        print("Atomic Mass: "  + str(atomic_mass_numbers[elements.index(input_element)]))    
    # if the user inputs the symbol of the element that is in the list symbols, print the name, number and mass
    elif input_element in symbols:
        # find the value of the element in the list by indexing
        print("Element: " + elements[symbols.index(input_element)].capitalize())
        # find the value of the atomic number in the list by indexing
        print("Atomic Number: " + str(atomic_numbers[symbols.index(input_element)]))
        # find the value of the atomic mass in the list by indexing
        print("Atomic Mass: " + str(atomic_mass_numbers[symbols.index(input_element)]))
    # if the user inputs the atomic number of the element that is in the list of atomic numbers, print the name, symbol and mass
    elif input_element.isdigit():  
        if int(input_element) <= 118: # checks if the input is a number less than 118
            # find the value of the element in the list by indexing
            print("Element: " + elements[atomic_numbers.index(int(input_element))].capitalize())
            # find the value of the symbol in the list by indexing
            print("Symbol: " + symbols[atomic_numbers.index(int(input_element))].capitalize())
            # find the value of the atomic mass in the list by indexing
            print("Atomic Mass: " + str(atomic_mass_numbers[atomic_numbers.index(int(input_element))]))
        else:
            # reminds user to input a number less than 119
            print("Hint: there are only 118 elements in the periodic table")
    else:
        # if the element does not exist, it prints the following
        print("Invalid input" + "\nPlease Try Again")
        

 # this function called property provides the properties of the element such as the protons, neutrons, electrons, and name  period number         
def property():        
    # if the user inputs the name of the element that is in the list elements, print the symbol, protons, electrons and neutrons
    if input_element in elements:
        # since the list of symbols were all capitalized to prevent case sensitivity, to print them as usual (first letter capital and second lowercase), we use .capitalize()
        print(f"Symbol: {symbols[elements.index(input_element)].capitalize()} for {elements[elements.index(input_element)].capitalize()}" )
        # proton number is the atomic number
        print("Protons: " + str(atomic_numbers[elements.index(input_element)]))
        #electrons are equal to protons
        print("Electrons: " + str(atomic_numbers[elements.index(input_element)]))
        # neutrons = atomic mass - protons
        print("Neutrons: " + str(round(atomic_mass_numbers[elements.index(input_element)] - atomic_numbers[elements.index(input_element)])))
    # if the user inputs the symbol of the element that is in the list symbols, print the name, protons, electrons and neutrons
    elif input_element in symbols:
        print("The Element: " + elements[symbols.index(input_element)].capitalize())
        # protons = atomic number
        print("Protons: " + str(atomic_numbers[symbols.index(input_element)]))
        # electrons are equal to the number of protons
        print("Electrons: " + str(atomic_numbers[symbols.index(input_element)]))
        # neutrons = atomic mass - protons
        print("Neutrons: " + str(round(atomic_mass_numbers[symbols.index(input_element)] - atomic_numbers[symbols.index(input_element)])))
    # if the user inputs the atomic number of the element that is in the list of atomic numbers, print the name, symbol, protons, electrons and neutrons
    elif input_element.isdigit(): # checks if the input is a number less than 118
        if int(input_element) <= 118:
            print(f"Symbol: {symbols[atomic_numbers.index(int(input_element))].capitalize()} for {elements[atomic_numbers.index(int(input_element))].capitalize()}")
            #protons are equal to the atomic number
            print("Protons: " + str(atomic_numbers[atomic_numbers.index(int(input_element))]))
            #electrons are equal to the atomic number
            print("Electrons: " + str(atomic_numbers[atomic_numbers.index(int(input_element))]))
            #neutrons is the atomic mass number minus the atomic number
            print("Neutrons: " + str(round(atomic_mass_numbers[atomic_numbers.index(int(input_element))] - atomic_numbers[atomic_numbers.index(int(input_element))])))
        else:
            # reminds user to input a number less than 119
            print("Hint: there are only 118 elements in the periodic table")          
    else:
    # if the element does not exist, it prints the following
        print("Invalid input" + "\nPlease Try Again")
        
# this function is to find which period the element is in using ranges since the atomic numbers are in numerical order        
def period():
    #if the element name is input and the atomic numbers are in range for each period, it prints the period number. this is possible since the lists are in numerical order
    if input_element in elements:
        if atomic_numbers[elements.index(input_element)] in range(1,3):
            print("Period: 1")
        elif atomic_numbers[elements.index(input_element)] in range(3,11):
            print("Period: 2")
        elif atomic_numbers[elements.index(input_element)] in range(11,19):
            print("Period: 3")
        elif atomic_numbers[elements.index(input_element)] in range(19,37):
            print("Period: 4")
        elif atomic_numbers[elements.index(input_element)] in range(37,55):
            print("Period: 5")
        elif atomic_numbers[elements.index(input_element)] in range(55,87):
            print("Period: 6")
        elif atomic_numbers[elements.index(input_element)] in range(87,119):
            print("Period: 7")
    # if the element symbol is input and the atomic numbers are in range for each period, it prints the period number
    elif input_element in symbols:
        if atomic_numbers[symbols.index(input_element)] in range(1,3):
            print("Period: 1")
        elif atomic_numbers[symbols.index(input_element)] in range(3,11):
            print("Period: 2")
        elif atomic_numbers[symbols.index(input_element)] in range(11,19):
            print("Period: 3")
        elif atomic_numbers[symbols.index(input_element)] in range(19,37):
            print("Period: 4")
        elif atomic_numbers[symbols.index(input_element)] in range(37,55):
            print("Period: 5")
        elif atomic_numbers[symbols.index(input_element)] in range(55,87):
            print("Period: 6")
        elif atomic_numbers[symbols.index(input_element)] in range(87,119):
            print("Period: 7")
    # if the atomic number is input and the atomic numbers are in range for each period, it prints the period number
    elif input_element.isdigit():# checks if the input is a number
        if int(input_element) in range(1,3):
            print("Period: 1")
        elif int(input_element) in range(3,11):
            print("Period: 2")
        elif int(input_element) in range(11,19):
            print("Period: 3")
        elif int(input_element) in range(19,37):
            print("Period: 4")
        elif int(input_element) in range(37,55):
            print("Period: 5")
        elif int(input_element) in range(55,87):
            print("Period: 6")
        elif int(input_element) in range(87,119):
            print("Period: 7")
            
# below are the functions for the conversions  
def mol_to_atoms():
    # enter the number of mols
    mols = float(input("Enter the number of mols: "))
    # if the input is in the list of elements, multiply the mols by Avagrado's number to get atoms
    if input_element in elements:
        print(f"The number of atoms in {str(mols)} mol of {elements[elements.index(input_element)].capitalize()} is {str(round(float(mols) * 6.022 * (10 ** 23),3))} atoms")
    # if the input is in the list of symbols, multiply the mols by Avagrado's number to get atoms
    elif input_element in symbols:
        print(f"The number of atoms in {str(mols)} mol of {elements[symbols.index(input_element)].capitalize()} is {(round(float(mols) * 6.022 * (10 ** 23),3))} atoms")
    # if the input is in the list of atomic numbers, multiply the mols by Avagrado's number to get atoms
    elif input_element.isdigit():# checks if the input is a number under 118
        print(f"The number of atoms in {str(mols)} mol of {elements[atomic_numbers.index(int(input_element))].capitalize()} is {str(round(float(mols) * 6.022 * (10 ** 23),3))} atoms")
    else:
        # if the element does not exist, it prints the following
        print("Invalid input" + "\nPlease Try Again")     
        
def grams_to_mol():
    # enter the number of grams
    grams = float(input("Enter the number of grams: "))
    # if the element name is in the list, divide the grams by molar mass to get mol
    if input_element in elements:
        print(f"The number of mols in {str(grams)} grams of {elements[elements.index(input_element)].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[elements.index(input_element)],3))} mols")
    # if the element symbol is in the list, divide the grams by molar mass to get mol
    elif input_element in symbols:
        print(f"The number of mols in {str(grams)} grams of {elements[symbols.index(input_element)].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[symbols.index(input_element)],3))} mols")
    # if the atomic number is in the list, divide the grams by molar mass to get mol
    elif input_element.isdigit():# checks if the input is a number
        print(f"The number of mols in {str(grams)} grams of {elements[atomic_numbers.index(int(input_element))].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[atomic_numbers.index(int(input_element))],3))} mols")
    else:
        # if the element does not exist, it prints the following
        print("Invalid input" + "\nPlease Try Again")
          
def grams_to_atoms():
    # enter the number of grams
    grams = float(input("Enter the number of grams: "))
    # if the element name is in the list divide grams by molar mass and multiply by Avagrado's number
    if input_element in elements:
        print(f"The number of atoms in {str(grams)} grams of {elements[elements.index(input_element)].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[elements.index(input_element)] * 6.022 * (10 ** 23),3))} atoms")
    # if the element symbol is in the list divide grams by molar mass and multiply by Avagrado's number
    elif input_element in symbols:
        print(f"The number of atoms in {str(grams)} grams of {elements[symbols.index(input_element)].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[symbols.index(input_element)] * 6.022 * (10 ** 23),3))} atoms")
    # if the atomic number is in the list divide grams by molar mass and multiply by Avagrado's number
    elif input_element.isdigit():# checks if the input is a number
        print(f"The number of atoms in {str(grams)} grams of {elements[atomic_numbers.index(int(input_element))].capitalize()} is {str(round(float(grams) / atomic_mass_numbers[atomic_numbers.index(int(input_element))] * 6.022 * (10 ** 23),3))} atoms")
    else:
        # if the element does not exist, it prints the following
        print("Invalid input" + "\nPlease Try Again")
        
def mol_to_grams():
    # enter the number of mols
    mols = float(input("Enter the number of mols: "))
    # if the element name is is list, multiply mols by molar mass to get grams
    if input_element in elements:
        print(f"The number of grams in {str(mols)} mol of {elements[elements.index(input_element)].capitalize()} is {str(round(float(mols) * atomic_mass_numbers[elements.index(input_element)],3))} grams")
    # if the element symbol is is list, multiply mols by molar mass to get grams
    elif input_element in symbols:
        print(f"The number of grams in {str(mols)} mol of {elements[symbols.index(input_element)].capitalize()} is {str(round(float(mols) * atomic_mass_numbers[symbols.index(input_element)],3))} grams")
    # if the atomic number is is list, multiply mols by molar mass to get grams
    elif input_element.isdigit():# checks if the input is a number
        print(f"The number of grams in {str(mols)} mol of {elements[atomic_numbers.index(int(input_element))].capitalize()} is {str(round(float(mols) * atomic_mass_numbers[atomic_numbers.index(int(input_element))],3))} grams")
    else:
        # if the element does not exist, it prints the following
        print("Invalid input")
        
if __name__ == "__main__":
    # calls the function to make the lists of elements accessible
    my_lists()
    #make list into uppercase to prevent case sensitivity
    symbols = [symbols.upper() for symbols in symbols]
    elements = [elements.upper() for elements in elements]
    #asks if user wants to see the periodic table
    periodic_table()
    my_search = input ("Would you like to search for an element or do conversions? (Y/N): ").upper()
    if my_search == "Y" or my_search == "YES":
        # if yes or y, sets counter x to True
        x = True
        #prints once when program is first run
        print("You can always see the menu by typing 'menu'") 
        print("All inputs are not case sensitive")
        menu()
    else:
        # if not yes, sets the counter False
        x = False
    # while x is  true    
    while True:
        # ask for what program user wants to run and prints each input option 
        search = input("Enter 'name' or 'property' or 'conversion' or 'menu' or 'table' or 'exit': ")
        print("")
        # makes input uppercase to prevent case sensitivity
        search = search.upper()
        # if name is entered,asks for element name the name function is called
        if search == "NAME":
            input_element = input("Enter element name, symbol, or atomic number: ").upper()
            print("")
            name()
            print('')
         # if the user enters 'property', the property function is called 
        elif search == "PROPERTY":
            # user is asked to input the element name, symbol, or atomic number
            input_element = input("Enter element name, symbol, or atomic number: ").upper()
            #if the element name is in the list, the property function is called
            if input_element in elements:
                print("")
                property()
                period()
                print('')
            #if the element symbol is in the list, the property function is called
            elif input_element in symbols:
                print("")
                property()
                period()
                print('')
            #if the atomic number is in the list up to 118, the property function is called
            elif input_element.isdigit() and int(input_element) <= 118:
                print("")
                property()
                period()
                print('')
            else:
                # if the element does not exist, it prints the following
                print("Invalid input" + "\nPlease Try Again")
                print('')
        # if the user enters 'conversion', the conversion function is called   
        elif search == "CONVERSION":
            # user is asked to input the element name, symbol, or atomic number
            input_element = input("Enter element name, symbol, or atomic number: ").upper()
            # ask user what they are converting from
            conversion1 = input("what are you converting from? (Mol or Gram): ").upper()
            # ask user what they are converting to
            # if mol is entered, the second conversion is grams and atoms. This is to prevent user from converting mol to mol
            if conversion1 == "MOL":
                conversion2 = input("what are you converting to? (Atom, or Gram): ").upper()
            # if grams is entered, the second conversion is mol and atoms. This is to prevent user from converting gram to gram
            if conversion1 == "GRAM":
                conversion2 = input("what are you converting to? (Atom, or Mol): ").upper()
            #depending on what the user inputs first and second, runs the corresponding function
            if conversion1 == 'MOL' and conversion2 == 'ATOM' :
                mol_to_atoms()
            elif conversion1 == 'MOL' and conversion2 == 'GRAM' :
                mol_to_grams()
            elif  conversion1 == 'GRAM' and conversion2 == 'MOL':
                grams_to_mol()
            elif conversion1 == 'GRAM' and  conversion2 == 'ATOM':
                grams_to_atoms()  
            # if the input does not contain the words mol, atom,or gram, it prints the following
            else:
                print("Invalid input" + "\nPlease Try Again")
        # if the user enters menu, shows the menu again
        elif search == "MENU":
            menu()
        # if the user enters table, shows the periodic table
        elif search == "TABLE":
            periodic_table()
        # if the user enters exit, the value x is set to False and the program ends  
        elif search == "EXIT":
            #sets x to false
            x = False
        else: # if the user does not enter name, property, conversion, or exit, it prints the following and asks again
            print("Invalid input" + "\nPlease Try Again")
        # if x is set to False, program exists
        while x == False:
            print("program closed successfully")
            #exit the program
            exit()
            
          