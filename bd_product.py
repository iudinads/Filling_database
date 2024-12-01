import csv

data = [
    ['267','11.0','11.2','28.9','Дэнвич ветчина и сыр','289','Закуски','/images/product/denwich_hum.jpg','270'],
    ['263','9.8','10.3','31.2','Дэнвич чоризо барбекю','289','Закуски','/images/product/denwich_chorizo.jpg','210'],
    ['231','9.4','7.2','30.7','Паста с креветками','369','Закуски','/images/product/pasta_chrimps.jpg','300'],
    ['251','8.4','14.1','20.9','Паста карбонара','369','Закуски','/images/product/pasta_carbonara.jpg','350'],
    ['253','12.4','20.4','3.1','Омлет с беконом','199','Завтрак','/images/product/omlet_bacon.jpg','130'],
    ['221','14.0','16.6','2.4','Омлет с пепперони','199','Завтрак','/images/product/omlet_pepperoni.jpg','110'],
    ['256','9.5','13.4','22.6','Додстер с ветчиной','229','Завтрак','/images/product/dodster_hum.jpg','160'],
    ['301','11.2','15.8','28.6','Сырники со сгущенным молоком','165','Завтрак','/images/product/pancakes.jpg','140'],
    ['42','0.0','0.0','10.6','Добрый кола','Напитки','145','/images/product/cola.jpg','500'],
    ['162','3.3','7.1','11.3','Молочный коктейль','215','Напитки','/images/product/milkshake.jpg','270'],
    ['55','2.8','3.0','4.0','Кофе капучино','169','Напитки','/images/product/coffee_cap.jpg','250'],
    ['47','2.8','3.1','4.2','Кофе латте','169','Напитки','/images/product/coffee_lat.jpg','330'],
    ['470','1.6','49.7','3.0','Соус сырный','45','Соусы','/images/product/cause_cheese.jpg','25'],
    ['473','1.8','45.6','3.2','Соус чесночный','45','Соусы','/images/product/cause_garlic.jpg','25'],
    ['430','5.2','26.0','43.0','Фондан','389','Десерты','/images/product/fondan','160'],
    ['400','5.0','23.0','44.0','Маффин соленая карамель','109','Десерты','/images/product/maffin','120'],
]

with open('product.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Название пиццы", "Состав"])

    for row in data:
        writer.writerow(row)

print("Данные записаны в файл product.csv")