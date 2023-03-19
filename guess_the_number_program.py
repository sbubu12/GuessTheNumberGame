# 概要
# ユーザが数値を入力
# プログラムは n と m の範囲 (含む) で乱数を生成
# ユーザーは正しい数字を当てるまで、繰り返し数字を入力
# 与えられた範囲内の乱数を生成するには、random モジュールと randint 関数を使用
# ユーザが試行できる回数を n 回に制限して、最大 n ループの for ループで行う

import sys
import random

trycount = 3
sys.stdout.buffer.write(b'Enter a Min number\n')
sys.stdout.flush()
min = int(sys.stdin.buffer.readline())
sys.stdout.buffer.write(b'Enter a Max number\n')
sys.stdout.flush()
max = int(sys.stdin.buffer.readline())

sys.stdout.buffer.write(b'I have generated a random number between min and max.\n Guess What it is. You have 3 tries.\n')
randumNumber = random.randint(min,max)
# sys.stdout.buffer.write(str(randumNumber).encode()) # 整数を文字列に変換し、さらにバイト列に変換
sys.stdout.flush()

for i in range(0,trycount):
    inputnumber = int(sys.stdin.buffer.readline())
    if(inputnumber == randumNumber):
        sys.stdout.buffer.write(b'Correct!\n')
        break
    else:
        sys.stdout.buffer.write(b'Enter again!\n')

sys.stdout.buffer.write(b'try once again\n')