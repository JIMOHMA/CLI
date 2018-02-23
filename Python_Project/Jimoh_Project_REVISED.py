## Author: Muyideen A. Jimoh
## jimohma, 001327114
## Project Name: Inventory Management
## Comp Sci 1XA3 Final Porject
## Due Date April 9th 2017

#########################################################################################################################################
## A Few Notes                                                                                                                         ##                        
## The valid entry for the fields Item Name, Location and Description should be written in the format explained below.                 ##
## If the input of the field is more than one word(string), the strings/words whould be separated with any                             ##
## hyphen in order to distinguish between the strings/words. Example of an item is shown below;                                        ##
## Item Number: 2222, Quantity: 20, Item Name: Screwdrivers, Item Location: Warehouse-C, Item Description: Large-Phillips-Screwdrivers.##
##                                                                                                                                     ##
## However, if a item properties if just one word, the inclusion of the hyphen could be disregarded                                    ##
#########################################################################################################################################

 
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Inventory:
    
    ## Used by the load_func method
    templist = []  ## This is a temporary list to hold the current data about to be loaded
    mylist = []    ## For holding all the data that the user enters into the program

    ## Used by the sort_data method 
    newlist = []      ## This holds the data in memory which is about to be finally sorted
    sorted_data = []  ## For holding the sorted data

    ## Used when loading the data from a textfile to the program
    load_temp = []
    load_list = []
    load_inventory = []
    
    def __init__(self, master):

        mainframe = ttk.Frame(master, style='My.TFrame', padding="3 3 12 12")
        mainframe.grid(column=0, row=0, columnspan=6, rowspan=8, sticky='NWES')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        

## The labels for the item description & display message/informations for user
################################################################
        self.label_Number = ttk.Label(mainframe, text="Item Number")
        self.label_Number.grid(row=0, column=0, sticky=W)

        self.label_Quantity = ttk.Label(mainframe, text="Quantity")
        self.label_Quantity.grid(row=1, column=0, sticky=W)
        
        self.label_Name = ttk.Label(mainframe, text="Item Name")
        self.label_Name.grid(row=2, column=0, sticky=W)
        
        self.label_Location = ttk.Label(mainframe, text="Item Location")
        self.label_Location.grid(row=3, column=0, sticky=W)

        self.label_Description = ttk.Label(mainframe, text="Item Description")
        self.label_Description.grid(row=4, column=0, sticky=W)

        self.label_ = ttk.Label(mainframe, text=" Message >>> ")
        self.label_.grid(row=5, column=0, columnspan=6, sticky=W)

        self.label_Message = ttk.Label(mainframe, text=" Welcome! Your inventory program is ready for operation and you may proceed to \n add a new 'Item' or load a textfile!")
        self.label_Message.grid(row=6, column=0, columnspan=6, sticky=W)
#################################################################
## End of label descriptions

## The entry widget for the item descriptions
#################################################################
        self.entry_Number = ttk.Entry(mainframe)
        self.entry_Number.grid(row=0, column=1, padx=5, pady=5)

        self.entry_Quantity = ttk.Entry(mainframe)
        self.entry_Quantity.grid(row=1, column=1, padx=5, pady=5)

        self.entry_Name = ttk.Entry(mainframe)
        self.entry_Name.grid(row=2, column=1, padx=5, pady=5)

        self.entry_Location = ttk.Entry(mainframe)
        self.entry_Location.grid(row=3, column=1, padx=5, pady=5)

        self.entry_Description = ttk.Entry(mainframe)
        self.entry_Description.grid(row=4, column=1, padx=5, pady=5)
##################################################################
## End of Entry descriptions

## The Buttons for the item manupulations
##################################################################
        self.New_button = ttk.Button(mainframe, text ="New", command=self.Add_New_Data_func)
        self.New_button.grid(row=4, column=2)

        self.Delete_button = ttk.Button(mainframe, text ="Delete", state=DISABLED, command=self.Delete_func)
        self.Delete_button.grid(row=1, column=2)

        self.Search_button = ttk.Button(mainframe, text ="Search", state=DISABLED, command=self.Search_func)
        self.Search_button.grid(row=2, column=2)

        self.Update_button = ttk.Button(mainframe, text ="Update", state=DISABLED, command=self.Update_func)
        self.Update_button.grid(row=3, column=2)

        self.Load_button = ttk.Button(mainframe, text ="Load Data", command=self.Load_func)
        self.Load_button.grid(row=0, column=2, columnspan=2)

        self.Save_button = ttk.Button(mainframe, text ="Save Data", state=DISABLED, command=self.Save_Data_func)
        self.Save_button.grid(row=4, column=3, padx=5, pady=5)

        self.Confirm_button = ttk.Button(mainframe, text ="Confirm", state=DISABLED, command=self.Confirm_func)##Delete-Confirmation Button
        self.Confirm_button.grid(row=1, column=3, padx=5, pady=5)
###################################################################
## End of button descriptions

    ## Funtion that writes to the file
    def Load_func(self):
        
        ## Warns user if the there is some data in the inventory before loading a new file
        if self.sorted_data != []:
           self.label_Message.config(text=" Warning! Your existing inventory data will be replaced. You can always re-load them anytime you want")

        ## Reading from a file intially for it's data to be stored in filename
        file_path = filedialog.askopenfilename()
        filename = open(file_path, "r")
        file_length = len(filename.readlines())
        filename.close()


        ## The files being read from the the textfile are of the form e.g 2222,30,Hammer,Warehouse-B,Wooden-Hammer
        ##
        myfile = open(file_path, "r")    
        for i in range(file_length):

            ## Each data in the file has the new line character in it. This block of code removes the "\n" from
            ## it by first splitting the item properties by "," and later removing the "\n" in the end of each line
            data = myfile.readline().split(',')
            temp = data[-1]
            data.remove(data[-1])
            temp1 = temp.strip('\n')
            new_data = data + [temp1]  ## Augmented data which is in the form of a list of string
                                       ## e.g ['2222','30','Hammer','Warehouse-B','Wooden-Hammer']

            ## The data loaded into the program is in t he form of a list of list
            self.load_temp = [[new_data[0]] + [new_data[1]] + [new_data[2]] + [new_data[3]] + [new_data[4]]]  

            self.load_list = self.load_list + self.load_temp
            
        myfile.close()

        
        del self.sorted_data[:]  ## deletes the previously data from other text files
                                 ## and make it available for the new one to be stored

        for index in self.load_list:

            load_item = Item(index[0], index[1], index[2], index[3], index[4])
            
            self.load_inventory = self.load_inventory + [load_item]

        ## Sorts the data from the loaded text file                    
        self.sorted_data = sorted(self.load_inventory, key=lambda x: x.Number)

        ## deleting the data contained in this list before a new one is loaded
        ###########################
        del self.load_temp[:]
        del self.load_list[:]
        del self.load_inventory[:]
        ###########################

        self.label_Message.config(text=" You've successfully loaded your text file")
        
        ###########################################
        ## Since the button are initially disabled, when a textfile is loaded
        ## into the inventory, they get enabled so operations data in the program.
        ## When the search button is active, it also makes the delete and update button active
        ## when it's clicked on.
        self.Search_button.config(state=NORMAL)
        ###########################################
        

        print((self.sorted_data))

    ## Search function for the search button
    def Search_func(self):

        number_List = []  ## List for tracking all the item numbers in the inventory

        try:
            eval(self.entry_Number.get())
            
        except UnboundLocalError:
            self.label_Message.config(text=" You have not entered any 'Item Number' to search! ")
        except SyntaxError:
            self.label_Message.config(text=" You have to enter a valid search 'Item Number' ! ")
        except NameError:
            self.label_Message.config(text=" 'Item Number' can't be a string! Enter a valid number > or = 0. ")
        else:

            if eval(self.entry_Number.get()) >= 0:
                
                ## gets the item number in its text field on the GUI which is later
                ## searched for in the inventory
                item_search = self.entry_Number.get()

                ## Item is the index from 0....***
                for item in range(len(self.sorted_data)):
                    if item_search == self.sorted_data[item].Number:  ## When the item matches the
                                                                      ## one in the inventory.
                        
                        ## The found variable contains the informations about
                        ## the searched item number... This
                        found = self.sorted_data[item]
                        break  ## This breaks out of the for-loop

                for n in range(len(self.sorted_data)):
                    number_List = number_List + [self.sorted_data[n].Number]

                ## Searching to see if the item number is in the inventory and returns it as a list
                item_ = list(filter(lambda x: x == item_search, number_List))
                

                if len(item_) > 0:  ## this means the item number is in the list   
                #if self.entry_Quantity.get() != '' and self.entry_Name.get() != '' and self.entry_Location.get() != '' and self.entry_Description.get() != '':
                    ## Deleting the previous data in the fields; Quantity, Name, Location && Description 
                    self.entry_Quantity.delete(0, END)
                    self.entry_Name.delete(0, END)
                    self.entry_Location.delete(0, 'end')
                    self.entry_Description.delete(0, 'end')
                    
                    ## Inserting the searched item properties to their respective entry field
                    self.entry_Quantity.insert(0, found.Quantity)
                    self.entry_Name.insert(0, found.Name)
                    self.entry_Location.insert(0, found.Location)
                    self.entry_Description.insert(0, found.Description)

                    self.Save_button.config(state=DISABLED) ## Disables the save button when the search
                                                            ## button is clicked
                    
                    ## Making the delete and update button available to the user after a successful search 
                    self.Update_button.config(state=NORMAL)
                    self.Delete_button.config(state=NORMAL)

                    self.label_Message.config(text=" Search of "+ str(item_search) + " is successful! " )  ## Text label for a successful search in the inventory
                    
                ## When the item number is not found in the inventory                                           
                else:
                    self.label_Message.config(text=" Item is not in the inventory! ")  ## Text label when Item is not found in the inventory
            else:
                self.label_Message.config(text=" 'Item Number' must be > or = 0. ") ## Text label when a negative number is enterd for Item Number or Quantity

                    
    def Update_func(self):

        ## Try clause is responsible for making sure the input field of Item Number and
        ## Quantity is of the type integer..If it's an int datatype, the program goes into
        ## the else of this try clause. Else if an exception is encountered, the right exception
        ## clause is executed. 
        try:
            eval(self.entry_Number.get())
            eval(self.entry_Quantity.get())
             
        except UnboundLocalError:
            self.label_Message.config(text=" You have not entered any 'Item Number' or 'Quantity' to search! ")
        except SyntaxError:
            self.label_Message.config(text=" You have to enter a valid search 'Item Number' or 'Quantity'. ")
        except NameError:
            self.label_Message.config(text=" 'Item Number' or 'Quantity' can't be a string! Enter a valid number > or = 0. ")
        else:

            ## Given that the Item Number and Quantity is a number
            ## This makes sure the the item number is a real string e.g 'Hammer' or 'Bolts-and-Nuts'.
            ## Given that the Item Number is a valid string, the program goes into the Exception block
            ## called NameError. If the Item Name is not a valid string, the proper exception block is
            ## executed. 
            try:
                eval(self.entry_Name.get())
                
            except UnboundLocalError:
                self.label_Message.config(text=" The Item Name can't be empty! ")
            except SyntaxError:
                self.label_Message.config(text=" Enter a valid Name(e.g Hammer) in order to update! ")
            except NameError:

                ## Makes sure the Loaction is of the correct data-type
                try:
                    eval(self.entry_Location.get())
                
                except UnboundLocalError:
                    self.label_Message.config(text=" The Item Location can't be empty! ")
                except SyntaxError:
                    self.label_Message.config(text=" Enter a valid Location(e.g 'Warehouse-C') in order to update! ")
                except NameError:

                    ## Makes sure the Description is of the correct data-type
                    try:
                        eval(self.entry_Description.get())

                    except UnboundLocalError:
                        self.label_Message.config(text=" The Item Description can't are empty! ")
                    except SyntaxError:
                        self.label_Message.config(text=" Enter a valid Description (e.g 'Wooden-Hammer') in order to update! ")
                    except NameError:

                        ## This is the block where all the fields have received the proper entry types.
                        ## It then checks to makes sure the Item Number and Quantity is not a negative number.
                        if eval(self.entry_Number.get()) >= 0 and eval(self.entry_Quantity.get()) >= 0:

                            ## gets the item number in its text field on the GUI
                            item_search = self.entry_Number.get()

                            ## Item is the index from 0....***
                            for item in range(len(self.sorted_data)):
                                if item_search == self.sorted_data[item].Number:  ## When the item matches the
                                                                                  ## one in the inventory.
                                    found = self.sorted_data[item]
                                    break  ## This breaks out of the for-loop
                                
                            ## Updating the data in memory with the new data in the entry fields
                            found.Quantity = self.entry_Quantity.get()
                            found.Name = self.entry_Name.get()
                            found.Location = self.entry_Location.get()
                            found.Description = self.entry_Description.get()

                            self.Save_button.config(state=NORMAL)

                            self.label_Message.config(text=" The item " + str(item_search) + " was successfully updated! ")
                    
                        else:
                            self.label_Message.config(text=" Item Number or Quantity can't be a negative value in order to update! ")
                            
                    else:
                        self.label_Message.config(text=" 'Item Description' can't be an integer! Enter a string! ")

                else:
                    self.label_Message.config(text=" 'Item Location' can't be an integer! Enter a string! ")

            else:
                self.label_Message.config(text=" 'Item Name' can't be an integer! Enter a string! ")


        
    ## This save_data function should sort the list and then write to a file.. this
    ## is where the magic of sorting is meant to take place
    def Save_Data_func(self):

        if len(self.mylist) == 0:
            self.sorted_data = sorted(self.sorted_data, key=lambda x: x.Number)
            
            ## This successfully writes to the file named inventory
            file_path = filedialog.askopenfilename()
            addData = open(file_path, "w")
            addData.write("\n".join(str(x) for x in self.sorted_data))
            addData.close()

            del self.newlist[:] ## once the save button is pressed, this list is emptied

            self.Search_button.config(state=NORMAL)
            
            self.label_Message.config(text=" Data has been permanently added to inventory and saved to your chosen file! ")

        else:
            try:
                self.mylist[0]
            except Exception:
                self.label_Message.config(text=" You have to add the updated item to the inventory first! ")

            else:
                ## Applying a sort algorithm to the list
                for index in self.mylist:
                    ## Using the Item class to make an new object somehow
                    entry = Item(index[0], index[1], index[2], index[3], index[4])
                    self.newlist = self.newlist + [entry]
                
                ## This doesn't use merge sort but an inbuilt sort algorithm
                ## The sorting workes based on the Item Number and other Item properties as well
                self.sorted_data = self.sorted_data + self.newlist
                self.sorted_data = sorted(self.sorted_data, key=lambda x: x.Number)
                
                ## This successfully writes to the file named inventory
                file_path = filedialog.askopenfilename()
                addData = open(file_path, "w")
                addData.write("\n".join(str(x) for x in self.sorted_data))
                addData.close()

                del self.newlist[:] ## once the save button is pressed, this list is emptied

                self.Search_button.config(state=NORMAL)
                
                self.label_Message.config(text=" Data has been permanently added to inventory and saved to your chosen file! ")
                

    ## The function to be called when a data is to be added to the list called mylist
    ## Basically a transition function for the mylist variable
    def Add_New_Data_func(self):

        ## This try and except block is similar to the error handlings in the Update function
        ## because the Update_func and the Add_New_Data_func both take in data from the entry fields
        try:
            eval(self.entry_Number.get())
            eval(self.entry_Quantity.get())
             
        except UnboundLocalError:
            self.label_Message.config(text=" You have not entered any 'Item Number' or 'Quantity'. ")
        except SyntaxError:
            self.label_Message.config(text=" You have to enter a valid 'Item Number' or 'Quantity' in order to add \n to inventory (e.g. )")
        except NameError:
            self.label_Message.config(text=" 'Item Number' or 'Quantity' can't be a string! Enter a valid number > or = 0. ")
        else:

            try:
                eval(self.entry_Name.get())
                
            except UnboundLocalError:
                self.label_Message.config(text=" The 'Item Name' can't be empty! ")
            except SyntaxError:
                self.label_Message.config(text=" Enter a valid Name(e.g Hammer or Bolts-and-Nuts) in order to add to inventory! ")
            except NameError:

                try:
                    eval(self.entry_Location.get())
                
                except UnboundLocalError:
                    self.label_Message.config(text=" The Item Location can't be empty! ")
                except SyntaxError:
                    self.label_Message.config(text=" Enter a valid Location(e.g 'Warehouse-C') in order to add to inventory! ")
                except NameError:
                    
                    try:
                        eval(self.entry_Description.get())

                    except UnboundLocalError:
                        self.label_Message.config(text=" The Item Description can't are empty! ")
                    except SyntaxError:
                        self.label_Message.config(text=" Enter a valid Description (e.g 'Wooden-Hammer') in order to add to inventory! ")
                    except NameError:
                    
                        if eval(self.entry_Number.get()) >= 0 and eval(self.entry_Quantity.get()) >= 0:

                            ## Adding the data entries to the temporary list while using the get
                            ## method to access those data..
                            ## This should basically give a list of string (data)
                            self.templist = [[self.entry_Number.get()] + [self.entry_Quantity.get()]
                            + [self.entry_Name.get()] + [self.entry_Location.get()] + [self.entry_Description.get()]]

                            ## Appending the temporary list to the actuall list we need
                            ## So we have a sequence of lists which contains a sequence of strings(type of the data)
                            self.mylist = self.mylist + self.templist

                            self.Save_button.config(state=NORMAL) ## Enables the save button
                                                              ## when the new button is pressed/clicked
                            self.label_Message.config(text=" You've successfully added an item to the inventory temporarily! ")

                            ## Once a new data is added, this temporary list is emptied
                            ## for new item to be stored in it
                            del self.templist[:]
                    
                        else:
                            self.label_Message.config(text=" Item Number or Quantity can't be a negative value in order to add to inventory! ")
                            
                    else:
                        self.label_Message.config(text=" 'Item Description' can't be an integer! Enter a string! ")

                else:
                    self.label_Message.config(text=" 'Item Location' can't be an integer! Enter a string! ")

            else:
                self.label_Message.config(text=" 'Item Name' can't be an integer! Enter a string! ")
        
        
    ## Delete function that temporary removes a data from the program(inventory) before
    ## the confirmation button is clicked 
    def Delete_func(self):

        ## gets the item number in its text field on the GUI
        item_search = self.entry_Number.get()

        ## Item is the index for 0....***
        for item in range(len(self.sorted_data)):
            if item_search == self.sorted_data[item].Number:  ## When the item matches the
                                                              ## one in the inventory.
                ## Item to be deleted
                delete_item = self.sorted_data[item]
                break  ## This breaks out of the for-loop
            
        ## Deletes the item from the inventory but it'll still be available in
        ## the entry fields
        self.sorted_data.remove(delete_item)
            

        ## The confirmation button gets enables once the delete button is clicked
        ## which allows for final deletetion of a data
        self.Confirm_button.config(state=NORMAL)

        self.label_Message.config(text=" The item has been temporarily deleted! ")

    ## Confirmes the deletion of the data from the whole program by removing it finally
    ## from the entry fields of the item
    def Confirm_func(self):

        item = self.entry_Number.get()
        ## Finally deletes the entries in the item fields; Number, Quantity, Name,
        ## Location && Description 
        self.entry_Number.delete(0, END)
        self.entry_Quantity.delete(0, END)
        self.entry_Name.delete(0, END)
        self.entry_Location.delete(0, 'end')
        self.entry_Description.delete(0, 'end')

        self.label_Message.config(text=" Item " + str(item) + " is now permanently deleted from your inventory! ")
        
        ## The confirmation button gets enables once the delete button is clicked
        ## which allows for final deletetion of a data
        self.Confirm_button.config(state=DISABLED)
        self.Delete_button.config(state=DISABLED)
        
        
## Class for formating how the data is to be represented and also holding the data
## about to be stored into the system's memory
class Item:

    def __init__(self, Number, Quantity, Name, Location, Description):

        self.Number = Number
        self.Quantity = Quantity
        self.Name = Name
        self.Location = Location
        self.Description = Description

    def __repr__(self):
        return '{},{},{},{},{}'.format(self.Number, self.Quantity, self.Name, self.Location, self.Description)
        
    
root = Tk()
root.title("Inventory Management")
##root.geometry("560x220")
##root.resizable(0, 0)
b = Inventory(root)
root.mainloop()



