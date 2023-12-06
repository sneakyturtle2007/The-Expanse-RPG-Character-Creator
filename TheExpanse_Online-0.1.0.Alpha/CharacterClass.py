class character:
    def __init__(self,name,age,height,weight,personality,accuracy, communication,constitution,dexterity,fighting,intelligence,perception,strength,willpower,origin,social_class,background,fortune):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.personality = personality
        self.accuracy = self.set_ability_score(accuracy)
        self.constitution = self.set_ability_score(constitution)
        self.fighting = self.set_ability_score(fighting)
        self.communication = self.set_ability_score(communication)
        self.dexterity = self.set_ability_score(dexterity)
        self.intelligence = self.set_ability_score(intelligence)
        self.perception = self.set_ability_score(perception)
        self.strength = self.set_ability_score(strength)
        self.willpower = self.set_ability_score(willpower)
        self.origin = self.set_origin(origin)
        self.social_class = self.set_social_class(social_class)
        self.background = self.set_background(background)
        self.fortune = int(fortune)
    
    def set_ability_score(self,ability_score):
        self.ability_score_table = [[[3],-2], [[4,5],-1],[[6,7,8],0],[[9,10,11],1], [[12,13,14],2], [[15,16,17],3], [[18],4]]
        for range_and_score in self.ability_score_table:
            if(ability_score in range_and_score[0]):
                return range_and_score[1]
    
    def set_stats(self,stats):
        self.name = stats[0]
        self.age = stats[1]
        self.height = stats[2]
        self.weight = stats[3]
        self.personality = stats[4]
        self.accuracy = self.set_ability_score(stats[5])
        self.constitution = self.set_ability_score(stats[6])
        self.fighting = self.set_ability_score(stats[7])
        self.communication = self.set_ability_score(stats[8])
        self.dexterity = self.set_ability_score(stats[9])
        self.intelligence = self.set_ability_score(stats[10])
        self.perception = self.set_ability_score(stats[11])
        self.strength = self.set_ability_score(stats[12])
        self.willpower = self.set_ability_score(stats[13])
        self.origin = self.set_origin(stats[14])
        self.social_class = self.set_social_class(stats[15])
        self.background = self.set_background(stats[16])
        
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
        return self.name+ "," + self.age+ "," +self.height + "," +self.weight + "," +self.personality + "," +  str(self.accuracy) + "," + str(self.communication) + "," + str(self.constitution) + "," + str(self.dexterity) + "," + str(self.fighting) + "," + str(self.intelligence) + "," + str(self.perception) + "," + str(self.strength) + "," +str(self.willpower) + "," + self.origin + "," + self.social_class + "," + self.background + "," + str(self.fortune)
   