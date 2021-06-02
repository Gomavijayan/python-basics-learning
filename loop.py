
list = ["goma", "kayal", "christi", "vish"]

def loop(x):
  print(x*4)

loop(list)

def map_simple(crazy,list):
    for items in list:
        crazy(items)

map_simple(loop,list)