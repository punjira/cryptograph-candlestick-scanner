import talib

def two_crows(open, high, low, close):
	try:
		data = talib.CDL2CROWS(open,high,low,close)
		return data
	except:
 		return None

def three_black_crows(open, high, low, close):
	try:
		data = talib.CDL3BLACKCROWS(open, high, low, close)
		return data
	except: 
 		return None

def three_inside_up_down(open, hight, low, close):
	try:
		data = talib.CDL3INSIDE(open, hight, low, close)
		return data
	except: 
 		return None

def three_line_strike(open, hight, low, close):
	try:
		data = talib.CDL3LINESTRIKE(open, hight, low, close)
		return data
	except: 
 		return None

def three_outside_up_down(open, hight, low, close):
	try:
		data = talib.CDL3OUTSIDE(open, hight, low, close)
		return data
	except: 
 		return None

def three_stars_in_the_south(open, hight, low, close):
	try:
		data = talib.CDL3STARSINSOUTH(open, hight, low, close)
		return data
	except: 
 		return None

def three_advancing_white_solders(open, high, low, close):
	try:
		data = talib.CDL3WHITESOLDIERS(open, high, low, close)
		return data
	except: 
 		return None

def abandoned_baby(open, high, low, close):
	try:
		data = talib.CDLABANDONEDBABY(open, high, low, close)
		return data
	except: 
 		return None

def advanced_block(open, high, low, close):
	try:
		data = talib.CDLADVANCEBLOCK(open, high, low, close)
		return data
	except: 
 		return None

def belt_hold(open, high, low, close):
	try:
		data = talib.CDLBELTHOLD(open, high, low, close)
		return data
	except: 
 		return None

def breakaway(open, high, low, close):
	try:
		data = talib.CDLBREAKAWAY(open, high, low, close)
		return data
	except: 
 		return None

def closing_marubozu(open, high, low, close):
	try:
		data = talib.CDLCLOSINGMARUBOZU(open, high, low, close)
		return data
	except: 
 		return None

def concealing_baby_swallow(open, high, low, close):
	try:
		data = talib.CDLCONCEALBABYSWALL(open, high, low, close)
		return data
	except: 
 		return None

def counterattack(open, high, low, close):
	try:
		data = talib.CDLCOUNTERATTACK(open, high, low, close)
		return data
	except: 
 		return None

def dark_cloud_cover(open, high, low, close):
	try:
		data = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
		return data
	except: 
 		return None

def doji(open, high, low, close):
	try:
		data = talib.CDLDOJI(open, high, low, close)
		return data
	except:
		return None

def doji_star(open, high, low, close):
	try:
		data = talib.CDLDOJISTAR(open, high, low, close)
		return data
	except: 
 		return None

def dragonfly_doji(open, high, low, close):
	try:
		data = talib.CDLDRAGONFLYDOJI(open, high, low, close)
		return data
	except: 
 		return None

def engulfing_pattern(open, high, low, close):
	try:
		data = talib.CDLENGULFING(open, high, low, close)
		return data
	except: 
 		return None

def evening_doji_star(open, high, low, close):
	try:
		data = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
		return data
	except: 
 		return None

def evening_star(open, high, low, close):
	try:
		data = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)
		return data
	except: 
		return None

def up_down_ap_side_by_side_white_lines(open, high, low, close):
	try:
		data = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)
		return data
	except: 
 		return None

def gravestone_doji(open, high, low, close):
	try:
		data = talib.CDLGRAVESTONEDOJI(open, high, low, close)
		return data
	except: 
 		return None

def hammer(open, high, low, close):
	try:
		data = talib.CDLHAMMER(open, high, low, close)
		return data
	except: 
 		return None

def hanging_man(open, high, low, close):
	try:
		data = talib.CDLHANGINGMAN(open, high, low, close)
		return data
	except: 
 		return None

def harami_pattern(open, high, low, close):
	try:
		data = talib.CDLHARAMI(open, high, low, close)
		return data
	except: 
 		return None

def harami_cross_pattern(open, high, low, close):
	try:
		data = talib.CDLHARAMICROSS(open, high, low, close)
		return data
	except: 
 		return None

def high_wave_candle(open, high, low, close):
	try:
		data = talib.CDLHIGHWAVE(open, high, low, close)
		return data
	except: 
 		return None

def hikkake_attern(open, high, low, close):
	try:
		data = talib.CDLHIKKAKE(open, high, low, close)
		return data
	except: 
 		return None
	
def modified_hikkake_pattern(open, high, low, close):
	try:
		data = talib.CDLHIKKAKEMOD(open, high, low, close)
		return data
	except: 
 		return None

def homing_pigeon(open, high, low, close):
	try:
		data = talib.CDLHOMINGPIGEON(open, high, low, close)
		return data
	except: 
 		return None

def identical_three_crows(open, high, low, close):
	try:
		data = talib.CDLIDENTICAL3CROWS(open, high, low, close)
		return data
	except: 
 		return None

def in_neck_pattern(open, high, low, close):
	try:
		data = talib.CDLINNECK(open, high, low, close)
		return data
	except: 
 		return None

def inverted_hammer(open, high, low, close):
	try:
		data = talib.CDLINVERTEDHAMMER(open, high, low, close)
		return data
	except: 
 		return None

def kicking(open, high, low, close):
	try:
		data = talib.CDLKICKING(open, high, low, close)
		return data
	except: 
 		return None

def kicking_bull_bear_determined_by_the_longer_marubozu(open, high, low, close):
	try:
		data = talib.CDLKICKINGBYLENGTH(open, high, low, close)
		return data
	except: 
 		return None

def ladder_bottom(open, high, low, close):
	try:
		data = talib.CDLLADDERBOTTOM(open, high, low, close)
		return data
	except: 
 		return None

def long_legged_doji(open, high, low, close):
	try:
		data = talib.CDLLONGLEGGEDDOJI(open, high, low, close)
		return data
	except: 
 		return None

def long_line_candle(open, high, low, close):
	try:
		data = talib.CDLLONGLINE(open, high, low, close)
		return data
	except: 
 		return None

def marubozu(open, high, low, close):
	try:
		data = talib.CDLMARUBOZU(open, high, low, close)
		return data
	except: 
 		return None

def matching_low(open, high, low, close):
	try:
		data = talib.CDLMATCHINGLOW(open, high, low, close)
		return data
	except: 
 		return None

def mat_hold(open, high, low, close):
	try:
		data = talib.CDLMATHOLD(open, high, low, close)
		return data
	except: 
 		return None

def morning_doji_star(open, high, low, close):
	try:
		data = talib.CDLMORNINGDOJISTAR(open, high, low, close)
		return data
	except: 
 		return None

def morning_star(open, high, low, close):
	try:
		data = talib.CDLMORNINGSTAR(open, high, low, close)
		return data
	except: 
 		return None

def on_neck_pattern(open, high, low, close):
	try:
		data = talib.CDLONNECK(open, high, low, close)
		return data
	except: 
 		return None

def piercing_pattern(open, high, low, close):
	try:
		data = talib.CDLPIERCING(open, high, low, close)
		return data
	except: 
 		return None

def rickshaw_man(open, high, low, close):
	try:
		data = talib.CDLRICKSHAWMAN(open, high, low, close)
		return data
	except: 
 		return None

def rising_falling_three_methods(open, high, low, close):
	try:
		data = talib.CDLRISEFALL3METHODS(open, high, low, close)
		return data
	except: 
 		return None

def separating_lines(open, high, low, close):
	try:
		data = talib.CDLSEPARATINGLINES(open, high, low, close)
		return data
	except: 
 		return None

def shooting_star(open, high, low, close):
	try:
		data = talib.CDLSHOOTINGSTAR(open, high, low, close)
		return data
	except: 
 		return None

def short_line_candle(open, high, low, close):
	try:
		data = talib.CDLSHORTLINE(open, high, low, close)
		return data
	except: 
 		return None

def spinning_top(open, high, low, close):
	try:
		data = talib.CDLSPINNINGTOP(open, high, low, close)
		return data
	except: 
 		return None

def stalled_pattern(open, high, low, close):
	try:
		data = talib.CDLSTALLEDPATTERN(open, high, low, close)
		return data
	except: 
 		return None

def stick_sandwich(open, high, low, close):
	try:
		data = talib.CDLSTICKSANDWICH(open, high, low, close)
		return data
	except: 
 		return None

def takuri_dragonfly_doji_with_very_long_lower_shadow(open, high, low, close):
	try:
		data = talib.CDLTAKURI(open, high, low, close)
		return data
	except: 
 		return None

def tasuki_gap(open, high, low, close):
	try:
		data = talib.CDLTASUKIGAP(open, high, low, close)
		return data
	except: 
 		return None

def thrusting_pattern(open, high, low, close):
	try:
		data = talib.CDLTHRUSTING(open, high, low, close)
		return data
	except: 
 		return None

def tristar_pattern(open, high, low, close):
	try:
		data = talib.CDLTRISTAR(open, high, low, close)
		return data
	except: 
 		return None

def unique_3_river(open, high, low, close):
	try:
		data = talib.CDLUNIQUE3RIVER(open, high, low, close)
		return data
	except: 
 		return None

def upside_gap_two_crows(open, high, low, close):
	try:
		data = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)
		return data
	except: 
 		return None

def upside_downside_gap_three_methods(open, high, low, close):
	try:
		data = talib.CDLXSIDEGAP3METHODS(open, high, low, close)
		return data
	except: 
 		return None
