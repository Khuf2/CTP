from Entry import *

# This is going to be my methods for the user, the client tools and functionality.
# CTP.py is destined to be the main file, which sets and cleans the table, saving to data.txt

class User:
    # the key for the self.data is being changed from name to int 'index' (because it is a list of entries)
    MALE_WEIGHTS = {"phys": 15, "att": 20, "soc": 20, "comm": 15, "intel": 20, "cons": 10}
    FEMALE_WEIGHTS = {"phys": 20, "att": 25, "soc": 15, "comm": 10, "intel": 20, "cons": 10}

    def __init__(self, name, data): 
        # gender = data[0]
        # scores = data[1]
        self.name = name.title()
        self.data = data
        self.greet()

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def addEntry(self, data):
        name = data[0]
        if self.getEntry(name) is None:
            # add a new entry
            self.data.append( Entry(data[0].title(), data[1], data[2], data[3], self.name) )
        else:
            print("Error: name exists already in your list")

    def editEntry(self, data):
        name = data[0]
        # Find and alter entry
        e = self.getEntry(name)
        self.data[self.data.index(e)] = Entry(data[0], data[1], data[2], data[3], self.name)

    def getEntry(self, name):
        for x in self.data:
            if(x.getName() == name.title()):
                return x
        
    
    def delEntry(self, name):
        e = self.getEntry(name)
        if e is not None:
            self.data.remove(e) 
            return e
        else:
            return None  

    def getWeights(self):
        # Low priority
        return None

    '''
    def setWeights(self):
        # Do as supplemental afterwards
        print()
    '''

    def ls(self):
        # this lists out all the people, maybe in a 3 column format
        output = "\nMy Entries:\n"
        col = 0
        for x in self.data:
            if (col % 3 == 2):
                output += str(x.getName()) + " (" + x.getGender() + ") [" + str(x.getCTP()) + "]\n"
            else: 
                output += str(x.getName()) + " (" + x.getGender() + ") [" + str(x.getCTP()) + "]\t\t\t\t"
            col += 1
        print (output)

    '''
    def find(self, *args):
        # do some test later for added args
        return self.ls()
    '''

    def greet(self):
        print ("\nWelcome, " + self.name + ", to your CTP dashboard.")

    def getData(self):
        return self.data

    def printDefaultWeights(self):
        outputM = "Male Weights: "
        outputF = "Female Weights: "
        i = 1
        for k in self.MALE_WEIGHTS.keys():
            outputM += k.title() + ": " + str(self.MALE_WEIGHTS[k]) + "%"
            outputF += k.title() + ": " + str(self.FEMALE_WEIGHTS[k]) + "%"
            if(i != len(self.MALE_WEIGHTS.keys())):
                outputM += ", "
                outputF += ", "
        output = outputM + "\n" + outputF + "\n"
        return output

    def strToList(self, input):
        list = []
        item = ""
        # This will work for brackets or no brackets, quotes or no quotes, and filters
        # out the extraneous formatting punctuation besides commas
        for char in input:
            if char.isalnum() == True:
                item += char
            elif char == ',':
                list.append(item)
                item = ""
                print (char)
        list.append(item)
        return list

    def menu(self):
        # I want to print a short menu of keybinds/brief commands
        # Then prompt the user for input, and call another method in a while,
        # which has an exit command.
        quit = False
        print("Type 'help' to see the list of commands.")
        while(not quit):
            select = input("\nAwaiting action: ") 
            if select == "ls":
                # ls()
                self.ls()
            elif select == "add":
                # addEntry()
                print("New Entry:")
                name = input("Name: ") 
                gender = input("Male or Female? (m or f): ").upper()
                if gender.__eq__("M"):
                    gender = "Male"
                else:
                    gender = "Female"
                age = int(input("Age: "))
                scores = {
                    "phys": int(input("Physique: ")), 
                    "att": int(input("Attractiveness: ")), 
                    "soc": int(input("Social: ")),
                    "comm": int(input("Communication: ")),  
                    "intel": int(input("Intelligence: ")), 
                    "cons": int(input("Consistency: "))
                }

                self.addEntry([name, gender, age, scores])
            elif select == 'edit':
                # editEntry()
                print("Edit Entry:")
                name = input("Name: ")
                entry = self.getEntry(name)
                if(entry) is not None:
                    # if a field is left blank, then keep the old value.
                    # display the old value alongside the variable prompt
                    updateGender = input("Male or Female? (m or f) [curr = " + entry.getGender() + "]: ").upper()
                    if updateGender == ("M"):
                        gender = "Male"
                    elif updateGender == ("F"):
                        gender = "Female"
                    else:
                        gender = entry.getGender()
                    age = input("Age: ")
                    if age.isspace() or len(age) == 0:
                        age = entry.getAge()
                    else:
                        age = int(age)
                    scores = {
                        "phys": input("Physique [curr = " + str(entry.getScore("phys")) + "]: "), 
                        "att": input("Attractiveness [curr = " + str(entry.getScore("att")) + "]: "), 
                        "soc": input("Social [curr = " + str(entry.getScore("soc")) + "]: "), 
                        "comm": input("Communication [curr = " + str(entry.getScore("comm")) + "]: "), 
                        "intel": input("Intelligence [curr = " + str(entry.getScore("intel")) + "]: "), 
                        "cons": input("Consistency [curr = " + str(entry.getScore("cons")) + "]: ")
                    }
                    for x in scores.keys():
                        # revert unchanged values
                        if (scores[x].isspace() or len(scores[x]) == 0):
                            scores[x] = entry.getScore(x)
                        else:
                            scores[x] = int(scores[x])
                    self.editEntry([name, gender, age, scores])

                else:
                    print("Entry does not exist. Check your spelling or try adding a new entry.")

            elif select == 'del':
                # delEntry()
                print("Delete Entry:")
                name = input("Name: ") 
                deleted = self.delEntry(name)
                if(deleted != None):
                    print(name.title() + " deleted from your entries.")
                else:
                    print("Error: " + name.title() + " delete failure.")
            elif select == 'f':
                # find()
                print(None)
            elif select == 'lb':
                # getWeights
                print(self.printDefaultWeights())
            elif select == 'help':
                # print menu
                print ("List = ls, Add = add, Edit = edit, Delete = del, Find = f, Weights = lb, report = rpt, Quit = q")
            elif select == 'rpt':
                # report()
                # ("name1", "name2", "name3", "name4")
                listStr = input("Enter a comma-separated list of entry names to report: ") 
                rpt_list = self.strToList(listStr)
                output = ""
                for x in range(0, len(rpt_list)):
                    e = self.getEntry(rpt_list[x])
                    if(e != None):
                        output += str(e) + "\n"
                if(output == ""):
                    output = "No matching entries to report."
                print ( (output) )
            elif select == 'q':
                # quit and exit to CTP, where you finish and quit
                print("System quitting.")
                quit = True
            else:
                # invalid
                print("Invalid input")
        
