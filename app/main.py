import random
import countries
import places

print('''
    .-"       \-.                       
      /           ; \                      
     :           /:  \                     
     ;         .'  ;  ;                    
     ;      .-"    :  :                    
    :   _.+(   .-- :  :                    
    ;  ;   ' :  :                    
    ;  :           ;  ;                    
    :   ;    -    :  :                     
     )  '   .-.   '  :                     
    (    '. `"' .'   ;                     
     "-._.:`---':-"-.'+'                   
          ;     ;    "                     
   _..__.-. -. (:                          
 ,'   .:(o);     "-._                      
 :    _: 0 ;        \`.                    
 ;  .'/.\-/-.        `:                    
:  : :  -U--:"-.  \    ;                   
;  ; :  ----;   "-.L.-" \                  
'. '  \ ---(      ;O:    ;                 
  \ '. '-;-'      :-:    :                 
   `. ""/         ; :    ;                 
     ""T      .-":  :`. /                  
       :  --""   :   ; Y                   
        ;        ;   : :                   
        :       :     ; ;                  
         ;      :   ; : :                  
         :      ;   :  ; \                 
          ;    :    ;  :  \_               
          :    :        \  \"-.            
          ;    ;         \  `. "-.         
         :    :     c     \   `./"-._      
         ;    :            \    \    "-.   
        :     ;             `.   ;-.  -.`. 
        :    :       __..--"" \  :  `.\.`.\
        ;    :_..--"";  ;  _.-'\  ;   ")))T
       :     ;      _L.-'""     ; :    '-='
       ;    :_..--""            :  ;       
      /     ;                   ;; :       
    .'     /                    ;: J       
    `.    /                     ;'"        
      :-.'         /\           ;          
      ;           /  ;          :          
     :           /   :          :          
     ;          /     ;         :          
    :          /  bug ;         :          
    ;         /       :         :          
   :         /        :         :

   CARMEN SANDIEGO GAME
         CREATED TO LEARN PYTHON
''')

print("==================================================")

print("Welcome to the Carmen Sandiego game!")
detective_name = input("Detective on keyboard, please, identify yourself: \n")


def main():
    global detective_experience
    global detective_life
    global carmen_sandiego_life

    carmen_sandiego_life = 10
    detective_experience = 0
    detective_life = 5

    while detective_life > 0 and carmen_sandiego_life > 0:
        setup()
        first_message()

    setup()
    if detective_life < 0:
      print("Carmen Sandiego scape and nobody knows where she is... you lose!")
      print("GAME OVER")
    elif carmen_sandiego_life < 0:
      print("You catch Carmen Sandiego and recover the object! You win!")
      print("GAME OVER")


def first_message():
    global detective_experience
    global detective_life
    global carmen_sandiego_life

    print("=======================================================================")
    if detective_experience < 3:
        print("You position at the agency is: Rookie")
    elif detective_experience >= 3 and detective_experience < 6:
        print("You position at the agency is: Detective")
    elif detective_experience >= 6 and detective_experience <= 10:
        print("You position at the agency is: Senior Detective")
    print("=======================================================================")

    print("Detective " + detective_name + ", you have " +
          str(detective_experience) + " experience points.")

    print("=======================================================================")

    print("")
    print("")
    print(
        "************************* URGENT MESSAGE ******************************"
    )
    print("")
    print("Carmen Sandiego has stolen a valuable object!")
    print("We need you to find her and recover the object.")
    print("=======================================================================")
    print("Your phone is ringing...")
    print(f"Hi detective " + detective_name + ", I'm the chief of the agency.")
    print("We receive a message:")
    carmen_sandiego_action()


def carmen_sandiego_action():
    global detective_life

    carmen_location = random.choice(places.list_of_places)
    carmen_are_at = random.choice(countries.list_of_countries)

    array_of_countries = []
    array_of_countries.append(carmen_are_at['name'])

    counter = 0
    for country in countries.list_of_countries:
        if counter < 2 and array_of_countries.count(country['name']) == 0:
            array_of_countries.append(country['name'])
            counter += 1

    random.shuffle(array_of_countries)

    print("")
    print(
        f"Carmen Sandiego is in the {carmen_location['name']} and {carmen_location['action']}"
    )
    print(f"a country where the flag is {carmen_are_at['flag_color']}.")
    print("")
    print("=======================================================================")
    print("")
    print(
        "You have to find her and recover the object. What country do you think she is? \n"
    )
    detective_choice = input(
        f"1 - {array_of_countries[0]} | 2 - {array_of_countries[1]} | 3 - {array_of_countries[2]} \n"
    )

    country_selection = int(detective_choice) - 1

    if array_of_countries[country_selection] == carmen_are_at['name']:
        print(
            "======================================================================="
        )
        print("You find her! You have to arrest her!")
        trying_to_arrest_carmen_sandiego()
    else:
        print(
            "======================================================================="
        )
        print("You are wrong! She scape from you.")
        print("You loose 1 life point.")
        detective_life -= 1
        print(f"You have {detective_life} life points.")
        print("=======================================================================")
        if detective_life < 1:
            print("You have no life points. GAME OVER")


def trying_to_arrest_carmen_sandiego():
    global detective_experience
    global carmen_sandiego_life

    if detective_experience < 3:
        print(f"You have only {detective_experience}, she is too strong for you. She scape from you.")
        print("You don't loose life points this time.")
        carmen_sandiego_life = carmen_sandiego_life - 1

        print(f"Carmen Sandiego loose 1 life point. Now she has {carmen_sandiego_life} life points.")
        print("You gain 3 experience points.")
        detective_experience += 3
        print("=======================================================================")
        print(f"LEVEL UP! You are now a Detective! You have {detective_life} life points.")
    else:
        print("You have enough experience to arrest her.")
        print("You gain 5 experience points.")

        carmen_sandiego_life -= 3
        detective_experience += 5

        print(f"Carmen Sandiego loose 3 life points. Now she has {carmen_sandiego_life} life points.")


def setup():
    print(f"Detective life: {detective_life}                              Carmen Sandiego life: {carmen_sandiego_life}")

main()
