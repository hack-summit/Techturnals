def load_data(n = None):
    # Default dataset

    #for doctors
    males = {'0': ['7', '5', '6', '4'],
             '1': ['5', '4', '6', '7'],
             '2': ['4', '5', '6', '7'],
             '3': ['4', '5', '6', '7']}
    #for nurse grp or patient
    females = {'4': ['0', '1', '2', '3'],
               '5': ['0', '1', '2', '3'],
               '6': ['0', '1', '2', '3'],
               '7': ['0', '1', '2', '3']}

    # Dataset 1
    if n == 0:
        males = {'k': ['b', 'c', 'a'],
                 'l': ['a', 'c', 'b'],
                 'm': ['a', 'b', 'c']}

        females = {'a': ['k', 'l', 'm'],
                   'b': ['l', 'm', 'k'],
                   'c': ['m', 'l', 'k']}            
    return males, females

class Male:
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference
        self.is_matched = False
        self.partner = None
        self.index = 0 # Index to hold the position of the proposed wives
    
    def propose(self):
        female = self.preference[self.index]
        self.index += 1
        return female
    
    def is_available(self):
        return not self.is_matched

    def __str__(self):
        if self.is_matched:
            return '{} is matched to {}'.format(self.name, self.partner.name)
        return '{} is single'.format(self.name)

class Female:
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference
        self.is_matched = False
        self.partner = None
    
    def is_available(self):
        return not self.is_matched

    def rank(self, m1, m2):
        m1_score = self.preference.index(m1)
        m2_score = self.preference.index(m2)

        # Lower index means higher preference
        return m1 if m1_score < m2_score else m2

    def __str__(self):
        if self.is_matched:
            return '{} is matched to {}'.format(self.name, self.partner.name)
        return '{} is single'.format(self.name)

class Matches:
    def __init__(self, males, females):
        self.matches = {}

        self.choices = len(males)
        self.males = list(males.keys())
        self.females = list(females.keys())
        self.match_count = 0
        
        for i in males:
            self.matches[i] = Male(i, males[i])

        for j in females:
            self.matches[j] = Female(j, females[j])
        
    def engage(self, male_name, female_name):
        """Engage the male to the female if both of them are still available
        
        Args:
            male_name (str): The name of the male
            female_name (str): The name of the female
        """
        male = self.matches[male_name]
        female = self.matches[female_name]
        
        male.is_matched = True
        male.partner = female
        
        female.is_matched = True
        female.partner = male
        
        self.match_count += 1
    
    def breakup(self, male_name, female_name):
        """Break the engagement for both the male and female
        
        Args:
            male_name (str): The name of the male
            female_name (str): The name of the female
        """
        male = self.matches[male_name]
        female = self.matches[female_name]
        
        male.is_matched = False
        male.partner = None
        
        female.is_matched = False
        female.partner = None

        self.match_count -= 1
    
    def match(self):
        """Recursively match the male and female as long as they 
        have not been matched. The matching ends once each male is
        paired with a female"""
        for m in self.males:
            male = self.matches[m]
            if not male.is_available():
                continue

            female = self.matches[male.propose()]
            if female.is_available():
                self.engage(male.name, female.name)
            else:
                male_name = female.rank(male.name, female.partner.name)
                self.breakup(female.partner.name, male_name)
                self.engage(male_name, female.name)
        if self.match_count < self.choices:
            self.match()

        return self.sets()
    
    def sets(self):
        """Returns the male-female pairs that have been matched
        
        Returns:
            matches (:obj:`list` of :obj:`str`): The unique pairs of male-female
        """
        matches = {}
        for i in self.matches:
            match = self.matches[i]
            matches[frozenset([match.name, match.partner.name])] = True
        return list(matches.keys())
male_data, female_data = load_data(1)
matches = Matches(male_data, female_data)
print (matches.match())