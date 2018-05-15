# -*- coding: utf-8 -*-

class Solution():
    def __init__(self,word):
        self.a = word
    def __call__(self):
        print(self.a)
        answer = self.a[0::2] #偶数番目の要素の取り出し方    
        print(answer)
def main():
    a = Solution('パタトクカシーー')
    a()

if __name__ == '__main__':
    main()
