def solution(id_list, report, k):
  answer = []
  
  reporter_list = [[] for _ in range(len(id_list))]
  reported_list = [[] for _ in range(len(id_list))]
  people_dict = {}
  for i in range(len(id_list)):
    people_dict[id_list[i]] = i       
  name_dict = {}
  for id in id_list:
    name_dict[id] = 0
  
  for report_ in report:
    reporter, reported = report_.split()
    if reported not in reporter_list[people_dict[reporter]]:
      reporter_list[people_dict[reporter]].append(reported)
      reported_list[people_dict[reported]].append(reporter)
  
  for id in id_list:
    banned_num = 0
    if len(reporter_list[people_dict[id]]) > 0:
      for reported_person in reporter_list[people_dict[id]]:
        if len(reported_list[people_dict[reported_person]]) >= k:
          banned_num += 1
    answer.append(banned_num)
      
  return answer