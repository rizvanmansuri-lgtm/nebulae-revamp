import json,os,re,shutil,glob,sys
ROOT=sys.argv[1]; SRC=sys.argv[2]
IMG=ROOT+'/assets/images/products/'
T=lambda n:SRC+'/'+n+'.webp'
# slug -> list of (source name, label, alt-suffix)
M={
'nlg8140':[('HHU - NLG8140','Handheld view','handheld LoRaWAN gateway with external antenna')],
'nlg6x40g-in':[('IP65 MultiChannel LoRaWAN Gateway','IP65 gateway','IP65 multi-channel LoRaWAN gateway with external antenna')],
'nlg6x40h-in':[('IP67 MultiChannel LoRaWAN Gateway','IP67 gateway','IP67 multi-channel LoRaWAN gateway with external antenna'),('IP67 MultiChannel LoRaWAN Gateway (1)','Enclosure & antenna','IP67 gateway enclosure with antenna and mounting straps')],
'nlg6770in':[('NLG6770-IN - WiSUN Gateway','DCU view','Wi-SUN DCU enclosure with external antenna')],
'nlg8520':[('NLG8520 - WiSUN Gateway','Gateway view','Wi-SUN gateway enclosure with external antenna')],
'nlg8400':[('NLG8400 & NLG8600 (1)','Board view','SCADA RTU board with screw terminals'),('NLG8400 & NLG8600','Board with antenna','SCADA RTU board with external cellular antenna')],
'nlg8600':[('NLG8400 & NLG8600','Board with antenna','SCADA RTU board with external cellular antenna'),('NLG8400 & NLG8600 (1)','Board view','SCADA RTU board with screw terminals')],
'nln0651i':[('LoRa EVK Kit (1)','EVK board','LoRa Arduino-compatible EVK board'),('LoRa EVK Kit (2)','Kit contents','LoRa EVK with USB cable and antenna')],
'nln0721':[('NLN0721 Wi-SUN Module','Top view','Wi-SUN module top view'),('NLN0721 Wi-SUN Module (3)','Top view (PCB)','Wi-SUN module on PCB, top view'),('NLN0721 Wi-SUN Module (1)','Bottom view','Wi-SUN module bottom view with pin labels'),('NLN0721 Wi-SUN Module (2)','Size vs SIM','Wi-SUN module next to a SIM card for scale')],
'nln0725is':[('NLN 0725-IS Wi-SUN High Power Module','Module view','Wi-SUN high power module')],
'nln500a':[('NLN500a','Shielded module','LoRaWAN node module with shield'),('NLN 500a','Board view','LoRaWAN node board'),('NLN 500a (1)','Board bottom','LoRaWAN node board, alternate view')],
'nln500b':[('NLN 500b','Top view','LoRa module top view'),('NLN 500b (1)','Size vs SIM','LoRa module next to a SIM card for scale')],
'nm0221i':[('NM0221-I','Board view','Wi-SUN module board'),('NM0221-I (1)','Size vs coin','Wi-SUN module next to a coin for scale')],
'nm0221i-nic':[('NM0221-I','Board view','NM0221-I module board'),('NM0221-I (1)','Size vs coin','NM0221-I module next to a coin for scale')],
'nln111p':[('Zigbee MG21 Module','Module view','Zigbee MG21 module')],
'nln811p':[('Zigbee MG24 Module','Module view','Zigbee MG24 module')],
'p2p-gateway':[('P2P Gateway','Kit contents','P2P LoRa gateway with power adapter, plug and antennas')],
'sls-som-mx6':[('SoM Module','Top view','i.MX6ULL system on module, top view'),('SoM Module (1)','Bottom view','i.MX6ULL system on module, bottom view')],
}
KEEP=('diagram','drawing','response','insertion','pinout','application','annotated','wiring','dimension','interface','accessor','illustration')
used={}; prim={}
for slug,items in M.items():
    f=f'{ROOT}/tools/products/{slug}.json'; d=json.load(open(f,encoding='utf-8'))
    old=d['gallery']; new=[]
    for i,(src,label,alt) in enumerate(items,1):
        fn=f'{slug}-{i}.webp'; shutil.copy(T(src),IMG+fn)
        new.append({'file':fn,'alt':f"{d['model']} {alt}",'label':label})
    kept=[g for g in old if any(k in g['file'].lower() for k in KEEP)]
    prim[old[0]['file']]=new[0]['file']
    d['gallery']=new+kept
    json.dump(d,open(f,'w',encoding='utf-8'),indent=1,ensure_ascii=False)
    print(slug,[g['file'] for g in d['gallery']])
# swap old primary image refs elsewhere (non-generated pages / js)
n=0
for f in glob.glob(ROOT+'/*.html')+glob.glob(ROOT+'/industries/*.html')+glob.glob(ROOT+'/solutions/*.html')+glob.glob(ROOT+'/assets/js/*.js'):
    s=o=open(f,encoding='utf-8').read()
    for a,b in prim.items(): s=s.replace('products/'+a,'products/'+b)
    if s!=o: open(f,'w',encoding='utf-8').write(s); n+=1
print('other files updated',n)
