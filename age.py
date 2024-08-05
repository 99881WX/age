driving = input('請問您有沒有開過車？ ')
age = input('請問您的年齡？ ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了！！')
	else:
		print('這是說謊的味道（舔')
elif driving == '沒有':
	if age >= 18:
		print('還不快去考（瞪')
	else:
		print('你還年輕呢（瞪')
else:
	print('只能回答「有」或「沒有」，年齡只能填整數！')