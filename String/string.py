
def reverse_iter(string):
	string = list(string)
	start = 0
	end = len(string)-1
	while end > start:
		temp = string[start]
		string[start] = string[end]
		string[end] = temp
		end -= 1
		start += 1
	new_string = "".join(string)
	return new_string

def reverse_rec(string):
	if len(string) < 1:
		return ""
	if len(string) < 2:
		return string[0]
	end = string[0]
	start = string[len(string)-1]
	return start+str(reverse_rec(string[1:len(string)-1]))+end

def is_anagram_iter(string):
	start = 0
	end = len(string)-1
	while end > start:
		if string[start] != string[end]:
			return False
		start += 1
		end -= 1
	return True

def is_anagram_rec(string):
	if len(string) < 1:
		return True
	if string[0] != string[len(string)-1]:
		return False
	return is_anagram_rec(string[1:-1])

if __name__ == "__main__":
	string = "string"
	print string
	print reverse_iter(string)
	string = list(string)
	print reverse_rec(string)
	print is_anagram_iter(string)
	print is_anagram_iter("abba")
	print is_anagram_rec(string)
	print is_anagram_rec("abba")
