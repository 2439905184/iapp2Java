rem 打包pyz应用 zipapp
python -m py_compile __main__.py
python -m py_compile compile.py
python -m py_compile func_fr.py
python -m py_compile IntentFlags.py
python -m py_compile tokenizer.py
python -m py_compile tojava.py

cd __pycache__
rename __main__.cpython-38.pyc __main__.pyc
rename compile.cpython-38.pyc compile.pyc
rename func_fr.cpython-38.pyc func_fr.pyc
rename IntentFlags.cpython-38.pyc IntentFlags.pyc
rename tojava.cpython-38.pyc tojava.pyc
rename tokenizer.cpython-38.pyc tokenizer.pyc
rename writejava.cpython-38.pyc writejava.pyc

7z a compile.zip __main__.pyc compile.pyc func_fr.pyc IntentFlags.pyc tojava.pyc tokenizer.pyc writejava.pyc

move compile.zip ../dist/compile.zip