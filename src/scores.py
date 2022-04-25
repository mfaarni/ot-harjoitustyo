class Scores:
    def __init__(self):
        self.first_write = True

    def save_score(self, score):
        with open("src/highscores.txt", "a", encoding="utf8") as text_file:
            if self.first_write:
                text_file.write("\n Player score:" + str(score))
                text_file.write("\n Player score: 0")
                self.first_write = False

    def print_highscores(self):
        with open("src/highscores.txt", "r", encoding="utf8") as text_file:
            highscores = text_file.read().splitlines()
            highscores_list = []
            for i in highscores:
                highscores_list.append(i.split(":"))

        for i in enumerate(highscores_list):
            if len(highscores_list[i]) != 2:
                highscores_list = highscores_list[:i-1]+highscores_list[i+1:]
        highscores_list = highscores_list[1:11]
        highscores_list = sorted(highscores_list, key=lambda x: x[1])
        highscores_list.reverse()
        print(highscores_list)

    def return_highscores(self):
        with open("src/highscores.txt", "r", encoding="utf8") as text_file:
            highscores = text_file.read().splitlines()
            highscores_list = []
            for i in highscores:
                highscores_list.append(i.split(":"))
        highscores_list_updated = []
        for i in range(len(highscores_list)-1):
            if len(highscores_list[i]) == 2:
                highscores_list_updated.append(highscores_list[i])

        highscores_list = highscores_list_updated[0:22]
        highscores_list = sorted(highscores_list, key=lambda x: x[1])
        highscores_list.reverse()
        highscores_list = highscores_list[0:11]
        return highscores_list
