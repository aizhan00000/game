
class Guests:
    def __init__(self, file_name):
        self.file_name = file_name

    def add(self):
        guest = input("enter a name and surname of the guest:  ")
        return guest

    # def create_file(self):
    #     file_name = input("enter a name of the file:  ")
    #     file = open(file_name + '.txt', 'w')
    #     file.close()
    #     return file_name

    def show_guests(self):
        file = open()


def main():
    create_file = input("do you want to create a new file?  y/n")
    if create_file.lower() == 'y':
        file_name = input("enter a file name:  ")
        file = open(f"{file_name}.txt", 'w')
        guest = Guests(f"{file_name}.txt")
        user_choice = input("enter an action:  \n"
                            "1) add guest in list\n"
                            "2) search guest\n"
                            "3) show list\n"
                            "4) create new file\n"
                            "enter a num of the action")
    if int(user_choice) == 1:
        guest.add()
    elif int(user_choice) == 2:
        guest.search_guest()
    elif int(user_choice) == 3:
        guest.show_guests()
    elif int(user_choice) == 4:
        guest.create_file()














