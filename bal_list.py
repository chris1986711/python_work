from typing import List

#有幾種顏色

def n_colors(balls: List) -> int:
    """"This function counts balls"""
    return len(set(balls))

#列出所有顏色

def list_colors(balls:list)->list:
    """this function list balls color"""
    return set(balls)

#有幾顆球

def count_balls(balls:list)->int:
   """this function count ball number"""
   return len(balls)

#每一種顏色有幾個

def blue_ball_n(balls:list)->int:
   """this function count blue ball"""
   return balls.count("blue")

def yellow_ball_n(balls:list)->int:
    """this function count yellow ball"""
    return balls.count("yellow")

def red_ball_n(balls:list)->int:
    """this function count red ball"""
    return balls.count("red")

def orange_ball_n(balls:list)->int:
    """this function count orange ball"""
    return balls.count("orange")

#最多顏色的球是什麼色

def max_color(n_balls:dict)->dict:
   return max(n_balls, key=n_balls.get)

#那個顏色的球最少

def min_color(n_balls:dict)->dict:
   return min(n_balls, key=n_balls.get)

#平均每個顏色有幾顆球

#打印每個顏色及其數量

#打印出顏色數量由大到小 
def k(n_balls:dict)->dict:
    return (sorted(n_balls.items(), key=lambda x:x[1],reverse=True))

if __name__ == "__main__":
   balls = ["blue", "yellow", "red", "red", "orange", "blue", "yellow"]
   
   print("所有的球:",balls)
   
   print("有幾種顏色",n_colors(balls))
   
   print("列出所有顏色",list_colors(balls))
  
   print("有幾顆球",count_balls(balls))

   print("有幾顆藍色的球",blue_ball_n(balls))

   print("有幾顆黃色的球",yellow_ball_n(balls)) 

   print("有幾顆紅色的球",red_ball_n(balls))

   print("有幾顆橘色的球",orange_ball_n(balls)) 

#嘗試用Dictionary解決
   
   n_balls = {"blue":blue_ball_n(balls),"yellow":yellow_ball_n(balls),"red":red_ball_n(balls),"orange":orange_ball_n(balls)}
   
   max_key = max_color(n_balls)

   max_balls_number = n_balls[max_key]

   min_key = min_color(n_balls)
   
   min_balls_number = n_balls[min_key]
   
   max_in_n_balls=[]

   min_in_n_balls=[]
   
if blue_ball_n(balls) == max_balls_number:
    max_in_n_balls.append("blue")
if yellow_ball_n(balls) == max_balls_number:
    max_in_n_balls.append("yellow")
if red_ball_n(balls) == max_balls_number:
    max_in_n_balls.append("red")
if orange_ball_n(balls) == max_balls_number:
    max_in_n_balls.append("orange")   
    
if blue_ball_n(balls) == min_balls_number:
    min_in_n_balls.append("blue")
if yellow_ball_n(balls) == min_balls_number:
    min_in_n_balls.append("yellow")
if red_ball_n(balls) == min_balls_number:
    min_in_n_balls.append("red")
if orange_ball_n(balls) == min_balls_number:
    min_in_n_balls.append("orange")

print("最多球的顏色",max_in_n_balls)   

print("最少球的顏色",min_in_n_balls) 

print("平均一個色多少球",count_balls(balls)/n_colors(balls))

print("{顏色：數量}",n_balls)

print("由多到少排序",k(n_balls))