from tkinter import *
from calculating_calories import male_calories_1, male_calories_2, male_calories_3, male_calories_4, male_calories_5,\
     female_calories_1, female_calories_2, female_calories_3, female_calories_4, female_calories_5
from tkinter import messagebox

root = Tk()
root.title("Fitness Guide")
gender = IntVar()
activity = IntVar()

def Calculate():
    age = float(age_input.get())
    weight = float(weight_input.get())
    height = float(height_input.get())

    if gender.get() == 0 and activity.get() == 0:
        calories_burnt = male_calories_1(weight, height, age)
    elif gender.get() == 0 and activity.get() == 1:
        calories_burnt = male_calories_2(weight, height, age)
    elif gender.get() == 0 and activity.get() == 2:
        calories_burnt = male_calories_3(weight, height, age)
    elif gender.get() == 0 and activity.get() == 3:
        calories_burnt = male_calories_4(weight, height, age)
    elif gender.get() == 0 and activity.get() == 4:
        calories_burnt = male_calories_5(weight, height, age)
    elif gender.get() == 1 and activity.get() == 0:
        calories_burnt = female_calories_1(weight, height, age)
    elif gender.get() == 1 and activity.get() == 1:
        calories_burnt = female_calories_2(weight, height, age)
    elif gender.get() == 1 and activity.get() == 2:
        calories_burnt = female_calories_3(weight, height, age)
    elif gender.get() == 1 and activity.get() == 3:
        calories_burnt = female_calories_4(weight, height, age)
    elif gender.get() == 1 and activity.get() == 4:
        calories_burnt = female_calories_5(weight, height, age)


    result = Toplevel()
    result.title("Calories Burnt")
    goal = IntVar()
    
    message_label = Label(result, text=f"You are burning {calories_burnt} calories daily")
    message_label.grid(row=0, column=1)
    question = Label(result, text="What is your fitness goal")
    question.grid(row=1, column= 1)

    

    def gain_or_lose():
        activity = int(calories_burnt)

        if goal.get() == 0:
            new_goal= activity - 500
        elif goal.get() == 1:
            new_goal= activity + 500
        else:
            new_goal= activity

        messagebox.showinfo("GOAL", f"In order to reach achieve your goal, your daily calorie intake should be {new_goal} calories")


    goal_rb0 = Radiobutton(result, text="lose weight", variable=goal, value=0)
    goal_rb0.grid(row=2, column=0)
    goal_rb1 = Radiobutton(result, text="gain weight", variable=goal, value=1)
    goal_rb1.grid(row=2, column=1)
    goal_rb2 = Radiobutton(result, text="maintain weight", variable=goal, value=2)
    goal_rb2.grid(row=2, column=2)

    #fitness goal button
    Goal_button = Button(result, width=10, text="NEXT", command=gain_or_lose)
    Goal_button.grid(row=3, column=1, columnspan=2)

     
def clear():
    age_input.delete(0,END)
    weight_input.delete(0, END)
    height_input.delete(0, END)
        

#labels and entry
age_label = Label(root, text="Age  ")
age_label.grid(row=0, column=0, columnspan=2)
age_input = Entry(root, width=10)
age_input.grid(row=0, column=2, columnspan=2)

weight_label = Label(root, text="Weight(in lbs)  ")
weight_label.grid(row=1, column=0, columnspan=2)
weight_input = Entry(root, width=10)
weight_input.grid(row=1, column=2, columnspan=2)

height_label = Label(root, text="Height(in inches)  ")
height_label.grid(row=2, column=0, columnspan=2)
height_input = Entry(root, width=10)
height_input.grid(row=2, column=2, columnspan=2)

activity_label = Label(root, text="Daily Activity Level : ")
activity_label.grid(row=4, column=0)

#radiobuttons
rb1 = Radiobutton(root, text = "Male", variable=gender, value=0)
rb1.grid(row=3, column=0)

rb2 = Radiobutton(root, text = "Female", variable=gender, value=1)
rb2.grid(row=3, column=2)

rb3 = Radiobutton(root, text ="No Excercise", variable=activity, value=0)
rb3.grid(row=5, column=0)

rb4 = Radiobutton(root, text="Light Excercise", variable=activity, value=1)
rb4.grid(row=6, column=0)

rb5 = Radiobutton(root, text="Moderate Excercise", variable=activity, value=2)
rb5.grid(row=7, column=0)

rb6 = Radiobutton(root, text="Active", variable=activity, value=3)
rb6.grid(row=8, column=0)

rb7 = Radiobutton(root, text="Very Active", variable=activity, value=4)
rb7.grid(row=9, column=0)

#calculate_button
calculate = Button(root, width=20, text="Calculate", command=Calculate)
calculate.grid(row=10, column=0, columnspan=4)

#exit_button
exit_button = Button(root, width=10, text="Exit", command=root.destroy)
exit_button.grid(row=11, column=0, columnspan=2)

#clear button
clear_button = Button(root, width=10, text="Clear", command=clear)
clear_button.grid(row=11, column=2, columnspan=2)

root.mainloop()
