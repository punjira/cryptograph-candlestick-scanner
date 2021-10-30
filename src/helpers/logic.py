import sys
import os
import json
import numpy as np

from redisClient import redisInterface
from talibHelpers import *

rd = redisInterface("history-redis-python-replica",6379)
# rd = redisInterface("localhost",6380)

def convertToArray(opens,highs,lows,closes):
    return [
        np.array(opens, dtype="float64"),
        np.array(highs, dtype="float64"),
        np.array(lows, dtype="float64"),
        np.array(closes, dtype="float64"),
    ]

def routine(hashkey):
    candles = rd.getCandles(hashkey)
    if candles != None:
        close = []
        open = []
        high = []
        low = []
        date = []
        sortedDict = dict(sorted(candles.items()))
        for i in sortedDict:
            close.append(eval(sortedDict[i])[4])
            open.append(eval(sortedDict[i])[1])
            high.append(eval(sortedDict[i])[2])
            low.append(eval(sortedDict[i])[3])
            date.append(eval(sortedDict[i])[0])
        ### talib expects numpy standard array
        npar = convertToArray(open,high,low,close)
        bulls = scanBullishPatterns(npar[0],npar[1],npar[2],npar[3],hashkey, date)
        bears = scanBearishPatterns(npar[0],npar[1],npar[2],npar[3],hashkey, date)
        merged = bulls + bears
        return [x for x in merged if x is not None]
        
        

def scanBullishPatterns(o,h,l,c, hashkey, date):
    publishables = []
    publishables.append(createResultObject(date,hammer(o,h,l,c),"hammer",hashkey,100,1))
    publishables.append(createResultObject(date,morning_star(o,h,l,c),"morning_star",hashkey,100,1))
    publishables.append(createResultObject(date,morning_doji_star(o,h,l,c),"morning_doji_star",hashkey,100,1))
    publishables.append(createResultObject(date,inverted_hammer(o,h,l,c),"inverted_hammer",hashkey,100,1))
    publishables.append(createResultObject(date,piercing_pattern(o,h,l,c), "piercing_line",hashkey,100,1))
    publishables.append(createResultObject(date,harami_pattern(o,h,l,c), "harami", hashkey,100, 1))
    publishables.append(createResultObject(date,harami_cross_pattern(o,h,l,c),"harami_cross",hashkey,100, 1))
    publishables.append(createResultObject(date,engulfing_pattern(o,h,l,c),"engulfing", hashkey, 100, 1))
    return [x for x in publishables if x is not None]

def scanBearishPatterns(o,h,l,c, hashkey, date):
    publishables = []
    publishables.append(createResultObject(date, shooting_star(o,h,l,c), "shooting_star", hashkey, 100, -1))
    publishables.append(createResultObject(date, evening_star(o,h,l,c), "evening_star", hashkey, 100, -1))
    publishables.append(createResultObject(date, evening_doji_star(o,h,l,c), "evening_doji_star", hashkey, 100, -1))
    publishables.append(createResultObject(date, hanging_man(o,h,l,c), "hanging_man", hashkey, 100, -1))
    publishables.append(createResultObject(date, dark_cloud_cover(o,h,l,c), "dark_cloud_cover", hashkey, 100, -1))
    publishables.append(createResultObject(date, engulfing_pattern(o,h,l,c), "engulfing", hashkey, -100, -1))
    publishables.append(createResultObject(date, harami_pattern(o,h,l,c), "harami", hashkey, -100, -1))
    publishables.append(createResultObject(date, harami_cross_pattern(o,h,l,c), "harami_cross", hashkey, -100, -1))
    return [x for x in publishables if x is not None]

def createResultObject(date, data, pattern, hash, compare_, direction=0):
    non_z = np.where(data==compare_)
    if(len(non_z[0])):
        return {
            'key': hash,
            "pattern": pattern,
            "location": date[non_z[0][len(non_z[0])-1]],
            "interval": hash.split("-")[1],
            "direction": direction
        }
    else:
        return