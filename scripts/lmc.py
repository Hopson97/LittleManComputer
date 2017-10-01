from tkinter import *
from lmc_parser import LMCParser
import random
import time

class Window(Frame):

    """LMC""" 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #Frame.configure(self, bg = 'black')
        Frame.grid_columnconfigure(self, 3, minsize=20)#Add a spacer
        Frame.grid_columnconfigure(self, 5, minsize=20)

        self.master = master
      
        self.memory                 = [] 
        self.progCounter            = 0
        self.instructionRegister    = -1
        self.addressRegister        = 0
        self.accumulator            = 0

        for i in range (100):
            self.memory.append(0)
    
        self.init_window()
        self.update_memory()
        self.update_counters()

    def load_instructions(self):
        """Loads Instructions Into Memory"""
        
        instructionList = self.textarea.get(1.0, END)
        instructionList.upper()
        instructionList = instructionList.split("\n") #split the string into individual instructions

        
        instructionList.pop(len(instructionList) - 1) #get rid of the final char, which is random space for some reason

        asmler = LMCParser()
        asmler.assemble(instructionList, self.memory)
        #update the GUI
        self.update_memory()

    def run(self):
        """Execute the code"""
        def lmcAdd():
            self.accumulator += self.memory[self.addressRegister]
            
        def lmcSub():
            self.accumulator -= self.memory[self.addressRegister]

        def lmcLoad():
            self.accumulator = self.memory[self.addressRegister]

        def lmcStore():
            self.memory[self.addressRegister] = self.accumulator
            
        def lmcInput():
            self.accumulator = int(input("Enter input: "))
            
        def lmcOutput():
            print ("Output:", self.accumulator)

        def lmcBranchAlways():
            self.progCounter = self.addressRegister

        def lmcBranchIfZero():
            if self.accumulator == 0:
                lmcBranchAlways()

        def lmcBranchIfZeroOrPositive():
            if self.accumulator >= 0:
                lmcBranchAlways()

        print ("\n RUNNING \n")
        while self.instructionRegister != 0:
            #split instructions into instruction and address
            #bus would move to address, take into cpu registers
            instr   = str(self.memory[self.progCounter])
            if int(instr) == 0:
                break
            opcode  = instr[0]

            if len(instr) == 3:
                address = instr[1] + instr[2]
            else:
                address = instr[1]

            self.progCounter += 1
            
            #push to registers
            self.instructionRegister = int(opcode)
            self.addressRegister     = int(address)

            print ("Inst: ", self.instructionRegister)
            
            #interpret
            if self.instructionRegister == 1:
                lmcAdd()
            elif self.instructionRegister == 2:
                lmcSub()
            elif self.instructionRegister == 3:
                lmcStore()
            elif self.instructionRegister == 5:
                lmcLoad()
            elif self.instructionRegister == 6:
                lmcBranchAlways()
            elif self.instructionRegister == 7:
                lmcBranchIfZero()
            elif self.instructionRegister == 8:
                lmcBranchIfZeroOrPositive()
            elif self.instructionRegister == 9:
                if self.addressRegister == 1:
                    lmcInput()
                elif self.addressRegister == 2:
                    lmcOutput()
            else:
                print ("UNRECOGNISED SYMBOL: ", self.instructionRegister)
            
    def init_window(self):
        """ Creates window and all the options"""
        self.master.title("LMC")
        self.pack(fill=BOTH, expand=1)
        self.header_label = Label(self, text="Little Man Computer")
        self.header_label.grid(row = 0, column = 0, columnspan = 3)
        # Create text box
        self.textarea = Text(self,width = 20, height = 35)
        #self.textarea.pack(expand=NO, fill ="y")
        self.textarea.grid(row = 1, column = 0, columnspan = 3, rowspan = 20)

        self.execute_button = Button(self, text = "Execute", command = self.run)
        self.execute_button.grid(row = 22, column = 0)
        self.reset_button = Button(self, text = "Reset", command = self.reset)
        self.reset_button.grid(row = 22, column = 1)
        self.burn_it_all = Button(self, text = "Exit", command = self.exit)
        self.burn_it_all.grid(row = 22, column = 2)
        self.randmem = Button(self, text = "randmem", command = self.update_random_mem)
        self.randmem.grid(row = 23, column = 2)
        self.assemble = Button(self, text = "Load", command = self.load_instructions)
        self.assemble.grid(row = 23, column = 0)


    def update_counters(self):
        self.accumulator_label = Label(self,text="Accumulator")
        self.accumulator_label.grid(row = 1, column = 4)
        self.accumulator_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.accumulator_value.grid(row = 2, column = 4)

        self.prog_label = Label(self, text="Progress")
        self.prog_label.grid(row=4, column=4)
        self.prog_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.prog_value.grid(row = 5, column = 4)
        
        self.address_label = Label(self, text="Current Address")
        self.address_label.grid(row = 7, column = 4)
        self.address_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.address_value.grid(row = 8, column = 4)

        self.instruction_label = Label(self, text = "Instruction Register")
        self.instruction_label.grid(row = 10, column = 4)
        self.instruction_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.instruction_value.grid(row = 11, column = 4)
        
    def update_memory(self):
        for x in range(0,10):
            for y in range(0,20):
                var = StringVar()
                value_var = StringVar()
                if y % 2 == 0:
                    loc_var = int((y / 2) * 10 + x)
                    var.set("Address " + str(loc_var))
                    self.memory_label = Label(self, textvariable = var)
                    self.memory_label.grid(row = 1 +(y), column = 6+(x),ipadx = 5, ipady = 2 )
                else:
                    value_var.set(self.memory[loc_var])
                    self.memory_value = Label(self, textvariable = value_var, bg = 'grey')
                    self.memory_value.grid(row = 1 +(y), column = 6+(x))
    def reset(self):
        self.textarea.delete(1.0, END)
        
    def exit(self):
        exit()

    def update_random_mem(self):
        for x in range(0,100):
            self.memory[x] = random.randint(0,999)
        self.update_memory()

def main():
    print ("\n\nLITTLE MAN COMPUTER\n\n")

    #Creates UI and starts
    root = Tk()
    root.geometry("1100x650")
    app = Window(master=root)
    #app.update_memory()
    app.mainloop()
    
if __name__ == "__main__":
    main()
