#question 1

#for taking custom input
# l = list(map(int, input().split(",")))
print("Answer 1: ", end=" ")
l = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
     953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
     687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
     742, 717, 958, 743, 527]
res=[]
for i in l:
    if i>237:
        break
    if i%2==0: #checking if even
        res.append(i)
print(res, end =" ")
print(" ")
######################################
#question 2

print("Answer 2: ", end=" ")
s1 = set(["White", "Black", "Red"])
s2 = set(["Red", "Green"])
print(s1-s2)

#######################################
# question 3
print("Answer 3: ", end=" ")
al ="abcdefghijklmnopqrstuvwxyz"

#we can take custom input as well
s="asdfgwerfghgfdcfvbvccvb vcv"
f=0
for i in al :
    if i not in s:
        f=1
if(f==0):
    print("TRUE")
else :
    print("False")

######################################
#question 4
print("Answer 4: ", end=" ")
n =3
print(n+int(str(n)*3)+int(str(n)*2))


######################################
#question 5
print("Answer:5 ",end =" ")
q= "23 24 45#345 34 12"
l = list(map(str, q.split()))
l1 = [int(l[0]), int(l[1]), int(l[2][:l[2].index("#")])]
l2 = [int(l[2][l[2].index("#") + 1:]), int(l[3]), int(l[4])]
print("l1: ", *l1)
print("l2:", *l2)

######################################
#question 6

print("Answer 6: ", end=" ")
p = "without,hello,bag,world"

#sorting the list
l = sorted(list(map(str, p.split(","))))
print(*l)

######################################
#question 7
print("Answer:7 ",end =" ")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakh'],'Marks': [57,87,67,79]}
marks_list = d['Marks']
max_marks = max(marks_list)
max_marks_index = marks_list.index(max_marks)
student_list = d['Student']
print(student_list[max_marks_index])


######################################
#question 8
print("Answer:8 ",end =" ")
t ="HelloWorld131 !"
l =0
n =0
for i in range(len(t)):
    if(t[i].isalpha()):
        l+=1
    elif(t[i].isdigit()):
        n+=1
print('LETTERS ' + str(l))
print('DIGITS ' + str(n))

print()
#######################################
# question 9
print("Answer:9 ",end =" ")
d = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

d1 = {'Name' : [],'Ratings' : []}
index = 0
for sub in d['Subject']:
    if(sub == 'Python'):
        d1['Name'].append(d['Name'][index])
        d1['Ratings'].append(d['Ratings'][index])
    index += 1

print('New dictionary: ',d1)
######################################
# question 10
print("Answer 10: ", end=" ")


class gene:
    def __init__(self):
        self.l = []


    def solve(self, n):
        for i in range(1, n):
            if i % 7 == 0:
                self.l.append(i)
        print(*self.l)
s = gene()
s.solve(100)
######################################
# question 11
print("Answer: 11 ", end  =" ")
import math
pos=[0,0]
moves={"UP":[0,1],
       "DOWN":[0,-1],
       "LEFT":[-1,0],
       "RIGHT":[1,0]}
data=["UP 5",
    "DOWN 3",
    "LEFT 3",
    "RIGHT 2"]
for inp in data:
    parts=inp.split()
    mv=parts[0]
    val=parts[1]
    if mv in moves and val.isnumeric():
        pos[0] += moves[mv][0]*int(val)
        pos[1] += moves[mv][1]*int(val)
distance=math.sqrt(pos[0]**2 + pos[1]**2)
print(distance)
######################################


