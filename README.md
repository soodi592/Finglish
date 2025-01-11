# 📖 Farsi-English(Finglish) Python Library
This library is made for iranian people to code better and easier.
I know this library might be useless because its hard to code with this library, but i built this library to get more experience in coding, thanks for reading this.

## ❓ Fn & Finglish?
Fn is the same as Finglish, but an abbreviated version for people who don't like their code to be too big and ugly.

## 📃 Functions
```python
finglish_instance = Finglish()
fn_instance = Fn()
```

inits the library to make it possible to work with data.
```python
finglish_instance.benevis(content)
fn_instance.bn(content)
```

prints the content given to it, content must be either String, Integer, Boolean or Float.

```python
finglish_instance.zakhire_kon(key, value)
fn_instance.zk(key, value)
```

saves the given information as a variable, key is the variable name and value is the value of the variable.
key can't start with an integer, boolean or float.
value must be either String, Integer, Boolean or Float.

```python
finglish_instance.zakhire_bede(key)
fn_instance.zb(key)
```

returns the saved information, key is the saved variable name.

```python
finglish_instance.agar(condition, action)
fn_instance.ag(condition, action)
```

works like the "if" in normall python, if condition is true, does the action, else, does nothing.

```python
finglish_instance.reshte_kon(content)
fn_instance.rk(content)
```

returns string type of the content.

```python
finglish_instance.adad_kon(content)
fn_instance.ak(content)
```

returns integer type of the content.

```python
finglish_instance.boolean_kon(content)
fn_instance.bk(content)
```

returns boolean type of the content.

```python
finglish_instance.shenavar_kon(content)
fn_instance.sk(content)
```

returns float type of the content.
