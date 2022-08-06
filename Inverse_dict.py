









from collections import defaultdict 

def collect_dictionary(obj):

  inv_obj = defaultdict(list)

  for key, value in obj.items():

    inv_obj[value].append(key)

  return dict(inv_obj)

Example:

ages = {

  'Peter': 10,

  'Isabel': 10,

  'Anna': 9,

}

collect_dictionary(ages)  

Output: { 10: ['Peter', 'Isabel'], 9: ['Anna'] }



