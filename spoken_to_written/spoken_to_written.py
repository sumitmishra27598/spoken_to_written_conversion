from spoken_to_written import conversion_rule as cr
def spoken_2_written(para):
  rules = cr.coversion_rules()
  
  #lower case of all words in paragraph annd making word list.
  words = para.lower().split()
  
  #conversion for rule type number i.e. from five to 5
  for index,word in enumerate(words):
    if word in rules['numbers'].keys():
      words[index] = str(rules['numbers'][word])
      
  #conversion for rule type currency i.e. from dollar to $
  for index,word in enumerate(words):
    if word in rules['currency'].keys():
      if words[index-1].isdigit():
        words[index] = str(words[index-1]+rules['currency'][word])
        del words[index-1]
      else:
        str(rules['currency'][word])
        
  #conversion for rule type multi and others i.e. from triple a to aaa and c m to cm
  for index,word in enumerate(words):
    if index < len(words)-1:
      if word in rules['multi'].keys() and len(words[index+1])==1:
        words[index] = rules['multi'][word] * words[index+1]
        del words[index+1]
      if words[index]+' '+words[index+1] in rules['others'].keys():
        words[index] = rules['others'][words[index]+' '+words[index+1]]
        del words[index+1]
  return " ".join(words)
