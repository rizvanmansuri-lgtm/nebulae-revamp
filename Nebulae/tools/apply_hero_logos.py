#!/usr/bin/env python3
"""Home hero: tech-card icons -> clickable logo cards; stats in one row. Idempotent. Run on index.html, index1.html, index-new.html"""
import re,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO={'lora':('LoRaWAN.png','lora'),'wisun':('Wi-SUN-Main-Logo.png','wisun'),'zigbee':('zigbee.png','zigbee'),'wifi':('WiFi.png','wifi'),'gsm':('NB-IoT.png','gsm'),'ble':('Bluetooth.png','ble')}
pat=re.compile(r'<div class="nbl-mini-card nbl-mini-card--(\w+)"><div class="nbl-mini-card__icon">.*?</div>(<span class="nbl-mini-card__label">.*?</span>)(<span class="nbl-mini-card__sub">.*?</span>)</div>',re.S)
def rep(m):
    k=m.group(1); img,proto=LOGO[k]
    alt=re.sub('<.*?>','',m.group(2))
    return (f'<a class="nbl-mini-card nbl-mini-card--{k}" href="products.html?proto={proto}" aria-label="{alt} products">'
            f'<span class="nbl-mini-card__logo"><img src="./assets/images/SupportedTech/{img}" alt="{alt}" loading="lazy"></span>{m.group(2)}{m.group(3)}</a>')
for f in ['index.html','index1.html','index-new.html']:
    p=os.path.join(ROOT,f)
    if not os.path.exists(p): continue
    s=open(p,encoding='utf-8').read()
    s2,n=pat.subn(rep,s)
    print(f,n,'cards')
    open(p,'w',encoding='utf-8').write(s2)
