

#******* import standard libraries *******

from hashlib import sha256

from re import findall

from random import choice

from string import ascii_lowercase as chars

#********Languages Alphabet**********

PersianLetters = ["آ","ا","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ک","گ","ل","م","ن","و","ه","ی","۱","۲","۳","۴","۵","۶","۷","۸","۹","۰","،","؟","«","»","؛","\u200c"]

EnglishLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",",","",";",'"']

ArabicLetters = ["آ","ا","ء","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ک","ل","م","ن","و","ه","ة","ی","ي","۱","۲","۳","۴","۵","۶","۷","۸","۹","۰","،","؟","«","»","؛","\u200c"]

RussianLetters = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","1","2","3","4","5","6","7","8","9","0",".",",",'"']

GermanyLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",",","",";",'"',"ü","ö","ä"]

#****************Tools****************

def abbreviation(text):

	'a method that may be very, very useful to you; As the name implies, this method gives you the abbreviation of several words; Just give it a String.'

	speld,result = [] , ""

	for word in text.split():

		speld.append(word[0])

	for item in speld:

		result += item

	return result.upper()

def checkFile(FilePath,listName):

	'a method that takes a list of letters of the alphabet and a file address, and detects the language used in its data.'

	return build(open(FilePath,'r').read,listName)

def crack(hashword,alphabet):

	'is a method to restore hashes created with the hasher method.'

	result = ""

	for hashletter in findall(".{64}",hashword.lower()):

		for letter in alphabet:

			if sha256(letter.encode()).hexdigest() == hashletter:

				result += letter

	return result

class count:

	'count is a class by two methods for counting letters and words of a text.'

	@staticmethod

	def letters(text,WithWhiteSpace):

		'using this method, you can counting text letters with WhiteSpace or not.'

		if WithWhiteSpace == False:

			result = []

			for char in text:

				if char == " " or char == "\u200c" or char == "\n" or char == "\t":

					pass

				else:

					result.append(char)

			return len(result)

			

		else:

			result = list(text)

			return len(result)

	@staticmethod

	def words(text):

		'using words method , you can counting text words!'

		result = text.split()

		return len(result)

def delete(letter,text):

	'this method can to delete a letter from text'

	chars = list(text)

	result = ""

	for char in chars:

		if char != letter:

			result += char

	return result

def dispersion(text,*count):

		'dispersion method can to dispersion text by your personal length or standard'

		characters = list(text)

		result = []

		try:

			Count = count[0]

			

		except:

			Count = len(text)

			

		if  Count <= len(text):

			for i in range(Count):

				random = choice(characters)

				result.append(random)

				characters.remove(random)

					

			return "".join(result)

			

		else:

			return f"LengthError: {Count} is oversize of {text}\'s length !"

		

def find(value,origin,destination):

	'find: Using this tool, you can find an item from one list equal to the position of the same item in another list. For example, from Persian Letters, you can find an item equal to a in English Letters.'

	chars = ""

	

	for char in list(value):

		chars += origin[destination.index(char)]

		

	return chars

def hasher(word):

	'hasher: For more security of your data, easily convert it to sha256 with this method and then with the crack method, return it to its original state; Just give it a String. '

	result = ""

	for letter in word:

		result += sha256(letter.encode()).hexdigest()

		

	return result

def match(char,alphabet):

	'match a character with an alphabet characters'

	result = []

	for letter in alphabet:

		result.append(char+letter) 		

	return result

def repeat(text,count):

	'repeat a text with your personal count'

	return text*count

def repeatCount(letter,text):

	'a method for get count of repeat a letter in text'

	counter = 0

	for char in list(text):

		if char == letter:

			counter += 1

	return counter

def replace(x,text,y,CaseSensitive,*From,**To):

	'replace x in text locate any y in your text. you can set case sensitivity to True or False , start point and finish point !'

	chars = list(text)

	result = ""

	try:

		from_,to = From[0]-1,From[1]

	except:

		from_,to = 0,len(chars)

		

	for char in chars[from_:to]:

		if char == x and CaseSensitive == True:

			result += y

			

		elif char.lower() == x.lower() and CaseSensitive == False:

			result += y

			

		else:

			result += char

			

	return result

def reverse(word):

	'using this method, reversing text is possible! '

	return word[::-1]

Colors = {"bold":"\033[1m","underline":"\033[4m","important":"\033[7m","black":"\033[30m","dred":"\033[31m","dgreen":"\033[32m","dyellow":"\033[33m","dblue":"\033[34m","lblue":"\033[36m","dpink":"\033[35m","white":"\033[37m","bg_black":"\033[40m","bg_dred":"\033[41m","bg_dgreen":"\033[42m","bg_dyellow":"\033[43m","bg_dblue":"\033[44m","bg_lblue":"\033[46m","bg_pink":"\033[45m","bg_white":"\033[47m","grey":"\033[90m","lred":"\033[91m","lgreen":"\033[92m","lyellow":"\033[93m","purple":"\033[94m","lpink":"\033[95m","cyan":"\033[96m","bg_lred":"\033[101m","bg_lgreen":"\033[102m","bg_lyellow":"\033[103m","bg_lpurple":"\033[104m","bg_lpink":"\033[105m","bg_lcyan":"\033[106m","bg_light":"\033[107m"}

def style(text,key):

	'set color for texts, using style method'

	if key in Colors.keys():

		return Colors.get(key)+text+Colors.get("white")+""

	return "UndefindError: color not defind"

def sorter(arr,request):

	'sorting array\'s items in concerned key'

	characters = {i: [] for i in chars}

	for element in arr:

		key = element[0].lower()

		if key in characters:

			characters[key].append(element)

	return characters.get(request.lower())

def translate(text,origin,destination) -> str:

	'translate texts using google translate api'

	from requests import get

	data = get("http://api.codebazan.ir/lang/google/?FROM="+origin+"&TO="+destination+"&TEXT="+text)

	

	return data.text

def T_PDF(path,page,origin,destination) -> str:

	'Translate PDF files data'

	from PyPDF2 import PdfFileReader as PDF

	File = open(path,'rb')

	content = PDF(File)

	text = content.getPage(page)

	return translate(text.extractText(),origin,destination)

def T_TXT(path,origin,destination) -> str:

	'Translate TXT files data'

	File = open(path,'r')

	return translate(File.read(),origin,destination)

def T_DOCX(path,origin,destination) -> str:

	'Translate DOCX files data'

	from docx2txt import process as WORD

	File = open(path,'rb')

	content = WORD(File)

	return translate(content,origin,destination)

def TTS(text,slow,path):

	'convert Text To Speech on audio files with slow speed or not.'

	from gtts import gTTS

	tts = gTTS(text=text,slow=slow)

	tts.save(path)

def wiki(text):

	'search the wikipedia using wikipedia library'

	from wikipedia import summary as search

	return search(text)

def write(text,*speed):

	'print texts with write mood'

	from time import sleep

	

	for letter in text:

		print("\r",text[:text.index(letter)]+letter,end="")

		try:

			sleep(*speed)

			

		except:

			sleep(0.01)

	print(end="\n")

#***********Orginal Functions**********

#@@@ Creator Function @@@#

def build(text,alphabet):

	'building language recognize method'

	return any(char in alphabet for char in text)

#$$$ Languages Functions $$$#

def Arabic(ar):

	'recognize arabic texts'

	return build(ar,ArabicLetters)

	

def English(en):

	'recognize english texts'

	return build(en,EnglishLetters)

	

def Germany(ge):

	'recognize germany texts'

	return build(ge,GermanyLetters)

def Persian(fa):

	'recognize persian texts'

	return build(fa,PersianLetters)

def Russian(ru):

	'recognize russian text'

	return build(ru,RussianLetters)
