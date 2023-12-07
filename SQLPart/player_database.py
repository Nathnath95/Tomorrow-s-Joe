import sqlite3
import time
import os
from abc import ABC, abstractmethod

class PlayerDatabase:
    ##UPDATE DATABASE
    def update_table(self):
        file_path_names = 'C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/name.txt'
        with open(file_path_names, 'r') as names:
            PlayerName = [line.strip() for line in names.readlines()]

        file_path_endings = 'C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/endingchosen.txt'
        with open(file_path_endings, 'r') as endings:
            EndingChosen = [line.strip() for line in endings.readlines()]

        file_path_fidelity = 'C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/fidelity.txt'
        with open(file_path_fidelity, 'r') as fidelity:
            Fidelity = [line.strip() for line in fidelity.readlines()]

        connection = sqlite3.connect('player_data.db')  
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (name TEXT, ending TEXT, fidelity TEXT)''')
        cursor.executemany('''INSERT INTO players (name, ending, fidelity) VALUES (?, ?, ?)''', zip(PlayerName, EndingChosen, Fidelity))
        connection.commit()
        connection.close()

    def main_menu(self):
        view_details = ViewDetails()
        view_tally = ViewTally()
        os.system('cls')
        print("\t\t\t===============================================")
        print("\t\t\t               WELCOME TO JoeSQL               ")
        print("\t\t\t          database of Tomorrow's Joe           ")
        print("\t\t\t===============================================")
        print("\t\t\t===============   MAIN MENU   =================\n")
        print("\t | Enter 1 to UPDATE DATA            |")
        print("\t | Enter 2 to VIEW                   |")
        print("\t | Enter 3 to TALLY                  |\n")    
        choice = input("\t  ENTER CHOICE: ")

        if choice == '1':
            if os.path.exists("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/name.txt") and os.path.exists("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/endingchosen.txt") and os.path.exists("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/fidelity.txt"):
                self.update_table()
                max_periods = 3
                current_periods = 0
                while current_periods <= max_periods:
                    os.system('cls')
                    print("\t\t\t==============   UPDATE DATA   ================\n")
                    print("\n\t\t SYNCHRONIZING DATA" + "." * current_periods)
                    time.sleep(1)
                    current_periods += 1            
                os.system('cls')
                print("\t\t\t==============   UPDATE DATA   ================\n")
                print("\n\t\t COMPLETE !")
                print("\n\t\t RETURNING TO MAIN MENU...")
                time.sleep(3)
                os.remove("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/name.txt")
                os.remove("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/endingchosen.txt")
                os.remove("C:/Users/WORKSTATION/Documents/renpy-8.1.3-sdk/my_files/fidelity.txt")
                self.main_menu()
            else:
                os.system('cls')
                print("\t\t\t==============   UPDATE DATA   ================\n")
                print("\n\t\t DATA IS ALREADY UP TO DATE")
                print("\n\t\t RETURNING TO MAIN MENU...")
                time.sleep(3)
                self.main_menu()
        
        elif choice == '2':
            os.system('cls')
            print("\t\t\t=================   VIEW   ====================\n")
            print("\t\t 1. All Players")
            print("\t\t 2. Players who chose Rose")
            print("\t\t 3. Players who chose Dana")
            print("\t\t 4. Players who chose Lyka")
            print("\t\t 5. Players who got a Bad Ending")
            print("\t\t 6. Players who are faithful")
            print("\t\t 7. Players who are unfaithful")
            print("\t\t 8. Back")
            choice2 = input("\n\t\t ENTER CHOICE: ")
            if choice2 == '1':
                os.system('cls')
                view_details.view_tableAll()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '2':
                os.system('cls')
                view_details.view_tableRose()
                print("\n")            
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '3':
                os.system('cls')
                view_details.view_tableDana()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '4':
                os.system('cls')
                view_details.view_tableLyka()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '5':
                os.system('cls')
                view_details.view_tableBad()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '6':
                os.system('cls')
                view_details.view_tableFaithful()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '7':
                os.system('cls')
                view_details.view_tableUnfaithful()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice2 == '8':
                os.system('cls')
                self.main_menu()

            else:
                os.system('cls')
                print("\tPlease only select from the available options.\n\n")
                time.sleep(3)
                os.system('cls')
                self.main_menu()

        elif choice == '3':
            os.system('cls')
            print("\t\t\t=================   TALLY   ===================\n")
            print("\t\t 1. All Players")
            print("\t\t 2. Players who chose Rose")
            print("\t\t 3. Players who chose Dana")
            print("\t\t 4. Players who chose Lyka")
            print("\t\t 5. Players who got a Bad Ending")
            print("\t\t 6. Players who are faithful")
            print("\t\t 7. Players who are unfaithful")
            print("\t\t 8. Back")
            choice3 = input("\n\t\t ENTER CHOICE: ")
            if choice3 == '1':
                os.system('cls')
                view_tally.view_tableAll()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '2':
                os.system('cls')
                view_tally.view_tableRose()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '3':
                os.system('cls')
                view_tally.view_tableDana()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '4':
                os.system('cls')
                view_tally.view_tableLyka()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '5':
                os.system('cls')
                view_tally.view_tableBad()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '6':
                os.system('cls')
                view_tally.view_tableFaithful()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '7':
                os.system('cls')
                view_tally.view_tableUnfaithful()
                print("\n")
                os.system("PAUSE")
                os.system('cls')
                self.main_menu()

            elif choice3 == '8':
                self.main_menu()

            else:
                os.system('cls')
                print("\tPlease only select from the available options.\n\n")
                time.sleep(3)
                os.system('cls')
                self.main_menu() 
        
        else:
            os.system('cls')
            print("\tPlease only select from the available options.\n\n")
            time.sleep(3)
            os.system('cls')
            self.main_menu()

#class AbstractTable(ABC):
#    @abstractmethod
#    def open(self):
#        pass

#    @abstractmethod
#    def close(self):
#        pass

class OpenTable:
    def open(self):
        self.connection = sqlite3.connect('player_data.db')
        self.cursor = self.connection.cursor()

class CloseTable:
    def close(self):
            print (self.cursor.fetchall())
            self.connection.commit()
            self.connection.close()

class ViewDetails (OpenTable, CloseTable):
    ##VIEW EVERYTHING
    def view_tableAll(self):
        self.open()
        self.cursor.execute('''SELECT * FROM players''')
        self.close()

    ##VIEW WHO FINISHED ROSE ENDING
    def view_tableRose(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE ending = "Rose Ending"''')
        self.close()
        
    ##VIEW WHO FINISHED DANA ENDING
    def view_tableDana(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE ending = "Dana Ending"''')
        self.close()

    ##VIEW WHO FINISHED LYKA ENDING
    def view_tableLyka(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE ending = "Lyka Ending"''')
        self.close()

    ##VIEW WHO GOT A BAD ENDING
    def view_tableBad(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE ending = "Bad Ending"''')
        self.close()
        
    ##VIEW WHO IS FAITHFUL
    def view_tableFaithful(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE fidelity = "Faithful"''')
        self.close()        

    ##VIEW WHO IS UNFAITHFUL
    def view_tableUnfaithful(self):
        self.open()        
        self.cursor.execute('''SELECT * FROM players WHERE fidelity = "Unfaithful"''')
        self.close()        

class ViewTally (OpenTable, CloseTable):
     ## TALLY EVERYTHING
    def view_tableAll(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players''')
        self.close()        

    ##TALLY WHO FINISHED ROSE ENDING
    def view_tableRose(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE ending = "Rose Ending"''')
        self.close()        

    ##TALLY WHO FINISHED DANA ENDING
    def view_tableDana(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE ending = "Dana Ending"''')
        self.close()        

    ##TALLY WHO FINISHED LYKA ENDING
    def view_tableLyka(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE ending = "Lyka Ending"''')
        self.close()  

    ##TALLY WHO GOT A BAD ENDING
    def view_tableBad(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE ending = "Bad Ending"''')
        self.close()        

    ##TALLY WHO IS FAITHFUL
    def view_tableFaithful(self):
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE fidelity = "Faithful"''')
        self.close()        

    ##TALLY WHO IS UNFAITHFUL
    def view_tableUnfaithful(self): 
        self.open()        
        self.cursor.execute('''SELECT COUNT (*) FROM players WHERE fidelity = "Unfaithful"''')
        self.close()
           


