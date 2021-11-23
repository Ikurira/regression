from regress import performRegression
import time

def ukEquities():
   
    aerospace=('RR','RR')
    banks=('BARC','HSBA','LLOY','NWG','STAN')
    beverages=('CCH','DGE')
    brokerage=('III','ABDN','HL','ICP','MNG','SDR','STJ')
    chemicals=('CRDA','JMAT')
    ceif=('PSH','SMT')
    construction=('CRH','CRH')
    consumer=('CPG','CPG')
    credit=('LSEG','LSEG')
    electronics=('HLMA','HLMA')    
    food=('ABF','ABF')
    health=('BNZL','MRO','MNDI','SMDS','SMIN','SKG')
    household=('BDEV','BKG','PSN','TW')
    indEng=('SPX','WEIR')
    indSpt=('DCC','EXPN','FERG','ITRK','RTO')
    indTrans=('AHT','RMG')
    lifeIns=('AV','LGEN','PHNX','PRU')
    media=('INF','ITV','PSON','REL','WPP')
    medicalEqp=('SN','SN')
    metalsMining=('ANTO','BHP','EVR','GLEN','RIO')                
    nonLife=('ADM','ADM')
    oilGas=('BP','RDSA','RDSB')
    personalCare=('OCDO','RKT','SBRY','TSCO','ULVR')
    personalGoods=('BRBY','BRBY')
    pharma=('AZN','GSK','HIK')
    preciousMetals=('FRES','POLY')
    realEstateServ=('RMV','RMV')
    reit=('BLND','LAND','SGRO')
    retailers=('BME','JD','KGF','NXT')
    software=('AUTO','AVST','AVV','JET','SGE')
    telecommsProviders=('VOD','VOD')
    tobacco=('BATS','IMB')
    travelLeisure=('ENT','FLTR','IHG','IAG','WTB')
    utilities=('NG','SVT','UU','SSE')

    sectors=(banks,construction,aerospace,beverages,chemicals,ceif,consumer,electronics,credit,food,utilities,
        health,household,indEng,metalsMining,indSpt,indTrans,brokerage,lifeIns,media,medicalEqp,nonLife,oilGas,
        personalCare,personalGoods,pharma,preciousMetals,realEstateServ,reit,retailers,software,telecommsProviders,
        tobacco,travelLeisure)

    for i in sectors:
        performRegression(i)
        
if __name__ == "__main__":

    t0=time.time()
    ukEquities()
    t1=time.time()
    print ('UK_Equities process took: ', t1-t0)
