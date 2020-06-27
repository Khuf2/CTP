class Entry: 
    # default values given to the person
    MALE_WEIGHTS = {"phys": 15, "att": 20, "soc": 20, "comm": 15, "intel": 20, "cons": 10}
    FEMALE_WEIGHTS = {"phys": 20, "att": 25, "soc": 15, "comm": 10, "intel": 20, "cons": 10}

    # parameterized constructor 
    def __init__(self, name, gender, age, scores, author): 
        # name
        self.name = name.title()
        # gender, weighting
        self.gender = gender.capitalize()
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
        self.CTP_score = round(cum_score, 2)

    def setWeights(self): 
        # Not meant to be any kind of statement about gender and equality or whatever.
        # This is just as a demonstration of a fork based off of innate data, in this case, gender.
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
        return self.CTP_score
    
    def getScore(self, index):
        return self.scores[index]

    def getAllScores(self):
        return self.scores
    
    def setScore(self, key, val):
        self.scores[key] = val

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
        report = ""
        report += "\n\n"
        report += self.name + " (" +  self.getGender() + ")\n"
        report += "Score: " + str(self.CTP_score) + "\n\n"
        for key in self.scores.keys():
            report += key.capitalize() + ": " + str(self.scores[key]) + "\n"
        report += "\n\n"
        return report
