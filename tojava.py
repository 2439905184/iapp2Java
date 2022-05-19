#只转译函数名和函数参数 不转译函数体定义

def head_to_java(syntax_data:dict):
    function_name = syntax_data['function_name']
    function_params = syntax_data['function_params']
    
    if function_name == "cls":
        params = len(function_params)
        useage = "" #cls的重载方法
        if params == 2:
            useage = "getClass"
        elif params == 3:
            useage = "getClassFromJar"
        
        if useage == "getClass":
            class_name = function_params[0]
            return_var = function_params[1]
            java_code = "Class " + return_var + " = " + "getClass().forName(" + class_name +");"
        elif useage == "getClassFromJar":
            pass
        return java_code

    if function_name == "java":
        return_var = function_params[0]
        class_name = function_params[1]
        method = function_params[2]
        param_type = function_params[3]
        param_data = function_params[4]

        #处理一下完整类名
        pre_syntax_method = method.split(".")
        pre_syntax_method_name_index = len(pre_syntax_method)-1
        
        method_str = pre_syntax_method[pre_syntax_method_name_index]
        if return_var != "null":
            java_code = return_var + " = " + class_name +"." + method_str.strip('"') + "(" +param_data + ");" #去除双引号
        else:
            java_code = class_name +"." + method_str.strip('"') + "(" +param_data + ");" #去除双引号
        #print(java_code)
        return java_code
    pass