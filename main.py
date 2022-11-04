
def list_sayer(ls:list):
  if len(ls) > 0: # Since non-empty lists are truthy and empty lists are falsey, we could also write 'if ls:'
    for i in range(len(ls)):
      print(f"Name: {ls[i]}, Index: {i}")
    return True
  else: 
    print("The list is empty.")
    return False

def dict_sayer(d:dict): 
  if len(d) > 0: # Empty dictionaries are falsey and non-empty dictionaries truthy, so we could also write 'if d:' 
    for key, value in d.items():
      print(f"Key name: {key}, Value: {value}")
    return True
  else:
    print("The dictionary is empty")
    return False

def greatest(d:dict):
   # Note that there could be multiple entries in the dict sharing the "greatest value"
  max_val = max(d.values())
  # Because this list comprehension produces a set, which is unordered, the order of the keys might be changed: 
  matching_keys = list({key for key in d if d[key] == max_val}) 
  # Hence, matching_keys[0] might not be the first key listed in the dictionary that has the greatest value 
  return (max_val, matching_keys[0])

def zipper(l1:list, l2:list):
  if len(l1) == len(l2):
    out_dict = {}
    for i in range(len(l1)):
      out_dict[l1[i]] = l2[i]
    return(out_dict)
  else: 
    return (l1, len(l1), l2, len(l2))
