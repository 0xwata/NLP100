# -*- coding: utf-8 -*-
import re

class Solution():
    def __init__(self,x):
        self.a = x
    def __call__(self):
        keys = []
        value = []
        i = 0
        #splitには正規表現を用いた
        pre = filter(lambda x: len(x) > 0, re.split(r'\s|"|,|\.', self.a)) #フィルター関数はリストやタプルの要素のうち関数を適用した結果が Trueとなるもののみイテレータを返す
        for values in pre:
            i += 1
            value.append(values)
            if i==1 or i==5 or i==6 or i==7 or i==8 or i==9 or i==15 or i==16 or i==19:
                keys.append(values[0])
            else:
                keys.append(values[0:2])

        answer = dict(zip(keys, value))
        print(answer)

def main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    a = Solution(sentence)
    a()

if __name__ == '__main__':
    main()
