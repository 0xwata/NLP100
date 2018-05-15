# -*- coding: utf-8 -*-

class Solution():
    def __init__(self,word):
        self.a = word
    def __call__(self):
        print(self.a)
        answer = self.a[::-1] #文字列逆順
        print(answer)
def main():
    a = Solution('stressed')
    a()

if __name__ == '__main__':
    main()
