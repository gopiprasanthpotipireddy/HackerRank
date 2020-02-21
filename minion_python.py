
def minion_game(string):
    # your code goes here
    vowels=['A','E','I','O','U']
    stuart_score=0
    kevin_score=0
    combinations=[]

    for i in range(len(string)):
        j=0
        while (j+i)<len(string):
            s=string[j:j+i+1]
            if s[0] in vowels:
                kevin_score+=1
            else :
                stuart_score+=1
            j+=1

    #         if string[j:j+i+1] not in combinations:
    #              combinations.append(string[j:j+i+1])
           
                
    #         j+=1
    
    
    # for i in combinations:
    #     if i[0] in vowels:
    #         kevin_score+=string.count(i)
    #     else:
    #          stuart_score+=string.count(i)
    if stuart_score>kevin_score :
        print("stuart ",stuart_score)
    elif stuart_score<kevin_score :
        print("kevin ",kevin_score)
    else :
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)