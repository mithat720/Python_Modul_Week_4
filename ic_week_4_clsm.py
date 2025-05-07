from functools import reduce

sayilar = [1, 2, 3, 4]
toplam = reduce(lambda x, y: x + y, sayilar)
ciftler = filter(lambda x: x % 2 == 0, sayilar)
print(list(ciftler))  # [2, 4]
print(toplam)  # 10
ikiler = map(lambda x: x * 2, sayilar)
print(list(ikiler))  # [2, 4, 6, 8]
