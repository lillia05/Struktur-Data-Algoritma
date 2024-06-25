class HighScores:
    def __init__(self, capacity):
        self.scores = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def add_score(self, score):
        if self.size < self.capacity:
            self.scores[self.size] = score
            self.size += 1
        else:
            print("Daftar skor tinggi sudah penuh. Tidak dapat menambahkan skor lagi.")

    def display_scores(self):
        print("High Scores:")
        for i in range(self.size):
            print(self.scores[i])

high_scores = HighScores(5)
high_scores.add_score(100)
high_scores.add_score(75)
high_scores.add_score(120)
high_scores.add_score(90)
high_scores.add_score(110)

high_scores.display_scores()
