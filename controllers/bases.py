
from models import bases

    
def getAllBases(host,user,contra,pueto):
    dataBases=bases.getAllBases(host,user,contra,pueto)
    return print(dataBases)
    
def creteBase(host,user,contra,pueto,base):
  bases.createbase(host,user,contra,pueto,base)
  