from faker import Faker
import json

fake_ru = Faker('ru_RU')
# print(fake_ru.name())  # рандомное ФИО
# print(fake_ru.simple_profile())
# print(fake_ru.isbn13())


def create_json():
    with open("output.json", 'w', encoding="utf8") as f:  # записать список в JSON файл
        data_list = []
        for i in range(1, 251):
            data = {'N': i, 'Имя': fake_ru.name(), 'Тел': fake_ru.phone_number(), 'Профессия': fake_ru.job(), 'Адрес': fake_ru.job()}
            data_list.append(data)
        f.write(json.dumps(data_list, ensure_ascii=False, indent=4))


def create_json_v2():
    name = fake_ru.name()
    tel = fake_ru.phone_number()
    prof = fake_ru.job()
    address = fake_ru.job()
    dict[i] = i:{'name', 'tel', 'prof', 'address'}
    with open("output.json", 'w', encoding="utf8") as f:
        json.dumps(name, tel, prof, address)



if __name__ == '__main__':
    create_json()

