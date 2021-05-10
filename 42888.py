def change(string):
    return string.split(" ")
    
def solution(record):
    data = {}
    procedure = []
    answer = []
    for c in record:
        string = change(c)
        if string[0] == "Enter":
            data[string[1]] = string[2]
            procedure.append(["Enter", string[1]])
        elif string[0] == "Leave":
            procedure.append(["Leave", string[1]])
        elif string[0] == "Change":
            data[string[1]] = string[2]
            
    for c in procedure:
        if c[0] == "Enter":
            ans = data[c[1]] + "님이 들어왔습니다."
        else:
            ans = data[c[1]] + "님이 나갔습니다."
        answer.append(ans)
    
    return answer
