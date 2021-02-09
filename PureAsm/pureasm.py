#初始化
#测试语言1.0
print('\n')
print('?-PureAsm bate 0.8.4b')#My English is very less....我英语很差xwx
print('?-Time 2021 2 9')
print('?-Can call the 3597974497@qq.com to discuss the Codes \n')
stact ={}
proc = {}#空的哎？
proclist = []#过程表，辅助调用
retline = []#没办法xwx，咱实力不够，必须再开一个表来辅助咯
Error = ['Value Error','OP Error','Stact Error','Function Error','Add Error','Time Error','Div Error','Minus Error','Put Error','Input Error','Less Error','Equal Error','Greater Error','Type Error','Power Error']
f = input("file_> ")
print('\n')
f = open(f,'r')
d = f.readlines()
d.append('exit')
f.close()
#op实现
def push(name,v):
	try:
		if v[0] == '"' and v[-1] == '"':
			stact[name] = v.strip('"')
		elif v == 'True' or v == 'true':
			stact[name] = True
		elif v == 'False' or v == 'false':
			stact[name] = False
		else:
			stact[name] = float(v)
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot kown the Value')
		print(Error[0])
		input()
		exit()
def add(one,two,v):
	try:
		a = stact.get(one)
		b = stact.get(two)
		c = a + b
		stact[v] = c
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot Add < ' + str(one)+'='+str(stact.get(one))+' , '+str(two)+'='+str(stact.get(two))+' >')
		print(Error[1],Error[4])
		input()
		exit()
def minus(one,two,v):
	try:
		a = stact.get(one)
		b = stact.get(two)
		c = a - b
		stact[v] = c
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot Minus < ' + str(one)+'='+str(stact.get(one))+' , '+str(two)+'='+str(stact.get(two))+' >')
		print(Error[1],Error[7])
		input()
		exit()
def put(v):
	try:
		if v[0] != '"' and v[-1] != '"':
			print(stact.get(ce[1]))
		else:
			print(v)
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot PUT ')
		print(Error[1],Error[8])
		input()
		exit()
def time(one,two,v):
	try:
		a = stact.get(one)
		b = stact.get(two)
		c = a * b
		stact[v] = c
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot Time < ' + str(one)+'='+str(stact.get(one))+' , '+str(two)+'='+str(stact.get(two))+' >')
		print(Error[1],Error[5])
		input()
		exit()
def div(one,two,v):
	try:
		a = stact.get(one)
		b = stact.get(two)
		c = a * b
		stact[v] = c
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+v +'" Cannot Div < ' + str(one)+'='+str(stact.get(one))+' , '+str(two)+'='+str(stact.get(two))+' >')
		print(Error[1],Error[6])
		input()
		exit()
def stdinput(name):
	try:
		a = input()
		if a.isnumeric() == True:
			stact[name] = float(a)
		elif '.' in a:
			stact[name] = float(a)
		else:
			stact[name] = a
			print(a)
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< in "'+name +'" Cannot Input ')
		print(Error[1],Error[9])
		input()
		exit()
def less(a,b,c):
	if type(stact.get(a)) == type(stact.get(b)):
		if stact.get(a) < stact.get(b):
			stact[c] = True
		else:
			stact[c] = False
	else:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< , type error in > '+ a + '='+str(stact.get(a))+' , '+ b+ '=' +str(stact.get(b))+' <')
		print(Error[1],Error[10],Error[13])
		input()
		exit()
def greater(a,b,c):
	if type(stact.get(a)) == type(stact.get(b)):
		if stact.get(a) > stact.get(b):
			stact[c] = True
		else:
			stact[c] = False
	else:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< , type error in > '+ a + '='+str(stact.get(a))+' , '+ b+'='+str(stact.get(b))+' <')
		print(Error[1],Error[11],Error[13])
		input()
		exit()
def equal(a,b,c):
	if type(stact.get(a)) == type(stact.get(b)):
		if stact.get(a) == stact.get(b):
			stact[c] = True
		else:
			stact[c] = False
	else:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< , type error in > '+ a + '='+str(stact.get(a))+' , '+ b+'='+str(stact.get(b))+' <')
		print(Error[1],Error[12],Error[13])
		input()
		exit()
def asmif(a):
	if stact.get(a) == True:
		return True
	else:
		return False
def power(a,num,v):
	try:
		a = stact.get(a)
		num = stact.get(num)
		pown = a**num
		stact[v] = pown
	except:
		print('\n')
		print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t +'  "< , type error in >  ' + str(ce[1]) +' = ' + str(stact.get(ce[1])) + '  < is ' + str(type(stact.get(str(ce[1])))))
		print(Error[1],Error[14])
		input()
		exit()
def nop():
	pass
#第一次用上proc过程栈
#初始化行指针
l = 0
havecall = 0
#主循环
while True:
	t = d[l]
	t = str(t)
	t = t.strip()
	ce = t.split(' ')
	#开始
	if ce[0] == 'push':#这里要重新初始化，因为分割符不一样了，会造成歧义（）
		a = d[l]
		t=str(a)
		t = t.strip()
		ce = t.split(' ',2)
		push(ce[1],ce[2])
	elif ce[0]=='add':
		add(ce[1],ce[2],ce[3])
	elif ce[0] == 'put':
		put(ce[1])
	elif ce[0] == 'minus':
		minus(ce[1],ce[2],ce[3])
	elif ce[0] == 'time':
		time(ce[1],ce[2],ce[3])
	elif ce[0] == 'div':
		div(ce[1],ce[2],ce[3])
	elif ce[0] == 'jump':
		#改变行指针
		l = (int(ce[1])-2)
	elif ce[0] == 'input':
		stdinput(ce[1])
	elif ce[0] == 'equal':
		equal(ce[1],ce[2],ce[3])
	elif ce[0] == 'less':
		less(ce[1],ce[2],ce[3])
	elif ce[0] == 'greater':
		greater(ce[1],ce[2],ce[3])
	elif ce[0] == 'call':
		if ce[1] in proclist:
			havecall += 1
			retline.append(l+4)
			lt = proc.get(ce[1])
			lt = int(lt[0])
			l = (lt-2)
		else:
			print('\n')
			print('    ASM Error in line  '+str(l+1)+'  :  >"  '+ t  +'  "< , CALL error in >  ' + str(ce[1]) )
			print(Error[1],Error[14])
			input()
			exit()
	elif ce[0] == 'if':
		x = asmif(ce[1])
		if x == True:
			pass
		else:
			l += 1
	elif ce[0] == 'power':
		power(ce[1],ce[2],ce[3])
	elif ce[0] == 'exit':
		exit()
	elif ce[0] == 'ret':
		if havecall >= 1:
			l = (int(retline[-1])-4)
	elif len(ce) == 1 and str(ce[0])[-1] == ':':#获得过程头指针
		func = str(ce[0])[0:-1]#有点乱
		line = l + 2
		proc[func] = [line]
		proclist.append(func)
		for i in d[line:]:
			line = line + 1
			if i.strip() == 'ret':
				endline = line
				proc[func].append(endline)
				l = (endline-1)
				break
	elif ce[0] == 'nop':
		nop()
	#行指针判定
	if l < (len(d)-1):
		l += 1
	else:
		exit()
input()