import random


def roll_dice(face_num: int, amount: int):
  ret = [random.randint(1, face_num) for _ in range(amount)]
  return "[{0}] => {1}".format(', '.join(map(str, ret)), sum(ret))
