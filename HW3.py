# HW Collections P1
# 1. Сгенерировать список из 500 Emails где каждый email заканчивается на @gmail.com 
# текст до @gmail.com - символы (Латиница, цифры, _ . ) [user_29@gmail.com, alex.braun@gmail.com, …]
import random


def random_emails(emails_number):
    email_list = []
    for i in range(emails_number):
        email_list.append(''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789_.") for _ in range(random.randint(7, 10))) + "@gmail.com")
    return email_list


emails = random_emails(3)
print(emails)

# 2. Преобразовать список Emails в Dict где ключ - это index элемента в списке
def list_to_dict(input_list):
    my_dict = {}
    for item in input_list:
        my_dict[input_list.index(item)]  = item
    return my_dict


print(list_to_dict(emails))

# 3. Создать список Name_Surname из 100 элементов, где каждое 10 имя “Adam”
# [“Adam_black”, “Olga_Savitskaya, …]
names = ['Bob', 'Johny', 'Steve', 'Ivan', 'Horhe', 'Maria', 'Laura', 'Olga', 'Sveta', 'Lily']
surnames = ['Black', 'Johnson', 'Stevenson', 'Huares', 'White', 'Perkinson', 'Jagger', 'Tailor']

def random_persons(names, surnames, number):
    result = []
    for i in range(1, number + 1):
        print(i)
        if i > 0 and i % 10 == 0:
            result.append(''.join('Adam_' + random.choice(surnames)))
        else:
            result.append(''.join(random.choice(names) + '_' + random.choice(surnames)))
    return result


persons = random_persons(names, surnames, 20)
print(persons)

# 4. Создать список списков в котором будут пары 
# [[“Adam_Black”, “Eva_Brain”], [], …]
# Этот список надо создать из списка в задании #3, в него должны войти все имена с фамилиями Adam-ов, парой для Адамав в каждом внутреннем списке должна быть Eva_фамилия
# [[“Adam_Black”, “Eva_Brain”], [], …]
def adam_pair(input_list):
    result_dict = []
    for item in input_list:
        if item.split('_')[0] == 'Adam':
            result_dict.append([item, 'Eva_' + item.split('_')[1]])
    return result_dict


print(adam_pair(persons))

# 5. Сгенерировать список из 100 кличек для животных , в списке должно быть 10 одинаковых кличек [“Spike”, “Barboss”, “Bloom”, “Spike”, …]
pets = ['Spike', 'Barbos', 'Bloom', 'Salma', 'Bobik', 'Zhupel', 'Gena', 'Chip', 'Dale']
def pets_names(number):
    result = []
    for i in range(1, number):
        result.append(random.choice(pets))
    return result


pets = pets_names(1000)
# print(pets)

# 6. Найти дубликаты в списке кличек и удалить их из списка, оставив один экземпляр клички дубликатов.
print([*set(pets)])

