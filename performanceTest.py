from cleverminer import cleverminer
import timeit
import pandas as pd
import math
from miar.measures import yule_y

df = pd.read_csv('Airlines.csv')
clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':2000, 'aad':0.4},
                  ante ={
                      'attributes':[
                          {'name': 'Airline', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
                          {'name': 'DayOfWeek', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
                      ], 'minlen':1, 'maxlen':3, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'Delay', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
                      ], 'minlen':1, 'maxlen':3, 'type':'con'}
                  )

def my_function():
    for i in (range(clm.get_rulecount())):
        rule_id = i+1
        arr = clm.get_fourfold(rule_id)
        krit = yule_y(arr)
        #if krit > 0.1:
            #print(f"Rule {rule_id}: {clm.get_ruletext(rule_id)} krit:{krit}")

def raw_code():
    for i in (range(clm.get_rulecount())):
        rule_id = i+1
        arr = clm.get_fourfold(rule_id)
        krit = (math.sqrt((arr[0]/sum(arr)) * (arr[3]/sum(arr))) - math.sqrt((arr[1]/sum(arr)) * (arr[2]/sum(arr)))) / (math.sqrt((arr[0]/sum(arr)) * (arr[3]/sum(arr))) + math.sqrt((arr[1]/sum(arr)) * (arr[2]/sum(arr))))
        #if krit > 0.1:
            #print(f"Rule {rule_id}: {clm.get_ruletext(rule_id)} krit:{krit}")


setup_code = "from miar.measures import yule_y"

time_func = timeit.repeat(my_function, setup=setup_code, number=10000000, repeat=5)
time_raw = timeit.repeat(raw_code, number=10000000, repeat=5)

print(f"Using function:{time_func} seconds")
print(f"Raw code:{time_raw} seconds")
