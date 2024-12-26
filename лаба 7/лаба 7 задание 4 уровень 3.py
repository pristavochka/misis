class Member:
    def __init__(self, surname, result):
        self.surname = surname
        self.result = result

    def __repr__(self):
        return f"{self.surname} ({self.result})"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []

    def add_member(self, surname, result):
        member = Member(surname, result)
        self.members.append(member)

    def sort_members(self):
        self.members.sort(key=lambda x: x.result)

    def get_sorted_results(self):
        return self.members


def print_table(group_1, group_2):
    print(f"{'Место':<6} {'Фамилия':<20} {'Результат':<10}")
    print("-" * 40)

    group1 = group_1.get_sorted_results() 
    group1.sort(key=lambda x: x.result, reverse=True)
    group2 = group_2.get_sorted_results()
    group2.sort(key=lambda x: x.result, reverse=True)
    print("группа 1:")
    for index, member in enumerate(group1, start=1):
        print(f"{index:<6} {member.surname:<20} {member.result:<10}")
    print("группа 2:")
    for index, member in enumerate(group2, start=1):
        print(f"{index:<6} {member.surname:<20} {member.result:<10}")

if __name__ == "__main__":
    group_a = Group("Группа A")
    group_b = Group("Группа B")

    group_a.add_member("Петров", 20.5)
    group_a.add_member("Сидоров", 18.0)
    group_a.add_member("Кузнецов", 22.3)

    group_b.add_member("Иванов", 21.0)
    group_b.add_member("Федоров", 19.5)
    group_b.add_member("Семенов", 17.8)

    group_a.sort_members()
    group_b.sort_members()

    print_table(group_a, group_b)