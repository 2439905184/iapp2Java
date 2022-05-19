import tokenizer
import tojava


code = 'java(b,a,"android.widget.TextView.setText","CharSequence","我是文本")'
head_data = tokenizer.split_head(code)
data = tojava.head_to_java(head_data)

print("生成的代码:")
print(data)
#a = '"a"'
#print(a.strip()+".")