def arithmetic_arranger(x, y = False):
	length_mass = len(x)
	if length_mass > 5:
		print("Error: Too many problems")
		return
	for item in x:
		if '+' not in item and '-' not in item:
				print("Error: Operator must be '+' or '-'")
				return
		if '+' in item:
			plus = item.replace(' ', '').split('+')
			# print(plus)
			
			if ((plus[0].isdigit()) and (plus[1].isdigit())) == False:
				
				print("Error: Numbers must only contain digits")
				return
			if len(plus[0]) > 4 or len(plus[1]) > 4:
				print('Error: Numbers cannot be more than four digits')
				return
			mar = len(plus[0])
			mar1 = len(plus[1])
			if mar == mar1:
				print((' '*2) + plus[0])
				print('+' + ' '+ plus[1])
				print('-'*(mar+2))
				if y == True:
					result = int(plus[0])+int(plus[1])
					rez = len(str(result))
					if rez == (mar1+1):
						print(' ' + str(result))


			#print(plus[0])
			#print('+' + plus[1])

		elif '-' in item:
			minus = item.replace(' ', '').split('-')
			#print(minus)
			if ((minus[0].isdigit()) and (minus[1].isdigit())) == False:
					print("Error: Numbers must only contain digits")
					return
			if len(minus[0]) > 4 or len(minus[1]) > 4:
				print('Error: Numbers cannot be more than four digits')
				return
			mar = len(minus[0])
			mar1 = len(minus[1])
			if mar == mar1:
				print((' '*2) + minus[0])
				print('-' + ' '+ minus[1])
				print('-'*(mar+2))
				if y == True:
					result = int(minus[0])-int(minus[1])
					rez = len(str(result))
					if rez == (mar1+1):
						print(' ' + str(result))
			elif mar > mar1:
				print(' ' + minus[0])
				print('-' + ' ' + minus[1])
				print('-'*(mar+1))
				if y == True:
					result = int(minus[0])-int(minus[1])
					rez = len(str(result))
					if rez == (mar1+1):
						print(' ' + str(result))
		print(" ")
arithmetic_arranger(["8 + 8", "1 - 5", "9999 + 9999", "523 - 49"], True)