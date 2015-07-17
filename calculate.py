

# Token types
INTEGER,OPER,EOF = 'INTEGER','OPER','EOF'
class Token(object):
	def __init__(self,type,value):
		self.type = type
		self.value = value
	def __str__(self):
		return 'Token({type},{value})'.format(
		type = self.type,value=repr(self.value)
		)
	def __repr__(self):
		return self.__str__()

class Interpreter(object):
	def deleteBlank(self,text):
		ans = ""
		for ch in text:
			if(ch!=' '):
				ans += ch
		return ans
	def __init__(self,text):
		self.text=self.deleteBlank(text)
		self.pos =0;
		self.current_token = None
	def error(self):
		raise Exception('Error parsing input')
	def get_next_token(self):
		text = self.text
		textLen = len(text)
		if self.pos > textLen-1:
			return Token(EOF,None)
		current_char = text[self.pos]
		mark = False
		number = ""
		while current_char.isdigit():
			mark = True
			number += current_char
			self.pos += 1
			if self.pos < textLen:
				current_char = text[self.pos]
			else:
				break;
		if mark == True:
			token = Token(INTEGER,int(number))
			return token
		if current_char =='+' or current_char=='-':
			token = Token(OPER,current_char)
			self.pos += 1
			return token
		self.error()
	def eat(self,token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()
	def expr(self):
		self.current_token = self.get_next_token()
		left = self.current_token
		self.eat(INTEGER)
		
		op = self.current_token
		self.eat(OPER)

		right = self.current_token
		self.eat(INTEGER)
		oper = op.value
		if oper=='+':
			result = left.value + right.value
			return result
		elif oper=="-":
			result = left.value - right.value
			return result
	
def main():
	while True:
		try:
			text = raw_input('calc>')
		except EOFError:
			break
		if not text:
			continue
		interpreter = Interpreter(text)
		result = interpreter.expr()
		print(result)

if __name__ == '__main__':
	main()
