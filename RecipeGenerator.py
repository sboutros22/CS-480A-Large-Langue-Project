from asyncio.windows_events import NULL
import os
import openai
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def GPT3():
    if(Custimization == NULL):
    # You need to insert your own key for it to work
        openai.api_key = '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'
        response = openai.Completion.create(model="text-davinci-002",
                                            prompt="This is a recipe for {} people for {}:".format(num_people.get(),food.get()),
                                            temperature=0.7,
                                            max_tokens=1000,
                                            top_p=1)
        return response.choices[0].text
    elif(Custimization != NULL):
       # You need to insert your own key for it to work
        openai.api_key = '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'
        response = openai.Completion.create(model="text-davinci-002",
                                            prompt="This is a recipe for {} people for {} with {}:".format(num_people.get(),food.get(),Custimization.get()),
                                            temperature=0.7,
                                            max_tokens=1000,
                                            top_p=1)
        return response.choices[0].text 
    

    recipe_window.mainloop()





####################################################################################################################################################################

root = tk.Tk()
# Adjust the size if you are adding more input bars or they will not show up
root.geometry("300x200")
root.resizable(False, False)
root.title('Sign In')

# Store food, num_people, and custimization values and need to add more if more features are added
food = tk.StringVar()
num_people = tk.StringVar()
Custimization = tk.StringVar()


# Info frame
info = ttk.Frame(root)
info.pack(padx=10, pady=10, fill='x', expand=True)


# food
food_label = ttk.Label(info, text="What do you want me to make?")
food_label.pack(fill='x', expand=True)

food_entry = ttk.Entry(info, textvariable=food)
food_entry.pack(fill='x', expand=True)
food_entry.focus()

# Number of people
people_label = ttk.Label(info, text="How many people will this be for?")
people_label.pack(fill='x', expand=True)

people_entry = ttk.Entry(info, textvariable=num_people)
people_entry.pack(fill='x', expand=True)

# Custimization
Custimization_label = ttk.Label(info, text="Would you like to custimize? Leave blank if no.")
Custimization_label.pack(fill='x', expand=True)

Custimization_entry = ttk.Entry(info, textvariable=Custimization)
Custimization_entry.pack(fill='x', expand=True)

# Submit button
login_button = ttk.Button(info, text="Generate Recipe", command=generate_recipie)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()

def AcceptableRecipe(Text):
    if(Text == "yes"):
        return print("Thank you for using AutoRecipes!")
        
    elif(Text == "no"):
        return print("please run the code again and if that doesn't work, please adjust peramiters.")
        
    elif(Text != "no" and Text != "yes"):
        print("please insert either yes or no.")
        Text = input()
        return AcceptableRecipe(Text)
        

