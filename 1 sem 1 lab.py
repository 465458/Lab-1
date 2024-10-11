RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'


#first part of the task
for i in range(4):
    print(GREEN + ' ' * 10 + YELLOW + ' ' * 20 + END)
for i in range(4):
    print(GREEN + ' ' * 10 + RED + ' ' * 20 + END)


#second part of the task
s1 = (WHITE + '   ') + (WHITE + '   ' * 3 + BLACK + '   ' + WHITE + '   ' * 2) * 6 + (WHITE + '   ' * 2) + END
s2 = (WHITE + '   ') + (WHITE + '   ' * 2 + BLACK + '   ' * 3 + WHITE + '   ') * 6 + (WHITE + '   ' * 2) + END
s3 = (WHITE + '   ') + (WHITE + '   ' + BLACK + '   ' * 5) * 6 + (WHITE + '   ' * 2) + END
s4 = WHITE + '   ' + BLACK + '   ' * 37 + END + WHITE + '   ' * 1 + END
s5 = BLACK + '   ' * 39 + END
s = [s1,s2,s3,s4]
for i in s:
    print(i)
print(s5)
for i in s[-1::-1]:
    print(i)


#third part of the task
for i in range(10,-1,-1):
    print(i * '   ' + GREEN + '   ' + END)


#fourth part of the task
a = [float(i) for i in open('sequence.txt')]
a1 = [i for i in a if -5<=i<=0] #len = 71 ~ 52,2%
a2 = [i for i in a if 0<=i<=5] #len = 65 ~ 47,8%
pr_a1 = round(100*len(a1)/136,1)
pr_a2 = round(100*len(a2)/136,1)
shkala = ''
for i in range(0,101,10):
    if len(str(i)) == 1:
        shkala = shkala + '|' + str(i) + '%       '
    if len(str(i)) == 2:
        shkala = shkala + '|' + str(i) + '%      '
    if len(str(i)) == 3:
        shkala = shkala + '|' + str(i) + '%'
print(GREEN + ' ' + END + ' - числа от -5 до 0 включительно')
print(YELLOW + ' ' + END + ' - числа от 0 до 5 включительно')
print(WHITE + shkala + END)
print(GREEN + ' ' * (int(pr_a1)-len(str(pr_a1) + '%')) + str(pr_a1) + '%' + END)
print(YELLOW + ' ' * (int(pr_a2)-len(str(pr_a2) + '%')) + str(pr_a2) + '%' + END)