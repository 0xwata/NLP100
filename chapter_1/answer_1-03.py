# -*- coding: utf-8 -*-
import re

class Solution():
    def __init__(self,x):
        self.a = x
    def __call__(self):
        answer = []
        #splitには正規表現を用いた
        pre = filter(lambda x: len(x) > 0, re.split(r'\s|"|,|\.', self.a)) #フィルター関数はリストやタプルの要素のうち関数を適用した結果が Trueとなるもののみイテレータを返す
        for i in pre:
            #$rint(len(i))
            answer.append(len(i))
        print(answer)
def main():
    sentence ='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
    a = Solution(sentence)
    a()

if __name__ == '__main__':
    main()
