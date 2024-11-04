# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c = ","):
    ans = []
    a = a.split(c)
    b = b.split(c)

    for i in a:
        for j in b:
            if i == j:
                ans.append(i)

    ans.sort()
    return(ans)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))
