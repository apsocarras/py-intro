
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



#     A function called zipper() that takes two lists as arguments
#         If the lists are the same length:
#             return a dictionary that has the items of the first list as keys, and each item in the same index in the second list as the value > For instance, the lists ["vanilla", "cherry"] and ["cake", "ice_cream"] would return {"vanilla": "cake", "cherry": "ice_cream"}
#         If the lists are different lengths:
#             return a tuple with each list and its length > For instance, the lists ["vanilla", "cherry", "pistachio"] and ["cake", "ice_cream"] would return (["vanilla", "cherry", "pistachio"], 3, ["cake", "ice_cream"], 4)

