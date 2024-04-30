# To DO List

class ToDoList():
    
    def __init__(self, string=None):
        self.string = string
        
    def load_numerate(self, filename="assets/numerate.txt"):
        with open(filename) as f:\
            numerate = f.readline()
        
        if numerate == '':
            return 1

        return int(numerate)
        
    def load_to_json(self, filename="assets/todolist.txt"):
        with open(filename, 'a') as f:
            numerate = self.load_numerate()
            # if number_count == "":
            #     number_count = 0
            f.write(f"{numerate}.{self.string}\n")
            
            self.write_numerate(numerate+1) 
    
    def read_list(self, filename="assets/todolist.txt"):
        with open(filename) as f:
            print(f.read())
    
    def clear_list(self, filename_list="assets/todolist.txt", filename_num="assets/numerate.txt"):
        with open(filename_list, 'w') as f:
            f.write("")
        
        with open(filename_num, 'w') as f:
            f.write("")
    
    def write_numerate(self, count, filename="assets/numerate.txt"):
        with open(filename, 'w') as f:
            f.write(str(count))

if __name__ == '__main__':
    ToDoList().read_list()
    print("Enter '!' or '?' to call the help command")
    while True:
        quest = input("Введите список дел: ")
        to_do_list = ToDoList(quest)
        
        if quest == 'q':
            to_do_list.read_list()
            break
        
        elif quest == 'cl':
            to_do_list.clear_list()
            continue
        
        elif quest == 'rd':
            to_do_list.read_list()
            continue
        
        elif quest == "!" or quest == "?":
            print("\n\n---Commands---")
            print(
                    "'q' - exit programm"\
                    "\n'cl' - clear list"\
                    "\n'rd' - read list\n"
                )
        
        to_do_list.load_to_json()
