def romanToInt(s):

    # Write your code here
    # Return the int value
    roman_map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    result = 0
    
    for i in range(len(s)):
        if i < len(s)-1:
            if roman_map.get(s[i+1]) > roman_map.get(s[i]):
                result += roman_map.get(s[i])
            else:
                val = (roman_map.get(s[i+1]) - roman_map.get(s[i]))
                result += val
        else:
            result += roman_map.get(s[i])
    return result

print(romanToInt('LXVII'))