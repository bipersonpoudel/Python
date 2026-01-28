import random
number_of_questions=int(input("Enter Number of Questions from 1 to 12 :"))
questions=("What is the capital city of Australia? ",
"Which planet in our solar system is known for having the most moons? ",
"Which element has the chemical symbol Fe?",
"What is the smallest country in the world by area?",
"Who painted the ceiling of the Sistine Chapel?",
"Which year did the Titanic sink?",
"Which famous physicist developed the theory of general relativity?",
"What is the hardest natural substance on Earth?",
"Which country is known as the Land of the Rising Sun?",
"What is the largest internal organ in the human body?",
"Which famous ship was discovered at the bottom of the Atlantic in 1985?",
"What is the main language spoken in Brazil?")
options=("A) Sydney \n B) Melbourne \n C) Brisbane \n  D) Canberra \n",
         "A) Saturn\nB) Jupiter\n C) Neptune\n D) Mars\n",
         "A) Fluorine\n B) Francium\n  C) Iron\n D) Fermium\n",
         "A) Monaco\nB) Vatican City\nC) San Marino\nD) Liechtenstein\n",
         "A) Leonardo da Vinci\nB) Raphael\n C) Michelangelo\nD) Donatello\n",
         "A) 1910\nB) 1912\nC) 1914\nD) 1920\n",
         "A) Isaac Newton\nB) Nikola Tesla\nC) Albert Einstein\nD) Stephen Hawking\n",
         "A) Gold\nB) Quartz\nC) Diamond\nD) Obsidian\n",
         "A) China\nB) Japan\nC) Thailand\nD) South Korea\n",
         "A) Heart\nB) Liver\nC) Lung\nD) Kidney\n",
         "A) HMS Bounty\nB) Lusitania\nC) Titanic\nD) Queen Mary\n",
         "A) Spanish\nB) Portuguese\C) French\nD) English\n")
answers=("D","A","C","B","C","B","C","C","D","B","C","B")
score=0
asked_questions = set()  
for i in range (0,number_of_questions):
    while True:
        rand_no = random.randint(0, len(questions) - 1)
        if questions[rand_no] not in asked_questions:
            
            print(questions[rand_no])
    
            print(options[rand_no])
            answer=input("Enter Your answer (A, B, C, D) : ").upper()
 
            print("\n")

            asked_questions.add(questions[rand_no])
            break
        
    
          # unique question found, exit the loop

    
  

    if (answer==answers[rand_no]):
        score +=1
    
print("Your Total score is ",score)