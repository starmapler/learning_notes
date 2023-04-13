def show_id(num, list_or, list_co, dic):
	num += 1
	list_or.append(1)
	list_co.append(1)
	dic['new'] = 1

	print("num's id: " + str(id(num)))
	print("list_or's id: " + str(id(list_or)))
	print("list_co's id: " + str(id(list_co)))
	print("dic's id: " + str(id(dic)))

num = 0
list = [22,33]
dic = {'first': -1, 'second': 2}

show_id(num, list, list[:], dic)

print("num's id: " + str(id(num)))
print("list's id: " + str(id(list)))
print("dic's id: " + str(id(dic)))