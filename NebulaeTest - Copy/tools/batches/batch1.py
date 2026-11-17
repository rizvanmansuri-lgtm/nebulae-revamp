# -*- coding: utf-8 -*-
import json
OUT='/home/claude/nb/tools/products/'
def J(d):
    json.dump(d,open(OUT+d['slug']+'.json','w',encoding='utf-8'),indent=1,ensure_ascii=False)
def G(f,a,l): return dict(file=f,alt=a,label=l)
def Q(i,l,v): return dict(icon=i,label=l,value=v)
def ST(n,l): return dict(num=n,label=l)
def W(t,d): return dict(t=t,d=d)
def F(i,c,b,t,d): return dict(icon=i,color=c,bg=b,t=t,d=d)
def A(i,t,d): return dict(icon=i,t=t,d=d)
def SP(g,rows): return dict(group=g,rows=[list(r) for r in rows])
def SC(f,a,c): return dict(file=f,alt=a,cap=c)
COL=[('#2563eb','rgba(37,99,235,.1)'),('#059669','rgba(16,185,129,.1)'),('#d97706','rgba(251,191,36,.12)'),('#4f46e5','rgba(79,70,229,.1)'),('#ea580c','rgba(234,88,12,.1)'),('#7c3aed','rgba(124,58,237,.1)'),('#0d9488','rgba(13,148,136,.1)'),('#dc2626','rgba(220,38,38,.1)')]
def FS(items): return [F(i,COL[k%8][0],COL[k%8][1],t,d) for k,(i,t,d) in enumerate(items)]
def DOC(name,path,sub): return dict(name=name,path='./assets/docs/'+path,sub=sub)

# ---------------- NLN0721 ----------------
J(dict(slug='nln0721',model='NLN0721',full='NebuLink Module NLN0721 — Wi-SUN',title_name='NebuLink Wi-SUN Module',
 type_key='module',type_label='Module',proto_key='wisun',proto_crumb='Wi-SUN',proto_label='Wi-SUN',badge='Wi-SUN Module',category='Wi-SUN Sub-GHz IoT Module',
 tagline='Sub-GHz Wi-SUN module based on the EFR32FG28 — +20 dBm, WPC certified, 26.68 × 16 mm.',
 meta_desc='NebuLink NLN0721 — EFR32FG28 based sub-GHz Wi-SUN module: +20 dBm TX, -108 dBm sensitivity, Wi-SUN / Amazon Sidewalk / WM-BUS, WPC certified, 26.68 x 16 x 3.6 mm.',
 desc='The NLN0721 is an ideal sub-GHz solution for Internet of Things applications such as smart metering, smart lighting, building automation and smart homes. Based on the EFR32FG28, this single-die, multi-core module offers long-range and mesh connectivity for multi-hop connections, with industry-leading security, low power consumption and fast wake-up times.',
 cert_badges=['WPC Certified','Wi-SUN','AES-256'],
 gallery=[G('nln0721-vs-sim.png','NebuLink Module NLN0721 shown beside a standard SIM card for size comparison','vs SIM card'),G('nln0721-module-photo.png','NLN0721 Wi-SUN module, 26.69 mm long, beside a 25 mm SIM card','Module view')],
 quick=[Q('wifi','Protocols','Wi-SUN · Amazon Sidewalk · WM-BUS'),Q('range','TX / RX','+20 dBm · −108 dBm @ 100 kbps'),Q('grid','Frequency Band','EU 863-870 · US 902-928 · IN865'),Q('chip','Core & Memory','78 MHz Cortex-M33 · 1024 KB flash / 256 KB SRAM'),Q('plug','I/O','Up to 21 pins · U(S)ART · LPUART'),Q('ruler','Size (L × W × H)','26.68 × 16.0 × 3.6 mm')],
 stats=[ST('+20 dBm','Maximum TX power'),ST('−109.5 dBm','Sensitivity @ 50 kbps, no FEC'),ST('1 km','RF range, line of sight'),ST('10 years','Module lifespan & support')],
 overview=['The NLN0721 is an ideal sub-GHz solution for Internet of Things applications such as smart metering, smart lighting, building automation and smart homes. The module is based on the EFR32FG28 and offers long-range and mesh connectivity for multi-hop connections.',
  'This single-die, multi-core solution provides industry-leading security features, low power consumption with fast wake-up times, and integrated power amplifiers to enable the next level of secure connectivity for IoT devices. A large memory footprint enables flexible solutions for dynamic protocol support.',
  'The compact size of the module makes it an ideal choice for any IoT device. With a lifespan and support of 10 years, the module suits IoT end devices that must stay in the field for a long time. It is WPC certified and is available with a u.FL connector or a feed line for the antenna.'],
 overview_note='',
 why=[W('Wi-SUN, Sidewalk & WM-BUS','Three sub-GHz protocols supported on one hardware platform.'),W('Mesh, long range','Multi-hop mesh connectivity with an estimated 1 km line-of-sight range.'),W('Secure','Hardware cryptographic acceleration for AES-128/192/256.'),W('WPC certified','The module is WPC certified (regulatory approval per the datasheet).'),W('10-year support','A lifespan and support commitment of 10 years.')],
 showcase=dict(title='Pinout, Block Diagram & Mechanical Drawings',intro='Reference drawings taken from the NLN0721 datasheet (version 3.0).',items=[
  SC('nln0721-pinout.png','NLN0721 module pinout diagram','Module pinout'),SC('nln0721-block-diagram.png','NLN0721 block diagram based on the EFR32FG28','Block diagram — EFR32FG28'),
  SC('nln0721-package-outline.png','NLN0721 package outline drawing with front, side and bottom views','Package outline (all dimensions in mm)'),SC('nln0721-footprint.png','NLN0721 recommended PCB footprint','Recommended footprint')]),
 specs=[SP('Performance',[('TX Power','+20 dBm'),('RX Sensitivity — IN865 MHz','100 kbps, no FEC, PER < 10%: −108 dBm'),('RX Sensitivity — IN865 MHz','50 kbps, no FEC, PER < 10%: −109.5 dBm'),('RX Sensitivity — EU 863-870 MHz','50 kbps, no FEC, PER < 10%: −109.5 dBm'),('Tolerance','± 2 dBm variation in test results'),('RF Range (Line of Sight)','1 km'),('RF Data Rate','50 kbps, 100 kbps')]),
  SP('Processor Specifications',[('Processor','32-bit 78 MHz ARM Cortex-M33 with DSP instruction and floating-point unit'),('Memory','Up to 1024 KB flash, 256 KB SRAM'),('Frequency Band','EU 863-870, US 902-928, IN865'),('Mounting Type','1.27 mm pitch SMD'),('Antenna Option','u.FL, Feedline'),('Size (L × W × H)','26.68 × 16.0 × 3.6 mm')]),
  SP('I/O Specifications',[('Serial Interface','1 × U(S)ART, 1 × LPUART'),('Other Peripherals','1 × I2C, 1 × SPI'),('Analog Input','2 × 12-bit ADC, 2.5 Msps'),('Digital IO','Up to 21 pins')]),
  SP('Electrical Specifications',[('Supply Voltage (VDD)','1.8 V ~ 3.6 V, 3.3 V'),('Current — Standby Mode','6.95 mA'),('Current — TX Mode','98.5 mA'),('Current — RX Mode','6.21 mA'),('Operating Temperature','−30 °C to 85 °C')]),
  SP('Networking & Compliance',[('Protocol','Amazon Sidewalk, WM-BUS, Wi-SUN'),('Security','Hardware cryptographic acceleration: AES-128/192/256'),('Firmware Update','Over-the-air (FUOTA); programming via SWD'),('Regulatory','WPC certified')])],
 spec_note='Specification values as published in the NLN0721 product brochure; the datasheet (v3.0) adds the peripheral counts.',
 features=FS([('network','Sub-GHz Mesh Connectivity','Long-range and mesh connectivity for multi-hop connections.'),('bolt','Integrated Power Amplifier','Up to +20 dBm TX power with an integrated PA; 98.5 mA in TX mode.'),('wifi','Multi-Protocol','Amazon Sidewalk, WM-BUS and Wi-SUN on one module.'),('chip','Cortex-M33 Processing','78 MHz ARM Cortex-M33 with DSP instructions and FPU; 1024 KB flash, 256 KB SRAM.'),('lock','Hardware Security','Cryptographic acceleration for AES-128/192/256.'),('download','FUOTA & SWD','Firmware update over the air, with serial-wire debugging.'),('shield','RF Shield','Shield protects the radio from external electromagnetic interference.'),('plug','Solderable, 21 I/O','Up to 21 I/Os on edge plated holes; solder directly to any device board.')]),
 apps=[A('meter','Smart Metering','Sub-GHz Wi-SUN connectivity for utility metering.'),A('bulb','Smart Street Lighting','Mesh networking for street lighting nodes.'),A('trash','Smart Waste Management','Long-range links for waste-bin monitoring.'),A('city','Smart City Network','Sub-GHz mesh for city infrastructure.'),A('city','Smart City Traffic Control','Connected control for traffic infrastructure.'),A('sprout','Smart Agriculture','Field sensing over long-range links.'),A('building','Building Automation & Monitoring','Wireless connectivity for building systems.'),A('bulb','Lighting Controls','Wireless control of lighting networks.'),A('box','Inventory Management','Tracking and status reporting for stock.'),A('leaf','Environmental Monitoring','Distributed environmental sensing.'),A('factory','Industrial Monitoring','Remote monitoring across industrial sites.'),A('gauge','Machinery Condition Monitoring','Condition and performance monitoring of machinery.')],
 part_rows=[['PL0NL0721I100','NLN0721 — u.FL RF output'],['PL0NL0721S100','NLN0721 — feed line RF output']],
 docs=[DOC('NLN0721 Brochure','NLN0721_Brochure.pdf','PDF · Product brochure'),DOC('NLN0721 Datasheet v3.0','NLN0721_Datasheet_v3.0.pdf','PDF · Technical datasheet, May 2024')],
 related=['nln0725is','nm0221i'],primary_doc='./assets/docs/NLN0721_Brochure.pdf'))

# ---------------- NLN0725-IS ----------------
J(dict(slug='nln0725is',model='NLN0725-IS',full='Wi-SUN High Power Module NLN0725-IS',title_name='Wi-SUN High Power Module',
 type_key='module',type_label='Module',proto_key='wisun',proto_crumb='Wi-SUN',proto_label='Wi-SUN',badge='High Power Wi-SUN Module',category='High Power Wi-SUN IoT Module',
 tagline='High power Wi-SUN module — up to +27 dBm (WPC limit), -107 dBm sensitivity, 39.5 × 16 mm.',
 meta_desc='Nebulae NLN0725-IS High Power Wi-SUN module: +27 dBm TX (WPC limit, +30 dBm capable), -107 dBm RX sensitivity, Cortex-M33, 1024 KB flash, Wi-SUN / Amazon Sidewalk / WM-BUS.',
 desc='NLN0725-IS is a high power Wi-SUN module delivering long-range, secure and energy-efficient wireless communication, designed for robust, large-scale IoT networks. With extended transmission range, strong penetration and mesh networking support, it enables reliable connectivity for smart metering, street lighting, industrial automation and other mission-critical applications.',
 cert_badges=['Wi-SUN','+27 dBm','AES'],
 gallery=[G('nln0725is-module.png','NLN0725-IS high power Wi-SUN module, top view','Module view')],
 quick=[Q('bolt','TX Power','+27 dBm (WPC limit) · up to +30 dBm capable'),Q('range','RX Sensitivity','−107 dBm @ 100 kbps (IN865)'),Q('wifi','Protocols','Wi-SUN · Amazon Sidewalk · WM-BUS'),Q('chip','Core & Memory','78 MHz Cortex-M33 · 1024 KB flash / 256 KB SRAM'),Q('plug','I/O','Up to 21 pins · U(S)ART · LPUART'),Q('ruler','Size (L × H × W)','39.50 × 16 × 3.6 mm')],
 stats=[ST('+27 dBm','TX power (WPC limit)'),ST('−107 dBm','RX sensitivity, IN865 @ 100 kbps'),ST('39.5 × 16 mm','Module footprint'),ST('1024 KB','Flash program memory')],
 overview=['NLN0725-IS is Nebulae\'s high power Wi-SUN module, delivering long-range, secure and energy-efficient wireless communication for robust, large-scale IoT networks.',
  'With extended transmission range, strong penetration and mesh networking support, it enables reliable connectivity for smart metering, street lighting, industrial automation and other mission-critical applications.',
  'Built for harsh environments, the module ensures stable performance and low power consumption, with seamless interoperability with global Wi-SUN standards. Output power can reach +30 dBm on a 5 V PA supply, but as per WPC criteria the module is limited to +27 dBm.'],
 overview_note='',
 why=[W('High output power','+27 dBm within the WPC limit; hardware capable of up to +30 dBm.'),W('Wi-SUN mesh','Extended range and strong penetration with mesh networking support.'),W('Multi-protocol','Wi-SUN, Amazon Sidewalk and WM-BUS.'),W('Flexible modulation','2/4 (G)FSK with configurable shaping, OQPSK DSSS, (G)MSK and OOK TX.'),W('Field updatable','Over-the-air firmware update mechanism.')],
 showcase=None,
 specs=[SP('Performance',[('TX Power','+27 dBm (maximum power up to +30 dBm is supported, but as per WPC criteria it cannot go beyond +27 dBm)'),('RX Sensitivity — IN865 MHz','−107 dBm @ 100 kbps with PER < 10%'),('RF Data Rate','50 kbps, 100 kbps')]),
  SP('Processor Specifications',[('Processor','32-bit 78 MHz ARM Cortex-M33 with DSP instruction and floating-point unit'),('Memory','Up to 1024 KB flash, 256 KB SRAM'),('Frequency Band','EU 863-870, US 902-928, IN865'),('Mounting Type','1.27 mm pitch SMD'),('Antenna Option','u.FL, Feedline'),('Size (L × H × W)','39.50 × 16 × 3.6 mm')]),
  SP('I/O Specifications',[('Serial Interface','1 × U(S)ART, 1 × LPUART'),('Analog Input','2 × 12-bit ADC, 2.5 Msps'),('Digital IO','Up to 21 pins')]),
  SP('Electrical Specifications',[('Power Supply — FG28','1.8 V ~ 3.6 V, 3.3 V'),('Power Supply — PALNA','3.3 V (+27 dBm), 5 V (+30 dBm)'),('Current — Standby Mode','18.4 mA'),('Current — TX Mode','360 mA'),('Current — RX Mode','30 mA'),('Operating Temperature','−30 °C to +85 °C')]),
  SP('Networking',[('Protocol','Amazon Sidewalk, WM-BUS, Wi-SUN'),('Frequency Band (features)','863 MHz to 876 MHz'),('Standard','IEEE 802.15.4 compliant')])],
 spec_note='Specification values as published in the NLN0725-IS product brochure.',
 features=FS([('bolt','High Power Output','Up to +27 dBm TX power (+30 dBm capable, limited by WPC criteria).'),('wifi','Flexible Modulation','2/4 (G)FSK with fully configurable shaping, OQPSK DSSS, (G)MSK and OOK TX modulation formats.'),('chip','Cortex-M33 + Memory','78 MHz ARM Cortex-M33 with 1024 KB flash and 256 KB RAM.'),('gauge','Real-Time Counter & Watchdog','32-bit real-time counter and calendar; 2 × watchdog timer with dedicated RC oscillator.'),('shield','IEEE 802.15.4','IEEE 802.15.4 compliant radio.'),('download','OTA Update','Provides an over-the-air firmware update mechanism.'),('plug','Antenna Options','u.FL connector for an external antenna, or feed line for a PCB antenna.'),('network','Mesh Networking','Mesh support for large-scale, mission-critical IoT networks.')]),
 apps=[A('meter','Smart Metering','Long-range Wi-SUN connectivity for metering networks.'),A('city','Smart Cities','Robust connectivity for city-scale infrastructure.'),A('factory','Smart Factory','Reliable wireless links for industrial automation.'),A('server','Data Centre / Server Room','Wireless monitoring for data centres and server rooms.')],
 part_rows=[['NLN0725-IS','High Power Wi-SUN Module — 39.50 × 16 × 3.6 mm, 1.27 mm pitch SMD']],
 docs=[DOC('NLN0725-IS Brochure','NLN0725-IS_Brochure.pdf','PDF · Product brochure')],
 related=['nln0721','nm0221i'],primary_doc='./assets/docs/NLN0725-IS_Brochure.pdf'))

# ---------------- NM0221-I module ----------------
J(dict(slug='nm0221i',model='NM0221-I',full='NebuLink Module NM0221-I — Wi-SUN',title_name='NebuLink Wi-SUN Module',
 type_key='module',type_label='Module',proto_key='wisun',proto_crumb='Wi-SUN',proto_label='Wi-SUN',badge='Wi-SUN Module',category='Wi-SUN IoT Module',
 tagline='WPC certified SoC-based Wi-SUN / IEEE 802.15.4 module for self-forming, self-healing mesh networks.',
 meta_desc='Nebulae NM0221-I — SoC-based low-power Wi-SUN / IEEE 802.15.4 module, WPC certified for IS16444 smart metering: +19.8 dBm TX, -105 dBm sensitivity, 1 km range, FOTA.',
 desc='NM0221-I is a SoC-based low-power wireless module by Nebulae that provides long-range connectivity for IoT devices. It is engineered to support Wi-SUN and IEEE 802.15.4 PHY networks and is ideal for applications that need self-forming and self-healing mesh networks. It is equipped with sufficient memory for IS16444 smart metering applications and is WPC certified.',
 cert_badges=['WPC Certified','Wi-SUN','IEEE 802.15.4'],
 gallery=[G('nm0221i-module.jpg','NM0221-I Wi-SUN module shown next to an Indian coin, 34.2 mm long','Module with coin scale')],
 quick=[Q('wifi','Protocols','Wi-SUN · Zigbee · Thread · Proprietary Mesh'),Q('range','TX / RX','+19.8 dBm · −105 dBm @ 38.4 kbps'),Q('grid','Frequency Band','863 ~ 876 MHz'),Q('chip','Core & Memory','Cortex-M4 @ 40 MHz · 1024 kB flash / 128 kB RAM'),Q('bolt','Supply Voltage','1.62 V ~ 3.8 V DC'),Q('ruler','Size (L × W × H)','34.2 × 25 × 4.6 mm')],
 stats=[ST('+19.8 dBm','TX power'),ST('−105 dBm','Sensitivity @ 38.4 kbps, 1% PER'),ST('1000 m','Range @ 38.4 kbps, line of sight'),ST('38.4–100 kbps','RF data rate')],
 overview=['NM0221-I is a SoC-based low-power wireless module by Nebulae that provides long-range connectivity for IoT devices. It is engineered to support Wi-SUN and IEEE 802.15.4 PHY networks.',
  'The module is ideal for applications which need self-forming and self-healing mesh networks. It is well suited to IS16444 smart metering applications because it is equipped with sufficient memory and is WPC certified.',
  'NM0221-I\'s FOTA capability makes it suitable for remote security updates. It is a 1.27 mm pitch SMD module with a U.FL connector for an external antenna.'],
 overview_note='',
 why=[W('Wi-SUN & 802.15.4','Supports 802.15.4 PHY/MAC with Zigbee, Thread, proprietary mesh and Wi-SUN.'),W('Self-healing mesh','Designed for self-forming, self-healing mesh networks.'),W('Smart-metering ready','WPC certified, with enough memory for IS16444 smart metering.'),W('Remote updates','OTA firmware update mechanism for remote security updates.'),W('Wide supply range','Runs from 1.62 V to 3.8 V DC.')],
 showcase=None,
 specs=[SP('Performance',[('TX Power','+19.8 dBm'),('RX Sensitivity (@ 1% PER)','38.4 kbps: −105 dBm · 100 kbps: −101 dBm'),('RF Range (Line of Sight)','1000 meters @ 38.4 kbps data rate'),('RF Data Rate','38.4 ~ 100 kbps')]),
  SP('Processor Specifications',[('Processor','32-bit ARM Cortex-M4 core with DSP instruction and floating point unit operating @ 40 MHz'),('Memory','1024 kB Flash Program, 128 kB RAM Data'),('Frequency Band','863 ~ 876 MHz'),('Mounting Type','1.27 mm pitch SMD'),('Antenna Options','U.FL'),('Size (L × W × H)','34.2 × 25 × 4.6 mm')]),
  SP('I/O Specifications',[('Serial Interface','1 × UART'),('Analog Input','2 × 12-bit 1 MSPS SAR ADC'),('Digital IO','25 ~ 27')]),
  SP('Electrical Specifications',[('Supply Voltage','1.62 V ~ 3.8 V DC, 3.3 V'),('Current — TX (868 MHz, CW, 20 dBm match, +3.3 V external PA supply)','79.7 ~ 106.7 mA'),('Current — TX (868 MHz, CW, 14 dBm match, external PA supply on DCDC output)','35.3 ~ 41 mA'),('Current — RX (38.4 kbit/s, 2GFSK, 868 MHz, radio clock prescaled by 4)','8.6 ~ 10.2 mA'),('Operating Temperature','−20 °C to 85 °C'),('Storage Temperature','−30 °C to 125 °C')]),
  SP('Networking',[('Protocol','802.15.4 PHY/MAC — Zigbee, Thread, Proprietary Mesh, Wi-SUN')])],
 spec_note='Specification values as published in the NM0221-I product brochure.',
 features=FS([('network','Self-Healing Mesh','Built for self-forming, self-healing mesh networks over 802.15.4.'),('range','Long-Range Connectivity','Up to 1000 m line of sight at 38.4 kbps.'),('chip','Cortex-M4 with FPU','32-bit ARM Cortex-M4 with DSP instructions at 40 MHz.'),('grid','Generous Memory','1024 kB flash and 128 kB RAM.'),('wifi','BPSK / DBPSK TX','Supports BPSK / DBPSK TX modulation formats.'),('gauge','RTC, Watchdog & ADC','32-bit RTC and calendar, 2 × watchdog timers, 12-bit 1 MSPS SAR ADC.'),('download','OTA Firmware Update','Over-the-air firmware update mechanism (FOTA).'),('plug','U.FL Antenna Connector','Connect an external antenna via the U.FL connector.')]),
 apps=[A('meter','Smart Grid Meter','Connectivity for smart-grid metering devices.'),A('bolt','Smart Energy','Energy-usage monitoring and reporting.'),A('leaf','Environmental Monitoring','Distributed environmental sensing.'),A('bulb','Smart Street Lighting','Mesh connectivity for street lighting.')],
 part_rows=[['NM0221-I','NebuLink Module NM0221-I — Wi-SUN / IEEE 802.15.4, U.FL antenna']],
 docs=[DOC('NM0221-I Brochure','NM0221-I_Brochure.pdf','PDF · Product brochure')],
 related=['nm0221i-nic','nln0721'],primary_doc='./assets/docs/NM0221-I_Brochure.pdf'))

# ---------------- NM0221-I NIC card ----------------
J(dict(slug='nm0221i-nic',model='NM0221-I NIC Card',full='NM0221-I WPC Certified NIC Card',title_name='Wi-SUN / 6LoWPAN NIC Card',
 type_key='module',type_label='NIC Card',proto_key='wisun',proto_crumb='Wi-SUN',proto_label='Wi-SUN / 6LoWPAN',badge='NIC Card',category='Wi-SUN / 6LoWPAN Meter NIC Card',
 tagline='WPC certified NM0221-I based NIC card for IS16444 smart meters — 2-wire UART meter interface.',
 meta_desc='Nebulae NM0221-I NIC card — WPC certified 6LoWPAN / IEEE 802.15.4 network interface card for IS16444 smart meters: 863-876 MHz, 15 dBm radiated TX, 2-wire UART, FOTA.',
 desc='The NM0221-I NIC Card by Nebulae provides long-range connectivity for IoT devices and is engineered to support 6LoWPAN and IEEE 802.15.4 PHY networks. It is ideal for IS16444 smart metering applications, is WPC certified, and offers FOTA for remote security updates. It connects to the meter through a 2-wire serial UART interface.',
 cert_badges=['WPC Certified','6LoWPAN','IS16444'],
 gallery=[G('nm0221i-nic-block-diagram.png','NM0221-I NIC card functional block diagram showing the main board and antenna board','Block diagram'),G('nm0221i-module.jpg','NM0221-I module used on the NIC card, shown next to an Indian coin','NM0221-I module')],
 quick=[Q('plug','Meter Interface','2-wire serial UART'),Q('range','TX / RX','15 dBm radiated · −105 dBm @ 38.4 kbps'),Q('grid','Frequency Band','863 MHz to 876 MHz'),Q('bolt','Input Supply','3.3 V to 5 V DC'),Q('thermo','Working Temperature','0 ~ 70 °C or −40 ~ 85 °C (industrial)'),Q('ruler','Dimensions','62.8 × 42.8 mm, 2-layer PCB')],
 stats=[ST('15 dBm','Radiated transmit power'),ST('−105 dBm','Sensitivity @ 38.4 kbps, 1% PER'),ST('100 mA','TX current @ 3.3 V'),ST('62.8 × 42.8 mm','Card dimensions')],
 overview=['The NM0221-I NIC Card is a SoC-based low-power wireless network interface card by Nebulae that provides long-range connectivity for IoT devices. It is engineered to support 6LoWPAN and IEEE 802.15.4 PHY networks and is ideal for applications that need self-forming and self-healing mesh networks.',
  'The card is ideal for IS16444 smart metering applications because it is equipped with sufficient memory and is WPC certified. Its FOTA capability makes it suitable for remote security updates.',
  'By leveraging 6LoWPAN technology it enables communication between meters and utility providers, supporting advanced smart-grid capabilities such as reliable mesh connectivity, long-range communication, low power consumption and real-time monitoring of energy usage patterns. Two LEDs indicate power and network status, and the card is easy to install.'],
 overview_note='',
 why=[W('Built for smart meters','WPC certified NIC card for IS16444 smart metering applications.'),W('Simple meter interface','2-wire serial UART communication to the meter.'),W('Self-healing mesh','6LoWPAN over IEEE 802.15.4 for self-forming, self-healing networks.'),W('Status LEDs','One LED for power and one for network status.'),W('Remote updates','OTA firmware update mechanism for remote security updates.')],
 showcase=None,
 specs=[SP('Card Specifications',[('Base Module','NM0221-I (WPC certified)'),('Frequency Band','863 MHz to 876 MHz'),('Radiated Transmit Power','15 dBm'),('RX Sensitivity (@ 1% PER)','38.4 kbps: −105 dBm · 100 kbps: −101 dBm'),('Meter Interface','2-wire serial UART'),('Dimensions','62.8 × 42.8 mm'),('PCB','2-layer design')]),
  SP('Processor & Memory',[('Flash Program Memory','Up to 1024 kB'),('RAM Data Memory','Up to 128 kB'),('Modulation','BPSK / DBPSK TX'),('Timers','2 × watchdog timer with dedicated RC oscillator'),('Standard','IEEE 802.15.4 compliant')]),
  SP('Electrical & Environmental',[('Operating Voltage','3.3 V to 5 V DC input supply'),('Current Consumption','100 mA @ 3.3 V, TX mode'),('Working Temperature','0 ~ 70 °C (commercial grade) or −40 ~ 85 °C (industrial grade)')]),
  SP('Meter Pin Connection (meter pin → NM0221-I module pin)',[('Meter pins 1, 2, 4, 5, 8, 9, 11','NC'),('Meter pin 3 — Power EN (option with NL)','Module pin 1'),('Meter pin 6 — Meter TX','Module pin 26'),('Meter pin 7 — Meter RX','Module pin 8'),('Meter pin 10 — NIC Reset (optional with NL)','Module pin 27'),('Meter pins 13, 14','GND')])],
 spec_note='Specification values as published in the NM0221-I NIC card datasheet (version 1.0).',
 features=FS([('plug','2-Wire UART Meter Interface','Serial UART communication to the meter over two wires.'),('network','6LoWPAN Mesh','6LoWPAN over IEEE 802.15.4 for reliable, self-healing connectivity.'),('shield','WPC Certified','WPC certified NM0221-I based NIC card.'),('chip','Ample Memory','Up to 1024 kB flash and 128 kB RAM.'),('bolt','Low Power','Low power consumption; 100 mA in TX mode at 3.3 V.'),('eye','Power & Network LEDs','Two LEDs: one for power and one for network status.'),('download','FOTA','Over-the-air firmware update mechanism.'),('grid','Easy to Install','Designed for straightforward installation in the meter.')]),
 apps=[A('meter','IS16444 Smart Metering','Network interface for IS16444 smart meters.'),A('bolt','Smart Grid','Meter-to-utility communication for smart-grid deployments.'),A('gauge','Energy Usage Monitoring','Real-time insight into energy usage patterns.')],
 part_rows=[['NM0221-I NIC Card','WPC certified NIC card based on the NM0221-I module']],
 docs=[DOC('NM0221-I Module Brochure','NM0221-I_Brochure.pdf','PDF · Base module brochure')],
 related=['nm0221i','nln0721'],primary_doc=''))

# ---------------- NLN111P ----------------
J(dict(slug='nln111p',model='NLN111P',full='Zigbee MG21 Module NLN111P',title_name='Zigbee MG21 Module',
 type_key='module',type_label='Module',proto_key='zigbee',proto_crumb='Zigbee',proto_label='Zigbee · Thread · BLE 5',badge='Zigbee MG21 Module',category='Zigbee Multiprotocol IoT Module',
 tagline='EFR32MG21 based 2.4 GHz Zigbee / Thread / Bluetooth 5 module with PCB antenna.',
 meta_desc='Nebulae NLN111P — EFR32MG21 based 2.4 GHz Zigbee, Thread and Bluetooth 5 module: +20 dBm TX, -104.3 dBm sensitivity, 1024 kB flash, secure boot, OTA, PCB antenna, 26.7 x 16 mm.',
 desc='NLN111P is a compact-size, high-performance Zigbee module based on the Silicon Labs EFR32MG21 SoC. Ideal for energy-friendly, multiprotocol, multiband networking for IoT devices, it features an integrated PCB antenna for excellent RF performance in dense environments and ultra-low power consumption for both battery-powered and always-on devices.',
 cert_badges=['Zigbee','Thread','Bluetooth 5'],
 gallery=[G('nln111p-module.jpg','NLN111P Zigbee MG21 module, top view with RF shield and PCB antenna','Module view')],
 quick=[Q('wifi','Protocols','Zigbee · Thread · Bluetooth 5'),Q('range','TX / RX','Up to +20 dBm · −104.3 dBm @ 250 kbps'),Q('grid','Frequency Band','2.4 GHz ISM'),Q('chip','Core & Memory','80 MHz Cortex-M33 · 1024 kB flash / 96 kB RAM'),Q('lock','Security','AES-128/192/256 HW crypto · secure boot'),Q('ruler','Size','26.7 × 16 × 3.6 mm')],
 stats=[ST('+20 dBm','Maximum TX power'),ST('−104.3 dBm','Sensitivity @ 250 kbps'),ST('60 µA','Standby current'),ST('26.7 × 16 mm','Module footprint')],
 overview=['NLN111P is a compact-size, high-performance Zigbee module based on the Silicon Labs EFR32MG21 SoC. It is ideal for enabling energy-friendly, multiprotocol, multiband networking for IoT devices.',
  'It features an integrated PCB antenna for excellent RF performance in dense environments. With ultra-low power consumption it is suited to both battery-powered and always-on IoT devices.',
  'The 80 MHz ARM Cortex-M33 with 1024 kB flash and 96 kB RAM delivers significant processing capability for complex IoT applications, while hardware-accelerated cryptography, secure boot loading, debug access control and a true random number generator keep devices secure. Firmware can be updated over the air.'],
 overview_note='',
 why=[W('Multiprotocol','Bluetooth 5, Zigbee and Thread on the EFR32MG21 SoC.'),W('Longer battery life','60 µA standby current for battery-powered devices.'),W('Robust RF performance','Integrated PCB antenna, up to +20 dBm TX and −104.3 dBm sensitivity.'),W('Secure','Secure boot loading, hardware-accelerated AES and debug access control.'),W('OTA updates','Update firmware in the field without physical access.')],
 showcase=None,
 specs=[SP('Processor & Memory',[('Processor','Silicon Labs EFR32MG21 SoC'),('CPU','80 MHz ARM Cortex-M33'),('Memory','1024 kB Flash, 96 kB RAM'),('Firmware','OTA updates, Secure Boot')]),
  SP('Radio',[('Frequency Bands','2.4 GHz ISM'),('TX Power','Up to +20 dBm'),('RF Sensitivity','−104.3 dBm @ 250 kbps'),('Network Protocols','Bluetooth 5, Zigbee, Thread'),('Antenna','Integrated PCB antenna')]),
  SP('Power & Current',[('Supply','3.3 V'),('Standby','60 µA'),('TX','185 mA'),('RX','9.5 mA')]),
  SP('Security',[('Cryptography','AES-128/192/256 (hardware accelerated)'),('Boot & Debug','Secure boot loading, debug access control, true random number generator')]),
  SP('Physical & Environment',[('Size','26.7 × 16 × 3.6 mm'),('I/O','Serial, Analog, Digital (21 pins)'),('Mounting','1.27 mm pitch SMD'),('Shielding','EMI RF shield'),('Temperature Range','−20 °C to +85 °C')])],
 spec_note='Specification values as published in the NLN111P product brochure.',
 features=FS([('wifi','Multiprotocol Radio','Bluetooth 5, Zigbee and Thread from one 2.4 GHz SoC.'),('bolt','Ultra-Low Power','60 µA standby, 9.5 mA RX and 185 mA TX at 3.3 V.'),('chip','Cortex-M33 Performance','80 MHz core with 1024 kB flash and 96 kB RAM for complex applications.'),('lock','Hardware Security','Accelerated AES-128/192/256, secure boot and a true random number generator.'),('download','OTA Updates','Field firmware updates over the air.'),('range','Strong RF Range','Up to +20 dBm TX power with −104.3 dBm sensitivity at 250 kbps.'),('shield','EMI RF Shield','Shielded module for dense RF environments.'),('plug','SMD, 21 I/O','1.27 mm pitch SMD with serial, analog and digital I/O (21 pins).')]),
 apps=[A('chip','IoT Multi-Protocol Devices','Devices that need Zigbee, Thread and Bluetooth 5.'),A('city','Smart Cities & Smart Factory','Connected infrastructure and factory automation.'),A('bulb','Smart Lights & Smart Metering','Lighting and metering endpoints.'),A('building','Building Automation & Security','Connected building systems and security devices.'),A('home','Gateways & Digital Assistants','Hubs and voice or digital assistant devices.')],
 part_rows=[['NLN111P','Zigbee MG21 Module — EFR32MG21, integrated PCB antenna, 1.27 mm pitch SMD']],
 docs=[DOC('NLN111P Brochure','NLN111P_Brochure.pdf','PDF · Product brochure')],
 related=['nln811p','nln0721'],primary_doc='./assets/docs/NLN111P_Brochure.pdf'))
print('json done')
