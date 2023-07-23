from itertools import groupby

NUMS = "Zero One Two Three Four Five Six Seven Eight Nine".split()
NUMS_PLURAL = "Zeros Ones Twos Threes Fours Fives Sixes Sevens Eights Nines".split()

def grouper(seq):
    for num, grp in groupby(seq):
        print(f'{num=}, {grp=}')
        num = int(num)
        length = len(list(grp))
        if length > 1:
            yield f"{NUMS[length]} {NUMS_PLURAL[num]}"
        else:
            yield NUMS[num]




if __name__ == "__main__":
    inp = '2880'
    print(*grouper(inp))