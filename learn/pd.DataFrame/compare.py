import pandas as pd


d = {
    'a': [1,2,None],
    'b': [10,None,30],
}

data = pd.DataFrame(d)

print(data)
print(data.compare(other=pd.DataFrame({'a': [10,20,30],'b': [1.1,1.2,1.3]}),
                   result_names=("data", "other")))