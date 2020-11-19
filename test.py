import PlaceNember as pn
from Get_numbers_v2 import get_numbers
from sqlalchemy import create_engine
# test 1
def checkNumber(num1, num2, P, N):
	fP, fN = pn.PlaceNumber(num1, num2)
	if fP == P and fN == N:
		print('TestOK', num1, num2)
	else:
		print('TestBad ..', num1, num2, fP, fN, P, N)
 
def createListToNumberTest():
	testlist = list()
 	# добавляем num1, num2, P, N
	testlist.append([100000, 100001, 5, 0])
	testlist.append([100010, 100001, 4, 2])
	testlist.append([123456, 123456, 6, 0])
	testlist.append([123456, 654321, 0, 6])
	testlist.append([271234, 275689, 2, 0])
	testlist.append([123427, 560872, 0, 2])
	testlist.append([100234, 100567, 3, 0])
	testlist.append([234100, 100567, 0, 3])
	for elem in testlist:
		checkNumber(elem[0], elem[1], elem[2], elem[3])
createListToNumberTest()
# test 2 
# проверка на подключение к бд (узнать самому)
def checkConnection():
	engine = create_engine('mysql+mysqlconnector://arkhipov:Fest2020@104.154.72.248/numbers', echo=False)
	if engine.connect() != None:
		print("TestOK")
	else:
		print("Bad Connection")
checkConnection()

# test 3
def checkSize(sizeList: list):
 	# каждый элемент списка - количество чисел которые мы запрашиваем у бд
 	# заполняй элементам - 0, 10000 - граничные элементы +++ любые из середины
 	for count in sizeList:
 		returnedList = get_numbers(count)
 		if len(returnedList) == count:
 			print('TestOK', count)
 		else:
 			print('TestBad', count)
countList = list()
countList.append(0)
countList.append(5)
countList.append(10000)
checkSize(countList)
 # test 4 
 # тест на порядок выгруженных чисел
 # вызываешь дважды get_numbers(count) значение count одинаково
 # необходимо проверить является ли вывод различным 
 # списки выданные должны не совпадать
list1 = get_numbers(10)
list2 = get_numbers(10)
def get_equivalence(list1,list2):
	if list1 == list2:
		print("TestBad")
	else:
		print('TestOK')
get_equivalence(list1,list2)