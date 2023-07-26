def arithmetic_arranger(problems, display_answers = False):
  if len(problems) > 5:
      return "Error: Too many problems."

  list_prob = []
    
  for prob in problems:
    prob = prob.split(" ")
    
    first = prob[0]
    operator = prob[1]
    second = prob[-1]
    
    if (operator != "+") & (operator != "-"):
      return "Error: Operator must be '+' or '-'."

    if (len(first) > 4) | (len(second) > 4):
      return "Error: Numbers cannot be more than four digits."

    if not (first.isnumeric() and second.isnumeric()):
      return "Error: Numbers must only contain digits."

    length = 2 + len(max(prob, key=len))
    dict_prob = dict()

    dict_prob['first'] = first
    dict_prob['spaces1'] = length - len(first)
    dict_prob['operator'] = operator
    dict_prob['spaces2'] = length - 1 - len(second)
    dict_prob['second'] = second
    dict_prob['length'] = length
    dict_prob['answer'] = 0

    list_prob.append(dict_prob)

  arranged_problems = ""

  for i in range(len(list_prob)):
    
    arranged_problems += " "*list_prob[i]['spaces1'] + list_prob[i]['first']
    
    if i != len(list_prob) - 1:
      arranged_problems += " "*4
    else:
      arranged_problems += "\n"
      
  for i in range(len(list_prob)):
    
    arranged_problems += list_prob[i]['operator'] + " "*list_prob[i]['spaces2'] + list_prob[i]['second']
    
    if i != len(list_prob) - 1:
      arranged_problems += " "*4
    else:
      arranged_problems += "\n"

  for i in range(len(list_prob)):
    arranged_problems += "-"*list_prob[i]['length']
    if i != len(list_prob) - 1:
        arranged_problems += " "*4

  if display_answers:
    for i in range(len(list_prob)):
      operator = list_prob[i]['operator']
      
      if operator == "+":
        list_prob[i]['answer'] = int(list_prob[i]['first']) + int(list_prob[i]['second'])
      else:
        list_prob[i]['answer'] = int(list_prob[i]['first']) - int(list_prob[i]['second'])
      
      list_prob[i]['spaces3'] = list_prob[i]['length'] - len(str(list_prob[i]['answer'])) 
      
    arranged_problems += "\n"

    for i in range(len(list_prob)):
      arranged_problems += " "*list_prob[i]['spaces3'] + str(list_prob[i]['answer'])

      if i != len(list_prob) - 1:
        arranged_problems += " "*4
      
  return arranged_problems