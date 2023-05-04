# Building Name Replacer

# dictionary matching building codes with their respective names
d = {'343':'1700','302':'1810','303':'ALTER','305':'ANNENBERG','306':'ARCHITECTURE',\
'374':'ASTARC','308':'TPAC','315':'BARRACK','310':'BEURY','338':'BELL','311':'BIO','373':'BOATHOUSE',\
'313':'CARNELL','375':'CHARLES','318':'CONWELL','323':'COE','201':'DENTAL (NEW)','202':'DENTAL (OLD)',\
'359':'ECEC','363':'EDBERG/OLSON','376':'FRAT HOUSE','324':'GLADFELTER','325':'GROUNDS','326':'HEALTH SERV',\
'360':'IBC','327':'KARDON','328':'KLEIN','306':'LIAC GARAGE','304':'MAZUR','335':'MCGONIGLE','370':'MESSIAH',\
'331':'MITTEN','368':'MONT GARAGE','372':'MORGAN 27TH','336':'OFM','333':'PALEY','335A':'PEARSON','339':'PRESSER',\
'340':'RITTER ANNEX','341':'RITTER HALL','342':'ROCK','369':'SERC','334':'SHUSTERMAN','345':'SPEAKMAN',\
'371':'SPORTS COMPLEX','353':'STUDENT CENTER (S)','350':'STUDENT CENTER (N)','362':'STUDENT PAV', '351':'SULLIVAN',\
'354':'TOMLINSON','361':'TUTTLEMAN','365':'TYLER','317':'WACHMAN','358':'WEISS','367':'WEST POD','601':'TUCC,',\
'05001':'BUSINESS OFFICES','05003':'TRIANGLE','05004':'TEMPLE TOWERS','05006':'JOHNSON','05007':'PEABODY',\
'05008':'AMBLER','05009':'TYLER','05020':'JH/AMBLER,TYLER','05021':'WHITE','05023':'1940','05027':'1300',\
'05035':'MORGAN (N)','05036':'MORGAN (S)','05037':'MORGAN DINING','86001':'LOT 1','86002':'LOT 2','86004':'TYLER LOT',\
'86005':'LOT 7','86006':'LOT 9','86007':'LOT 10','86008':'TEMPLE TOWERS LOT','05006A':'HARDWICK','Property':'Property'}

def convertBldgs(filename):
    # open the browse file that AIM exports
    # it must be in the same folder as this .py file
    data = open(filename,'r')
    # writes a new file which is placed in the same folder
    output = open('browse_updated.csv','w')
    for line in data:
        strings = line.split(',')
        # goes line by line and rewrites them to only include WO#, description, and the converted bldg name
        line = strings[0]+','+strings[1]+','+d[strings[7]]+'\n'
        # adds to the new file
        output.write(line)
    data.close()
    output.close()
# when running input the name of the .csv file that AIM exported in the parameters
convertBldgs('browse.csv')
