def reverseString(str):
	#Write your code here.
    res = str.strip().split()
    return " ".join(res[::-1])

print(reverseString("Hello World!!"))