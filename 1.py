# 8.42 禁止函数修改列表

# 向函数传递列表的副本而不是原件

#列表作为副本传递给函数，在列表后加[:]就可,其实利用了列表切片的原理

function_name(list_name[:])

print_models(unprinted_designs[:], completed_models)

def show_completed(completed_models): 
    for completed_model in completed_models: 
        print("已完成打印：" + completed_model) 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 
print_models(unprinted_designs[:], completed_models) 
show_completed(completed_models)
print(unprinted_designs)
