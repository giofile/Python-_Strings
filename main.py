# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goalScorerOne = "Ruud Gullit"
goalScorerTwo = "Marco van Basten"

goalOne = '32nd'
goalTwo = '54th'

scorers = goalScorerOne +  str(goalOne) , goalScorerTwo +  str(goalTwo)
print(scorers)


report = f"{goalScorerOne} scored in the {goalOne} minute\n {goalScorerTwo} scored in the {goalTwo} minute"
print(report)


player = "Ruud Gullit"
first_name =  player[0:5]
print(first_name)

last_name = player[-6:]
print(last_name)

last_name_len = len(player[5:11])
print(last_name_len)

name_short = player[0:1] +'.' +" "+ last_name
print(name_short)

chant = 3*(first_name+"!") 
print(chant)



