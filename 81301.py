def solution(s):
    alphabet = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
        else:
            if s[i:i+3] in alphabet:
                answer += alphabet[s[i:i+3]]
                i += 3
            elif s[i:i+4] in alphabet:
                answer += alphabet[s[i:i+4]]
                i += 4
            else: 
                answer += alphabet[s[i:i+5]]
                i += 5
    return int(answer)