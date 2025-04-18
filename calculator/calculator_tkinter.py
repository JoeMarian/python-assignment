from tkinter import *

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.window.geometry("400x500")
        self.window.configure(bg='#333333')

        # Initialize variables
        self.current = ""
        self.expression = ""

        # Create display
        self.display = Entry(window, width=25, font=('Arial', 20), justify=RIGHT, 
                           bg='#666666', fg='white', borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("%", 4, 2)
        self.create_button("+", 4, 3)
        
        self.create_button("C", 5, 0)
        self.create_button("←", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)
        
        self.create_button("=", 6, 0, 4)

    def create_button(self, text, row, col, columnspan=1):
        button = Button(self.window, text=text, width=8 if columnspan==1 else 36, 
                       height=2, font=('Arial', 12), 
                       bg='#666666' if text in '0123456789.' else '#FF9500',
                       fg='white',
                       command=lambda: self.click(text))
        button.grid(row=row, column=col, columnspan=columnspan, padx=2, pady=2)

    def click(self, key):
        if key == 'C':
            self.current = ""
            self.display.delete(0, END)
        
        elif key == '←':
            self.current = self.current[:-1]
            self.display.delete(0, END)
            self.display.insert(END, self.current)
        
        elif key == '=':
            try:
                # Check for division by zero before evaluation
                if '/0' in self.current.replace(' ', ''):
                    raise ZeroDivisionError
                
                result = eval(self.current)
                self.display.delete(0, END)
                self.display.insert(END, result)
                self.current = str(result)
            except ZeroDivisionError:
                self.display.delete(0, END)
                self.display.insert(END, "Cannot divide by zero")
                self.current = ""
            except:
                self.display.delete(0, END)
                self.display.insert(END, "Error")
                self.current = ""
        
        elif key == '%':
            try:
                result = float(self.current) / 100
                self.display.delete(0, END)
                self.display.insert(END, result)
                self.current = str(result)
            except:
                self.display.delete(0, END)
                self.display.insert(END, "Error")
                self.current = ""
        
        else:
            self.current += key
            self.display.delete(0, END)
            self.display.insert(END, self.current)

# Create and run calculator
if __name__ == "__main__":
    window = Tk()
    calculator = Calculator(window)
    window.mainloop()
