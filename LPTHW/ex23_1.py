import sys
script, encoding, error = sys.argv
raw = open("C:/workspace/languages.txt", "wb")
cooked = open("test4.txt", "w")

def main(language_file, encoding, errors):
	print(">>>>> main", repr(language_file))
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)
	
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	raw.write(raw_bytes)
	print(raw_bytes, "<===>", cooked_string)
#language = open("C:/workspace/languages.txt")
languages = open("C:/workspace/languages.txt", encoding="utf-8")

main(languages, encoding, error)

languages.close()

