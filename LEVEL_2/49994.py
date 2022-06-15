def solution(dirs):
    x, y = 0, 0
    answer = 0
    visited = set()
    for d in dirs:
        if d == "U":
            if y < 5:
                nx, ny = x, y+1
                if (x, y, nx, ny) not in visited:
                    visited.add((x, y, nx, ny))
                    visited.add((nx, ny, x, y))
                    answer += 1
                y += 1
        elif d == "R":
            if x < 5:
                nx, ny = x+1, y
                if (x, y, nx, ny) not in visited:
                    visited.add((x, y, nx, ny))
                    visited.add((nx, ny, x, y))
                    answer += 1
                x += 1
        elif d == "D":
            if y > -5:
                nx, ny = x, y-1
                if (x, y, nx, ny) not in visited:
                    visited.add((x, y, nx, ny))
                    visited.add((nx, ny, x, y))
                    answer += 1
                y -= 1
        elif d == "L":
            if x > -5:
                nx, ny = x-1, y
                if (x, y, nx, ny) not in visited:
                    visited.add((x, y, nx, ny))
                    visited.add((nx, ny, x, y))
                    answer += 1
                x -= 1
    return answer
