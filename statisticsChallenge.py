import re
import tkinter
from tkinter import filedialog

class Statistics():

    #Constructor
    def __init__(self, read):
        self.read = read

    # Reads File
    def readFile(self):
        try:
            with open(self.read) as f:
                text = f.read()
        except FileNotFoundError:
            print("Error: File not found")
        # print(text)
        self.content = text
    #Finds and prints the overall Word Count
    def wordCount(self):
        r_file.readFile()
        # using regex (findall()) function
        words = len(re.findall(r'\w+', self.content))
        print("Word Count : " + str(words))
    
    # Finds and prints the Line Count, does not count blank lines
    def lineCount(self):
        r_file.readFile()
        counter = 0
        Lines = self.content
        List = Lines.split("\n")
        for i in List:
            if i:
                counter += 1
        print("Line Count : " + str(counter))
    
    #Finds and prints the Mean word count
    def meanCount(self):
        r_file.readFile()
        sentence = self.content
        words = sentence.split()
        average = sum(len(word) for word in words ) / len(words)
        print("Mean Word Length : " + str(average))
    
    # A simple user prompt to close out the script
    def closeFile(self):
        input("Press the Enter key to exit : ") 

    def main(self):
        r_file.wordCount()
        r_file.lineCount()
        r_file.meanCount()
        r_file.closeFile()

if __name__ == "__main__":
    # Hides the file browser
    root = tkinter.Tk()
    root.wm_withdraw() 

    #instantiates and calls the main method
    filename = filedialog.askopenfilename()
    r_file = Statistics(filename)
    r_file.main()








