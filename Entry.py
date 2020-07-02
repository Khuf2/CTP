class Entry: 
    # default values given to the person
    MALE_WEIGHTS = {"phys": 11, "looks": 19, "soc": 23, "comm": 19, "intel": 11, "cons": 17}
    FEMALE_WEIGHTS = {"phys": 17, "looks": 21, "soc": 17, "comm": 15, "intel": 16, "cons": 14}

    # parameterized constructor 
    def __init__(self, name, gender, age, scores, author): 
        # name
        self.name = name.title()
        # gender, weighting
        self.setGender(gender)
        self.setWeights()
        # scores
        self.scores = scores
        # CTP
        self.CTP()
        # age
        self.age = age
        # author
        self.author = author
      
    def CTP(self): 
        # calculate updated CTP for this entry
        cum_score = 0
        for key in self.scores.keys():
            cum_score += (self.scores[key] / 100) * self.weights[key]
        self.ctp_score = (round(cum_score, 2))

    def setWeights(self): 
        if (self.getGender() == ("Male")):
            self.weights = self.MALE_WEIGHTS
        else:
            self.weights = self.FEMALE_WEIGHTS

    # Add other accessor and mutator methods
    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        if (gender.__eq__("Male")):
            self.gender = "Male"
        elif (gender.__eq__("Female")):
            self.gender = "Female"
        else:
            self.gender = "Other"

    def getCTP(self):
        return self.ctp_score
    
    def getScore(self, key):
        return self.scores[key]

    def getAllScores(self):
        return self.scores
    
    def setScore(self, key, val):
        self.scores[key] = val
        self.CTP()

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAge(self):
        return self.age

    def setAge(self, val):
        self.age = val

    def getAuthor(self):
        return self.author
    
    def __str__(self):
        # Returns a list of the categories and the values, the user's name, and the final CTP score. 
        report = "\n"
        report += self.name + " (" +  self.getGender() + ")\n"
        report += "Age: " + str(self.getAge()) + "\n"
        report += "Score: " + str("{:.2f}".format(self.ctp_score)) + "\n\n"
        for key in self.scores.keys():
            report += key.capitalize() + ": " + str(self.scores[key]) + "\n"
        return report
