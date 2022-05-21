#只转译函数名和函数参数 不转译函数体定义
import IntentFlags
#将完整类名和方法名转换为简单方法名
def to_simpleMethod(full_method:str):
    syntax1 = full_method.split(".")
    index = len(syntax1)-1
    simple_name = syntax1[index]
    return simple_name

#从三开始的奇数为实参 当出现多个参数时，取实参操作
def get_real_params(tokenzier_params):
    real_params = []
    for index,name in enumerate(tokenzier_params):
        if index %2 == 1 and index !=1:
            #print(name)
            real_params.append(name)
    return real_params
#从三开始的偶数为实参 当出现多个参数时，取实参操作
def get_oushu_real_params(tokenzier_params):
    real_params = []
    for index,name in enumerate(tokenzier_params):
        if index %2 == 0 and index !=0 and index !=2:
            #print(name)
            real_params.append(name)
    return real_params

def head_to_java(syntax_data:dict):
    function_name = syntax_data['function_name']
    function_params = syntax_data['function_params']

    if function_name == "cls":
        params = len(function_params)
        useage = ""
        if params == 2:
            useage = "getClass"
        elif params == 3:
            useage = "getClassFromJar"
        
        if useage == "getClass":
            class_name = function_params[0]
            return_var = function_params[1]
            syntax1 = "Class " + return_var + " = "
            syntax2 = "getClass().forName(" + class_name +")"
            java_code =  syntax1 + syntax2 + ";"

        elif useage == "getClassFromJar":
            return_var = function_params[2]
            class_name = function_params[1]
            syntax1 = "Class " + return_var + " = "
            syntax2 = "getClass().forName(" + class_name +")"
            java_code = syntax1 + syntax2 + ";"

        return java_code

    #java(赋值变量, 类, "完整类名和方法名")
    #java(赋值变量, 类, "完整类名和方法名", "参数类型", "参数")
    if function_name == "java":
        params = len(function_params)
        return_var = function_params[0]
        class_name = function_params[1]
        method = function_params[2]
        if params == 3:
            simple_name = to_simpleMethod(method.strip('""'))
            syntax1 = return_var + " = "
            syntax2 =  class_name + "." + simple_name +"()"
            java_code = syntax1 + syntax2 + ";"

        if params == 5:
            param_type = function_params[3]
            param_data = function_params[4]
            if return_var.strip('""') != "null":
                simple_name = to_simpleMethod(method.strip('"'))
                syntax_class = class_name
                syntax_var = class_name + " " + return_var + " = " 
                syntax_body = class_name + "." + simple_name + "(" + param_data +")"
                java_code = syntax_var + syntax_body + ";"
            else:
                simple_name = to_simpleMethod(method.strip('"'))
                syntax = class_name + "." + simple_name + "()"
                java_code = syntax + ";"

        if params > 5:
            syntax_var = class_name  + " " + return_var + " = "
            syntax_method = class_name + "." + to_simpleMethod(method.strip('""'))
            names = get_oushu_real_params(function_params)
            syntax_body = "(" + ','.join(names) + ")"
            java_code = syntax_var + syntax_method + syntax_body + ";"
        return java_code

    #javanew(赋值变量, 类型)
    #javanew(赋值变量, "完整类名和方法名", "参数类型", "参数")
    if function_name == "javanew":
        params = len(function_params)
        return_var = function_params[0]
        raw_return_var = function_params[1]
        if params == 2:
            syntax1 = return_var + " = new "
            syntax2 = raw_return_var + "()"
            java_code = syntax1 + syntax2 + ";"

        if params == 4:
            param_type = function_params[2]
            param_data = function_params[3]
            class_name = to_simpleMethod(raw_return_var.strip('""'))
            syntax_var = class_name + " " + return_var + " = "
            syntax_body = "new " + class_name + "(" + param_data + ")"
            java_code = syntax_var + syntax_body + ";"

        if params > 4:
            syntax_class = to_simpleMethod(raw_return_var.strip('""'))
            syntax_var = syntax_class + " " + return_var + " = "
            names = get_real_params(function_params)
            syntax_body = "new " + to_simpleMethod(syntax_class) + "(" + ','.join(names) + ")"
            java_code = syntax_var  + syntax_body + ";"

        return java_code

    if function_name == "syso":
        param_data  = function_params[0]
        java_code = "System.out.println(" + param_data + ");"
        return java_code

    if function_name == "tw":
        param_data = function_params[0]
        java_code = "Toast.makeText(this," + param_data + ",Toast.LENGTH_SHORT)"+".show();"
        return java_code

    #sit(赋值变量, "方法","属性值")
    #sit对应Intent类 可用方法：setAction(),setType(String type),putExtra(String,CharSequence)
    if function_name == "sit":
        return_var = function_params[0]
        prop_flag = function_params[1].strip('""')
        param_data = function_params[2]

        pre_code = "Intent " + return_var + " = new Intent();\n"
        if len(function_params) == 4:
            param_data2 = function_params[3]
            #java_code = "判断长度为4" + ";"

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
        
        if prop_flag == "classname":
            param_flag = "setClassName"
            syntax_class = "Intent"
            syntax_var = syntax_class + " " + return_var + " = "
            syntax_body = return_var + "." +  param_flag + "(" + param_data + "," + param_data2 + ")"
            java_code = syntax_var  + syntax_body+ ";"

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
    
    #访问java变量 javags(赋值变量, new的java对象, .前面的类, "变量名")
    #访问静态java变量 javags(赋值变量, null , .前面的类, "变量名")
    if function_name == "javags":
        return_var = function_params[0]
        param1 = function_params[1]
        param_class = function_params[2]
        param_var = function_params[3].strip('""')
        if param1 != "null":
            visit_type = "NotStatic"
        else:
            visit_type = "Static"
        
        if visit_type == "Static":
            syntax1 = return_var + " = "
            syntax2 = param_class + "." + param_var + ";"
            java_code = syntax1 + syntax2
        if visit_type == "NotStatic":
            syntax1 = return_var + " = "
            syntax2 = param1 + "." + param_var + ";"
            java_code = syntax1 + syntax2
        return java_code
        
    #修改java变量值 javass(赋值变量，new出来的java对象，类，"变量名称"，"变量值")
    if function_name == "javass":
        return_var = function_params[0]
        object_name = function_params[1]
        class_name = function_params[2]
        param_var = function_params[3].strip('""')
        param_var_value = function_params[4]
        syntax1 = class_name + " " + return_var + " = "
        syntax2 = object_name + "." + param_var + " = " + str(param_var_value)
        java_code = syntax1 + syntax2 + ";"
        print(param_var_value)
        return java_code
    else:
        return "暂时不支持的函数,iyu分词码:"+ str(function_name) + str(function_params) + ";"