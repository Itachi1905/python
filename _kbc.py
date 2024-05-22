questions = ["When did India got Independent","When did the movie Avengers End Game released","Who manages KBC","Which anime girl is the best","Which is the best anime","Which is the best Harem Anime"]
answers = ["1947","2019","amitabh bachan","kurumi tokisaki","bleach","date a live"]
i = 10000
j = 0
for q in questions :
    print(q)
    k = input("Enter the answer for the above question : ")
    if k == answers[j] : 
        i=i*2
    j = j+1
print(i)
