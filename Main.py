import tokenizer
import tojava
#api参考
#javanew(赋值变量, "完整类名和方法名", "参数类型", "参数")
#javax(赋值变量, "参数", "第二个实参的类型", "方法名", "方法参数类型", "方法参数")
#uit(Intent类型 sit变量,"chooser","标题")
#javanew(赋值变量, new的类型, 构造参数类型, 构造参数)
code = 'java(b,a,"android.widget.TextView.setText","CharSequence","我是文本")'
code2 = 'cls("String",b)'
code3 = 'javanew(a,"java.lang.StringBuilder" ,"String","12345")'

def interactive(code:str):
    head_data = tokenizer.split_head(code)
    data = tojava.head_to_java(head_data)
    print(head_data)
    print("生成的代码:")
    print(data)
    pass

def main():
    print("欢迎使用iapp2java编译器，请选择你要使用的模式")
    print("此版本目前只支持函数调用的转译，不支持函数定义的转义\n 如java(){}")
    print("1.交互式编译模式")
    print("2.单文件编译模式")
    user = input()
    if user == "1":
        while True:
            iyu = input("请输入裕语言代码\n")
            interactive(iyu)
    if user == "2":
        file_name = input("请输入iyu文件名称\n")
        iyu_file = open(file_name, "r")
        out_file = open("out.java","w",encoding="utf-8")
        for line in iyu_file.readlines():
            syntax_data = tokenizer.split_head(line)
            out_line = tojava.head_to_java(syntax_data)
            print("每行输出:"+str(out_line))
            out_file.write(str(out_line) + "\n")
        iyu_file.close()
    pass

main()
