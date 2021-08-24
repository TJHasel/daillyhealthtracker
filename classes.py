
class User():
    '''
    A class object to contain information on the user's current weight, 
    ideal weight, and calculate ideal intake to achieve their weight goals
    
    Attributes: 
    __current_weight (int): The user's current weight in lbs
    ideal_weight (int): The user's target weight to be achieved in lbs
    name (str): User's first name

    '''
    #constructor to with current weight, ideal weight, and name attributes
    def __init__(self, currentweight=100, idealweight=160, name="Tom"):
        '''
        Constructor of the User() class

        Parameters:

        currentweight(int) - user's current weight in lbs
        idealweight(int) - user's ideal weight in lbs
        name - User's first name
        
        '''
        #attr.
        self.__current_weight = int(currentweight)
        self.ideal_weight = int(idealweight)
        self.name = name
    
    def cal_calculation(self, calories_consumed, calories_burned):

        '''
        Method of the User() class that calculates how much the
        user was below or above the target caloric intake 
        for the day
        
        Parameters:

        calories_consumed - how many calories the use had taken in that day
        calories_burned - how many calories the user had 
        burned that day from exercise
        
        Returns:

        whether or not user was above or below their intake goal 
        for the day. if they were, it will be displayed as good, 
        bad if not. The difference in actual caloric intake v. ideal will 
        be displayed.
    
        '''
        #get ideal weight caloric intake
        i = self.ideal_weight * 12
       
        #get base level difference from calories consumed v. burned
        d = calories_consumed - calories_burned
        
        #check to see if above or below target intake
        if d <= i:
            return f'=> You were below target intake today by {d-i} cals! :)'
        else:
            return f'=> You were over target intake today by {d-i} cals :|'
    
    def weight_grabber(self, date, weight):
        '''
        Contains and returns the weight of the user and date

        Parameters:

        date - to be date in time
        idealweight(int) - to be weight of user

        Returns:

        weight displayed, date displayed
        
        '''
        #grab weight and date and return
        date1 = f'Date: {date}'
        weight1 = f'Weight: {weight}'
        return date1, weight1

    def __repr__(self):
        '''
        __repr__ method to pull name and current weight 
        of the user in string format

        Parameters:

        N/A

        Returns:

        name and current weight of the user

        '''
        #name/weight 
        return f'(name = {self.name}, weight = {self.__current_weight})'

    def __add__(self):

        '''
        Magic method to add ideal weight to current weight

        Parameters:

        N/A

        Returns:

        ideal weight and current weight

        '''
        return self.ideal_weight + self.__current_weight

if __name__ == '__main__':
    #instantiating the class with new User type (user1)
    user1 = User(currentweight=165, idealweight=145, name="James")

    def unit_tests():
        #assert to test get_word, using index of 3
        assert user1.cal_calculation(1000,500) == ("=> You were below target " 
        "intake today by -1240 cals! :)"), "Error!"
        assert user1.weight_grabber("08/18/21","200") == ('Date: 08/18/21', 
        'Weight: 200'), "Error!"
        assert "James" in user1.__repr__(),  "Error!"
        assert user1.__add__() > user1.ideal_weight, ("Error, addition ",
        "did not work")

        print("Passed all assert tests!")
    
    unit_tests()