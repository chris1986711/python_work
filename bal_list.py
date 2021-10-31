balls = ["blue", "yellow", "red", "red", "orange", "blue", "yellow"]

print ("this is ball list:",balls)

print()
#有幾種顏色

n_colors_balls = len(set(balls))

print("How many colors in balls:",n_colors_balls)

print ("colors in balls",set(balls))

print()

#有幾顆球

n_balls = len(balls)

print ("How many balls :",n_balls)

print()

#每一種顏色有幾個

n_blue_ball = balls.count("blue")
n_yellow_ball = balls.count("yellow")
n_red_ball = balls.count("red")
n_orange_ball = balls.count("orange")

print( "How many blue balls:",n_blue_ball )
print( "How many yellow balls:",n_yellow_ball )
print( "How many red balls:", n_red_ball)
print( "How many orange balls:", n_orange_ball)
print()

#最多顏色的球是什麼色

n_balls = [n_blue_ball,n_yellow_ball,n_red_ball,n_orange_ball]

max_n_ball=[]

max_n_ball_color = max(n_balls)

if n_blue_ball == max_n_ball_color:
   max_n_ball.append("blue")
if n_yellow_ball == max_n_ball_color:
   max_n_ball.append("yellow")
if n_red_ball == max_n_ball_color:
   max_n_ball.append("red")
if n_orange_ball == max_n_ball_color:
   max_n_ball.append("orange")
print ("maximun number ball color:",max_n_ball)   

print()
#那個顏色的球最少

min_n_ball=[]

min_n_ball_color = min(n_balls)

if n_blue_ball == min_n_ball_color:
   min_n_ball.append("blue")
if n_yellow_ball == min_n_ball_color:
   min_n_ball.append("yellow")
if n_red_ball == min_n_ball_color:
   min_n_ball.append("red")
if n_orange_ball == min_n_ball_color:
   min_n_ball.append("orange")
print ("minimun number ball color:",min_n_ball)

print()
#平均每個顏色有幾顆球

print ("avg ball in color:",sum(n_balls)/len(n_balls))

print()
#打印每個顏色及其數量

color_and_number = [("blue",n_blue_ball),("orange",n_orange_ball),("red",n_red_ball),("yellow",n_yellow_ball)]

print ("color and how many:",color_and_number)

print()
#打印出顏色數量由大到小

def takeSecond(elem):
    return elem[1]
 
color_and_number.sort(reverse=True,key=takeSecond)

print ("由大到小排列:",color_and_number)