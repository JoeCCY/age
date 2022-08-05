driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有' :
	if age >= 18 :
		print('你已通過測驗')
	else:
		print('奇怪 你怎麼開過車')
elif driving == '沒有' :
	if age >= 18 :
		print('你可以考駕照了, 怎麼不去考')
	else:
		print('Good! 再過幾年 你就可以考駕照了')