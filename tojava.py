#只转译函数名和函数参数 不转译函数体定义
import IntentFlags
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
    
    if function_name == "javanew":
        return_var = function_params[0]
        raw_return_var = function_params[1]
        
        #处理一下完整类名
        pre_syntax_type = raw_return_var.split(".")
        pre_syntax_type_index = len(pre_syntax_type)-1
        
        return_var_type = pre_syntax_type[pre_syntax_type_index]

        param_type = function_params[2]
        param_data = function_params[3]
        java_code = return_var_type.strip('""') + " " + return_var + " = new " + return_var_type.strip('""') + "(" + param_data + ");"
        return java_code

    if function_name == "syso":
        param_data  = function_params[0]
        java_code = "System.out.println(" + param_data + ");"
        return java_code

    if function_name == "tw":
        param_data = function_params[0]
        java_code = "Toast.makeText(this," + param_data + ",Toast.LENGTH_SHORT)"+".show();"
        return java_code

    if function_name == "sit":
        return_var = function_params[0]
        prop_flag = function_params[1].strip('""')
        param_data = function_params[2]

        pre_code = "Intent " + return_var + " = new Intent();\n"
        if len(function_params) == 4:
            param_data2 = function_params[3]
        if prop_flag == "action":
            param_flag = "setAction"
            pre_code1 = return_var + "." + param_flag + "(" + param_data +");"
            java_code = pre_code + pre_code1

        if prop_flag == "type":
            param_flag = "setType"
            pre_code1 = return_var + "." + param_flag + "(" + param_data + ");"
            java_code = pre_code + pre_code1

        if prop_flag == "extra":
            param_flag = "putExtra"
            pre_code1 = return_var + "." + param_flag + "(" + param_data + "," + param_data2 + ");"
            java_code = pre_code + pre_code1

        if prop_flag == "flags":
            param_flag = "setFlags"
            if int(param_data) == IntentFlags.FLAG_ACTIVITY_NEW_TASK:
                pre_code1 = return_var + "." + param_flag + "(Intent.FLAG_ACTIVITY_NEW_TASK);"
            else:
                pre_code1 = return_var + "." + param_flag + "(" + param_data + ");"
            java_code = pre_code + pre_code1
        return java_code
    if function_name == "uit":#chooser的情况没加上 startActivityForResult()
        return_var = function_params[0]
        pre_code = "startActivity("
        java_code = pre_code + return_var + ");"
        return java_code

    if function_name == "uigo":
        param_data = function_params[0]
        java_code = 'startActivity(new Intent(this,'+ param_data + '));'
        return java_code

    if function_name == "loadso":
        param_data = function_params[0]
        java_code = "static\n{\n System.loadLibrary(" + param_data + ");\n}"
        return java_code
    
    #javax(赋值变量, "参数", "第二个实参的类型", "方法名", "方法参数类型", "方法参数")
    if function_name == "javax":
        return_var = function_params[0]
        param_data2 = function_params[1]
        param_class = function_params[2]
        param_method = function_params[3].strip('""')
        param_type = function_params[4] #调用方法的参数类型
        param = function_params[5]
        java_code = return_var + " = " + param_class + "." + param_method + "(" + param + ");"
        return java_code
    else:
        return "暂时不支持的函数,iyu分词码:"+ str(function_name) + str(function_params) + ";"