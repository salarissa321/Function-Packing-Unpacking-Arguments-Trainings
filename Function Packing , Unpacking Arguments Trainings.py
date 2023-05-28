


#--------------------------------------------------------------------------------
#----------- Function Packing , Unpacking Arguments Trainings---------------
#--------------------------------------------------------------------------------


myTuple = ("Html" , "Css" , "Js")



mySkills = {
    "Go" : "90%" ,
    "Python" : "70%" ,
    "SQL" : "50%"
}

def show_skills(name , *skills , **skillsWithProgress) :
    print(f"Hello {name} \n Skills Without Progress is : ")

    for skill in skills :
        print(f" - {skill}")


    print("Skills With Progress Is : ")
    for skill_key , skill_value in skillsWithProgress.items() :
        print(f" - {skill_key} => {skill_value} ")

show_skills("Salar") # Hello Salar
show_skills("Salar" , "Html" , "Css" , "Js") 
# Hello Salar 
#  Skills Without Progress is :
#  - Html
#  - Css
#  - Js

show_skills("Salar", *myTuple ) 
# Hello Salar is
#  Skills Without Progress is :
#  - Html
#  - Css
#  - Js
# Skills With Progress Is :

show_skills("Salar", *myTuple , **mySkills ) 
# Hello Salar is
#  Skills Without Progress is :
#  - Html
#  - Css
#  - Js
# Skills With Progress Is :
# - Go => 90%
#  - Python => 70%
#  - SQL => 50%
