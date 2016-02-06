import random
rand_num=random.randint(1,10)
guesses=[]
allowed=5
while len(guesses)<allowed:
    guess=input("guess a number btw 1 and 10 : ")

    try:
        player_num=int(guess)
    except:
        print("please enter a whole no")
        break
    
    if not player_num>0 or not player_num<11:
        print("please enter btw 1 and 10 only...!!")
        break

    guesses.append(player_num)

    if player_num==rand_num:
        print("YEs!!You have guessed the number!!")
        print("it took u {} tries to guess the no".format(len(guesses)))
        break
    else:
        if rand_num>player_num:
            print("nope!My no is higher than {} -- guess#{}".format(player_num,len(guesses)))
        else:
            print("nope!My no is lower than {} -- guess#{}".format(player_num,len(guesses)))
        continue
if not rand_num in guesses:
        print("sorry bhai! my no was {}".format(rand_num))
        
        
    
