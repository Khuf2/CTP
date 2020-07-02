from Entry import *
import copy

# This is going to be my methods for the user, the client tools and functionality.
# CTP.py is destined to be the main file, which sets and cleans the table, saving to data.txt

class User:
    # the key for the self.data is being changed from name to int 'index' (because it is a list of entries)
    MALE_WEIGHTS = {"phys": 11, "looks": 19, "soc": 23, "comm": 19, "intel": 11, "cons": 17}
    FEMALE_WEIGHTS = {"phys": 17, "looks": 21, "soc": 17, "comm": 15, "intel": 16, "cons": 14}
    help = {
        "List": "ls",
        "Add": "add",
        "Edit": "edit",
        "Delete": "del",
        "Sort": "sort",
        "Find": "f",
        "Weights": "lb",
        "Report": "rpt",
        "Quit": "q"
    }

    def __init__(self, name, data): 
        self.name = name.title()
        self.data = data
        self.query = copy.deepcopy(self.data)
        # The stack will eventually be a small ADT that we make and implement based on a list
        # it tracks filter conditionals for find query
        self.stack = []
        self.criteria = None
        self.asc = None
        self.fcriteria = None
        self.fasc = None
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

    def ls(self, list):
        # this lists out all the people, maybe in a 3 column format
        if(list is self.data):
            output = "\nMy Entries:"
            criteria = self.criteria
            asc = self.asc
        else:
            output = "\nMy Search Query:"
            criteria = self.fcriteria
            asc = self.fasc

        if(criteria is not None and asc is not None):
            output += " Sorted by " + criteria.title() + ": "
            if(asc is True):
                output += "Ascending order"
            else:
                output += "Descending order"
        output += "\n\n"
        for x in list:
            output += str(x.getName()) + " (" + x.getGender() + ") [" + str("{:.2f}".format(x.getCTP())) + "]\n"
        print (output)

    def report(self, list):
        output = ""
        for x in range(0, len(list)):
            e = self.getEntry(list[x])
            if(e != None):
                output += str(e) + "\n"
        if(output == ""):
            output = "No matching entries to report."
        return output

    def sort(self, list, criteria, asc):
        # list is the list to sort
        # criteria is the thing to sort by
        # and asc is a boolean that if true will sort ascending, otherwise, descending
        sortFunc = None

        def ageFunc(e):
            return e.getAge()

        def alphaFunc(e):
            return e.getName()

        def CTPFunc(e):
            return e.getCTP()
        
        def scoreFunc(e):
            return e.getScore(criteria)

        def authorFunc(e):
            return e.getAuthor()
        
        # criteria: age, alphabetical, CTP, other scores, author alphabetical
        if(criteria == 'age'):           
            sortFunc = ageFunc
        elif(criteria == 'alpha'):
            sortFunc = alphaFunc
        elif(criteria == 'ctp'):
            sortFunc = CTPFunc
        elif(criteria == 'phys' or criteria == 'looks' or criteria == 'soc' or criteria == 'comm' or criteria == 'intel' or criteria == 'cons'):
            sortFunc = scoreFunc
        elif(criteria == 'author'):
            sortFunc = authorFunc
        else:
            return "Aborted: sortFunc is unassigned."

        list.sort(reverse=(not asc), key=sortFunc)

    def queryRead(self, args):
        # line = "age=80, phys>=80"
        # This needs to be updated. I used to send in line. Now I send in the args list of conditions, which need to be translated and appended to fullList.
        category = ""
        condEx = ""
        fullList = []
        list = []
        for condition in args:
            for letter in condition:
                if(letter == ' ' or letter == ","):
                    continue

                if(not letter.isalnum()):
                    if(category != ""):
                        list.append(category)
                        category = ""
                    condEx += letter
                else:
                    if(condEx != ""):
                        list.append(condEx)
                        condEx = ""
                    category += str(letter)
            if(category != ""):
                list.append(category)
            fullList.append(list.copy())
            list = []
            category = ""
            condEx = ""
        return fullList
    
    def find(self, bools):
        # do some test later for added args
        # This will be getting passed a lenN list of len3 lists, where N = filter conditions/
        self.query = copy.deepcopy(self.data)

        def ageFunc(e):
            return e.getAge()

        def alphaFunc(e):
            # should return slices of word length to see if it matches the name.
            # Ex: Al- searches for two-letter starting with Al-. Like Alex, Allen, Albert, etc.
            return e.getName()

        def CTPFunc(e):
            return e.getCTP()
        
        def scoreFunc(key):
            return (lambda e: e.getScore(key))

        def authorFunc(e):
            # should return slices of word length to see if it matches the name.
            # Ex: Al- searches for two-letter starting with Al-. Like Alex, Allen, Albert, etc.
            return e.getAuthor()

        filterFunc = {
            "age": ageFunc,
            "alpha": alphaFunc,
            "ctp": CTPFunc,
            "phys": scoreFunc("phys"),
            "looks": scoreFunc("looks"),
            "soc": scoreFunc("soc"),
            "comm": scoreFunc("comm"),
            "intel": scoreFunc("intel"),
            "cons": scoreFunc("cons"),
            "author": authorFunc
        }

        for cond in bools:

            print (cond)
            print ( "Pre: " + str(len(self.query)) )

            if (cond[1] == '>'):
                # condition = lambda e: filterFunc[x[0]](e) > int(x[2])
                self.query[:] = [x for x in self.query if filterFunc[cond[0]](x) > int(cond[2])]
            elif (cond[1] == '<'):
                # condition = lambda e: filterFunc[x[0]](e) < int(x[2])
                self.query[:] = [x for x in self.query if filterFunc[cond[0]](x) > int(cond[2])]
            elif (cond[1] == '>='):
                # condition = lambda e: filterFunc[x[0]](e) >= int(x[2])
                self.query[:] = [x for x in self.query if filterFunc[cond[0]](x) >= int(cond[2])]
            elif (cond[1] == '<='):
                # condition = lambda e: filterFunc[x[0]](e) <= int(x[2])
                self.query[:] = [x for x in self.query if filterFunc[cond[0]](x) <= int(cond[2])]
            elif (cond[1] == '=' or cond[1] == '=='):
                # condition = lambda e: filterFunc[x[0]](e) == int(x[2])
                self.query[:] = [x for x in self.query if filterFunc[cond[0]](x) == int(cond[2])]
            else:
                print ("Error reading expression operator")

            self.ls(self.query)
            print ( "Post: " + str(len(self.query)) )

        self.ls(self.query)

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

    def editCategory(self, name, category, change=0):
        # make for list of names instead of single name later
        entry = self.getEntry(name)
        if(change==0):
            change = input(category.title() + " [curr = " + str(entry.getScore(category)) + "]: ")

        if(change[0]=='+'):
            # we're adding change to old val in category
            newVal = entry.getScore(category)+int(change[1:])
            entry.setScore(category, newVal)
        else:
            change = int(change)
            if(change < 0):
                # we're subtracting change from old val in category
                newVal = entry.getScore(category)+change
                entry.setScore(category, newVal)
            else:
                entry.setScore(category, change)

    def printHelp(self):
        output = "(Help) Function : Shortcut\n"
        for x in self.help.keys():
            output += "\t" + x + " : " + self.help[x] + "\n"
        output += "Type 'help <shortcut>' to get an explanation and syntax for the function's usage.\n"
        return output

    def menu(self):
        quit = False
        print("Type 'help' to see the list of commands.")

        while(not quit):
            line = ""
            while(len(line) == 0):
                line = input("\nCommand Line >> ")
            args = line.split(" ")
            # Remove any mishap blank args
            while(args.count("") > 0):
                args.remove("")
            print()
            # Make sure we always check length of argument list before doing these nested conditionals


            if(args[0].lower() == 'help'):
                if(len(args) == 1):
                    print(self.printHelp())           
                elif(len(args) == 2):
                    if(args[1] == 'ls'):
                        output = args[1] + ": [list] name, gender, and CTP of all entries.\n"
                        output += "Usage: >> ls\n"
                        print(output)
                    elif(args[1] == 'add'):
                        output = args[1] + ": [add] a new entry.\n"
                        output += "Usage: >> add, add <name>\n"
                        print(output)
                    elif(args[1] == 'edit'):
                        output = args[1] + ": [edit] an existing entry.\n"
                        output += "Usage: >> edit, edit <name>, edit <name> <category>, edit <name> <category> <new value or relative change>\n"
                        print(output)
                    elif(args[1] == 'del'):
                        output = args[1] + ": [delete] an existing entry.\n"
                        output += "Usage: >> del, del <name>\n"
                        print(output)
                    elif(args[1] == 'lb'):
                        output = args[1] + ": prints [weights] used for CTP calculation.\n"
                        output += "Usage: >> lb"
                        print(output)
                    elif(args[1] == 'sort'):
                        output = args[1] + ": [sort] data list by specified criteria.\n"
                        output += "Usage: >> sort, sort <criterion> <order>"
                        print(output)
                    elif(args[1] == 'rpt'):
                        output = args[1] + ": [report] entries from a comma-separated list of names.\n"
                        output += "Usage: >> rpt, rpt *, rpt <name1>, <name2>, <name3>, <...>"
                        print(output)
                    elif(args[1] == 'q'):
                        output += args[1] + ": [quits] and saves new changes to JSON.\n"
                        output += "Usage: >> q"
                        print(output)
                else:
                    print("Too many arguments for 'help'.")


            elif(args[0].lower() == 'f'):
                # If you send to sort, rpt, or ls, args.pop(0) would get rid of the f list element and give you an adjusted args list.
                args.pop(0)

                if(args[0].lower() == 'ls'):
                    # send to other ls with list = query
                    self.ls(self.query)

                elif(args[0].lower() == 'sort'):
                    # send to other sort with list = query
                    print("Sort Entries:")
                    # if list is not sent as self.query, its self.data
                    if(len(args) > 2 and len(args[1]) > 0):
                        # sort with a criteria and asc
                        criteria = args[1]
                        if(args[2].lower() == 'a'):
                            asc = True
                        else:
                            asc = False
                    else:
                        # sort the old way
                        criteria = input("Criteria: ").lower()
                        asc = input("Ascending or Descending order (a / d): ").lower()
                        if asc == 'a':
                            asc = True
                        elif asc == 'd':
                            asc = False
                        else:
                            asc = None
                    self.sort(self.query, criteria, asc)
                    self.fcriteria = criteria
                    self.fasc = asc
                    print("Sorted.")

                elif(args[0].lower() == 'rpt'):
                    # send to other rpt with list = query
                    if(len(args) > 1):
                        if(len(args) == 2 and args[1] == '*'):
                            # report all from the given list
                            # grab all names from self.data
                            all_names = []
                            for x in self.query:
                                all_names.append(x.getName())
                            print ( (self.report(all_names)) )
                        else:
                            # we have been given a comma-separated list in this case.
                            # Do as before, but in one step
                            for x in range(1, len(args)):
                                args[x] = args[x].replace(",", "")
                            print ( (self.report( args[1:] )) )
                    else:
                        # rpt the old way
                        listStr = input("Enter a comma-separated list of entry names to report: ") 
                        rpt_list = self.strToList(listStr)
                        print ( (self.report(rpt_list)) )

                elif(args[0].lower() == 'push'):
                    print("@f push: ")
                elif(args[0].lower() == 'pop'):
                    print("@f pop: ")
                elif(args[0].lower() == 'popall'):
                    print("@f popall: ")
                else:
                    # we have been given a comma-separated list in this case.
                    # Do as before, but in one step
                    for x in range(1, len(args)):
                        args[x] = args[x].replace(",", "")
                    self.find(self.queryRead(args))
                    # print("Could not read your find command. Learn about our find syntax.")

            elif(args[0].lower() == 'ls'):
                self.ls(self.data)


            elif(args[0].lower() == 'add' and len(args) <= 2):
                # if args[1] exists, thats our name
                print("New Entry:")
                if(len(args) > 1 and len(args[1]) > 0):
                    name = args[1]
                else:
                    name = input("Name: ")

                gender = input("Male or Female? (m or f): ").upper()
                if gender.__eq__("M"):
                    gender = "Male"
                else:
                    gender = "Female"
                age = int(input("Age: "))
                scores = {
                    "phys": int(input("Physique: ")), 
                    "looks": int(input("Looks: ")), 
                    "soc": int(input("Social: ")),
                    "comm": int(input("Communication: ")),  
                    "intel": int(input("Intelligence: ")), 
                    "cons": int(input("Consistency: "))
                }
                self.addEntry([name, gender, age, scores])


            elif(args[0].lower() == 'edit'):
                if(len(args) > 1):
                    name = args[1]
                    if(len(args) > 2):
                        # This is a whole different thing in here, will break from rest before end of code block
                        category = args[2]
                        if(len(args) > 3):
                            # edit instantly with name, category, and change value
                            change = args[3]
                            self.editCategory(name, category, change)
                            continue
                        # edit with a name and category
                        self.editCategory(name, category)
                        continue
                    print("Edit Entry:")
                else:
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
                        "looks": input("Looks [curr = " + str(entry.getScore("looks")) + "]: "), 
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
                    print("Entry does not exist. Check your spelling or add this entry.")
                

            elif(args[0].lower() == 'del'):
                print("Delete Entry:")
                if(len(args) > 1):
                    name = args[1]
                else:
                    name = input("Name: ") 

                deleted = self.delEntry(name)
                if(deleted != None):
                    print(name.title() + " deleted from your entries.")
                else:
                    print("Error: " + name.title() + " delete failure.")
                

            elif(args[0].lower() == 'sort'):
                print("Sort Entries:")
                # if list is not sent as self.query, its self.data
                if(len(args) > 2 and len(args[1]) > 0):
                    # sort with a criteria and asc
                    criteria = args[1]
                    if(args[2].lower() == 'a'):
                        asc = True
                    else:
                        asc = False
                else:
                    # sort the old way
                    criteria = input("Criteria: ").lower()
                    asc = input("Ascending or Descending order (a / d): ").lower()
                    if asc == 'a':
                        asc = True
                    elif asc == 'd':
                        asc = False
                    else:
                        asc = None
                self.sort(self.data, criteria, asc)
                self.criteria = criteria
                self.asc = asc
                print("Sorted.")

            elif(args[0].lower() == 'rpt'):
                # if list is not sent as self.query, its self.data
                if(len(args) > 1):
                    if(len(args) == 2 and args[1] == '*'):
                        # report all from the given list
                        # grab all names from self.data
                        all_names = []
                        for x in self.data:
                            all_names.append(x.getName())
                        print ( (self.report(all_names)) )
                    else:
                        # we have been given a comma-separated list in this case.
                        # Do as before, but in one step
                        for x in range(1, len(args)):
                            args[x] = args[x].replace(",", "")
                        print ( (self.report( args[1:] )) )
                else:
                    # rpt the old way
                    listStr = input("Enter a comma-separated list of entry names to report: ") 
                    rpt_list = self.strToList(listStr)
                    print ( (self.report(rpt_list)) )
                
            elif(args[0].lower() == 'lb'):
                print(self.printDefaultWeights())

            elif(args[0].lower() == 'q'):
                # quit and exit to CTP, where you finish and quit
                    print("System quitting.")
                    quit = True

            else:
                print("Could not read your command line.")
 
    '''
    These methods are used by the program automatically, and are not available to the user.
    They also don't qualify as accessor/mutator functions during primary menu() use.
    '''

    def greet(self):
        print ("\nWelcome, " + self.name + ", to your CTP dashboard.")

    def getData(self):
        return self.data

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
        list.append(item)
        return list
        
