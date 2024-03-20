#Chef is currently facing the north direction. Each second he rotates exactly 90 degrees in clockwise direction. Find the direction in which Chef is facing after exactly X seconds.

#Note: There are only 4 directions: North, East, South, West (in clockwise order).

#Input Format
#First line will contain T, number of testcases. Then the testcases follow.
#Each testcase contains of a single integer X.

#Output Format

#For each testcase, output the direction in which Chef is facing after exactly X seconds.

#Constraints
#1≤T≤100
#1≤X≤1000
#Sample Input 1 
#3
#1
#3
#6
#Sample Output 1 
#East
#West
#South
#Explanation
#Chef is facing North in the starting.

#Test Case 1: After 1 second he turns 90 degrees clockwise and now faces the east direction.

#Test Case 2: Direction after 1 second- east

#Direction after 2 seconds- south
T=int(input())
X=int(input())
for i in range(T):
    r=X%4
    if(r==0):
        print("North\n")
    if(r==1):
        print("East\n")
    if(r==2):
        print("South\n")
    if(r==3):
        print("West\n")
    i+=1
