
# Do we need all nine of these for every input?
# import activity.io # v.3
# import character.io # v.1
# import disease.io # v.3
# import helloworld.io # v.1
# import math.io # v.3
# import model.io # v.2
# import room.io # v.4
# import setting.io # v.1
# import state.io # v.5


GUIDEWORD = 'OBFUSCATED'
GRID = [
    'QWURAHIZEDDBRPPSWKETXWJDOV',
    'CQUNLCQMFHGYCGBAOCEXGYKFSZ',
    'MLQNKADCDNVJSNDXROCLDFASYB',
    'SHKHRKFXURYLSYPTSZSPSEJPZT',
    'HUMPKUFVOKABKBYGWEYVBVTWKH',
    'NRLNVLIOUNWLOIADZURRSTETXA',
    'OIIFYSXMYRASSQKYXYARKBJYZP',
    'PALOYQRLSYNZFDTTGZXYFTEPJV',
    'LXISNBLLHSYQZQXJODDBYCNWVX',
    'FGQZDLWFVTJMKTEUXTOLACGIJX',
    'PDXGAPXQXEHIJHTIEGRUPSESIZ',
    'XIHYEPKSUDIBATPQROLWLFOMJR',
    'HHIAAAUFGZFTSNPLLOFEHQUAXC',
    'LCCXJATDVBMULFYEQTPYRKXTNC',
    'CRIPGUMKOTGPTTWNOHYYIYPZRZ',
    'LTIGZNEWUTPHSDRGRDMUAJGJDT',
    'EDXOVHEQZFLZHTTPGFRSVZKIOG',
    'YTVJGJXFDIONZRBIHWIIEBIICL',
    'HZFDFZUKFXRXHGPDWRQBFTXMHO',
    'AYEAZZUADRBAWCDLVJNGGDGIRQ',
    'PGZSJWAUCFZXNIJGNPPNNLPBOT',
    'SKSXBWEVYBWUPONJSEFKSGTRFL',
    'QEOPYFIHUHCJAAMPQPLORAMPHX',
    'WRZRSZNJJUUDXGPZBAUTDKMWTK',
    'WTFTIPYHKIQOWKSIDHSZESVKTT',
    'JZWMRFLHQKDFTMUENPQBRFSBCJ'
]


def main():
    inp = int(input('Enter a number 0-8'))
    x = ord(GUIDEWORD[inp]) - 65
    y = ord(GUIDEWORD[inp + 1]) - 65
    word = ''
    while GRID[x][y] != 'X':
        word += GRID[x][y]
        temp = y
        y = (x + 6) % 26
        x = (temp + 14) % 26
    print(word)

# Be sure to consider the import version when evaluating export


if __name__ == '__main__':
    main()
