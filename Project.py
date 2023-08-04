import pandas as pd

def my_cool_function():
    
    age_input = int(input('Enter your age ( 0 -100): '))
    
    gender_input = input('Enter gender (Male or Female): ')
    
    fit_level = int(input('Enter fitness level 0 being unfit and 2 being super fit (0, 1, 2): '))
    
    smoking_status = int(input('Are you a smoker, 0 for no, 1 for yes: '))
    
    user = Create_lapse_decrement_table(gender_input,age_input,fit_level, smoking_status)


    print(f"Your life expectancy is age: {user.find_life_expectancy()}")
    
    
class Create_lapse_decrement_table:
    
    data = {
        'Age': list(range(101)),
        'Male': [0.00361, 0.0002, 0.00012, 0.0001, 8e-05, 7e-05, 7e-05, 6e-05, 6e-05, 6e-05, 6e-05, 7e-05, 9e-05, 0.00013, 0.00018, 0.00024, 0.00032, 0.00041, 0.00047, 0.00052, 0.00055, 0.00056, 0.00057, 0.00058, 0.0006, 0.00061, 0.00062, 0.00063, 0.00064, 0.00066, 0.00067, 0.00069, 0.00071, 0.00074, 0.00078, 0.00082, 0.00087, 0.00093, 0.00099, 0.00107, 0.00116, 0.00126, 0.00136, 0.00149, 0.00163, 0.0018, 0.00197, 0.00215, 0.00234, 0.00255, 0.00277, 0.00301, 0.00327, 0.00355, 0.00386, 0.00421, 0.0046, 0.00503, 0.00549, 0.00597, 0.00647, 0.00701, 0.00762, 0.00829, 0.00898, 0.00969, 0.01047, 0.01135, 0.01236, 0.01351, 0.01482, 0.01629, 0.01797, 0.01986, 0.02202, 0.02451, 0.02738, 0.03063, 0.03437, 0.03866, 0.04349, 0.04887, 0.05484, 0.06156, 0.06917, 0.07778, 0.08749, 0.09849, 0.11104, 0.12541, 0.14154, 0.15941, 0.17874, 0.19903, 0.21969, 0.23821, 0.25575, 0.27398, 0.29467, 0.32259, 0.35157],
        'Female': [0.00299, 0.00019, 8e-05, 8e-05, 7e-05, 7e-05, 6e-05, 6e-05, 6e-05, 6e-05, 6e-05, 7e-05, 8e-05, 0.0001, 0.00012, 0.00015, 0.00017, 0.00019, 0.00021, 0.00022, 0.00023, 0.00023, 0.00023, 0.00024, 0.00024, 0.00024, 0.00025, 0.00025, 0.00025, 0.00026, 0.00027, 0.0003, 0.00032, 0.00035, 0.00039, 0.00043, 0.00047, 0.00051, 0.00055, 0.00059, 0.00063, 0.0007, 0.00079, 0.00088, 0.00099, 0.00108, 0.00117, 0.00128, 0.0014, 0.00152, 0.00165, 0.00177, 0.00191, 0.00208, 0.00228, 0.00248, 0.00269, 0.00292, 0.00317, 0.00345, 0.00377, 0.00411, 0.00445, 0.00482, 0.00523, 0.0057, 0.00622, 0.00684, 0.00754, 0.00839, 0.00936, 0.01042, 0.01163, 0.01298, 0.01449, 0.01616, 0.01795, 0.02001, 0.02247, 0.02547, 0.02897, 0.03308, 0.03776, 0.04312, 0.04923, 0.05623, 0.06439, 0.07373, 0.08438, 0.09674, 0.11091, 0.127, 0.14461, 0.16416, 0.18603, 0.20632, 0.22454, 0.24979, 0.27006, 0.29026, 0.30855]
        }
    
    df = pd.DataFrame(data)
    
    fittness_level = [0,.2,.4]
    
    smoker_loading = 0.4
    
    
    def __init__(self, gender, age, fit_level, smoking_status):
        
        self.gender = gender
        self.age = age
        self.fit = fit_level
        self.smoking_status = smoking_status
        
        
    def create_decrement_list(self):
        if self.gender not in ['Male', 'Female']:
            return "Invalid gender. Please input 'Male' or 'Female'."
        if self.age < 0 or self.age > 101:
            return "Invalid age. Please input an age between 0 and 101."
        
        self.decrement_table = self.df.loc[self.df['Age'] > self.age, self.gender].tolist()
    
    
    def determine_life_expectancy(self):
        self.create_decrement_list()
        
        years_to_onehundred = 100 - self.age
        
        lx_table = [1]
        
        fitness_adjustment = self.fittness_level[self.fit]
        
        for i in range(years_to_onehundred):
            qx = self.decrement_table[i]
            
            new_lx = lx_table[-1] *(1- qx*(1-fitness_adjustment)*(1 + self.smoker_loading* self.smoking_status))
            
            lx_table.append(new_lx)
                        
        self.lx_table = lx_table
        
        
    def find_life_expectancy(self):
        self.determine_life_expectancy()
        
        for i,value in enumerate(self.lx_table):
            if value < 0.5:
                return i + self.age
        return None
            
    
my_cool_function()
