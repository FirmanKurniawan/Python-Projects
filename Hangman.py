print('\t', '\t', '\t', "WELCOME TO Hangman")
print()
print('*'*80)
print('\t', '\t', '\t',"WHAT YOU NEED TO KNOW:", '\n','\t', '\t', "1.Choose a category", '\n','\t', '\t', "2.Try guessing the word within 8 attempts", '\n','\t', '\t', "3.Each correct answer fetches 10 points")
print()
print("Categories:")
d = {"1.Capitals of the World":{'kabul': 'Afghanistan', 'canberra': 'Australia', 'dhaka':'Bangladesh','sofia':'Bulgaria', 'havana':'Cuba','cairo':'Egypt', 'dublin':'Ireland', 'oslo':'Norway', 'pyongyang':'North Korea', 'seoul':'South Korea','ulaanbatar':'Mongolia', 'belgrade':'Serbia','lima':'Peru','damascus':'Syria','ankara':'Turkey', 'kiev':'Ukraine', 'caracas':'Venezula', 'harare':'Zimbabwe', 'jerusalem':'Israel'}, "2.Currencies":{'dinar':'Jordan', 'rupiah' :'Indonesia', 'ringgit':'Malaysia', 'dirham':'Morocco', 'kyat':'Myanmar', 'krone':'Norway', 'rial':'Oman', 'ruble':'Russia', 'won':'South Korea','bhat':'Thailand'}, "3.Mythology" :{"dionysus":"Greek-wine", "hephaestus":"Greek-tinkerer", "luna": "Roman-Goddess of the moon", "bragi":"Norse-God of eloquence", "njord":"Norse-God of the sea", "anubis":"Egyptian-God of funerals", "sobek":"Egyptian-God of crocodiles", "nekhbet":"Egyptian-Goddess of vultures", "dhrishtadyumna":"Indian-Draupadi's brother", "shabari":"Indian-stone woman Ramayana", "vasuki":"Indian-serpent king"} ,"4.Famous authors":{"satyajit ray":"Feluda", "carolyn keene":"Nancy Drew", "agatha christie":"Miss Marple", "roald dahl":"BFG", "enid blyton":"The Faraway Tree", "dan brown":"Langdon", "cassandra clare":"Shadowhunter", "robert galbraith":"The Cuckoo's calling", "amish":"Shiva trilogy", "sudha murthy":"Grandmother tales"}, "5.Harry Potter characters" : {"newt scamander":"Magizoologist", "aberforth dumbledore":"Hog's Head", "xenophilius lovegood":"Quibbler", "charity burbage":"Muggle Studies", "antonin dolohov":"Death Eater- killed Molly weasley's brothers", "regulus black":"Death eater- locket", "madame maxime":"Beauxbatons", "petunia dursley":"Lily's sister", "severus snape":"Doe", "fat friar":"Hufflepuff ghost"}}
sm = 0
count =0
g = 0
sn = 0
for i in d.keys():
        print(i)
re = "Y"
while re =="Y":
        n = input("Enter category: ")
        while n not in ('1','2','3','4','5'):
                print("Sorry!Didn't get you!")
                n = input("Enter the category no.: ")
        nn = int(n)
        while sm<3:
                for i in d:
                        if str(nn)==i[0]:
                                print(i)
                                t = tuple(d[i].keys())
                                for k in t:
                                        import random
                                        r = random.randrange(len(t))
                                        a = t[r]
                                if " " in a:
                                        for kk in a:
                                            if kk!=" ":
                                                    g+=1
                                            else:
                                                    break
                                        b = ('_ ' * g) + "  " + ("_ " *(len(a)-g-1))
                                        print(b, len(a)-1, "characters")
                                else:
                                        b = '_ '*len(a)
                                        print(b, len(a), "characters")
                                for l in d[i]:
                                        if l==a:
                                                h = d[i][l]
                                sm = 3
                                break
                        else:
                                sm+=1

        b = list(b)
        h = str(h)
        i = 0
        while i<8:
                c = input("Enter single character guess(Hint?Press 5) ")
                cc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ5"
                while len(c)>1 or c not in cc:
                        if len(c)>1:
                                print("SINGLE CHARACTER GUESS!")
                        else:
                                print("INVALID!")
                        c = input("Enter a single character guess(Hint?Press 5)")
                ccc = c.lower()
                if ccc not in a:
                        if ccc=='5':
                                print("Hint:", h)
                        else:
                                i+=1
                                print(8-i, "chances left")
                else:
                        for j in range(0,len(a)):
                                if ccc==a[j]:
                                        if j!=0:
                                                b.pop(j*2)
                                                b.insert(j*2,ccc)
                                        else:
                                                b.pop(j)
                                                b.insert(j,ccc)
                        for k in b:
                                print(k,end='')
                if '_' not in b:   
                        i = 8
                        print('\n',"Congratulations!!")
                        count+=10
        if '_' in b: 
                print("Better luck next time!!", '\n', "Answer:", a)
        sm = 0
        g = 0
        sn+=1
        print("Would you like to play again?")
        m = input("Yes or No? ")
        jj = 0
        while jj==0:
                if m.upper()=="YES" or m.upper()=="NO":
                        re = m[0].upper()
                        jj +=1
                else:
                        print("Sorry!Didn't get you!")
                        m = input("Yes or No? ")
print('\t', '\t', '\t','GREAT JOB!!')
print("You guessed", int(count/10), "words out of", sn, "Your total score is", count)
        
               
                
        
                       
                
                
                        
                                
                        
                                 
                         
                 
                        
                        
                
                        
                
       

