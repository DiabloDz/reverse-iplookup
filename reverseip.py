
import requests, re, os, base64;
import urllib
import urllib2
def main():
    print ("""


                              ...
           s,                .                    .s
            ss,              . ..               .ss
            'SsSs,           ..  .           .sSsS'
             sSs'sSs,        .   .        .sSs'sSs
              sSs  'sSs,      ...      .sSs'  sSs
               sS,    'sSs,         .sSs'    .Ss
               'Ss       'sSs,   .sSs'       sS'
      ...       sSs         ' .sSs'         sSs       ...
     .           sSs       .sSs' ..,       sSs       .
     . ..         sS,   .sSs'  .  'sSs,   .Ss        . ..
     ..  .        'Ss .Ss'     .     'sSs. ''        ..  .
     .   .         sSs '       .        'sSs,        .   .
      ...      .sS.'sSs        .        .. 'sSs,      ...
            .sSs'    sS,     .....     .Ss    'sSs,
         .sSs'       'Ss       .       sS'       'sSs,
      .sSs'           sSs      .      sSs           'sSs,
   .sSs'____________________________ sSs ______________'sSs,
.sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,
                        ...         sS'
                         sSs       sSs
                          sSs     sSs       - Diablo.Dz Private reverse iplookup -
                           sS,   .Ss
author : Diablo.Dz         'Ss   sS'
Help : Fb.com/mahrez.benx   sSs sSs
                             sSsSs
                              sSs
                               s

     """)
    url = 'http://api.hackertarget.com/reverseiplookup/?q='
    outbb = raw_input("[Dx ]  IP's Listesname : ")
    outbb = open(outbb,'r')
    inbb = outbb.readlines()
    for ip in inbb:
     ip = ip.rstrip("\n")
     print("[Dx ] from this IP :  -> "+ip)
     curl = url+ip
     urlbb = urllib2.urlopen(curl)
     inbb = urlbb.read()
     file = open('rzlt.txt','a')
     file.write(inbb)
     file.close()
     file = open('rzlt.txt','r')
     inbb = file.readlines()
     file.close()
     os.system('rm rzlt.txt')
     for i in inbb:
      i = i.rstrip("\n")
      file = open('rzlt.txt','a')
      i = 'http://'+i
      file.write(i+"\n")
      file.close()
      print("[Dx] Done Sites Grabbed successfully :D ")
if __name__ == '__main__':main()
