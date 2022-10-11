import os
import openai
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def GPT3():
    openai.api_key = os.getenv("OPENAI_API_KEY") # API key will be pulled from environment variables from windows operating system.
                                                 # or you can set openai.api_key equal to your api key directly

    response = openai.Completion.create(model="text-davinci-002",
                                        prompt="This is a recipe for {} people for {}:".format(num_people.get(),food.get()),
                                        temperature=0.7,
                                        max_tokens=1000,
                                        top_p=1)
    return response.choices[0].text

def generate_recipie():
    """ callback when the generate button is clicked
    """
    recipie = GPT3()
    
    recipie_window = tk.Tk()

    recipie_label = ttk.Label(recipie_window, text="Here is your custom recipie!")
    recipie_label.pack(expand=True)

    recipie_text = tk.Text(recipie_window)
    recipie_text.insert('0.0', recipie)
    recipie_text.pack(expand=True)



    recipie_window.mainloop()





####################################################################################################################################################################

root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
food = tk.StringVar()
num_people = tk.StringVar()


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

# Submit button
login_button = ttk.Button(info, text="Generate Recipie", command=generate_recipie)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
