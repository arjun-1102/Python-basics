class Student:
    name = "Arjun"
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(grade):
        if grade>50:
            Student.praise(name)
        Student.reassurance(name)