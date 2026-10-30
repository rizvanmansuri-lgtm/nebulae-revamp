# -*- coding: utf-8 -*-
"""Industry pages (industries/*.html). Facts about products are taken from tools/products/*.json and tools/solutions_data.py.
Lines marked  [use-case]  describe typical applications for the industry (general knowledge, not customer claims or case studies) —
review them before launch.  Edit here, then run:  python3 tools/build_solutions.py
Chip/product links resolve from the page (industries/) so they use ../ ."""
BLUE = ('rgba(37,99,235,.1)', '#2563eb'); ORG = ('rgba(234,88,12,.1)', '#ea580c'); TEAL = ('rgba(13,148,136,.1)', '#0d9488')
PURP = ('rgba(124,58,237,.1)', '#7c3aed'); GRN = ('rgba(16,185,129,.1)', '#059669')

IND_RELATED = {
 'i-energy':  ('Industry', 'IoT in Energy & Utilities', 'Smart electricity, gas and water metering and transformer monitoring.', 'industries/iot-energy-utilities.html', ORG),
 'i-city':    ('Industry', 'Smart City Solutions', 'Street lighting, EV charging and city-wide LoRaWAN connectivity.', 'industries/smart-city-solutions.html', TEAL),
 'i-bms':     ('Industry', 'Building Management System', 'Wireless sensing and control for commercial buildings.', 'industries/building-management-system.html', BLUE),
 'i-iiot':    ('Industry', 'Industrial IoT', 'SCADA RTUs, industrial gateways and wireless sensor networks.', 'industries/industrial-iot.html', PURP),
 'i-tele':    ('Industry', 'Telematics & Fleet', 'Cellular and LoRa tracking hardware for vehicles and fleets.', 'industries/telematics-fleet.html', ORG),
 'i-logi':    ('Industry', 'IoT in Logistics', 'Asset tracking and condition monitoring across the supply chain.', 'industries/iot-logistics.html', ORG),
 'i-agri':    ('Industry', 'Smart Agriculture', 'Long-range LoRaWAN sensing for farms and irrigation.', 'industries/smart-agriculture.html', GRN),
 'i-farm':    ('Industry', 'Farm & Animal Management', 'Compact LoRa and 434 MHz tags for livestock monitoring.', 'industries/farm-animal-management.html', GRN),
 'i-health':  ('Industry', 'IoT in Healthcare', 'BLE, Wi-Fi and Zigbee connectivity for health and hospital devices.', 'industries/iot-healthcare.html', BLUE),
 'i-defence': ('Industry', 'IoT in Defence', 'Long-range, rugged-class wireless links and embedded computing.', 'industries/iot-in-defence.html', PURP),
 'i-sos':     ('Industry', 'SOS & Personal Safety', 'Compact radio modules for emergency alert devices.', 'industries/sos-devices.html', ORG),
 'i-consumer':('Industry', 'Consumer IoT', 'Matter, Zigbee, BLE and Wi-Fi modules for connected products.', 'industries/consumer-iot.html', TEAL),
 'i-home':    ('Industry', 'Home Security & Automation', 'Zigbee, Matter and Wi-Fi modules for smart-home devices.', 'industries/home-security-automation.html', BLUE),
}

def ind(slug, name, crumb=None, **kw):
    d = dict(dir='industries', slug=slug, parent=('Industries', 'industries.html'), crumb=crumb or name); d.update(kw); return d
LORA_GW = ('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway')
LORA_NODE = ('LoRa Nodes & Modules', '../products.html?proto=lora')
WISUN = ('Wi-SUN Products', '../products.html?proto=wisun')
ZIGBEE = ('Zigbee / BLE Modules', '../products.html?proto=zigbee')
WIFI = ('Wi-Fi Module', '../products.html?proto=wifi')
GSM = ('4G / Cellular Gateways', '../products.html?proto=gsm')

IND_PAGES = []
A = IND_PAGES.append

# ═══ 1. ENERGY & UTILITIES  (real data: solutions + HES + metering products)
A(ind('iot-energy-utilities', 'IoT in Energy & Utilities',
 title='IoT in Energy & Utilities — Smart Metering & Grid Monitoring | Nebulae',
 desc='Nebulae IoT for utilities: Wi-SUN and LoRaWAN smart metering for electricity, gas and water, Head End Systems, and distribution-transformer monitoring.',
 keywords='smart metering, AMI, AMR, HES, Wi-SUN, LoRaWAN, transformer monitoring, IS 16444, utilities IoT',
 eyebrow='Industry · Energy & Utilities', h1='IoT in Energy & Utilities',
 lead='Wireless modules, field gateways and Head End software for smart electricity, gas and water metering, plus real-time monitoring of distribution transformers.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits'), ('arch', 'Architecture')],
 overview=dict(img='elec-hw-lineup.jpg', alt='Nebulae Wi-SUN modules, NIC card and DCU for smart metering', stats=[('250', 'Nodes per Wi-SUN DCU'), ('IS 16444', 'Meter standard'), ('5+ yr', 'AMR battery life')],
  tag='Metering · Grid', title='One Vendor from Meter to Head End',
  desc=['Nebulae supplies the radio modules, NIC cards, data concentrators and AMR devices that connect meters, and the Network Management and Head End software that collects the data.',
        'Electricity meters follow IS 16444 over Wi-SUN or RF; gas and water meters use battery-powered LoRaWAN AMR devices. Distribution transformers are monitored with the DTMS.'],
  metrics=[('Wi-SUN', 'Electricity AMI'), ('LoRaWAN', 'Gas & water AMR'), ('HES', 'Data acquisition')],
  features=[('Electricity AMI', 'Wi-SUN module, RF NIC card and DCU for IS 16444 meters'), ('Gas AMR', 'LoRaWAN retrofit with tamper and magnetic alerts'), ('Water AMR', 'Pravah 15 smart meter and AMR retrofit devices'), ('Head End Systems', 'HES for electricity, gas and water metering'), ('Transformer monitoring', 'DTMS for distribution transformers')],
  chips=[WISUN, LORA_GW, ('Smart Electric Meter', '../solutions/smart-electric-meter.html'), ('Smart Gas Meter', '../solutions/smart-gas-meter.html')]),
 products=[('nm0221i-nic', 'WPC-certified NIC card for IS 16444 smart meters.'), ('nlg8520', 'Wi-SUN FAN gateway (DCU) for up to 250 nodes, IP65, 4G LTE.'), ('nlg6770in', 'Wi-SUN DCU for up to 200 nodes, 85–528 VAC, 10 kV surge protection.'), ('amr-gas', 'Battery-powered LoRaWAN AMR for gas meters.'), ('amr-water', 'AMR device for water meters, LoRaWAN / Sigfox.'), ('nlg6x40h-in', 'IP67 8-channel LoRaWAN gateway for field networks.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Utility Applications', cols=3, items=[
   ('Smart electricity metering', 'Wi-SUN mesh networks between IS 16444 meters and data concentrators.'), ('Gas meter reading', 'Remote reading of diaphragm gas meters without site visits.'), ('Water meter reading', 'Automatic reading for municipal and industrial water meters.'),
   ('Consumption analytics', 'Head End data feeds billing and consumer apps.'), ('Distribution transformer health', 'Track loading and conditions with the DTMS.'), ('Tamper and leak alerts', 'Alerts raised at the meter and surfaced in the HES.')])],
 arch=dict(id='arch', eyebrow='Architecture', title='From Meter to Utility', layers=[('Meters and AMR devices', 'IS 16444 electricity meters, gas and water meters'), ('Radio and NIC', 'Wi-SUN / RF modules, LoRaWAN AMR'), ('Field gateway / DCU', 'Aggregates nodes; 4G LTE backhaul'), ('Head End System', 'DLMS/COSEM acquisition, REST APIs'), ('Utility systems', 'MDMS, billing, analytics')]),
 related=['electric', 'gas', 'water', 'dt'], cta=('Plan Your Metering Network', 'Talk to us about smart metering for your utility.'), accent='#ea580c'))

# ═══ 2. SMART CITY  (real data)
A(ind('smart-city-solutions', 'Smart City Solutions',
 title='Smart City IoT — Street Lighting, EV Charging & City Networks | Nebulae',
 desc='Nebulae smart-city IoT: LoRa smart street lighting, CCMS panels, CityCharge EV charging, transformer monitoring and LoRaWAN gateways.',
 keywords='smart city IoT, smart street light, CCMS, EV charging, LoRaWAN gateway, LoRa management system',
 eyebrow='Industry · Smart City', h1='Smart City IoT Solutions',
 lead='Street-light control, EV charging, utility metering and city-wide LoRaWAN connectivity from one set of hardware and software.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits'), ('arch', 'Architecture')],
 overview=dict(img='sl-cover.jpg', alt='Smart street light with Nebulae controller', stats=[('LoRaWAN', 'City-scale network'), ('CCMS', 'Feeder panels'), ('EV', 'Charging on the pole')],
  tag='Urban infrastructure', title='Connect City Assets on One Platform',
  desc=['Cities use Nebulae controllers, CCMS panels and gateways to run lighting, EV charging and metering networks that report to a common management platform.',
        'The LoRa Management System controls street lights from a map, and the CityCharge unit adds EV charging to existing lighting infrastructure.'],
  metrics=[('Lights', 'Pole, retrofit, NEMA'), ('EV', 'CityCharge unit'), ('Grid', 'DTMS monitoring')],
  features=[('Smart street lighting', 'controllers, CCMS panels and cloud management'), ('EV charging', 'CityCharge CCMS + AC charger in one unit'), ('City-wide LoRaWAN', 'multi-channel gateways, IP65 and IP67'), ('Utility metering', 'water, gas and electricity AMR/AMI'), ('Transformer monitoring', 'DTMS for distribution transformers')],
  chips=[LORA_GW, ('Smart Street Light', '../solutions/smart-street-light.html'), ('LoRa Management System', '../services/lora-management-system.html'), ('CityCharge CCMS', '../services/cms-ev-charging-management-solution.html')]),
 products=[('nlg6x40h-in', 'IP67 8-channel LoRaWAN gateway for outdoor city coverage.'), ('nlg6x40g-in', 'IP65 8-channel industrial LoRaWAN gateway, 85–528 VAC.'), ('nlg7644', 'LoRaWAN gateway with 4G LTE backhaul and GPS.'), ('nlg8140', 'Handheld LoRaWAN gateway for site surveys and field tests.'), ('afl0003', 'IP67 band-pass filter for the 865 MHz Indian ISM band.'), ('nln500a', 'Compact LoRaWAN node, up to 10 km line of sight.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='City Applications', cols=3, items=[
   ('Street lighting control', 'Schedule, dim and monitor lights from the LoRa Management System.'), ('EV charging points', 'Add charging to existing lighting panels with the CityCharge unit.'), ('Utility metering', 'Water, gas and electricity meter reading across a city.'),
   ('Transformer monitoring', 'Watch distribution transformers across the grid.'), ('Environmental and parking sensing', 'LoRa nodes for city sensors (UrbanLink platform assets).'), ('Network surveys', 'Handheld gateway to check LoRaWAN coverage on site.')])],
 arch=dict(id='arch', eyebrow='Architecture', title='City Network', layers=[('Field devices', 'Light controllers, meters, sensors, EV chargers'), ('LoRaWAN / Wi-SUN radio', 'Long-range sub-GHz links'), ('Gateways', 'LoRaWAN gateways with 4G backhaul'), ('Management platform', 'LoRa Management System, HES, UrbanLink'), ('City operations', 'Command centre and integrations')]),
 related=['street', 'cc', 'lms', 'dt'], cta=('Build Your Smart City Network', 'Tell us what your city needs to connect.'), accent='#0d9488'))

# ═══ 3. INDUSTRIAL IoT
A(ind('industrial-iot', 'Industrial IoT', 
 title='Industrial IoT (IIoT) — SCADA RTUs, Gateways & Wireless Sensing | Nebulae',
 desc='Industrial IoT hardware from Nebulae: Cortex-A7 SCADA RTU gateways with RS485 and I/O, IP65/IP67 LoRaWAN gateways, wireless modules and embedded computing.',
 keywords='industrial IoT, SCADA RTU, RS485 gateway, LoRaWAN gateway industrial, IIoT hardware, Nebulae',
 eyebrow='Industry · Industrial IoT', h1='Industrial IoT (IIoT)',
 lead='Rugged gateways, SCADA RTUs and wireless modules that connect plant equipment, sensors and remote sites to your monitoring systems.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nlg8600-board.jpg', alt='NLG8600 SCADA RTU gateway board', stats=[('RS232 / RS485', 'Industrial serial'), ('4G LTE', 'Remote backhaul'), ('IP67', 'Outdoor gateway option')],
  tag='SCADA · Gateways', title='Connect Equipment and Remote Sites',
  desc=['The NebuLink SCADA RTUs run control logic on an ARM Cortex-A7 with RS232/RS485, analog and digital I/O and 4G LTE, for remote monitoring and control.',
        'LoRaWAN gateways with IP65 or IP67 housings and 85–528 VAC input collect wireless sensor data across a site, and system-on-modules support custom industrial products.'],
  metrics=[('Cortex-A7', 'RTU processor'), ('85–528 VAC', 'Gateway input'), ('Yocto', 'SoM Linux BSP')],
  features=[('SCADA RTU gateways', 'RS232/RS485, analog and digital I/O, 4G LTE'), ('Industrial LoRaWAN gateways', 'IP65 / IP67, wide AC input, battery backup'), ('Wireless sensing', 'LoRaWAN nodes for long-range, low-power sensors'), ('Custom products', 'i.MX6ULL system-on-module with Yocto BSP'), ('Secure comms', 'SSL/TLS on the NLG8600')],
  chips=[GSM, LORA_GW, ('System on Module', '../products.html?proto=som')]),
 products=[('nlg8600', 'SCADA RTU with 4G LTE, Ethernet, RS232/RS485, analog and digital I/O, SSL/TLS.'), ('nlg8400', 'SCADA RTU with 4G LTE, RS232/RS485, analog and digital I/O.'), ('nlg6x40h-in', 'IP67 industrial 8-channel LoRaWAN gateway.'), ('nlg6x40g-in', 'IP65 industrial 8-channel LoRaWAN gateway with battery backup.'), ('sls-som-mx6', 'i.MX6ULL Cortex-A7 system on module with Yocto BSP.'), ('nln500a', 'Compact LoRaWAN node for sensor connectivity.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Industrial Applications', cols=3, items=[    # [use-case]
   ('Remote site monitoring', 'RTUs report plant and pump-station data over 4G LTE.'), ('Equipment connectivity', 'RS485 / RS232 links to PLCs, meters and instruments.'), ('Wireless sensor networks', 'LoRaWAN nodes where cabling is costly.'),
   ('Process control', 'Control logic on the RTU for local actions.'), ('Energy monitoring', 'Meter readings collected through gateways.'), ('Custom controllers', 'Build products on the i.MX6ULL SoM.')])],
 related=['i-energy', 'i-bms', 'dt', 'lns'], cta=('Connect Your Plant', 'Tell us what you need to monitor or control.'), accent='#7c3aed'))

# ═══ 4. BUILDING MANAGEMENT
A(ind('building-management-system', 'Building Management System', crumb='Building Management System (BMS)',
 title='IoT Building Management System (BMS) | Nebulae',
 desc='Wireless modules and gateways for building management: Zigbee, Matter / OpenThread, BLE and Wi-Fi modules, LoRaWAN sensing and metering.',
 keywords='building management system, BMS IoT, Zigbee module, Matter OpenThread, BLE, smart building, Nebulae',
 eyebrow='Industry · Buildings', h1='Building Management System (BMS)',
 lead='Wireless connectivity for lighting, HVAC and energy sensing in commercial buildings, from Zigbee and Matter modules to LoRaWAN sensors and meters.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln811p-module.jpg', alt='NLN811P Zigbee MG24 module', stats=[('2.4 GHz', 'Zigbee / Thread / BLE'), ('Matter', 'Supported on NLN811P'), ('LoRaWAN', 'Long-range sensing')],
  tag='Wireless · Buildings', title='Wireless Building Control and Sensing',
  desc=['Building devices need low-power radios that interoperate. Nebulae offers EFR32 modules for Zigbee, Thread / Matter and Bluetooth 5, a Wi-Fi module, and LoRaWAN nodes and gateways for longer-range or hard-to-wire locations.',
        'Meters and sensors can report through the same networks to the Head End or your building platform.'],
  metrics=[('Zigbee', 'Mesh networking'), ('BLE 5', 'Commissioning'), ('Wi-Fi', 'IP connectivity')],
  features=[('Zigbee and Thread modules', 'MG21 and MG24 based modules with PCB antenna'), ('Matter-ready module', 'NLN811P for Matter, OpenThread, Zigbee and BLE 5'), ('Wi-Fi connectivity', '2.4 GHz 802.11 b/g/n NM0442-P'), ('LoRaWAN sensing', 'nodes and gateways for meters and sensors'), ('Metering', 'electricity, gas and water AMR devices')],
  chips=[ZIGBEE, WIFI, LORA_GW]),
 products=[('nln811p', 'EFR32MG24 module for Matter, OpenThread, Zigbee and Bluetooth 5.'), ('nln111p', 'EFR32MG21 Zigbee / Thread / Bluetooth 5 module.'), ('nm0442p', '2.4 GHz Wi-Fi module, up to 150 Mbps, −40 to +105 °C.'), ('nln500a', 'LoRaWAN node for battery-powered sensors.'), ('nlg6x40g-in', 'IP65 LoRaWAN gateway for site-wide coverage.'), ('amr-water', 'AMR for water sub-metering.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Building Applications', cols=3, items=[    # [use-case]
   ('Lighting control', 'Zigbee or Thread nodes for scheduling and dimming.'), ('Environmental sensing', 'Temperature and occupancy sensors on low-power radios.'), ('Energy and water sub-metering', 'AMR devices report consumption per floor or tenant.'),
   ('Equipment status', 'Wi-Fi or LoRaWAN links from plant rooms and rooftops.'), ('Commissioning by phone', 'Bluetooth 5 for setup and diagnostics.'), ('Multi-building campuses', 'LoRaWAN gateways cover a whole campus.')])],
 related=['i-energy', 'i-home', 'i-iiot', 'lns'], cta=('Make Your Building Smarter', 'Tell us about your building and we will suggest the right radios.'), accent='#2563eb'))

# ═══ 5. TELEMATICS & FLEET
A(ind('telematics-fleet', 'Telematics & Fleet Management', crumb='Telematics & Fleet',
 title='Telematics & Fleet Management IoT | Nebulae',
 desc='Hardware for telematics and fleet tracking: 4G LTE gateways with GPS, LoRa tracking links, 434 MHz modules and an i.MX6ULL system on module.',
 keywords='telematics, fleet management IoT, GPS tracking hardware, 4G LTE gateway, LoRa tracking, Nebulae',
 eyebrow='Industry · Telematics', h1='Telematics & Fleet Management',
 lead='Cellular, GPS and LoRa building blocks for vehicle and asset tracking devices.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nlg7644-gateway.jpg', alt='NLG7644 LoRaWAN 4G gateway with GPS', stats=[('4G LTE', 'Cellular backhaul'), ('GPS', 'On NLG7644'), ('15 km', 'LoRa line of sight')],
  tag='Tracking hardware', title='Build and Connect Tracking Devices',
  desc=['Nebulae gateways combine 4G LTE with GPS for mobile and remote installations, and its LoRa and 434 MHz modules provide low-power links for tags and sensors.',
        'The i.MX6ULL system on module and the NebuLink RTUs help OEMs create vehicle and asset trackers with their own software.'],
  metrics=[('GPS', 'Position'), ('LTE', 'Uplink'), ('LoRa', 'Tag links')],
  features=[('4G LTE + GPS gateway', 'NLG7644 with 1.2 GHz Cortex-A7'), ('Cellular RTU', 'NLG8600 with 4G LTE and optional GPS'), ('Low-power tag links', 'LoRaWAN nodes and a 434 MHz module'), ('Point-to-point LoRa', 'single-channel gateway with 4G backhaul'), ('Custom tracker design', 'system on module with Yocto Linux')],
  chips=[GSM, LORA_NODE, ('System on Module', '../products.html?proto=som')]),
 products=[('nlg7644', '8-channel LoRaWAN gateway with 4G LTE, GPS and Cortex-A7.'), ('nlg8600', 'SCADA RTU with 4G LTE, Ethernet, RS485 and optional GPS.'), ('p2p-gateway', 'Single-channel LoRa gateway for point-to-point links with 4G.'), ('otag433', 'Low-cost 434 MHz proprietary-protocol module.'), ('nln500b', 'Smallest STM32WL LoRaWAN / Sigfox module.'), ('sls-som-mx6', 'i.MX6ULL system on module with Yocto BSP.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Fleet Applications', cols=3, items=[    # [use-case]
   ('Vehicle tracking', 'Cellular and GPS hardware reports position and status.'), ('Asset and trailer tracking', 'Low-power radio tags for equipment yards.'), ('Yard and depot coverage', 'LoRaWAN gateway collects tag and sensor data on site.'),
   ('Driver and vehicle data', 'RS232/RS485 interfaces for onboard equipment.'), ('OEM trackers', 'Build branded devices on the SoM and modules.'), ('Remote units', 'Battery-powered nodes for temporary assets.')])],
 related=['i-logi', 'i-sos', 'i-iiot', 'lns'], cta=('Talk to Us About Tracking', 'Tell us what you want to track and we will propose hardware.'), accent='#ea580c'))

# ═══ 6. LOGISTICS  (replaces the placeholder)
A(ind('iot-logistics', 'IoT in Logistics',
 title='IoT in Logistics — Asset Tracking & Monitoring | Nebulae',
 desc='IoT for logistics: LoRaWAN and 4G gateways with GPS, low-power nodes and tag modules for tracking assets and shipments.',
 keywords='IoT logistics, asset tracking, shipment tracking, LoRaWAN, GPS gateway, supply chain IoT, Nebulae',
 eyebrow='Industry · Logistics', h1='IoT in Logistics',
 lead='Connected nodes, tags and gateways that give logistics teams live visibility of assets, warehouses and yards.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln500a-board.jpg', alt='NLN500a LoRaWAN node', stats=[('10 km', 'LoRaWAN line of sight'), ('4G + GPS', 'NLG7644 gateway'), ('434 MHz', 'Tag module')],
  tag='Logistics', title='Visibility Across Warehouses and Yards',
  desc=['Small LoRaWAN nodes and 434 MHz tag modules report from assets, while gateways with 4G LTE and GPS move data to the cloud from warehouses, yards and vehicles.',
        'Because LoRa links are low-power and long-range, a few gateways can cover a large site.'],
  metrics=[('Nodes', 'Battery-powered'), ('Gateways', '4G + GPS'), ('Tags', 'Low cost')],
  features=[('LoRaWAN nodes', 'compact STM32WL nodes, up to 10 km LoS'), ('4G + GPS gateway', 'NLG7644 for yards and vehicles'), ('434 MHz tags', 'EZR32HG220 module, up to −133 dBm sensitivity'), ('Point-to-point links', 'single-channel LoRa gateway'), ('Field testing', 'handheld LoRaWAN gateway')],
  chips=[LORA_GW, LORA_NODE, GSM]),
 products=[('nln500a', 'Compact LoRaWAN node, 16 × 32.6 mm, up to 10 km LoS.'), ('nln500b', 'Smallest LoRaWAN / Sigfox module, 26.68 × 16 mm.'), ('otag433', '434 MHz proprietary-protocol module for low-cost tags.'), ('nlg7644', 'LoRaWAN gateway with 4G LTE and GPS.'), ('p2p-gateway', 'Single-channel LoRa gateway with 4G LTE backhaul.'), ('nlg8140', 'Handheld LoRaWAN gateway for coverage testing.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Logistics Applications', cols=3, items=[    # [use-case]
   ('Warehouse asset tracking', 'Tags on pallets and equipment report to site gateways.'), ('Yard management', 'Locate trailers and containers across a large yard.'), ('Vehicle visibility', 'Gateways with GPS and 4G on vehicles.'),
   ('Condition monitoring', 'Add sensors to nodes for conditions that matter for your goods.'), ('Exception alerts', 'Notify teams when something leaves its zone or goes off-plan.'), ('Site coverage planning', 'Survey with the handheld gateway before installing.')])],
 related=['i-tele', 'i-iiot', 'lns', 'lms'], cta=('Talk to Us About Logistics IoT', 'Tell us what you need to track and we will propose a solution.'), accent='#ea580c'))

# ═══ 7. SMART AGRICULTURE
A(ind('smart-agriculture', 'Smart Agriculture System', crumb='Smart Agriculture',
 title='Smart Agriculture IoT — Long-Range LoRaWAN Sensing | Nebulae',
 desc='Smart agriculture with LoRaWAN: low-power nodes, long-range gateways and water-meter AMR for farms, irrigation and remote monitoring.',
 keywords='smart agriculture IoT, LoRaWAN farm sensors, irrigation monitoring, precision farming, Nebulae',
 eyebrow='Industry · Agriculture', h1='Smart Agriculture System',
 lead='Long-range, low-power LoRaWAN networks for monitoring fields, water and equipment across farms.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nlg6x40h-in.jpg', alt='NLG6X40H-IN outdoor LoRaWAN gateway', stats=[('10 km', 'Node range (LoS)'), ('IP67', 'Outdoor gateway'), ('−135 dBm', 'Node sensitivity, SF12')],
  tag='LoRaWAN · Farms', title='Connect Fields Without Cabling',
  desc=['Farms cover large areas with little infrastructure. LoRaWAN lets battery-powered nodes report over long distances to a single outdoor gateway.',
        'Nebulae nodes, modules and IP65 / IP67 gateways provide the radio network, and water-meter AMR devices can report irrigation usage.'],
  metrics=[('LoRaWAN', 'Long range'), ('Battery', 'Low power'), ('IP67', 'Gateway housing')],
  features=[('Compact LoRaWAN nodes', 'STM32WL, −135 dBm at SF12, up to 10 km LoS'), ('Outdoor gateways', 'IP65 / IP67, 85–528 VAC, battery backup option'), ('Evaluation kit', 'Arduino-compatible LoRa EVK for prototyping'), ('Water AMR', 'meter reading for irrigation lines'), ('Band-pass filters', 'IP67 filters for the 865 MHz Indian ISM band')],
  chips=[LORA_GW, LORA_NODE, ('LoRa EVK', '../products.html?proto=lora&type=evk')]),
 products=[('nln500a', 'Compact LoRaWAN node for field sensors.'), ('nln500b', 'Small LoRaWAN / Sigfox module for custom sensor boards.'), ('nlg6x40h-in', 'IP67 8-channel LoRaWAN gateway for outdoor farms.'), ('nlg6x40g-in', 'IP65 8-channel gateway with battery backup.'), ('nln0651i', 'Arduino-compatible LoRa evaluation kit.'), ('amr-water', 'AMR for water meters, LoRaWAN / Sigfox.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Farm Applications', cols=3, items=[    # [use-case]
   ('Soil and weather sensing', 'Battery nodes report readings from across a farm.'), ('Irrigation monitoring', 'Track water usage and pump status.'), ('Remote pump control', 'RTUs and nodes for on/off and status.'),
   ('Greenhouse monitoring', 'Low-power sensors inside greenhouses.'), ('Cold storage monitoring', 'Report storage conditions to the farm office.'), ('Prototype quickly', 'Use the LoRa EVK to test a sensor idea.')])],
 related=['i-farm', 'water', 'lns', 'i-city'], cta=('Plan a Farm Network', 'Tell us about your farm and we will suggest the right nodes and gateways.'), accent='#059669'))

# ═══ 8. FARM & ANIMAL MANAGEMENT
A(ind('farm-animal-management', 'Farm Animal Management', crumb='Farm & Animal Management',
 title='Farm & Animal Management IoT — Livestock Tracking Hardware | Nebulae',
 desc='Compact radio modules for livestock tracking and farm management: small LoRaWAN modules, low-cost 434 MHz tags and LoRaWAN gateways.',
 keywords='livestock tracking IoT, animal monitoring, LoRa tag, 434 MHz module, farm management, Nebulae',
 eyebrow='Industry · Livestock', h1='Farm Animal Management IoT',
 lead='Small, low-power radio modules and long-range gateways for tracking and monitoring animals across farms and grazing land.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:otag433-module.jpg', alt='OTAG-433 MHz module', stats=[('26.68 × 16 mm', 'NLN500b module'), ('434 MHz', 'OTAG module'), ('LoRaWAN', 'Long range')],
  tag='Livestock', title='Small Radios for Animal-Worn Devices',
  desc=['Collars and ear tags need small, low-power radios. The NLN500b is Nebulae\'s smallest LoRaWAN / Sigfox module, and the OTAG-433 is a low-cost 434 MHz proprietary-protocol module.',
        'Gateways collect tag data at the farm, and the RS-class 4G gateways link remote sheds and pastures.'],
  metrics=[('Small', 'Module size'), ('Low power', 'Battery tags'), ('Range', 'LoRa')],
  features=[('Smallest LoRaWAN module', 'NLN500b, −136 dBm sensitivity, +21 dBm TX'), ('Low-cost tag radio', 'OTAG-433 on EZR32HG220 (Cortex-M0+)'), ('Farm gateways', 'IP65 / IP67 LoRaWAN gateways'), ('Point-to-point option', 'single-channel LoRa gateway with 4G'), ('Prototyping', 'Arduino-compatible LoRa EVK')],
  chips=[LORA_NODE, LORA_GW, ('434 MHz Module', '../products/otag433.html')]),
 products=[('nln500b', 'Smallest STM32WL module — LoRaWAN and Sigfox.'), ('otag433', 'Low-cost 434 MHz module for tags.'), ('nln500a', 'Compact LoRaWAN node.'), ('nlg6x40h-in', 'IP67 LoRaWAN gateway for the farm.'), ('p2p-gateway', 'Single-channel LoRa gateway with 4G LTE.'), ('nln0651i', 'LoRa EVK for prototyping tag firmware.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Livestock Applications', cols=3, items=[    # [use-case]
   ('Herd location', 'Tags report position or presence to farm gateways.'), ('Grazing boundaries', 'Detect animals leaving a defined area.'), ('Activity tracking', 'Add sensors to tags to follow activity.'),
   ('Shed and barn monitoring', 'Nodes report conditions inside sheds.'), ('Remote pastures', 'LoRa links plus 4G backhaul at distant sites.'), ('Custom tag development', 'Use the modules and EVK to build your own tag.')])],
 related=['i-agri', 'i-logi', 'lns', 'i-sos'], cta=('Build Your Livestock Tracker', 'Tell us what you want to monitor and we will suggest hardware.'), accent='#059669'))

# ═══ 9. HEALTHCARE
A(ind('iot-healthcare', 'IoT in Healthcare',
 title='IoT in Healthcare — Wireless Modules for Health Devices | Nebulae',
 desc='Wireless connectivity for healthcare devices: Bluetooth 5, Zigbee, Matter and Wi-Fi modules, plus compact LoRa modules for asset tracking.',
 keywords='healthcare IoT, BLE module, medical device connectivity, hospital asset tracking, Nebulae',
 eyebrow='Industry · Healthcare', h1='IoT in Healthcare',
 lead='Compact wireless modules for connected health devices and hospital equipment, from Bluetooth and Wi-Fi to LoRa asset tracking.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln811p-module.jpg', alt='NLN811P wireless module', stats=[('BLE 5', 'EFR32 modules'), ('Wi-Fi', '802.11 b/g/n'), ('−40 to +105 °C', 'NM0442-P range')],
  tag='Connected health', title='Connectivity for Health Devices',
  desc=['Nebulae module families give device makers Bluetooth 5, Zigbee, Thread / Matter and Wi-Fi connectivity in small footprints, and LoRa nodes for tracking equipment around a campus.',
        'Nebulae also provides embedded hardware and firmware design services for building the device itself.'],
  metrics=[('BLE 5', 'Wearables'), ('Wi-Fi', 'Hospital network'), ('LoRa', 'Asset tracking')],
  features=[('Bluetooth 5 modules', 'MG21 / MG24 based modules with PCB antenna'), ('Wi-Fi module', '2.4 GHz, up to 150 Mbps'), ('Matter / Thread support', 'NLN811P with AI/ML accelerator'), ('LoRaWAN tracking', 'nodes and gateways for equipment and supplies'), ('Design services', 'embedded hardware and firmware')],
  chips=[ZIGBEE, WIFI, ('IoT Product Development', '../services/iot-product-development.html')]),
 products=[('nln811p', 'MG24 module: BLE 5, Zigbee, Thread / Matter, AI/ML accelerator.'), ('nln111p', 'MG21 module: Zigbee, Thread, Bluetooth 5.'), ('nm0442p', 'Wi-Fi module, up to 150 Mbps, −40 to +105 °C.'), ('nln500b', 'Smallest LoRaWAN module for compact tags.'), ('nln500a', 'Compact LoRaWAN node for equipment tracking.'), ('sls-som-mx6', 'System on module for custom device controllers.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Healthcare Applications', cols=3, items=[    # [use-case]
   ('Wearable and handheld devices', 'Bluetooth 5 for phone connectivity and setup.'), ('Connected hospital equipment', 'Wi-Fi modules for network-connected devices.'), ('Equipment tracking', 'LoRa tags help locate carts and devices on a campus.'),
   ('Cold-chain sensing', 'Add temperature sensors to LoRa nodes for storage monitoring.'), ('Smart-home care devices', 'Matter and Zigbee for in-home sensors.'), ('Device development', 'Nebulae engineers design hardware and firmware.')])],
 related=['i-consumer', 'i-sos', 'i-bms', 'lns'], cta=('Talk to Us About Health Devices', 'Tell us about your device and we will suggest the right radio.'), accent='#2563eb'))

# ═══ 10. DEFENCE
A(ind('iot-in-defence', 'IoT in Defence',
 title='IoT in Defence — Long-Range Links & Embedded Computing | Nebulae',
 desc='Long-range LoRa links, 4G LTE gateways, IP67 enclosures and i.MX6ULL embedded computing from Nebulae for strategic and field applications.',
 keywords='defence IoT, long range wireless, LoRa gateway IP67, embedded computing, SCADA RTU, Nebulae',
 eyebrow='Industry · Defence', h1='IoT in Defence',
 lead='Long-range wireless links, ruggedly housed gateways and embedded computing building blocks for field and perimeter applications.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nlg6x40h-in.jpg', alt='NLG6X40H-IN IP67 LoRaWAN gateway', stats=[('15 km', 'LoRa line of sight (NLG7644)'), ('IP67', 'Gateway housing'), ('−40 to +105 °C', 'NM0442-P Wi-Fi module')],
  tag='Field networks', title='Connectivity Where Infrastructure Is Limited',
  desc=['LoRa links reach several kilometres line of sight at low power, IP65 / IP67 gateways can be installed outdoors, and 4G LTE or point-to-point links carry data back to a command point.',
        'Nebulae also designs custom hardware and firmware on its i.MX6ULL system on module for projects with specific requirements.'],
  metrics=[('LoRa', 'Long range'), ('IP67', 'Outdoor'), ('SoM', 'Custom builds')],
  features=[('Long-range LoRa links', 'nodes and gateways, up to 15 km LoS on NLG7644'), ('Outdoor gateways', 'IP65 / IP67 housings, 85–528 VAC'), ('4G LTE + point-to-point', 'cellular gateway and single-channel LoRa gateway'), ('Custom embedded design', 'i.MX6ULL system on module, Yocto BSP'), ('RF filtering', 'IP67 band-pass filters')],
  chips=[LORA_GW, GSM, ('System on Module', '../products.html?proto=som')]),
 products=[('nlg7644', 'LoRaWAN gateway with 4G LTE, GPS, 15 km LoS.'), ('nlg6x40h-in', 'IP67 8-channel LoRaWAN gateway.'), ('p2p-gateway', 'Single-channel LoRa point-to-point gateway.'), ('nlg8600', 'SCADA RTU with 4G LTE, Ethernet and SSL/TLS.'), ('sls-som-mx6', 'i.MX6ULL system on module with Yocto BSP.'), ('afl0001', 'IP67 band-pass filter, 863–870 MHz, 30 W.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Field Applications', cols=3, items=[    # [use-case] — Nebulae does not claim defence certifications on this page
   ('Perimeter and site sensing', 'Battery LoRa nodes report from remote points.'), ('Remote monitoring', 'RTUs and gateways link isolated sites over 4G LTE.'), ('Point-to-point links', 'Single-channel LoRa links between fixed points.'),
   ('Field coverage checks', 'Handheld LoRaWAN gateway for surveys.'), ('Asset location', 'Tags and gateways for equipment inventory.'), ('Custom embedded systems', 'Project-specific hardware on the SoM.')])],
 related=['i-iiot', 'i-tele', 'lns', 'i-logi'], cta=('Discuss Your Requirement', 'Tell us the application and constraints; we will tell you what we can support.'), accent='#7c3aed'))

# ═══ 11. SOS
A(ind('sos-devices', 'SOS & Personal Safety Devices', crumb='SOS Devices',
 title='SOS & Personal Safety Devices — Radio Modules for Emergency Alerts | Nebulae',
 desc='Compact radio modules for SOS and personal-safety devices: small LoRaWAN modules, 434 MHz tag modules, Bluetooth 5 and 4G LTE gateways.',
 keywords='SOS device IoT, personal safety, panic button LoRa, emergency alert hardware, Nebulae',
 eyebrow='Industry · Personal Safety', h1='SOS & Personal Safety Devices',
 lead='Small, battery-friendly radio modules and gateways for panic buttons, lone-worker devices and emergency alert systems.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln500b-coin-scale.png', alt='NLN500b module next to a coin for scale', stats=[('26.68 × 16 mm', 'Smallest LoRa module'), ('434 MHz', 'Low-cost tag radio'), ('BLE 5', 'Phone link')],
  tag='Safety devices', title='Radios for Alert Devices',
  desc=['An SOS device needs to be small, run for a long time on a battery and reach a receiver reliably. Nebulae\'s LoRa and 434 MHz modules are designed for low power and long range, and Bluetooth 5 modules link devices to a phone.',
        'Gateways with 4G LTE (and GPS on the NLG7644) forward alerts to your control room.'],
  metrics=[('LoRa', 'Long range'), ('BLE', 'Phone link'), ('4G', 'To control room')],
  features=[('Compact LoRaWAN module', 'NLN500b, LoRaWAN and Sigfox'), ('434 MHz tag module', 'OTAG-433, low cost'), ('Bluetooth 5', 'MG21 / MG24 modules'), ('4G + GPS gateway', 'NLG7644'), ('Design services', 'hardware and firmware for your device')],
  chips=[LORA_NODE, ZIGBEE, GSM]),
 products=[('nln500b', 'Smallest LoRaWAN / Sigfox module — fits compact devices.'), ('otag433', 'Low-cost 434 MHz proprietary-protocol module.'), ('nln111p', 'Bluetooth 5 / Zigbee / Thread module.'), ('nln811p', 'MG24 module with BLE 5 and Matter support.'), ('nlg7644', 'LoRaWAN gateway with 4G LTE and GPS.'), ('p2p-gateway', 'Single-channel LoRa gateway with 4G backhaul.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Safety Applications', cols=3, items=[    # [use-case]
   ('Panic buttons', 'A press sends an alert to a gateway or phone.'), ('Lone-worker devices', 'Wearables report status or alerts back to a control room.'), ('Campus and site alerts', 'LoRa links cover large sites with few gateways.'),
   ('Elderly care pendants', 'Low-power radios for long battery life.'), ('Vehicle alerts', 'Cellular gateway with GPS forwards location.'), ('Custom device design', 'Nebulae engineers build the hardware and firmware.')])],
 related=['i-tele', 'i-health', 'i-farm', 'lns'], cta=('Build Your Safety Device', 'Tell us about your device and range needs.'), accent='#ea580c'))

# ═══ 12. CONSUMER IoT
A(ind('consumer-iot', 'Consumer IoT Solutions', crumb='Consumer IoT',
 title='Consumer IoT — Matter, Zigbee, BLE & Wi-Fi Modules | Nebulae',
 desc='Modules and design services for connected consumer products: Matter / OpenThread, Zigbee, Bluetooth 5 and Wi-Fi modules, an Arduino-compatible LoRa kit and an i.MX6ULL SoM.',
 keywords='consumer IoT, Matter module, Zigbee, BLE, Wi-Fi module, connected product development, Nebulae',
 eyebrow='Industry · Consumer', h1='Consumer IoT Solutions',
 lead='Wireless modules and engineering services for connected consumer products, from first prototype to production.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln811p-module.jpg', alt='NLN811P Matter-ready module', stats=[('Matter', 'On NLN811P'), ('150 Mbps', 'Wi-Fi module'), ('BLE 5', 'Phone connectivity')],
  tag='Connected products', title='Radios and Design Support for Product Makers',
  desc=['Product makers can pick from Zigbee, Thread / Matter, Bluetooth 5 and Wi-Fi modules, and prototype with an Arduino-compatible LoRa kit.',
        'Nebulae\'s IoT product development, hardware, firmware and mobile-app services cover the rest of the product.'],
  metrics=[('Matter', 'Interoperable'), ('Wi-Fi', 'IP link'), ('EVK', 'Prototype')],
  features=[('Matter / OpenThread / Zigbee', 'NLN811P (EFR32MG24) with AI/ML accelerator'), ('Zigbee, Thread, BLE 5', 'NLN111P (EFR32MG21)'), ('Wi-Fi 802.11 b/g/n', 'NM0442-P, up to 150 Mbps'), ('LoRa evaluation kit', 'Arduino Nano-compatible with USB-C'), ('Product development services', 'hardware, firmware, cloud and mobile app')],
  chips=[ZIGBEE, WIFI, ('IoT Product Development', '../services/iot-product-development.html'), ('IoT Mobile App', '../services/iot-mobile-app.html')]),
 products=[('nln811p', 'MG24 module for Matter, OpenThread, Zigbee and BLE 5.'), ('nln111p', 'MG21 module for Zigbee, Thread and BLE 5.'), ('nm0442p', '2.4 GHz Wi-Fi module, up to 150 Mbps.'), ('nln0651i', 'Arduino-compatible LoRa EVK with USB-C.'), ('nln500b', 'Smallest LoRaWAN module for compact products.'), ('sls-som-mx6', 'i.MX6ULL SoM for products that need Linux.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Consumer Product Ideas', cols=3, items=[    # [use-case]
   ('Smart-home devices', 'Matter and Zigbee for sensors, switches and plugs.'), ('Wearables and accessories', 'Bluetooth 5 modules for phone-paired devices.'), ('Wi-Fi appliances', 'Add cloud connectivity with the Wi-Fi module.'),
   ('Long-range trackers', 'LoRa modules for pet or bike trackers.'), ('Prototypes and maker projects', 'The LoRa EVK works with the Arduino IDE.'), ('Linux-based devices', 'Use the SoM for display or hub products.')])],
 related=['i-home', 'i-health', 'i-sos', 'i-bms'], cta=('Start Your Connected Product', 'Tell us about your product idea.'), accent='#0d9488'))

# ═══ 13. HOME SECURITY & AUTOMATION
A(ind('home-security-automation', 'Home Security & Automation', crumb='Home Security & Automation',
 title='Home Security & Automation — Zigbee, Matter & Wi-Fi Modules | Nebulae',
 desc='Radio modules for smart-home and security devices: Zigbee, Matter / OpenThread, Bluetooth 5 and Wi-Fi modules, and LoRa for long-range sensors.',
 keywords='home automation IoT, Zigbee module, Matter module, security sensor radio, smart home hardware, Nebulae',
 eyebrow='Industry · Smart Home', h1='Home Security & Automation',
 lead='Low-power wireless modules for door and window sensors, sirens, hubs and smart-home controls.',
 pills=[('overview', 'Overview'), ('products', 'Products'), ('usecases', 'Where it fits')],
 overview=dict(img='p:nln111p-module.jpg', alt='NLN111P Zigbee module', stats=[('Zigbee', 'Mesh networking'), ('Matter', 'On NLN811P'), ('BLE 5', 'Setup and sensors')],
  tag='Smart home', title='Radios for Sensors, Hubs and Controls',
  desc=['Home security and automation devices rely on low-power mesh radios. Nebulae offers Zigbee, Thread and Matter modules, Bluetooth 5 for easy setup, a Wi-Fi module for hubs, and LoRa nodes where signals must travel further than a single home.',
        'Nebulae\'s product-development services can take a device from design to production.'],
  metrics=[('Zigbee', 'Sensors'), ('Matter', 'Interop'), ('Wi-Fi', 'Hub')],
  features=[('Zigbee / Thread / BLE', 'NLN111P module with PCB antenna'), ('Matter-ready', 'NLN811P with AI/ML accelerator'), ('Wi-Fi hub connectivity', 'NM0442-P'), ('LoRa for outbuildings', 'long-range nodes and gateways'), ('System on module', 'i.MX6ULL for hub products')],
  chips=[ZIGBEE, WIFI, LORA_NODE]),
 products=[('nln111p', 'MG21 Zigbee / Thread / Bluetooth 5 module.'), ('nln811p', 'MG24 module with Matter, OpenThread, Zigbee and BLE 5.'), ('nm0442p', '2.4 GHz Wi-Fi module.'), ('nln500a', 'LoRaWAN node for long-range outbuilding sensors.'), ('nlg6x40g-in', 'LoRaWAN gateway for larger properties.'), ('sls-som-mx6', 'System on module for hub controllers.')],
 cards=[dict(id='usecases', eyebrow='Where it fits', title='Smart-Home Applications', cols=3, items=[    # [use-case]
   ('Door and window sensors', 'Low-power Zigbee or Thread sensors.'), ('Sirens and alarms', 'Mains or battery devices on a mesh network.'), ('Smart switches and plugs', 'Matter or Zigbee for lighting and appliances.'),
   ('Hubs and gateways', 'Wi-Fi and Zigbee together on a Linux SoM.'), ('Large-property sensing', 'LoRa for gates, barns and outbuildings.'), ('Phone commissioning', 'Bluetooth 5 setup flow.')])],
 related=['i-consumer', 'i-bms', 'i-sos', 'i-health'], cta=('Build a Smart-Home Product', 'Tell us about your device and we will suggest the right module.'), accent='#2563eb'))

# merge the extra sections (challenges / detailed use cases / flow / FAQ) from industries_extra.py
from industries_extra import EXTRA as _EX
for _p in IND_PAGES:
    _p.update(_EX.get(_p['slug'], {}))
