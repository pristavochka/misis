class People:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.total = self.total_score()
    def total_score(self):
        return sum([sum(points) for points in self.scores])


class Top:
    def __init__(self):
        self.people = []
    def add_people(self, people):
        self.people.append(people)
    def results(self):
        return sorted(self.people, key=lambda people: people.total, reverse=True)
    def print_results(self):
        sorted_people = self.results()
        print("Итоговый протокол:")
        for place, people in enumerate(sorted_people, start=1):
            print(f"{place}. {people.name}: {people.total:.0f}")

if __name__ == "__main__":
    leaderboard = Top()

    leaderboard.add_people(People("Николаев", [[8, 9, 8, 7, 9], [8, 8, 9, 8, 8]]))
    leaderboard.add_people(People("Петров", [[5, 9, 10, 9, 4], [6, 8, 9, 9, 6]]))
    leaderboard.add_people(People("Давыдов", [[6, 8, 5, 9, 7], [8, 8, 7, 8, 6.]]))
    leaderboard.add_people(People("Васильев", [[7, 8, 7, 9, 7], [7, 9, 8, 10, 6]]))
    leaderboard.add_people(People("Семёнов", [[6, 4, 6, 6, 5], [7, 4, 5, 4, 5]]))
    leaderboard.add_people(People("Нестеров", [[10, 8, 9, 7, 7], [9, 8, 9, 8, 8]]))

    leaderboard.print_results()