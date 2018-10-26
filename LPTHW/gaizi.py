import sys
script, encoding_way, error = sys.argv

def main(language_file, encoding_way, errors):
	line = language_file.readline()

	if line:
		print_line(line, encoding_way, errors)
		return main(language_file, encoding_way, errors)
	

def print_line(line, encoding_way, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding_way, errors=errors)
	cooked_string = raw_bytes.decode(encoding_way, errors=errors)
	
	print(raw_bytes, "====",cooked_string)
	print(cooked_string == next_lang)


languages = open("test2.txt", encoding = "utf-8")

main(languages, encoding_way, error)
