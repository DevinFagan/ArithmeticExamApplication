import random
import time


# Create the class Arithmetic Exam
class ArithmeticExam:
    def __init__(self):
        self.lvl = None
        self.your_int = None
        self.n = 0
        self.lvl_name = None
        self.username = None
        self.counter = 0

    # Create a method that informs the user to choose either #1 or #2  for their specific math level
    def choose_lvl(self):
        while True:
            try:
                self.lvl = int(input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29"))
                if self.lvl in [1, 2]:
                    return self.lvl
                    break
                else:
                    print("Incorrect format.")
            except ValueError:
                print("Incorrect format.")

    # This method will make sure users can and will only choose an integer
    def user_input(self, total):
        while True:
            try:
                self.your_int = int(input())
                return self.your_int
            except ValueError:
                print("Incorrect format.")

    # This method will ask users if they want to save their name and score to a text file
    def create_file(self, x):
        if x in ['yes', 'y', 'YES', 'Yes']:
            self.username = input("What is your name?")
            file = open('results.txt', 'a', encoding='utf-8')
            file.write(f"{self.username}: {self.n}/{self.counter} in level {self.lvl} ({self.lvl_name}).\n")
            file.close()
            print("The results are saved in results.txt.")
        else:
            exit()

    # This method creates the level one math exam and the questions are created randomly
    def level_one(self):
        self.lvl_name = 'simple operations with numbers 2-9'
        for i in range(5):
            total = f"{random.randint(2, 9)} {random.choice(['*', '-', '+'])} {random.randint(2, 9)}"
            print(total)

            if int(eval(total)) == self.user_input(f"{total}\n"):
                print("Right")
                self.n += 1
            else:
                print("Wrong")
            self.counter += 1
        # If a user answers all the questions properly. They will have an option to do lvl two
        if self.n % 5 == 0:
            progress = input("You have 5/5 correct would you like to continue?")
            if progress in ['yes', 'y', 'YES', 'Yes']:
                print("Beginning Level Two: Integral Squares of 11-29")
                self.level_two()
            else:
                pass

    # This method creates the level two math exam and the questions are created randomly
    def level_two(self):
        self.lvl_name = 'integral squares of 11-29'
        for i in range(5):
            total = f"{random.randint(11, 29)}"
            print(total)

            if int(total) ** 2 == self.user_input(f"{total}\n"):
                print("Right!")
                self.n += 1
            else:
                print("Wrong!")
            self.counter += 1

    # This method creates combines all the methods and prints the length of time it took to finish the exam
    def main(self):
        if self.choose_lvl() == 1:
            last_time = time.time()
            self.level_one()
            new_cur_time = time.time()
            min_passed = int((new_cur_time - last_time) / 60)
            secs_passed = int((new_cur_time - last_time))
        else:
            last_time = time.time()
            self.level_two()
            new_cur_time = time.time()
            min_passed = int((new_cur_time - last_time) / 60)
            secs_passed = int((new_cur_time - last_time))

        print(f"It took you {min_passed} minutes and {secs_passed} seconds to complete the exam.")
        print(f"Your mark is {self.n}/{self.counter}. Would you like to save your result to the file? Enter yes or no.")
        self.create_file(input())


test = ArithmeticExam()
test.main()
