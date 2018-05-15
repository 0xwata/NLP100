# -*- coding: utf-8 -*-

class Solution():
    def __init__(self,word1, word2):
        self.a = word1
        self.b = word2
    def __call__(self):
        answer = ""
        print(self.a)
        print(self.b)
        for i in range(4):
            answer += self.a[i]
            answer += self.b[i]
        print(answer)
def main():
    a = Solution('パトカー', 'タクシー')
    a()

if __name__ == '__main__':
    main()
