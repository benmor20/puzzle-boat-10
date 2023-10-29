
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

# The versions from the imports, in order
IMPORTS = {
    'ACTIVITY': 3,
    'CHARACTER': 1,
    'DISEASE': 3,
    'HELLOWORLD': 1,
    'MATH': 3,
    'MODEL': 2,
    'ROOM': 4,
    'SETTING': 1,
    'STATE': 5,
}


def main():
    words = []
    for inp in range(9):
        x = ord(GUIDEWORD[inp]) - 65
        y = ord(GUIDEWORD[inp + 1]) - 65
        word = ''
        while GRID[x][y] != 'X':
            word += GRID[x][y]
            temp = y
            y = (x + 6) % 26
            x = (temp + 14) % 26
        print(f'{inp}: {word}')
        words.append(word)

# Be sure to consider the import version when evaluating export


if __name__ == '__main__':
    main()
