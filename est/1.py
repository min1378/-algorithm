def solution(card_numbers):
  answer = []
  for card in card_numbers:
    print(card)
    temp = card.split("-")
    check_even = 0
    check_odd = 0
    check_four = False
    if len(temp) > 1:
      count = 0
      for tem in temp:
        if len(tem) != 4:
          check_four = True
      if check_four:
        answer.append(0)
        continue
    
      for tem in temp:
        for i in range(len(tem)):
          if i % 2 == 0:
            even2 = int(tem[i]) * 2
            if even2 > 9:
              check_even += int(str(even2)[0]) + int(str(even2)[1])
            else:
              check_even += even2
          
          else :
            check_odd += int(tem[i]) 
    else :
      if len(temp[0]) != 16:
        answer.append(0)
        continue
      for i in range(len(temp[0])):
        if i % 2 == 0:
          even2 = int(temp[0][i]) * 2
          if even2 > 9:
            check_even += int(str(even2)[0]) + int(str(even2)[1])
          else:
            check_even += even2
        else :
          check_odd += int(temp[0][i])
    if (check_even + check_odd) % 10 == 0:
      answer.append(1)
    else :
      answer.append(0)
  return answer

# 1  2  3  4  5  6  7  8 9 10 11 12 13 14 15 16
# 16 15 14 13 12 11 10 9 8  7  6  5  4  3  2  1
solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"])