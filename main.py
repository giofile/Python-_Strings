# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goal_scorer_one = "Ruud Gullit"
goal_scorer_two = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = goal_scorer_one +' '+ str(goal_0) + ', ' + goal_scorer_two+' ' + str(goal_1) 
print(scorers)


report = f"{goal_scorer_one} scored in the {goal_0}nd minute\n{goal_scorer_two} scored in the {goal_1}th minute"
print(report)


player = "Ruud Gullit"
# player_two = "Wim Suvrijn"
first_name = player[0:player.find(' ')]
print(first_name)
# first_name_two = player_two[0:player_two.find(' ')]
# print(first_name_two)



# last_name = player[player.find(" ")+1:]
# print(last_name)




last_name_len = len(player[player.find(' ')+1:])
print (last_name_len)

name_short = player[0] + '.' + player[player.find(' '):]
print(name_short)


# chant = 3*(first_name+"! \t") 
# print(chant)
# chant_test_een =  first_name + "!"
# print(chant_test_een)
# test_twee = len(first_name) - 2
# # print(test_twee)   #  3 keer een chant
# test_drie = len(first_name) - 1
# print(test_drie)   #  4 keer een chant


chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!')
print(chant)


good_chant = chant[-1] != " "
print(good_chant)

