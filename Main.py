import tokenizer
import tojava
#api参考
#java(赋值变量, 类, "完整类名和方法名", "参数类型", "参数")
#javanew(赋值变量, "完整类名和方法名", "参数类型", "参数")

code = 'java(b,a,"android.widget.TextView.setText","CharSequence","我是文本")'
code2 = 'cls("String",b)'
code3 = 'javanew(a,"java.lang.StringBuilder" ,"String","12345")'

head_data = tokenizer.split_head(code3)
data = tojava.head_to_java(head_data)

#print(head_data)
print("生成的代码:")
print(data)
#a = '"a"'
#print(a.strip()+".")