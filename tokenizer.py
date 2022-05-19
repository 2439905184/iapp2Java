import re
#此代码中的regex是正则表达式的意思
#java(赋值变量, 类, "完整类名和方法名", "参数")

#先切割括号，再切割参数
def split_head(param_str:str):
    regex_QuKuoHao = r"\(|\)"
    pre_syntax = re.split(regex_QuKuoHao, param_str)
    
    function_name = pre_syntax[0]
    pre_syntax_params = pre_syntax[1]
    
    pre_syntax_params2 = pre_syntax_params.replace(r",", " ")#这一个步骤是用来处理多余空格的
    function_params = re.split(r"[ ]+", pre_syntax_params2)#这一个步骤是用来处理多余空格的
    
    result = {}
    result['function_name'] = function_name
    result['function_params'] = function_params
    
    return result

# a = split_function(test_str)
# print(type(a))