#
# Created by Faisal Amir
# FrogoBox Inc License
# -----------------------------------------
# Learning-Python
# Copyright (C) 12/02/2020.      
# All rights reserved
# -----------------------------------------
# Name     : Muhammad Faisal Amir
# E-mail   : faisalamircs@gmail.com
# Github   : github.com/amirisback
# LinkedIn : linkedin.com/in/faisalamircs
# -----------------------------------------
# FrogoBox Software Industries
# 
# /

newLine = "\n"

typeStr = "Hello World"  # str
typeInt = 20  # int
typeFloat = 20.5  # float
typeComplex = 1j  # complex
typeList = ["apple", "banana", "cherry"]  # list
typeTuple = ("apple", "banana", "cherry")  # tuple
typeRange = range(6)  # range
typeDict = {"name": "John", "age": 36}  # dict
typeSet = {"apple", "banana", "cherry"}  # set
typeFrozenSet = frozenset({"apple", "banana", "cherry"})  # frozenset
typeBool = True  # bool
typeBytes = b"Hello"  # bytes
typeByteArray = bytearray(5)  # bytearray
typeMemoryView = memoryview(bytes(5))

specificStr = str("Hello World")  # str
specificInt = int(20)  # int
specificFloat = float(20.5)  # float
specificComplex = complex(1j)  # complex
specificList = list(("apple", "banana", "cherry"))  # list
specificTuple = tuple(("apple", "banana", "cherry"))  # tuple
specificRange = range(6)  # range
specificDict = dict(name="John", age=36)  # dict
specificSet = set(("apple", "banana", "cherry"))  # set
specificFrozenSet = frozenset(("apple", "banana", "cherry"))  # frozenset
specificBool = bool(5)  # bool
specificBytes = bytes(5)  # bytes
specificByteArray = bytearray(5)  # bytearray
specificMemoryView = memoryview(bytes(5))  # memoryview

print(specificStr)
print(specificInt)
print(specificFloat)
print(specificComplex)
print(specificList)
print(specificTuple)
print(specificRange)
print(specificDict)
print(specificSet)
print(specificFrozenSet)
print(specificBool)
print(specificBytes)
print(specificByteArray)
print(specificMemoryView)
print(newLine)
print(type(typeStr))
print(type(typeInt))
print(type(typeFloat))
print(type(typeComplex))
print(type(typeList))
print(type(typeTuple))
print(type(typeRange))
print(type(typeDict))
print(type(typeFrozenSet))
print(type(typeBool))
print(type(typeBytes))
print(type(typeByteArray))
print(type(typeMemoryView))