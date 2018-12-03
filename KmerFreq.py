from test import kmercount
from test import numofruns
#from test import hamlist
import matplotlib.pyplot as plt
import numpy as np
import math

#numofruns = 4


def hash2kmer(hashkey, k):
    """
    hashkey: hash key of kmer, numpy, 'uint32'
    k: length of kmer
    """
    base = np.array('ACGT', 'c')
    arr = np.chararray(k)
    mask = 0b11

    arr[-1]=base[ mask & hashkey]
    for i in range(2,k+1):
        hashkey = (hashkey>>2)
        arr[-i]=base[mask & hashkey]

    return arr.tostring().decode("utf-8")

"""
#test data to save input from "test.py" file
kmercount = [{},{4: {200: 113, 220: 98, 242: 51, 114: 49, 50: 35, 115: 34, 112: 33, 113: 33, 178: 32, 203: 29, 206: 24, 202: 23, 188: 22, 252: 22, 162: 20, 47: 20, 174: 20, 171: 20, 175: 20, 168: 19, 60: 19, 44: 19, 201: 19, 80: 19, 140: 18, 37: 18, 207: 18, 204: 18, 192: 18, 27: 18, 227: 18, 63: 18, 5: 18, 205: 18, 236: 18, 42: 17, 3: 17, 107: 17, 38: 17, 190: 17, 198: 17, 170: 17, 65: 17, 58: 17, 195: 17, 234: 16, 46: 16, 148: 16, 82: 16, 239: 16, 84: 16, 71: 16, 51: 16, 12: 15, 185: 15, 41: 15, 149: 15, 139: 15, 250: 15, 59: 15, 81: 15, 76: 15, 20: 15, 143: 14, 64: 14, 9: 14, 172: 14, 196: 14, 15: 14, 186: 14, 85: 14, 248: 14, 164: 14, 68: 14, 36: 14, 194: 13, 111: 13, 156: 13, 191: 13, 2: 13, 56: 13, 108: 13, 14: 13, 243: 13, 193: 13, 106: 13, 83: 13, 154: 13, 218: 13, 73: 13, 246: 12, 40: 12, 245: 12, 215: 12, 226: 12, 45: 12, 124: 12, 75: 12, 163: 12, 16: 12, 6: 12, 25: 12, 224: 12, 92: 12, 233: 12, 62: 12, 138: 12, 235: 12, 43: 12, 145: 12, 147: 12, 13: 12, 53: 12, 159: 12, 29: 12, 119: 12, 231: 12, 212: 12, 70: 12, 0: 12, 61: 12, 213: 12, 8: 11, 189: 11, 208: 11, 90: 11, 103: 11, 253: 11, 183: 11, 184: 11, 57: 11, 67: 11, 28: 11, 66: 11, 101: 11, 99: 11, 131: 11, 55: 11, 26: 11, 167: 11, 247: 11, 78: 11, 7: 11, 31: 11, 126: 11, 182: 11, 109: 10, 150: 10, 228: 10, 10: 10, 165: 10, 86: 10, 32: 10, 94: 10, 142: 10, 240: 10, 251: 10, 199: 10, 116: 10, 1: 10, 39: 10, 152: 10, 4: 10, 117: 10, 34: 10, 255: 10, 17: 10, 97: 10, 136: 9, 74: 9, 130: 9, 120: 9, 18: 9, 122: 9, 238: 9, 134: 9, 157: 9},
5: {882: 43, 968: 40, 883: 34, 880: 31, 456: 31, 200: 28, 712: 26, 881: 26, 459: 18, 462: 15, 242: 14, 562: 13, 754: 13, 457: 13, 50: 12, 498: 12, 1010: 12, 451: 12, 463: 11, 690: 11, 448: 11, 454: 11, 178: 11, 810: 10, 815: 10, 818: 10, 370: 10, 461: 10, 458: 10, 674: 9, 812: 9, 806: 9, 452: 9, 826: 9, 449: 9, 434: 9, 908: 9, 697: 8, 828: 8, 956: 8, 65: 8, 149: 8, 748: 8, 809: 8, 821: 8, 814: 8, 687: 8, 306: 8, 700: 8, 329: 8, 827: 8, 12: 7, 37: 7, 795: 7, 252: 7, 1008: 7, 771: 7, 108: 7, 455: 7, 773: 7, 580: 7}},
{4: {200: 150, 220: 125, 242: 75, 114: 49, 50: 35, 115: 34, 112: 33, 113: 33, 178: 32, 203: 29, 206: 24, 202: 23, 188: 22, 252: 22, 162: 20, 47: 20, 174: 20, 171: 20, 175: 20, 168: 19, 60: 19, 44: 19, 201: 19, 80: 19, 140: 18, 37: 18, 207: 18, 204: 18, 192: 18, 27: 18, 227: 18, 63: 18, 5: 18, 205: 18, 236: 18, 42: 17, 3: 17, 107: 17, 38: 17, 190: 17, 198: 17, 170: 17, 65: 17, 58: 17, 195: 17, 234: 16, 46: 16, 148: 16, 82: 16, 239: 16, 84: 16, 71: 16, 51: 16, 12: 15, 185: 15, 41: 15, 149: 15, 139: 15, 250: 15}, 5: {882: 46}}]
"""


def makexaxis():
    xaxis = ([])
    for i in range(numofruns):
        xaxis.append(i)
    return xaxis

def makeyaxis(i, k):
    yaxis = ([])
    for l in range(1, (len(kmercount))):
        total = sum(kmercount[l][k].values())
        if i in kmercount[l][k]:
            num =  kmercount[l][k][i]
            f = num/total
            freq = (f/(1-f))
            yaxis.append(math.log10(freq))
    return yaxis



def graphyboy(k):
    #graph = plt.subplots(1,1)
    plt.xlabel("SELEX round")
    plt.ylabel("Kmer count")
    plt.title("Kmer frequency")
    for l in range(1, len(kmercount)):
        for i in kmercount[l][k]:
            try:
                plt.plot(makexaxis(), makeyaxis(i,k), label = str(hash2kmer(i,k)))
            except:
                continue
    plt.show()


graphyboy(4)
