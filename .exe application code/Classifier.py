"""
@author Jakub Zawadowicz jsz952
"""

import pickle  # used to make possible using the previously trained model
import warnings  # filters out all the warnings
from tkinter import *  # used for GUI creation
from requests import get  # used for taking stuff from website
from bs4 import BeautifulSoup  # used for working with website text

root = Tk()
root.title('Fake News Classifier')
photo = PhotoImage(file="icon16.png")
root.iconphoto(False, photo)
root.minsize(500, 125)

helpLabel = Label(root, text='Enter URL below and click Classify button')
helpLabel.pack(pady=10)
e = Entry(root, width=60, borderwidth=3)
e.pack()


def myClick():
    website = e.get()

    '''
    different way to extracting text, using Requests instead of urllib3 hoping to reduce the noise (it does not change the outcomes)
    '''
    try:  # this try case is here to catch any errors that can be thrown when URL is incorrect
        text = get(website).text
    except Exception:
        e.delete(0, END)
        e.insert(0, "Please enter a correct URL.")

        raise

    soup = BeautifulSoup(text, features="html.parser")  # BeautifulSoup used to get pure html data from a website

    text = ''
    links = soup.find_all('p', class_=False, style_=False)
    '''
    prints website text
    '''
    for link in links:  # prints all website text

        text += ' ' + link.get_text()
    '''
    cleans the text that we got from a website so that it is in a single line and there are no weird distances between new sentences
    '''
    text = text.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').replace('.  ', '. ').replace("\'s",
                                                                                                      '').replace("s\'",
                                                                                                                  "s")  # cleans the text extracted from website and makes sure it is a single line

    text_final = text  # this line changes the classifier in a way that user do not need to enter text but can enter only website URL

    try:
        with warnings.catch_warnings():  # line needed to filter out warnings
            warnings.simplefilter("ignore",
                                  category=UserWarning)  # used to filter out the warnings that original model gives, the model was checked as if the warnings are something to concerned about and I decided that the warning are not critical
            warnings.simplefilter("ignore", category=FutureWarning)
            load_model = pickle.load(open('final_model.sav',
                                          'rb'))  # original model 18.2MB, my model 625MB how to make it more compressed or smaller?
    except Exception:
        e.delete(0, END)
        e.insert(0, "Please make sure that classification model is correct.")

    prediction = load_model.predict([
        text_final])  # changes the classifier in a way that user do not need to enter text but can enter only website URL
    prob = load_model.predict_proba([
        text_final])  # changes the classifier in a way that user do not need to enter text but can enter only website URL

    percentage = (int(prob[0][1] * 100))

    print("The given statement is ", str(prediction[0]))  # a line for checking the output
    print("The truth probability score is ", str(prob[0][1]))  # a line for checking the output

    outcomeText = str(prediction[0]) + ".     The truth probability is: " + str(percentage) + "%"

    e.delete(0, END)
    e.insert(0, outcomeText)


e.bind('<Return>', lambda event: myClick())  # user can use enter to perform classification
myButton = Button(root, text="Classify!", command=myClick)  # user cna use button to perform classification
myButton.pack(pady=15)

root.mainloop()
