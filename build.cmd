mkdir test_compile
rem 注释
python compile.py "iyu_src/shortCut.iyu" "test_compile/shortCut.java"
python compile.py "iyu_src/test.iyu" "test_compile/test.java"
python compile.py "iyu_src/zhushi.iyu" "test_compile/zhushi.java"
python compile.py "iyu_src/manyJava.iyu" "test_compile/manyJava.java"