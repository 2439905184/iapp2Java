## iapp2java 裕语言转java编译器
可以将裕语言编译成java代码，方便开发者学习编程
## 亮点
<ol>
<li>目前只支持函数调用的转译 如 java(a,b,c,d,e) 不支持函数定义的转译如 java(aaa) { }
</li>
</ol>

## 如何使用
* 安装python >=3
* git clone https://github.com/2439905184/iapp2Java.git
* 命令行调用方式 python compile.py "iyu源文件" "输出文件.java")
* 主程序交互式调用方式 python Main.py

## 例子
test.iyu源码文件
```java
cls("String", c)
javax(a,"123456789",c,"indexOf","String","56")
syso(a)
```
编译
```
python compile.py "test.iyu"  "out.java"
```
编译后的内容
```java
Class c = getClass().forName("String");
暂时不支持的函数,iyu分词码:javax['a', '"123456789"', 'c', '"indexOf"', '"String"', '"56"'];
System.out.println(a);

```

## 如何二次开发
* 如果要支持更多的裕语言函数调用转译，请修改tojava.py文件，添加新的处理代码
* tokenizer.py是进行编译前的词法分析器（目前仅支持函数头的分词处理 如: a(1,2,3,4)  )

## 代码著作权归属
* 原始副本归我（小沙盒工作室创始人所有）
* 你可以自由修改代码，但是二次分发时需注明出处。禁止将修改后的代码用于商业用途
* 根据GPL协议，二次修改的代码再分发时，必须开源，否则视为自动弃权免费开源协议，且行为恶劣者将不提供额外的技术支持。
