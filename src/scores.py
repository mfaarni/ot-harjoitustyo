import time
class Scores:
    def __init__(self):
        self.first_write = True
        self.score=8000
        self.start_time=time.time()

    def save_score(self, coin_count,death_count):
        with open("src/highscores.txt", "a", encoding="utf8") as text_file:
            if self.first_write:
                text_file.write("\n Player score:" + str(self.score-int(time.time() - self.start_time)*100+coin_count*100-1000*death_count))
                text_file.write("\n Player score: 0")
                self.first_write = False

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
        highscores_list = highscores_list_updated[0:len(highscores_list_updated)]
        #print("unsorted:",highscores_list)
        highscores_list = sorted(highscores_list, key=lambda x: int(x[1]))

        #print("sorted:",highscores_list)
        highscores_list.reverse()
        highscores_list = highscores_list[0:11]
        return highscores_list

    def update_start_time(self):
        self.start_time=time.time()