
class Triangle:
    def __init__(self, angle1, angle2, angle3): 
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

        number_of_sides = 3    
    
    def check_angles(self): 
            while self.angle1 and self.angle2 and self.angle3 > 0: 
                if self.angle1 + self.angle2 + self.angle3 == 180.00:
                    return True 
                else: 
                    return False
            print ("No negative values for angles, please." )
            return False 

my_triangle = Triangle(30,20,90)

print (my_triangle.angle1, my_triangle.angle2, my_triangle.angle3)
print (my_triangle.check_angles())

