###VISUALS###

import turtle

for x in range(180):
    turtle.backward(1)
    turtle.right(1)

turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(425)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.right(90)

for x in range(180):
    turtle.backward(1)
    turtle.right(1)
    
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(75)
turtle.right(45)
turtle.backward(100)
turtle.left(45)
turtle.backward(100)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.backward(90)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.right(45)
turtle.backward(75)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(125)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(125)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)

turtle.bye()


###INTRO###

print("Hi! This is a Hangman X History Quiz !!! \nWe will be focusing on Chapter 2\n")
print("Firstly, An Overview: \nStalin’s aim is to consolidate power and to modernise the Soviet Union to become a socialist state which is self sufficient and militarily strong\n")
print("0.\tEconomic Impact \nAIM: to modernise the USSR and catch up with western powers \n\t⁃Five-Year Plans \n\t⁃Collectivisation \n\t⁃Rapid Industrialisation \n")
print("0.\tPolitical Impact \n⁃Summary: Communist party was unpopular and Russian society was very unstable \n⁃In response: Stalin started the Great Terror (1934-1938) and used extensive propaganda \n")
print("0.\tSocial impact \n⁃Overview: Increased control over Everyday social life, living in fear, impact of policies on various groups \n⁃State Control of society : Fall in standard of living, famine, lack of consumer goods \n⁃Living in fear: secret police, gulags \n⁃Impacts on various groups: minority republics lost autonomy, publishing the ideal soviet man, women entering the workforce, compulsory education \n")

ready =""
while ready != "yes" :
    ready=input("Are you ready? (Type yes/no)\n")

print("\n\n\n")
###Hangman quiz

print("Now, with the brief summary of Chapter 2, The hangman quiz will start\n")
print("\n\tQUIZPLAY!!\n1.Try and guess the hangman word \n**CLUE: The word is a person who played a role in Chapter 2** \n2.Everytime your guess is wrong, a short quiz will start(3 - 6 questions, 30m) \n**The number of questions depends on whether you get the answer correct or wrong** \n3.After the quiz is done, a part of the word will be revealed \n4. Once the word is guessed, you will be directed to a final quiz to test your knowledge \n")
print("\n\tRULES!!\n1.Type all your answers in SMALL LETTERS.\n2.There is only ONE-TRY")
print("\n\nS\n\tT\n\t\tA\n\t\t\tR\n\t\t\t\tT\n\t\t\tR\n\t\tA\n\tT\nS\n\n\n")

list_of_words = ["politburo","l.trotsky","karl marx"]
import random
word = str(list_of_words[random.randint(0,2)])

total_correct_score = 0
number = 0
order = 0
reveal = -1



Question_set = [["Q1. MCQ: When did Lenin die? \n1)1921 \n2)1924 \n3)1929 ",
                 "Q2. What are the positive outcomes of Collectivisation? ",
                 "Q3. MCQ: What was Rapid Industrialisation? \n1) Development of industries (factories, coal, etc) \n2) researching and creating better weaponry \n3) Development of the cafe industry ",
                 "Q4. Why did Stalin start the Great Terror? ",
                 "Q5. MCQ: What are the effects of State control of society? \n1) Opioid Crisis \n2) Famine \n3) Homeless problems ",
                 "Q6. MCQ: What was the result of the State control of society? \n1) Increase of consumer goods \n2) More money printing \n3) Fall in standing of Living \n4) All of the above"
                 ],
                ["Q1. What are the key measures of collectivisation? ",
                 "Q2. MCQ: What was the ideal ‘Soviet Man’? \n1) A proud citizen willing to serve Russia selflessly \n2) communist-loving toilet paper dealers \n3) a toilet paper lover. ",
                 "Q3. MCQ: What are the key measures of collectivisation? \n1) bribery \n2) moral persuasion \n3) Quotas, working hours and wages ",
                 "Q4. What was Stalin’s key aim? ",
                 "Q5. MCQ: why did Stalin start The Great Terror? \n1) He felt like it \n2) He had to remove domestic opposition to the Soviet government \n3) he wanted people to love him",
                 "Q6. MCQ: What was a positive impact of Stalin’s social policies? \n1) Compulsory schooling \n2) Jon Snow came back to life \n3) Increase standard of living for citizens"
                 ],
                ["Q1. MCQ: Which of the following did NOT contribute to Stalin’s success? \n1) Trotsky turned up late for Lenin’s funeral \n2) Trotsky had a lesser IQ than Stalin \n3) Stalin used his powers as Secretary General",
                 "Q2. What are the positive effects of the Five-Year Plans?",
                 "Q3. MCQ: What was the positive outcomes of collectivisation? \n1) kulaks destroyed and land collectivised \n2) free toilet paper \n3) Distribution of wealth",
                 "Q4. MCQ: What is the aim of the Five-Year Plan? \n1) Modernise Soviet society by introducing women to the workforce \n2) Researching better weapons \n3) Modernise the USSR and catch up with Western Powers ",
                 "Q5. How did Stalin distribute his propaganda? ",
                 "Q6. MCQ: What was a key characteristic of the propaganda Stalin used? \n1) it portrayed Stalin as a rightful successor of Lenin \n2) Stalin was showed as a Jew \n3) Stalin was actually Jon Snow from Game of Thrones "
                 ]]

Answer_set = [["2",
               "collectivised",
               "1",
               "communist party",
               "2",
               "3"
               ],
              ["quotas",
               "1",
               "3",
               "consolidate",
               "2",
               "1"
               ],
              ["2",
               "rapid industrialisation",
               "1",
               "3",
               "media",
               "1"
               ]]

Solution_set = [["The answer is 2, Lenin died on 1924",
               "Farm collectivised, there was enough manpower for factories and enough grain to feed the people",
               "The answer is 1, Rapid Industrialisation refers to the development of Industries such as coal and oil.",
               "The Communist Party was extremely unpopular and the society was unstable",
               "The answer is 2, Famine was one of the effects of State control. Others include the fall in standard of living.",
               "The answer is 3, Fall in standard of living was one of the consequences of State control."
               ],
              ["Quotas, working hours and wages were set for workers",
               "The answer is 1, The ideal Soviet Man was someone who was patriotic, loyal and  would serve Russia selflessly",
               "The answer is 3, quotas, working hours and wages were set for workers",
               "Stalin's aim was to consolidate his power and to modernise the Soviet Union",
               "The answer is 2, Stalin started the Great Terror to remove opposition within the Soviet Government",
               "The answer is 1, Stalin's policies introduced compulsory schooling."
               ],
              ["The answer is 2, When Trotsky turned up late for the funeral, it made the public view him in a negative light",
               "Rapid Industrialisation was achieved, and the kulaks were destroyed",
               "The answer is 1, the Kulaks (private farms) were destroyed as land was collectivised.",
               "The answer is 3, The Five-Year Plan was created to modernise the Soviet Union and catch up with Western powers",
               "Stalin distributed his power through the Media and Arts",
               "The answer is 1, Stalin was potrayed as the rightful successor of Lenin."
               ]]

hints = [["_ _ _ " , word[3] , " _ " , word[5] , " _ _ _"],
         ["_ " , word[1], " _ " , word[3] , " _ " , word[5] , " _ " , word[7:]],
         [word[:6] , " _ " , word[7:]],
         [word]]
        

Letter_order = [["3","5"],["1","7","8"],["2","0","4"],["6"]]



def wordreveal(letter):
    global reveal
    reveal += 1
    if len(letter) == 2:
        print("REVEALMENT TIME!!\nThe letters are ", word[int(letter[0])],"and",word[int(letter[1])])
    else:
        print("REVEALMENT TIME!!\nThe letters are ", word[int(letter[0])],"and",word[int(letter[1])],"and",word[int(letter[2])])
    print("".join(hints[reveal]),"\n")
    
    
    

def wordquiz(Questions,Answer,Solution):
    points = 0
    i = 0
    while points < 30:
        print(Questions[i])
        userans = input()
        if Answer[i] in userans and userans.isspace()==False and userans != "":
            points += 10
            print("You are right!!\t You get 10 points")
            print(Solution[i],"\n")
        else:
            points += 5
            print("You are wrong!!\t You get 5 points")
            print(Solution[i],"\n")
        i += 1
    wordreveal(Letter_order[order])


userword = input("What is the Word?\n=")
if userword == word:
    print("You got it right!!XD")
else:
    print("That's not the word! :(")
             
while userword != word and number <= 2:
    print("We will be starting a short quiz.\nA part of the word will be revealed after!\nGood Luck!\n")
    wordquiz(Question_set[number],Answer_set[number],Solution_set[number])
    order += 1
    number += 1
    userword = input("What is the Word?\n=")
    if userword == word:
        print("You got it right!!")
    else:
        print("That's not the word! :(")
        continue


###THE FINAL QUIZ


print("\n\nCongratulations!!\nYou have finished the hangman quiz. Now, you should have a better knowledge about Chapter 2 of your history textbook.\nHope you had a good time.\nNow, to check on your knowledge. We wil be starting the FINAL QUIZ!!\nDon't worry, it won't be that difficult.\nGOODLUCK!!\n")

Qns = ["Q1. What was the Great Terror?",
       "Q2. What are the positive outcomes of Collectivisation? ",
       "Q3. What was the gosplan? ",
       "Q4. Define ‘consolidation of power.",
       "Q5. How was Rapid Industrialisation promoted by the state? ",
       "Q6. What happened to Minority republics of the former Russian Empire? ",
       "Q7. What did Stalin develop with propaganda? ",
       "Q8. MCQ: What is a Key characteristic of The Great Terror? \n1) Propaganda \n2) Show Trials \n3) Attacks on Poland \n4) Alliance with Germany",
       "Q9. Why did the Soviet people live in fear?",
       "Q10. MCQ: What was the result of the State control of society? \n1) Increase of consumer goods \n2) More money printing \n3) Fall in standing of Living",
       ]

Ans = ["political repression",
       "collectivised",
       "state planning agency",
       "strengthen political position",
       "education",
       "autonomy",
       "cult of personality",
       "2",
       "gulags",
       "3"
       ]

Sol = ["The Great Terror refers to policitcal repression.",
       "The kulaks were destroyed and land was collectivised",
       "The Gosplan as the State Planning Agency",
       "'Consolidation of power' is The concentration of authority to strengthen political position",
       "Education schemes were introduced, and women were allowed to enter the workforce",
       "Minority republics lost their autonomy",
       "Stalin developed his propaganda with the cult of personailty",
       "The answer is 2, Show trials were common to deter citizens from not supporting Stalin.",
       "The citizens were afraid of the secret police, and the punishments they face such as the gulags",
       "The answer is 3, The standard of living fell after the State started to control the society."
       ]



def finalquiz(Qns,Ans,Sol):
    global total_correct_score 
    points = 0
    i = 0
    while points < 50:
        print(Qns[i])
        userans = input()
        if Ans[i] in userans and userans.isspace()==False and userans != "":
            points += 10
            total_correct_score += 10
            print("You are right!!\t You get 10 points")
            print(Sol[i],"\n")
        else:
            points += 5
            print("You are wrong!!\t You get 5 points")
            print(Sol[i],"\n")
        i += 1


finalquiz(Qns,Ans,Sol)

print("Congratulations!!You got" ,(total_correct_score), "points out of 50 points")
print("\n")
    
###CONCLUSION###


print("CONCLUSION\n")
print("This is the end of the quiz.\nHope you have either revised your knowledge on Chapter 2 or even found out new facts!\nTo end it off, we provided a conclusion for you\n\n")
print("⁃Stalin’s policies did not completely devastate the USSR, there were economic, political and social successes \n⁃But it came at a great human cost \n\t•lack of freedom \n \t•punishments \n\t•death \n")
print("⁃But we need to question if the achievements were real or fraudulent \n \t•rise in education, but filled with propaganda \n\t•Rapid Industrialisation, though results could be faked by factory managers to avoid punishments \n")
print("Thank You and Bye!!")
