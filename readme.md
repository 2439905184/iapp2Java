## iapp2java 裕语言转java编译器[![test](https://github.com/2439905184/iapp2Java/actions/workflows/test.yml/badge.svg)](https://github.com/2439905184/iapp2Java/actions/workflows/test.yml)
可以将裕语言编译成java代码，方便开发者学习编程
## 亮点
<ol>
<li>目前只支持函数调用的转译 如 java(a,b,c,d,e) 不支持函数定义的转译如 java(aaa) { }
</li>
</ol>

## 目前支持的裕语言api
* cls()
* java()
* javanew()
* syso()
* tw()
* sit()
* uit()
* uigo()
* loadso()
* javax()
* javags()
* javass()
* 其他更多api敬请期待

## 如何使用
* 安装python >=3
* git clone https://github.com/2439905184/iapp2Java.git
* [源码解释运行](#源码解释运行需要python38)
* [pyz应用程序](#pyz应用程序需要安装python38)
* [exe运行](#源码解释运行需要python38)
## 源码解释运行(需要python3.8)
```
python compile.py "xxx.iyu" "xxx.java"
```
## pyz应用程序（需要安装Python3.8) 
请到release里下载compile.zip
```
python compile.zip "xxx.iyu" "xxx.java"
```
## exe运行 (不需要python)
```
compile.exe "xxx.iyu" "xxx.java"
```
## 编译窗口
```ps
PS D:\work\iapp2Java> python .\compile.py "test.iyu" "out.java"
编译 >>> Class c = getClass().forName("String");
编译 >>> 暂时不支持的函数,iyu分词码:javax['a', '"123456789"', 'c', '"indexOf"', '"String"', '"56"'];
编译 >>> System.out.println(a);
编译 >>> Toast.makeText(this,a,Toast.LENGTH_SHORT).show();
编译 >>> Intent a = new Intent();
a.setAction("android.intent.action.SEND");
编译 >>> Intent a = new Intent();
a.setType("text/plain");
编译 >>> Intent a = new Intent();
a.putExtra("android.intent.extra.SUBJECT","共享软件");
编译 >>> Intent a = new Intent();
a.putExtra("android.intent.extra.Text","共享软件");
编译 >>> Intent b = new Intent();
b.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
编译 >>> startActivity(a);
编译 >>> startActivity(new Intent(this,"abc.iyu"));
编译 >>> static
{
 System.loadLibrary("abc");
}
```
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
## 如何编译
<ol>
<li>pip install pyinstaller</li>
<li>pyinstaller -F compile.py -p tokenizer.py -p tojava.py 或者使用build.cmd编译成exe
</ol>

## 关于预构建的exe版本
默认只有64位的版本，32位的版本请自行编译，或者使用源码解释运行

## 如何二次开发
* 如果要支持更多的裕语言函数调用转译，请修改tojava.py文件，添加新的处理代码
* tokenizer.py是进行编译前的词法分析器（目前仅支持函数头的分词处理 如: a(1,2,3,4)  )

## 代码著作权归属
* 原始副本归我（小沙盒工作室创始人所有）
* 你可以自由修改代码，但是二次分发时需注明出处。禁止将修改后的代码用于商业用途
* 根据GPL协议，二次修改的代码再分发时，必须开源，否则视为自动弃权免费开源协议，且行为恶劣者将不提供额外的技术支持。
