import yfinance as yf
from datetime import datetime
import time
import pandas
from pandas import DataFrame
import mysql.connector

def import_iterate():

	conn = mysql.connector.connect(
    option_files="my.cnf")

	cursor = conn.cursor()

	ukEquities=('SKG','SPX','SSE','STJ','STAN','TW','TSCO','ULVR','UU','VOD','WEIR','WTB','WPP','III','ABDN','ADM','ANTO','AHT','ABF','AZN','AUTO',
        'AVST','AVV','AV','BME','BARC','BDEV','BKG','BHP','BP','BATS','BLND','BNZL','BRBY','CCH','CPG','CRH','CRDA','DCC',
        'DGE','ENT','EVR','EXPN','FERG','FLTR','FRES','GSK','GLEN','HLMA','HL','HIK','HSBA','IMB','INF','IHG','ICP','ITRK','IAG',
        'ITV','JD','JMAT','JET','KGF','LAND','LGEN','LLOY','LSEG','MNG','MRO','MNDI','NG','NWG','NXT','OCDO','PSON','PSH','PSN','PHNX',
        'POLY','PRU','RKT','REL','RTO','RMV','RIO','RR','RDSA','RDSB','RMG','SGE','SBRY','SDR','SMT','SGRO','SVT','SN','SMDS','SMIN')

	for i in ukEquities:

		data = yf.download(i + ".L", period = "4d")
		date64 = data.index
		Date=pandas.Series(date64.date)
		closePrice=data.iloc[:,3]
		
		size = len(data)
		iterator = (size)-(size)

		while iterator < size:

			sql ="INSERT INTO " + i + "(Date,Close) VALUES (%s,%s)"
			values = (Date[iterator], closePrice[iterator])

			cursor.execute(sql, values)
			conn.commit()
			print ('insert successful for ', i, 'dated ', str(Date[iterator]))

			iterator = iterator+1


if __name__ == "__main__":

	t0=time.time() #start timer
	import_iterate()
	t1=time.time() #end timer
	processDuration = t1-t0
	print ('\n','Process took: ', np.around((processDuration), decimals=2), 'seconds') 
