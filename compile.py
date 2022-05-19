#python compile.py "iyu源文件" "输出文件.java"
import sys
import tokenizer
import tojava
def main():
    iyu_file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    out_file = open(out_file_name,"w",encoding="utf-8")
    for line in open(iyu_file_name,"r"):
        print(line,end="")
        syntax_data = tokenizer.split_head(line)
        out_line = tojava.head_to_java(syntax_data)
        print("每行输出:"+str(out_line))
        out_file.write(str(out_line)+"\n")
    out_file.close()
    pass
#print("用法 python compile.py iyu源文件 输出文件.java")
main()