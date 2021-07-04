# Password-Manager

An intermediate level Python project that uses Python's Tkinter module to save passwords or generate passwords for different websites.

A person may find it insecure to store all of his passwords on some online cloud, while it is secure to save it all on his local machine.


This program uses Tkinter to save the website name, the email/username used on that website, and the password used on that website. 

When clicked on 'Add', the details are saved into a file 'data.txt'.


Since most of the people use 1 E-Mail for most of their websites, it has already been pre-populated in the E-Mail textbox, but can be changed as per user preference.


In case the user leaves website or password field blank, a dialogbox pops up to enter the fields.

Even before saving the details finally, a popup confirms if the details are captured correctly, and there are no typos from the user's side. Tkinter's messagebox comes in handy for all these dialog boxes.


'Generate Password' button generates a random password with 8-10 letters, 2-4 numbers and 2-4 special characters. 

The button not only fills up the password field with the random password, but also copies it to thw clipboard using the 'pyperclip' modue of Python. This way, the user can simply go to the website and type in the random password. He is saved with the extra 'highlight the password and copying it' task.
