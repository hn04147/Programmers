def solution(triangle):
  answer = [[0] * len(triangle) for _ in range(len(triangle))]

  for i in range(len(triangle)):
    for j in range(i + 1):
      if i == j == 0:
        answer[i][j] = triangle[i][j]
      else:
        if j > 0:
          answer[i][j] = answer[i - 1][j - 1] + triangle[i][j]
        if j < i:
          answer[i][j] = max(answer[i][j], answer[i - 1][j] + triangle[i][j])

  return max(answer[-1])