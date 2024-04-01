class character:
    def __init__(self,name,age,height,weight,personality,accuracy, communication,constitution,dexterity,fighting,intelligence,perception,strength,willpower,origin,social_class,background,fortune,conditions):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.personality = personality
        self.accuracy = accuracy
        self.constitution = constitution
        self.fighting = fighting
        self.communication = communication
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.perception = perception
        self.strength = strength
        self.willpower = willpower
        self.origin = self.set_origin(origin)
        self.social_class = self.set_social_class(social_class)
        self.background = self.set_background(background)
        self.fortune = int(fortune)
        self.conditions = conditions

        
    def set_origin(self,origin_roll):
        origins = ["Belter","Earther","Martian"]
        if origin_roll in origins:
            return origin_roll
        else:
            
            origin_roll = int(origin_roll)
            self.origin_roll_table = [[[1,2],["Belter"]]
                                    ,[[3,4],["Earther"]]
                                    ,[[5,6],["Martian"]]]
            for self.origin_range in self.origin_roll_table:
                if(origin_roll in self.origin_range[0]):
                    string_temp = str(self.origin_range[1][0])
                    return string_temp
                
    def set_social_class(self,social_class):
        social_classes = ["Outsider","Lower Class","Middle Class","Upper Class"]
        if social_class in social_classes:
            return social_class
        else:
            social_class = int(social_class)
            if(self.origin == "Belter"):
                self.social_class_roll_table = [[[2,3,4,5],"Outsider"],[[6,7,8],"Lower Class"],[[9,10,11],"Middle Class"],[[12],"Upper Class"]]
                for social_class_score in self.social_class_roll_table:
                    if( social_class in social_class_score[0]):
                        return social_class_score[1]
            elif(self.origin == "Earther"):
                self.social_class_roll_table = [[[2,3],"Outsider"],[[4,5,6],"Lower Class"],[[7,8,9,10],"Middle Class"],[[11,12],"Upper Class"]]
                for social_class_score in self.social_class_roll_table:
                    if( social_class in social_class_score[0]):
                        return social_class_score[1]
            else:
                self.social_class_roll_table = [[[2],"Outsider"],[[3,4,5,6],"Lower Class"],[[7,8,9,10,11],"Middle Class"],[[12],"Upper Class"]]
                for social_class_score in self.social_class_roll_table:
                    if( social_class in social_class_score[0]):
                        return social_class_score[1]
    
    def set_background(self,backgroundroll):
        backgrounds = ["Bohemian","Exile","Outcast","Military","Laborer","Urban","Academic","Suburban","Trade","Aristocratic","Corporate","Cosmopolitan"]
        backgroundroll = backgroundroll.replace("\n","")
        if backgroundroll in backgrounds:
            return backgroundroll
        else:
            
            backgroundroll = int(backgroundroll)
            if(self.social_class == "Outsider"):
                self.background_roll_table = [[[1,2],["Bohemian"]],[[3,4],["Exile"]],[[5,6],["Outcast"]]]
                for background_score in self.background_roll_table:
                    if( backgroundroll in background_score[0]):
                        return background_score[1][0]
            elif(self.social_class == "Lower Class"):
                self.background_roll_table = [[[1,2],["Military"]],[[3,4],["Laborer"]],[[5,6],["Urban"]]]
                for background_score in self.background_roll_table:
                    if( backgroundroll in background_score[0]):
                        return background_score[1][0]
            elif(self.social_class == "Middle Class"):
                self.background_roll_table = [[[1,2],["Academic"]],[[3,4],["Suburban"]],[[5,6],["Trade"]]]
                for background_score in self.background_roll_table:
                    if( backgroundroll in background_score[0]):
                        return background_score[1][0]
            else:
                self.background_roll_table = [[[1,2],["Aristocratic"]],[[3,4],["Corporate"]],[[5,6],["Cosmopolitan"]]]
                for background_score in self.background_roll_table:
                    if( backgroundroll in background_score[0]):
                        return background_score[1][0]
            
    def __repr__(self): 
        return self.name+ "," + self.age+ "," +self.height + "," +self.weight + "," +self.personality + "," +  str(self.accuracy) + "," + str(self.communication) + "," + str(self.constitution) + "," + str(self.dexterity) + "," + str(self.fighting) + "," + str(self.intelligence) + "," + str(self.perception) + "," + str(self.strength) + "," +str(self.willpower) + "," + self.origin + "," + self.social_class + "," + self.background + "," + str(self.fortune) + "," + self.conditions 
   