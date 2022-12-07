from KFC.models import *

user1 = User.objects.create(username='nikname21@gmail.com', password='defender42')
client1 = Client(user=user1, name='Азат Соколов', card_number='4147565798789009')
client1.save()

user2 = User.objects.create(username='altywa1998@gmail.com', password='nono34')
worker1 = Worker(user=user2, name='Алтынай Алиева', position='Оператор кассы')
worker1.save()

ingredient1 = Ingredient.objects.create(name='Сыр', extra_price=10)
ingredient2 = Ingredient.objects.create(name='Курица', extra_price=70)
ingredient3 = Ingredient.objects.create(name='Говядина', extra_price=80)
ingredient4 = Ingredient.objects.create(name='Салат', extra_price=15)
ingredient5 = Ingredient.objects.create(name='Фри', extra_price=15)

food1 = Food.objects.create(name='Шаурма', start_price=50)
food2 = Food.objects.create(name='Гамбургер', start_price=25)

food1.ingredients.set([ingredient1, ingredient3, ingredient4, ingredient5],
                      through_defaults={'client': client1, 'worker': worker1})

order1_bill = food1.start_price + ingredient1.extra_price + ingredient3.extra_price + ingredient4.extra_price + ingredient5.extra_price
print(order1_bill)

food2.ingredients.set([ingredient2, ingredient4],
                      through_defaults={'client': client1, 'worker': worker1})

order2_bill = food2.start_price + ingredient2.extra_price + ingredient4.extra_price
print(order2_bill)


