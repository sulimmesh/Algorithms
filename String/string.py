
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


if __name__ == "__main__":
	string = "string"
	print reverse_iter(string)
	string = list(string)
	print reverse_rec(string)