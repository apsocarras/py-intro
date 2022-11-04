
def list_sayer(ls:list):
  if len(ls) > 0: 
    for i in range(len(ls)):
      print(f"Name: {ls[i]}, Index: {i}")
    return True
  else: 
    print("The list is empty.")
    return False

def dict_sayer(d:dict): 
  if len(d) > 0:
    for key, value in d.items():
      print(f"Key name: {key}, Value: {value}")
    return True
  else:
    print("The dictionary is empty")
    return False

def greatest(d:dict):
  max_val = max(d.values())
  matching_keys = list({key for key in d if d[key] == max_val}) 
  return (max_val, matching_keys[0])

def zipper(l1:list, l2:list):
  if len(l1) == len(l2):
    out_dict = {}
    for i in range(len(l1)):
      out_dict[l1[i]] = l2[i]
    return(out_dict)
  else: 
    return (l1, len(l1), l2, len(l2))
