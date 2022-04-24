
class Scores:
    def __init__(self):
        self.first_write=True
    def save_score(self, score):
        self.text_file=open("src/highscores.txt", "a")
        if self.first_write:
            self.text_file.write("\n Player score:"+ str(score))
            print(self.first_write)
            self.first_write=False
            self.text_file.close()        

    def print_highscores(self):
        self.text_file=open("src/highscores.txt", "r")
        with self.text_file as f:
            highscores= f.read().splitlines()
            highscores_list=[]
            for i in highscores:
                highscores_list.append(i.split(":"))
                
            self.text_file.close()        
        highscores_list=highscores_list[1:11]
        highscores_list=sorted(highscores_list, key=lambda x : x[1])
        highscores_list.reverse()
        print(highscores_list)

    def return_highscores(self):
        self.text_file=open("src/highscores.txt", "r")
        with self.text_file as f:
            highscores= f.read().splitlines()
            highscores_list=[]
            for i in highscores:
                highscores_list.append(i.split(":"))
                
            self.text_file.close()        
        highscores_list=highscores_list[1:11]
        highscores_list=sorted(highscores_list, key=lambda x : x[1])
        highscores_list.reverse()
        return (highscores_list)
