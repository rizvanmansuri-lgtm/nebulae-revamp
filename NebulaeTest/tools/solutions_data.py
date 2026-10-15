# -*- coding: utf-8 -*-
"""Real content for solution/service pages — every fact below comes from the supplied brochures (solutions_pdfs.zip).
Source file per page is noted in a comment. Edit here and run: python3 tools/build_solutions.py"""
BLUE = ('rgba(37,99,235,.1)', '#2563eb'); ORG = ('rgba(234,88,12,.1)', '#ea580c'); TEAL = ('rgba(13,148,136,.1)', '#0d9488')
PURP = ('rgba(124,58,237,.1)', '#7c3aed'); GRN = ('rgba(16,185,129,.1)', '#059669')
RELATED = {
 'water':  ('AMI', 'Smart Water Meter', 'LoRa smart water meter (Nebulae Pravah 15) with AMR, gateway and HES.', 'solutions/smart-water-meter.html', BLUE),
 'electric': ('AMI', 'Smart Electric Meter', 'Wi-SUN / RF AMI for IS 16444 smart meters with NMS, HES and Energy+ app.', 'solutions/smart-electric-meter.html', ORG),
 'gas':    ('AMR', 'Smart Gas Meter', 'Battery-powered LoRaWAN AMR retrofit for diaphragm gas meters.', 'solutions/smart-gas-meter.html', PURP),
 'street': ('Smart City', 'Smart Street Light', 'Pole-mount, retrofit and NEMA controllers, CCMS panels and LMS software.', 'solutions/smart-street-light.html', TEAL),
 'dt':     ('DISCOM', 'Transformer Monitoring', 'DTMS: real-time electrical and sensor monitoring for distribution transformers.', 'solutions/transformer-monitoring.html', BLUE),
 'hes-e':  ('Software', 'HES — Electricity', 'Head End System for IS 16444 smart electricity meters.', 'services/hes-electricity-metering.html', ORG),
 'hes-g':  ('Software', 'HES — Gas', 'Head End System for smart gas metering networks.', 'services/hes-gas-metering.html', PURP),
 'hes-w':  ('Software', 'HES — Water', 'Head End System for smart water metering networks.', 'services/hes-water-metering.html', BLUE),
 'lms':    ('Software', 'LoRa Management System', 'Cloud platform to monitor and control street lights.', 'services/lora-management-system.html', TEAL),
 'lns':    ('Software', 'LoRaWAN Network Server', 'Network server to onboard, manage and secure LoRaWAN gateways and devices.', 'services/lorawan-network-server.html', PURP),
 'logi':   ('IoT', 'IoT in Logistics', 'Asset tracking and condition monitoring across the supply chain.', 'industries/iot-logistics.html', ORG),
 'cc':     ('Smart City', 'CityCharge CCMS + EV', 'Street-light control panel with built-in EV charging.', 'services/cms-ev-charging-management-solution.html', GRN),
}
COMMON = lambda s: s
PAGES = []

# ───────────────────────── SMART ELECTRIC METER  (Smart Metering_Wi-SUN_V1, AMR Bochure, HES FLYER, Wi-SUN HES Flyer)
PAGES.append(dict(
 dir='solutions', slug='smart-electric-meter', parent=('Solutions', 'solutions.html'), crumb='Smart Electric Meter',
 title='Smart Electric Meter Solution — Wi-SUN & RF AMI | Nebulae',
 desc='Nebulae smart electricity metering: Wi-SUN modules, RF NIC cards, Wi-SUN DCU, Network Management System, Head End System and Energy+ mobile app for IS 16444 smart meters.',
 keywords='smart electric meter, Wi-SUN AMI, IS 16444, RF NIC card, Wi-SUN DCU, head end system, HES, NMS, Energy+',
 eyebrow='Smart Metering · Electricity', h1='Smart Electric Meter',
 lead='A complete Wi-SUN and sub-GHz RF smart-metering stack for IS 16444 meters — communication modules and NIC cards, DCU gateways, Network Management System, Head End System and the Energy+ mobile app.',
 pills=[('overview', 'Overview'), ('hardware', 'Hardware'), ('software', 'Software'), ('specs', 'Specifications'), ('architecture', 'Architecture')],
 overview=dict(img='elec-hw-lineup.jpg', alt='Nebulae Wi-SUN module, high power module, RF NIC card and DCU',
  stats=[('250', 'Nodes per DCU'), ('863–876 MHz', 'Wi-SUN band'), ('IS 16444', 'Meter standard')],
  tag='Wi-SUN · RF · IS 16444', title='Smart Electricity Metering (AMI)',
  desc=['Nebulae supplies the hardware and software layers of an Advanced Metering Infrastructure: Wi-SUN protocol modules, NIC cards and DCUs in the field, and a Network Management Server, Head End System and mobile app on top.',
        'The NM0221-I Wi-SUN module is WPC certified and suited to IS 16444 smart-metering applications; its self-forming, self-healing mesh and FOTA capability allow remote security updates.'],
  metrics=[('Mesh', 'Self-forming / self-healing'), ('FOTA', 'Over-the-air updates'), ('LTE + Ethernet', 'DCU backhaul')],
  features=[('Wi-SUN module NM0221-I', 'low-power SoC module for long-range mesh connectivity; WPC certified; 1024 kB flash, 256 kB RAM'),
            ('Wi-SUN high power module NLN0725-IS', 'extended range and strong penetration, TX power up to +27/30 dBm'),
            ('RF NIC card', 'sub-GHz RF module with external antenna and interface connector for smart-meter communication'),
            ('Wi-SUN DCU NLG8520', 'Wi-SUN FAN gateway for up to 250 nodes with LTE and Ethernet backhaul and up to 6 hours battery backup'),
            ('NMS + HES + Energy+', 'network monitoring, head-end data acquisition with MDMS integration, and a consumer mobile app')],
  chips=[('NM0221-I Wi-SUN Module', '../products/nm0221i.html'), ('NLN0725-IS High Power', '../products/nln0725is.html'), ('RF NIC Card', '../products/amr-nic.html'), ('NLG8520 Wi-SUN DCU', '../products/nlg8520.html'), ('HES — Electricity', '../services/hes-electricity-metering.html')]),
 gallery=dict(id='hardware', eyebrow='Field Hardware', title='Modules, NIC Card and DCU', items=[
   ('elec-hw-lineup.jpg', 'Wi-SUN module, high power module, RF NIC card and DCU'), ('elec-dcu.jpg', 'Wi-SUN DCU NLG8520 — IP65, fibre-glass external antenna'), ('elec-nic.jpg', 'RF NIC card with sub-GHz RF module')]),
 tables=[dict(id='specs', eyebrow='Technical Specifications', title='RF NIC Card & Wi-SUN Modules', cols=[
   dict(title='RF NIC card — RF characteristics', rows=[('Transmit power', '+20 dBm'), ('Receive sensitivity (1% PER)', '−98 dBm'), ('RF range (line of sight)', '800 m'), ('Frequency band', '865 – 867 MHz'), ('CPU', '32-bit 40 MHz ARM Cortex-M4'), ('Memory', '1024 KB flash, 128 KB RAM'), ('Crystal', '38.4 MHz'), ('Operating / storage temp.', '−20 °C to +65 °C / −20 °C to +50 °C'), ('Humidity', 'Up to 95 % RH (non-condensing)')]),
   dict(title='RF NIC card — electrical', rows=[('Supply voltage', '3.3 V min, 4.2 V max'), ('Digital I/O voltage', '0.3 V to 3.3 V'), ('Current — transmit', '107 mA'), ('Current — receive', '10.2 mA'), ('Current — active mode', '70 µA'), ('Current — deep sleep', '1.5 µA')])]),
  dict(id='wisun', eyebrow='Wi-SUN Hardware', title='Module and DCU Comparison', cols=[
   dict(title='Wi-SUN modules', head=('Parameter', 'NM0221-I  /  NLN0725-IS'), rows=[('Frequency band', '863 – 876 MHz (both)'), ('Modulation', '2/4 (G)FSK with configurable shaping, OQPSK DSSS, (G)MSK, OOK TX'), ('Standard', 'IEEE 802.15.4 compliant'), ('Memory', 'Up to 1024 kB flash, 256 kB RAM'), ('Firmware update', 'Over-the-air (OTA)'), ('Antenna', 'U.FL connector for external antenna / PCB antenna feedline'), ('TX power', 'NLN0725-IS: up to +27/30 dBm'), ('Certification', 'NM0221-I: WPC certified')]),
   dict(title='Wi-SUN DCU NLG8520', rows=[('Network size', 'Up to 250 nodes on one DCU'), ('Operating system', 'Open-source embedded Linux'), ('Antenna', 'External fibre-glass, 5 dBi gain'), ('Backhaul', 'LTE and Ethernet'), ('Battery backup', 'Up to 6 hours'), ('Surge protection', '10 kV'), ('Enclosure', 'IP65, fire-retardant case'), ('Input supply', 'Wide input range — no extra over-voltage protection needed')])])],
 arch=dict(eyebrow='System Architecture', title='From Smart Meter to Billing', img='elec-ami-arch.jpg', layers=[
   ('Smart meters + Wi-SUN module / NIC card', 'IS 16444 meters, sub-GHz RF'), ('Wi-SUN DCU NLG8520', 'Mesh gateway, up to 250 nodes, LTE / Ethernet'), ('Network Management System (NMS)', 'Dashboard and RF-level network graph'), ('Head End System (HES)', 'DLMS/COSEM acquisition, REST APIs to MDMS and billing'), ('Energy+ mobile app', 'Consumption and recharge for end users')],
   note='Diagram: Energy AMI architecture from the Nebulae Smart Electricity Metering brochure.'),
 cards=[dict(id='software', eyebrow='Software Offerings', title='NMS, HES and Energy+ App', cols=4, items=[
   ('Network Management System', 'Dashboard overview of the field network and an RF-level network graph for the Wi-SUN mesh.'),
   ('Head End System (HES)', 'Centralised interface for all meter data; compatible with IS 16444 meters; GPRS and RF interfaces; prepaid and postpaid billing including net and gross metering; grid and DG consumption history; integrates with MDMS and third-party utility systems.'),
   ('Energy+ mobile app', 'Consumption and recharge information for consumers on a smartphone.'),
   ('Modules for any meter', 'Sub-GHz RF NIC cards give existing energy meters a communication path to the DCU and HES.')],
   stats=[('20,000+', 'Meters on HES'), ('1+ Lakh MW', 'Energy managed'), ('10+ Crore', 'Recharges handled')], note='HES figures as printed in the Nebulae Smart Electricity Metering brochure.')],
 related=['water', 'gas', 'street', 'dt'], cta=('Roll Out Wi-SUN Smart Metering', 'Modules, NIC cards, DCUs and the HES / NMS software — supplied and supported by one team.')))

# ───────────────────────── SMART GAS METER  (Gas AMR Datasheet, AMR Bochure, HES Gas Metering_v1)
PAGES.append(dict(
 dir='solutions', slug='smart-gas-meter', parent=('Solutions', 'solutions.html'), crumb='Smart Gas Meter',
 title='Smart Gas Meter Solution — LoRaWAN Gas AMR | Nebulae',
 desc='Nebulae gas meter AMR: plug-and-play LoRaWAN retrofit device for diaphragm gas meters with tamper and magnetic alerts, 5+ year battery life and HES for gas metering.',
 keywords='gas meter AMR, LoRaWAN gas meter, smart gas metering, retrofit AMR, HES gas metering, pulse reader',
 eyebrow='Smart Metering · Gas', h1='Smart Gas Meter',
 lead='A wireless, battery-based AMR device that retrofits onto existing diaphragm gas meters and reports consumption over LoRaWAN — managed by a Head End System for gas metering.',
 pills=[('overview', 'Overview'), ('gallery', 'In Detail'), ('specs', 'Specifications'), ('architecture', 'Architecture'), ('benefits', 'HES Advantages')],
 overview=dict(img='gas-amr-dev.jpg', alt='Nebulae Gas AMR device', stats=[('~10 km', 'LoRaWAN range (LoS)'), ('5+ yr', 'Battery life'), ('97×59×37', 'Size in mm')],
  tag='LoRaWAN · Retrofit · Tamper-proof', title='Automatic Meter Reading for Gas Meters',
  desc=['Nebulae AMR is a wireless, battery-based device for live reporting of gas consumption, with a built-in pulse detector. It installs on existing diaphragm gas meters and sends data through a single LoRaWAN gateway / DCU to Nebulae or another provider\'s LoRaWAN server.',
        'It is built on the NebuLink node NLN500a, described as the first and smallest STM32WL-based LoRaWAN module.'],
  metrics=[('Hall effect', 'Pulse counting'), ('IP65+', 'Ingress protection'), ('−20 to +85 °C', 'Operating range')],
  features=[('Plug-and-play retrofit', 'easy hook-on with screw or cable-tie; no configuration needed, sends live data at pre-configured intervals'),
            ('Accurate reading', 'incremental pulse count using Hall-effect sensing; the sensor stays on and wakes the device from sleep on a pulse'),
            ('Tamper proof', 'device-removal and magnetic-interference alerts; other operations can be disabled on a tamper event (configurable)'),
            ('Long battery life', 'replaceable non-rechargeable D-cell (Li-SOCl₂), 5+ years with deep-sleep technology'),
            ('No walk-by or drive-by', 'client–server model with multipoint communication, up to 10 km line of sight per gateway')],
  chips=[('Gas Meter AMR', '../products/amr-gas.html'), ('NLN500a LoRaWAN Node', '../products/nln500a.html'), ('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway'), ('HES — Gas', '../services/hes-gas-metering.html')]),
 gallery=dict(id='gallery', eyebrow='In Detail', title='Device, Ecosystem and Head End System', items=[
   ('gas-amr-dev.jpg', 'Nebulae Gas AMR device'), ('gas-amr-eco.jpg', 'Gas meter AMR ecosystem: meter → AMR → gateway → server → application'), ('hes-g-monitor.jpg', 'HES for gas metering dashboard')]),
 tables=[dict(id='specs', eyebrow='Technical Specifications', title='Gas AMR Device', cols=[
   dict(title='Radio & measurement', rows=[('Protocol', 'LoRaWAN (brochure also lists Sigfox)'), ('Frequency bands', 'EU 863–870, US 902–928, AU 915–928, IN865 MHz'), ('Transmit power', 'Up to +22 dBm'), ('Meter interface', 'Diaphragm magnetic / inductive pulse (Hall effect)'), ('Reporting', 'Fixed or configurable interval; sends pulse-count sum'), ('Supported meters', 'e.g. G1.6 domestic, Qmax 2.5 m³/h — 6 s / revolution'), ('Alerts', 'Battery, magnetic interference, tamper / removal')]),
   dict(title='Mechanical & environment', rows=[('Dimensions', '97 × 59 × 37 mm (customisation supported)'), ('Battery', 'Non-rechargeable D-cell Li-SOCl₂, replaceable'), ('Battery life', '5+ years'), ('Operating temperature', '−20 °C to +85 °C'), ('Ingress protection', 'IP65 or higher (self-certified)'), ('Maintenance', 'None required'), ('Installation', 'Retrofit hook — screw / cable tie')])])],
 arch=dict(eyebrow='Ecosystem', title='From Gas Meter to Utility Application', img='gas-amr-eco.jpg', layers=[
   ('Gas meter + AMR device', 'Magnetic / inductive pulse'), ('LoRaWAN gateway / DCU', 'Up to ~10 km line of sight'), ('Network server / IoT middleware', 'Nebulae private server or any LoRaWAN server'), ('HES for gas metering', 'Reads, alerts, billing data'), ('Utility application / end user', 'Dashboards, billing, consumer view')]),
 cards=[dict(id='benefits', eyebrow='HES for Gas Metering', title='What the Head End System Adds', cols=4, items=[
   ('Accurate & real-time data', 'Tracks consumption in real time, removing manual reading errors and enabling transparent billing.'),
   ('Leak detection & alerts', 'Detects leaks, pressure drops or abnormal usage and notifies consumers and the utility.'),
   ('Operational efficiency', 'Fewer field visits, demand forecasting and better infrastructure reliability.'),
   ('Safety & compliance', 'Continuous monitoring supports compliance and timely action on tampering or unsafe conditions.'),
   ('Efficient billing', 'Automated billing from actual usage; prepaid and postpaid models.'),
   ('Multi-network & multi-utility', 'Reads meters over LoRaWAN, NB-IoT, RF Mesh or GSM; one interface with electricity and water integration.')])],
 related=['water', 'electric', 'hes-g', 'dt'], cta=('Add Wireless Reading to Your Gas Meters', 'Retrofit AMR devices, LoRaWAN gateways and the gas HES from one supplier.')))

# ───────────────────────── SMART WATER METER (Smart Water Meter_V1, Water Meter Solution_V1, SLS_SinglePageWater, AMR Bochure, HES Water)
PAGES.append(dict(
 dir='solutions', slug='smart-water-meter', parent=('Solutions', 'solutions.html'), crumb='Smart Water Meter',
 title='Smart Water Meter Solution — Nebulae Pravah 15 | Nebulae',
 desc='Nebulae smart water metering: Pravah 15 LoRa smart water meter (ISO 4064), water AMR retrofit device, LoRaWAN gateway and Head End System for utilities and municipalities.',
 keywords='smart water meter, Pravah 15, LoRa water meter, ISO 4064, water AMR, HES water metering, municipal water',
 eyebrow='Smart Metering · Water', h1='Smart Water Meter',
 lead='A LoRa-based smart water meter, a retrofit AMR device, LoRaWAN gateways and a Head End System — giving utilities and municipalities accurate, real-time consumption data without manual reading.',
 pills=[('overview', 'Overview'), ('gallery', 'Ecosystem'), ('specs', 'Specifications'), ('architecture', 'Architecture'), ('benefits', 'Advantages')],
 overview=dict(img='pravah-cover.jpg', alt='Nebulae Pravah 15 smart water meter', stats=[('DN15 / DN20', 'Bore sizes'), ('Class 2', 'Accuracy'), ('5 yr', 'Battery (10 yr optional)')],
  tag='ISO 4064 · LoRa · AMR', title='Nebulae Pravah 15 Smart Water Meter',
  desc=['The LoRa-based smart water meter turns traditional metering into a connected, data-driven system for smart-city infrastructure. Low-power, long-range LoRa communication carries readings across wide urban and rural areas while the meter runs for years on a single battery.',
        'It reports to a centralised Head End System, which feeds dashboards, billing and the consumer mobile app.'],
  metrics=[('ISO 4064', 'Standard'), ('1.0 MPa', 'Max working pressure'), ('0.0001 m³', 'Least count')],
  features=[('Automatic reading', 'accurate meter reading with no manual intervention'), ('Real-time monitoring', 'usage visible on a centralised platform, dashboards and apps over secure wireless transfer'),
            ('Leakage and tamper alerts', 'abnormal usage and tampering detection, plus battery and status alerts'), ('Rugged design', 'weather-resistant meter with optimised power management and encrypted data transmission'),
            ('Open to HES', 'seamless integration with the Head End System for data management and billing')],
  chips=[('Water Meter AMR', '../products/amr-water.html'), ('NLN500a LoRaWAN Node', '../products/nln500a.html'), ('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway'), ('HES — Water', '../services/hes-water-metering.html')]),
 gallery=dict(id='gallery', eyebrow='Ecosystem', title='Meter, Gateway, HES and Mobile App', items=[
   ('pravah-meter.jpg', 'Nebulae Pravah 15 (ordering code SLS1612)'), ('pravah-eco.jpg', 'Ecosystem: meter → LoRaWAN gateway → network server → HES / app'), ('pravah-hes.jpg', 'Head End System (HES) dashboard'),
   ('wm-app.jpg', 'Citizen mobile app for consumption insight'), ('water-amr-dev.jpg', 'Water AMR retrofit device'), ('wm-products.jpg', 'Water meter AMR, LoRaWAN gateway and HES platform')]),
 tables=[dict(id='specs', eyebrow='Technical Specifications', title='Nebulae Pravah 15 Datasheet', cols=[
   dict(title='Flow & mechanical', head=('Parameter', 'DN15  /  DN20'), rows=[('Common flow Q3', '2.5 / 4 m³/h'), ('Boundary flow Q2', '0.04 / 0.064 m³/h'), ('Minimum flow Q1', '0.025 / 0.04 m³/h'), ('Overload flow Q4', '3.125 / 5 m³/h'), ('Max working pressure', '1.0 MPa'), ('Pressure-loss rating', 'Δp63'), ('Least count', '0.0001 m³'), ('Smallest data unit', '0.01 m³'), ('Full-scale reading', '99999.9999 m³')]),
   dict(title='Accuracy, electrical & environment', rows=[('Standard', 'ISO 4064'), ('Class of accuracy', 'Level 2'), ('Margin of error', 'Q1 ≤ Q < Q2: ≤ ±5 %;  Q2 ≤ Q ≤ Q4: ≤ ±2 %'), ('Flow profile sensitivity', 'U10, D5'), ('Power supply', '3.6 V disposable lithium battery pack'), ('Battery life', '5 years (10 years optional)'), ('Communication', 'LoRa (NB-IoT variant per datasheet; Wi-SUN / LTE Cat 1 bis on the IoT meter model)'), ('Working temperature', '0.1 °C – 30 °C'), ('Environmental range', '−25 °C to +70 °C'), ('Safety / EMC', 'Climate & mechanical level B · EMC rating E1')])]),
  dict(id='dimensions', eyebrow='Dimensions', title='Bore and Connection', cols=[
   dict(title='Pravah 15 dimensions', head=('Bore', 'L1 / L2 / L3 / H / W (mm) · thread'), rows=[('DN15', '165 / 255 / 14 / 130 / 104 · R 1/2'), ('DN20', '195 / 295 / 16 / 130 / 104 · R 3/4')]),
   dict(title='Water AMR retrofit device', rows=[('Dimensions', '97 × 59 × 37 mm'), ('Meter interface', 'Magnetic / inductive / RS-485 pulse'), ('Radio', 'LoRaWAN / Sigfox'), ('Battery life', '5+ years, deep-sleep technology'), ('Operating temperature', '−20 °C to +65 °C'), ('Ingress protection', 'IP65 (self-certified)')])])],
 arch=dict(eyebrow='Ecosystem', title='Four Layers, One Platform', img='wm-eco.jpg', layers=[
   ('Device layer', 'Smart water meter or water AMR on existing meter'), ('Network layer', 'LoRaWAN gateway and network server'), ('Application layer', 'Head End System (HES) — device and meter monitoring, consumption analytics, system management'), ('User interface', 'HES dashboard for officials; mobile app for households')]),
 cards=[dict(id='benefits', eyebrow='Advantages', title='For Households and for Utilities', cols=4, items=[
   ('Citizen engagement', 'Mobile app shows households their consumption so they can manage usage responsibly.'), ('Low-maintenance operation', 'Long battery life reduces field visits and service disruption.'), ('Billing transparency', 'Accurate, transparent billing improves ROI and customer trust.'), ('Smart maintenance data', 'Alerts and trends point maintenance where it is needed.'),
   ('Better resource planning', 'Usage trends and alerts help manage distribution and long-term planning.'), ('Central visibility', 'One dashboard for consumption, system health and alerts across all meters.'), ('Fewer billing disputes', 'Automated data builds trust through accurate, timely metering.'), ('Faster response', 'Quicker detection of leaks, tampering or supply issues reduces wastage.')],
   note='Applications: residential apartments, smart-city projects, commercial complexes, municipal water supply and industrial facilities.')],
 related=['gas', 'electric', 'hes-w', 'street'], cta=('Bring Smart Metering to Your Water Network', 'Meters, retrofit AMR, gateways and HES — designed and supported by Nebulae.')))

# ───────────────────────── SMART STREET LIGHT (Pole Mount & Retrofit, ILC NEMA, CCMS Brochure_V2, LMS_V1)
PAGES.append(dict(
 dir='solutions', slug='smart-street-light', parent=('Solutions', 'solutions.html'), crumb='Smart Street Light',
 title='Smart Street Light Solution — Controllers, CCMS & LMS | Nebulae',
 desc='ViaLights smart street lighting: pole-mount, retrofit and NEMA LoRaWAN / 4G controllers, CCMS feeder panels and a cloud LoRa Management System for municipalities.',
 keywords='smart street light, ViaLights, NEMA lighting controller, LoRaWAN street light, CCMS, lighting management system, LMS',
 eyebrow='Smart City · Street Lighting', h1='Smart Street Light',
 lead='Controllers for every luminaire, feeder-level CCMS panels and a vendor-neutral LoRa Management System — manage schedules, dimming, energy and faults for a whole city from one platform.',
 pills=[('overview', 'Overview'), ('gallery', 'Products'), ('specs', 'Specifications'), ('ccms', 'CCMS'), ('architecture', 'Platform')],
 overview=dict(img='sl-cover.jpg', alt='ViaLights smart street light controller on a street light', stats=[('0–10 V / PWM', 'Dimming'), ('10 km', 'LoRaWAN range (LoS)'), ('10 schedules', 'Per controller')],
  tag='LoRaWAN · 4G · NEMA', title='Smart Street Lighting System',
  desc=['The controller manages ON/OFF schedules, monitors temperature and offers over- and under-voltage protection. It measures power, energy, current and voltage so energy consumption can be tracked and optimised.',
        'Three product families cover every installation: pole-mount / retrofit controllers, NEMA (7-pin) intelligent lighting controllers with LoRaWAN or 4G, and CCMS feeder panels — all managed from the ViaLights LoRa Management System.'],
  metrics=[('LoRaWAN / 4G', 'Connectivity'), ('IP65 / IP66', 'Enclosures'), ('90–528 VAC', 'Supply range')],
  features=[('Remote control', 'manual and configurable ON / OFF / dimming schedules'), ('Power measurement', 'voltage, current, frequency, power factor, kW and kWh'), ('Dimming control', '0–10 VDC and PWM, up to 10 configurable schedules, LDR input on the pole-mount variant'),
            ('Grouping & fault monitoring', 'group-wise control; lamp burnout, abnormal power, low power factor reported to the cloud'), ('Alerts', 'e-mail or SMS notification as soon as a fault occurs')],
  chips=[('Browse LoRaWAN Gateways', '../products.html?proto=lora&type=gateway'), ('LoRa Modules', '../products.html?proto=lora&type=module'), ('LoRa Management System', '../services/lora-management-system.html'), ('CityCharge CCMS + EV', '../services/cms-ev-charging-management-solution.html')]),
 gallery=dict(id='gallery', eyebrow='Product Range', title='Controllers, CCMS Panel and LMS', items=[
   ('sl-ctrl.jpg', 'Pole-mount & retrofit street light controller'), ('sl-nema.jpg', 'NEMA intelligent lighting controller (LoRaWAN | 4G)'), ('sl-nema-pole.jpg', 'NEMA controller on a street-light pole'),
   ('ccms-box.jpg', 'CCMS feeder control panel'), ('ccms-eco.jpg', 'CCMS ecosystem'), ('lms-ui.jpg', 'LoRa Management System dashboard')]),
 tables=[dict(id='specs', eyebrow='Technical Specifications', title='Street Light Controllers', tabs=[
   ('Pole Mount & Retrofit', [('Processor', 'Cortex-M4 STM32WL 32-bit, 48 MHz'), ('Protocol', 'LoRaWAN, AES-128 (MAC and application)'), ('Frequency', '865–867 MHz, 902–915 MHz'), ('Open-field range', 'Up to 10,000 m (LoS)'), ('Data rate / TX power', '37.5 kbps max / +20 dBm'), ('RX sensitivity', '−128 dBm'), ('Mounting / enclosure', 'Retrofit or pole mount; IP65 (pole mount), polycarbonate'), ('Dimensions (L×W×H)', 'Pole mount 160×80×55 mm · Retrofit 168.53×74.62×40 mm'), ('Weight', '~250 g (pole mount) · ~200 g (retrofit)'), ('Supply', 'Single phase, 90–528 VAC, 50/60 Hz'), ('Switching load', '10 A, 230 VAC; high-voltage cut-off 290 VAC'), ('Surge protection', 'IEC/EN 61000-4-5, 10 kV'), ('Operating temp. / humidity', '−10 °C to +60 °C / 10–90 % RH'), ('Ambient sensor', 'Light sensing to switch lamp ON/OFF'), ('Certification', 'IEC/EN 61000-4-5 surge · WPC LoRaWAN module')]),
   ('NEMA ILC — LoRaWAN', [('Processor', 'Cortex-M4 STM32WL 32-bit, 48 MHz'), ('Antenna', 'Internal'), ('Mounting / enclosure', 'NEMA 7-pin standard, transparent-grey; IP66'), ('Protocol', 'LoRaWAN, AES-128 (MAC and application)'), ('Frequency', '865–867 MHz, 902–915 MHz'), ('Range / data rate', 'Up to 10,000 m (LoS) / 37.5 kbps max'), ('TX power / RX sensitivity', '+20 dBm / −135 dBm (SF12)'), ('Supply', 'Single phase, 90–528 VAC, 50/60 Hz'), ('Switching load', '10 A, 230 VAC; cut-off 290 VAC'), ('Surge protection', 'IEC/EN 61000-4-5, 10 kV'), ('Operating temp. / humidity', '−10 °C to +60 °C / 10–90 % RH'), ('Certification', 'IEC/EN 61000-4-5 · WPC LoRaWAN module')]),
   ('NEMA ILC — 4G', [('Processor / module', 'A7672S-FASE (SIMCom)'), ('Antenna', 'Internal flexible PCB antenna'), ('Mounting / enclosure', 'NEMA 7-pin standard, transparent-grey; IP66'), ('Protocol', 'GSM / GPRS (4G / LTE) with 2G fallback'), ('Response / update', 'Operation response < 5 s · data update on LMS < 10 min'), ('Server update frequency', 'Every 15 min (configurable up to 1 min)'), ('Diagnostics', 'Self-diagnostic check'), ('Supply', 'Single phase, 176–528 VAC, 50/60 Hz'), ('Switching load', '10 A, 230 VAC; cut-off 290 VAC'), ('Surge protection', 'IEC/EN 61000-4-5, 10 kV'), ('Operating temp. / humidity', '−10 °C to +60 °C / 10–90 % RH'), ('Ambient sensor', 'Light sensing to switch lamp ON/OFF')])],
   note='Common monitoring: voltage, current, power factor, frequency, power (kW) and energy (kWh). Notifications: lamp over-voltage, under-voltage, light fault, meter-chip fault, relay fault.')],
 arch=dict(eyebrow='Platform', title='Lamp to Command Centre', layers=[
   ('Luminaire controller', 'Pole mount · retrofit · NEMA 7-pin'), ('LoRaWAN gateway or 4G', 'LPWAN with deep coverage, or cellular backhaul'), ('Feeder CCMS panel (optional)', '30–50 poles per feeder, 4G to the internet'), ('LoRa Management System', 'Cloud or on-premise; vendor-neutral'), ('Command centre / integrations', 'Web API for third-party systems')],
   note='The LMS supports smart / NEMA-ready and non-NEMA lights of all major brands.'),
 cards=[dict(id='ccms', eyebrow='Feeder Control Panel', title='Centralised Control & Monitoring System (CCMS)', cols=4, items=[
   ('Feeder-level control', 'One panel controls a group of typically 30–50 poles and connects to the internet over 4G; designed for street-lighting projects in India.'), ('All lamp types', 'Applies to LED, HID, CFL, FTL and induction luminaires.'), ('Safe & resilient', 'Bypass switch for fail-safe operation, 4 hours RTU battery backup, offline data storage up to 6 months, over-voltage load cut-off.'),
   ('Scheduling', 'Remote ON/OFF, astronomical or independent schedules, timer-based scheduling, 100-year calendar RTC with battery backup.'), ('Alerts', 'Input/output power failure, contactor failure, power theft, earth leakage, high/low voltage, tilt, high temperature, low power factor, door open, low battery, meter communication fault.'), ('Secure & open', 'Secure, tamper-proof communication, FOTA firmware updates and third-party web-API integration.')],
   note='CCMS specification: EC20 4G module, external antenna, IP54 / IK08 cabinet, single or three phase 90–440 VAC, 40 A per phase (customisable), Type-2 40 kA surge protection, IS 13779 Class 1 energy meter (RS-485 / RS-232), −10 °C to +55 °C.'),
  dict(id='lms', eyebrow='LoRa Management System', title='Cloud Software for the Whole Network', cols=4, items=[
   ('Map-based control', 'Live device location on a map; group and individual control.'), ('Light planner', 'Scheduling and dimming plans per group or light.'), ('Ticketing & maintenance', 'Automatic failure detection with integrated work-order management and an escalation matrix.'), ('Dashboards & reports', 'Interactive dashboard, comprehensive reporting and analytics, asset tracking.'),
   ('Alerts & notifications', 'Instant notice of failures and abnormalities.'), ('Access control', 'Advanced user and access management with top-tier security.'), ('Flexible deployment', 'Cloud or on-premise; SaaS or one-time licence.'), ('Easy integration', 'Connects to the command centre.')])],
 related=['dt', 'hes-e', 'lms', 'cc'], cta=('Make Your Street Lighting Smart', 'Controllers, CCMS panels and the management platform — from one team.')))

# ───────────────────────── TRANSFORMER MONITORING (DTMS Brochure Version 2, Transformer_Monitoring_Profile)
PAGES.append(dict(
 dir='solutions', slug='transformer-monitoring', parent=('Solutions', 'solutions.html'), crumb='Transformer Monitoring',
 title='Distribution Transformer Monitoring System (DTMS) | Nebulae',
 desc='Nebulae DTMS: real-time monitoring of distribution transformers — voltage, current, harmonics up to 60, oil level and temperature — with firmware, portal and mobile app.',
 keywords='transformer monitoring system, DTMS, distribution transformer, DT monitoring, Rogowski coil, harmonics, oil level',
 eyebrow='Power Utilities · Grid Asset Monitoring', h1='Transformer Monitoring System',
 lead='Real-time monitoring of distribution transformers with direct electrical measurement and leading-indicator sensors — replacing periodic site visits with live data, alarms and trends.',
 pills=[('overview', 'Overview'), ('gallery', 'Hardware'), ('specs', 'Specifications'), ('architecture', 'Architecture'), ('benefits', 'Benefits')],
 overview=dict(img='dtms-unit.jpg', alt='Nebulae DTMS unit', stats=[('60', 'Harmonics measured'), ('2500 A', 'Rogowski coil range'), ('4–5 h', 'Battery backup')],
  tag='DISCOM · Asset Monitoring', title='Distribution Transformer Monitoring System',
  desc=['Conventional monitoring relies on periodic inspections and site visits with portable instruments — slow, dependent on skills and equipment, and a cause of downtime and transformer burn-outs. The DTMS measures electrical parameters and field sensors continuously and sends them to a central server.',
        'It takes its supply from any phase of the DT secondary, so no additional power input is required.'],
  metrics=[('GSM', 'Built-in module'), ('3-phase 4-wire', 'Compatible'), ('4–20 mA', 'Extra field sensors')],
  features=[('Electrical parameters', 'three-phase voltage, current, frequency, phase angle, active / reactive / apparent power, power factor, THD and harmonics up to 60'), ('Physical parameters', 'oil temperature, winding temperature, oil level, LV-side lug temperature'),
            ('Rogowski coil sensors', 'clamp-on installation without shutdown, up to 2500 A'), ('Alarm & fault management', 'predicts abnormal conditions, raises alarms for over-voltage, over-current and phase imbalance'),
            ('Connectivity', 'GSM, GPS, Bluetooth, RS-485 and Ethernet interfaces')],
  chips=[('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway'), ('NebuLink Modules', '../products.html'), ('Request a Demo', '../contact.html')]),
 gallery=dict(id='gallery', eyebrow='Hardware & Software', title='Unit, Sensors, Ecosystem and Portal', items=[
   ('dtms-unit.jpg', 'DTMS monitoring unit'), ('dtms-sensors.jpg', 'Compatible sensors: oil level, oil temperature, current, ambient temperature'), ('tms-sensors.jpg', 'Field sensors: Rogowski coil, oil-level sensor, PT100 sensor'),
   ('dtms-eco.jpg', 'DTMS ecosystem'), ('dtms-portal.jpg', 'DTMS smart portal'), ('tms-portal1.jpg', 'Portal map view of installed transformers')]),
 tables=[dict(id='specs', eyebrow='Technical Specifications', title='DTMS Unit', cols=[
   dict(title='Inputs, outputs & communication', rows=[('Communication', 'Inbuilt GSM module; GPS, Bluetooth, RS-485, Ethernet'), ('Harmonics measurement', 'Up to 60 harmonics'), ('Analog inputs', '4 channels, 4–20 mA'), ('Digital inputs', '4 channels optically isolated, 24 V to 110 V; 3 channels for oil-level measurement'), ('Digital outputs', '2 relay outputs up to 10 A (potential-free contacts)'), ('Current sensing', 'Rogowski coil (CT) up to 2500 A, no shutdown'), ('Supported system', 'Three-phase 4-wire')]),
   dict(title='Power & sensors', rows=[('Power supply', 'From any phase of the DT secondary'), ('Backup battery', 'Li-ion with charging circuit, 4–5 hours'), ('Field sensors', 'Oil level, oil temperature, winding / palm temperature, ambient temperature, humidity, vibration, current'), ('Firmware', 'Over-voltage, over-current and phase-imbalance logic; data validation; mobile-app link'), ('Mobile app', 'Bluetooth local access for installation, commissioning and servicing'), ('Portal', 'User, data, alarm, fault and transformer management')])])],
 arch=dict(eyebrow='Ecosystem', title='From Transformer to Portal', img='dtms-eco.jpg', layers=[
   ('DTMS unit at the transformer', 'Metering chip, ADC and sensors'), ('Gateway / GSM', 'Regular uploads of sensor and energy data'), ('Cloud server', 'Collection, validation, storage'), ('DTMS smart portal', 'Graphs, alarms and fault management'), ('Mobile application', 'Local commissioning and fault isolation over Bluetooth')]),
 cards=[dict(id='benefits', eyebrow='Why Monitor Transformers', title='Benefits for Utilities', cols=4, items=[
   ('Better reliability', 'Improves transformer reliability and reduces DT downtime.'), ('Live visibility', 'Real-time and trend monitoring of many transformers at once.'), ('Lower losses', 'Detects abrupt load changes and supports reducing technical losses and demand charges.'), ('No extra DTR meter', 'The unit also measures energy, so no separate DTR meter needs to be installed.'),
   ('Faster maintenance', 'Failed transformers are detected and O&M routed to them.'), ('Digital records', 'Records of replaced and to-be-procured transformers support inventory planning.'), ('Roadmap', 'Geo-location based predictive analysis, AI-based energy-consumption prediction and oil-quality sensors are listed as upcoming features.'), ('Phone-based service', 'Identify and isolate faults on site from a phone.')],
   stats=[('6–8 lakh', 'DTs fail every year in India'), ('15–20 %', 'DT failure rate in India'), ('1–2 %', 'In developed countries')],
   note='Industry figures as cited in the Nebulae Transformer Monitoring System profile (source cited there: ica.org). The profile also estimates a 3–5 % reduction in failure rate, ~2 % inventory reduction and ₹10,000–15,000 saving per DT by avoiding an extra DTR meter; these are Nebulae estimates, not guarantees.')],
 related=['street', 'electric', 'hes-e', 'gas'], cta=('Protect Your Distribution Transformers', 'Talk to us about DTMS units, sensors, portal and mobile app for your DISCOM.')))

# ───────────────────────── SERVICES: HES ×3, LMS, CityCharge CCMS
def hes(slug, kind, name, pdfnote, img1, tag, lead, funcs, feats, advs, hero_alt, extra_img, accent, rel):
    return dict(dir='services', slug=slug, parent=('Services', 'services.html'), crumb=f'HES — {name}',
      title=f'HES for {name} Metering — Head End System | Nebulae',
      desc=f'Nebulae Head End System (HES) for {name.lower()} metering: collect meter data, send commands, billing and alerts over secure, scalable AMR / AMI networks.',
      keywords=f'HES {name.lower()} metering, head end system, AMI, AMR, DLMS COSEM, smart {name.lower()} meter software',
      eyebrow='Software · Head End System', h1=f'HES for {name} Metering', lead=lead,
      pills=[('overview', 'Overview'), ('gallery', 'Dashboard'), ('benefits', 'Advantages')],
      overview=dict(img=img1, alt=hero_alt, stats=tag[0], tag=tag[1], title=f'Head End System for {name} Metering', desc=funcs, metrics=tag[2],
        features=feats, chips=[('Browse Products', '../products.html')] + extra_img, ),
      gallery=dict(id='gallery', eyebrow='Platform', title='Dashboard and Data Acquisition', items=pdfnote),
      cards=[dict(id='benefits', eyebrow='Advantages', title=f'What HES Delivers for {name} Utilities', cols=4, items=advs)],
      related=rel, cta=(f'Run Your {name} Metering Network on HES', 'Secure, scalable data acquisition from field meters to billing and analytics.'), accent=accent)

PAGES.append(hes('hes-electricity-metering', 'e', 'Electricity', [('hes-e-monitor.jpg', 'HES — smart metering dashboard'), ('hes-e-arch.jpg', 'Data acquisition: retrofit, GPRS, LoRa and RF meters → gateways → HES cloud → DISCOM'), ('elec-hes-dash.jpg', 'HES dashboard overview'), ('hes-wisun-monitor.jpg', 'HES for Wi-SUN')],
 'hes-e-monitor.jpg', ([('IS 16444', 'Compatible meters'), ('DLMS/COSEM', 'Meter protocol'), ('REST APIs', 'Integration')], 'IS 16444 · DLMS/COSEM · LoRaWAN · Wi-SUN', [('RF · 2G/3G', 'Connectivity'), ('LoRaWAN', 'DLMS over LoRa'), ('Wi-SUN', 'Via gateways')]),
 'A scalable head-end data acquisition solution for Advanced Metering Infrastructure: an IoT-based software layer between field meters and MDM, billing and enterprise systems.',
 ['The HES monitors and controls smart meters as a communication driver between MDM systems and measurement devices. It collects system-wide telemetry, integrates with smart energy devices and supports remote device management.'],
 [('Platform-wide connectivity', 'between field devices and enterprise-level software; manages and stores acquired meter data'), ('REST API integration', 'with billing, data management and enterprise AMI applications, plus standard connectors for third-party MDM and billing'), ('IS 16444 meters', 'DLMS/COSEM data acquisition over RF, 2G/3G, LoRaWAN and Wi-SUN'),
  ('DLMS over LoRaWAN', 'fragmentation and de-fragmentation of large DLMS frames through LoRa gateways and servers'), ('Remote management', 'configuration, firmware upgrade, identity and access management of field devices'), ('Prepaid & postpaid billing', 'including net and gross metering, with grid and DG consumption history')],
 [('Friendly dashboards', 'Collected data shown in a GUI for internal users and consumers.'), ('Site-specific insight', 'Information that supports business decisions.'), ('Network protection', 'Manages gateways to prevent overload.'), ('Scale', 'Monitors, analyses and manages numerous field meters and gateways.')],
 'HES for smart electricity metering', [('Electric Meter Solution', '../solutions/smart-electric-meter.html')], '#4f46e5', ['electric', 'hes-g', 'hes-w', 'dt']))

PAGES.append(hes('hes-gas-metering', 'g', 'Gas', [('hes-g-monitor.jpg', 'HES for gas metering dashboard'), ('hes-arch.jpg', 'Data acquisition: retrofit, GPRS, LoRa and RF meters, gas and water meters → HES cloud'), ('gas-amr-eco.jpg', 'Gas meter AMR ecosystem')],
 'hes-g-monitor.jpg', ([('LoRaWAN', 'Networks'), ('NB-IoT', 'Networks'), ('RF Mesh · GSM', 'Networks')], 'AMR · AMI · Multi-utility', [('Real-time', 'And scheduled reads'), ('Alerts', 'Leak · tamper · pressure'), ('Prepaid / Postpaid', 'Billing models')]),
 'The central intelligence hub of a smart gas metering network — secure, reliable data exchange between field meters and utility platforms.',
 ['The Head-End System communicates with smart gas meters across residential, commercial and industrial areas to collect consumption data, send remote commands and deliver real-time insight into the gas distribution system, whether integrated with AMR or AMI.'],
 [('Unified interface', 'manage gas metering from one place, with multi-utility integration (electricity, water, etc.)'), ('Real-time and scheduled reading', 'from all endpoints with a secure, scalable data infrastructure'), ('Automated acquisition', 'from thousands of smart gas meters over LoRaWAN, NB-IoT, RF Mesh or GSM'),
  ('Pressure and flow monitoring', 'pressure drops and flow anomalies, helping reduce unaccounted gas'), ('Tamper & abnormal-usage alerts', 'real-time detection for swift corrective action'), ('Automated billing', 'from real consumption data, with customisable reports for operations and regulators')],
 [('Accurate & real-time data', 'Removes manual errors and enables transparent billing.'), ('Leak detection & alerts', 'Identifies leaks, pressure drops or abnormal usage and notifies consumers and the utility.'), ('Operational efficiency', 'Fewer field visits; supports demand forecasting and reliability.'), ('Safety & compliance', 'Continuous monitoring supports compliance and timely action.'), ('Efficient billing', 'Prepaid and postpaid support.')],
 'HES for gas metering', [('Gas Meter Solution', '../solutions/smart-gas-meter.html')], '#7c3aed', ['gas', 'hes-e', 'hes-w', 'electric']))

PAGES.append(hes('hes-water-metering', 'w', 'Water', [('hes-w-monitor.jpg', 'HES for water metering dashboard'), ('pravah-hes.jpg', 'HES dashboard for Nebulae Pravah 15 smart water meters'), ('hes-arch.jpg', 'Data acquisition: field meters and gateways → HES cloud → utility'), ('wm-hes.jpg', 'Head End System (HES) — water meter solution')],
 'hes-w-monitor.jpg', ([('LoRaWAN', 'Networks'), ('NB-IoT', 'Networks'), ('RF Mesh · GSM', 'Networks')], 'AMR · AMI · Smart City Water', [('Real-time', 'And scheduled reads'), ('Alerts', 'Leak · tamper · abnormal use'), ('Prepaid / Postpaid', 'Billing models')]),
 'The command centre of a smart water metering network — unified, secure communication between meters and utility platforms.',
 ['The Head-End System communicates with smart meters deployed across residential, commercial and industrial zones to gather usage data, send commands and give real-time visibility into the water distribution ecosystem, whether integrated with AMR or AMI.'],
 [('Unified interface', 'manage water metering from one place, with multi-utility integration (electricity, gas, etc.)'), ('Real-time and scheduled reading', 'from all endpoints into one secure, scalable repository'), ('Automated acquisition', 'from thousands of smart water meters over LoRaWAN, NB-IoT, RF Mesh or GSM'),
  ('Flow anomaly detection', 'identifies unexpected continuous flow or backflow, reducing non-revenue water'), ('Event alerts', 'leaks, tampering, abnormal usage and system faults'), ('Automated billing', 'accurate bills from real-time usage; prepaid and postpaid models')],
 [('Accurate & real-time data', 'Eliminates manual reading errors and estimated billing.'), ('Leak detection & alerts', 'Alerts users and the utility to prevent water loss and damage.'), ('Operational efficiency', 'Lower manpower and operating cost; demand forecasting and resource allocation.'), ('Water conservation', 'Usage insights and alerts help spot overconsumption and savings areas.'), ('Efficient billing', 'Billing based on actual consumption.')],
 'HES for water metering', [('Water Meter Solution', '../solutions/smart-water-meter.html')], '#2563eb', ['water', 'hes-e', 'hes-g', 'street']))

# LMS  (LMS_V1)
PAGES.append(dict(dir='services', slug='lora-management-system', parent=('Services', 'services.html'), crumb='LoRa Management System',
 title='LoRa Management System (LMS) for Street Lights | Nebulae',
 desc='LoRa Management System (LMS) by Nebulae: cloud-based, vendor-neutral platform for monitoring and controlling street lights with maps, scheduling, ticketing, analytics and alerts.',
 keywords='LoRa management system, lighting management system, LMS, street light management software, vendor neutral, ViaLights, CMS',
 eyebrow='Software · Street Lighting', h1='LoRa Management System (LMS)',
 lead='A cost-effective, cloud-based platform that gives municipalities complete control over street-light infrastructure — real-time monitoring, dashboards, analytics, inventory and maintenance in one place.',
 pills=[('overview', 'Overview'), ('benefits', 'Why LMS'), ('benefits2', 'Benefits')],
 overview=dict(img='lms-ui.jpg', alt='LoRa Management System dashboard, live map and ticketing', stats=[('Vendor', 'Neutral'), ('Cloud', 'Or on-premise'), ('SaaS', 'Or one-time licence')],
  tag='Cloud · Vendor-neutral', title='Street Light Management System',
  desc=['The LMS gives complete control over street-light infrastructure with real-time monitoring, insightful dashboards and advanced analytics to optimise energy consumption and streamline operations.',
        'It also covers inventory management, task allocation and maintenance planning. As a vendor-neutral solution it supports all street-light brands and suits both upgrades and new deployments, with automatic failure detection and an integrated work-order module.'],
  metrics=[('Map', 'Live device location'), ('Planner', 'Light scheduling'), ('Tickets', 'Escalation matrix')],
  features=[('Live location map', 'see and control devices on a map'), ('Group and individual control', 'switch and dim lights singly or in groups'), ('Light planner & scheduling', 'scheduled dimming and controllability'), ('Ticket management', 'escalation matrix and integrated work orders'), ('Alerts & notifications', 'automatic detection of failures and abnormalities'), ('Reporting & analytics', 'interactive dashboard, asset tracking and comprehensive reports')],
  chips=[('Smart Street Light Solution', '../solutions/smart-street-light.html'), ('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway')]),
 gallery=dict(id='gallery', eyebrow='Platform', title='Dashboard, Map and Ticketing', items=[('lms-ui.jpg', 'Interactive device dashboard, live location map and ticket management'), ('ccms-dash.jpg', 'CCMS dashboard — energy comparison, daily consumption and device status')]),
 cards=[dict(id='benefits', eyebrow='Why LMS', title='Why Choose ViaLights LMS', cols=4, items=[
   ('Manage all lighting types', 'Smart / NEMA-ready and non-NEMA lights.'), ('Reduce maintenance cost', 'Automated detection of failures and abnormalities.'), ('Vendor neutral', 'Supports all major brands.'), ('Troubleshoot quickly', 'Automatic failure detection with integrated work-order management.'), ('Optimise energy', 'Scheduled dimming and controllability.'), ('Flexible deployment', 'Cloud or on-premise; SaaS or one-time licence.')]),
  dict(id='benefits2', eyebrow='Benefits', title='What You Get', cols=3, items=[('Map-based interaction', 'Direct interaction with lights on a map.'), ('Ticketing & maintenance automation', 'Work orders and escalations built in.'), ('Analytics & reports', 'In-depth analytics and customisable reports.'), ('Top-notch security', 'Safety and confidentiality of your data.'), ('User & access management', 'Advanced roles and permissions.'), ('Cabinet (group) control', 'Control by cabinet or group.'), ('Alerts & notifications', 'Instant notice of faults.'), ('Command-centre integration', 'Easy integration with a command centre.')])],
 related=['street', 'cc', 'dt', 'hes-e'], cta=('See the LMS in Action', 'Request a demo of the LoRa Management System for your city.')))

# CityCharge CCMS + EV  (CityCharge-CCMS-Unit, CCMS Brochure_V2)
PAGES.append(dict(dir='services', slug='cms-ev-charging-management-solution', parent=('Services', 'services.html'), crumb='CityCharge CCMS + EV Charging',
 title='CityCharge CCMS Unit — Street Light Control with EV Charging | Nebulae',
 desc='CityCharge CCMS unit combines a street-light control panel with an AC EV charger, using existing CCMS infrastructure for a revenue-generating smart-city asset.',
 keywords='CityCharge CCMS, EV charging, street light control panel, smart city EV, UrbanLink, CMS EV charging',
 eyebrow='Smart City · EV Charging', h1='CityCharge CCMS + EV Charger',
 lead='One compact unit that adds EV charging to a street-lighting control panel — efficient, scalable, revenue-generating and ready for smart-city projects.',
 pills=[('overview', 'Overview'), ('economics', 'Economics'), ('benefits', 'Benefits'), ('platform', 'Platform')],
 overview=dict(img='cc-unit.jpg', alt='CityCharge CCMS unit with EV charger on a street', stats=[('2', 'Utility sockets'), ('RFID / App', 'Access'), ('CCMS + EV', 'In one unit')],
  tag='CCMS · AC EV Charging', title='CCMS + EV Charger in One Unit',
  desc=['The CityCharge CCMS Unit leverages existing CCMS infrastructure to add EV charging without additional cabling or control systems. It turns lighting infrastructure into a revenue-generating platform through paid EV charging and socket usage.',
        'It suits smart-city projects that integrate smart lighting and smart mobility under one centralised platform.'],
  metrics=[('Plug & charge', 'RFID or mobile app'), ('Load mgmt', 'EV vs CCMS'), ('Outdoor', 'Weather-resistant')],
  features=[('User-friendly', 'simple plug-and-charge with RFID or mobile-app access'), ('Dual utility sockets', 'two 3-pin and IEC sockets for light loads such as two-wheelers, e-rickshaws or EV cars'), ('Load management', 'intelligent power distribution between EV charger and CCMS prevents overload'),
            ('Durable design', 'weather-resistant with overload and short-circuit protection for outdoor installation'), ('Flexible deployment', 'public spaces, parking areas, residential complexes, campuses and commercial sites')],
  chips=[('Smart Street Light Solution', '../solutions/smart-street-light.html'), ('LoRa Management System', '../services/lora-management-system.html')]),
 gallery=dict(id='gallery', eyebrow='Hardware', title='CityCharge Unit and CCMS Panel', items=[('cc-unit.jpg', 'CityCharge CCMS unit (CCMS + EV charger)'), ('ccms-cover.jpg', 'ViaLights CCMS feeder panel on site'), ('ccms-box.jpg', 'CCMS feeder control panel')]),
 tables=[dict(id='economics', eyebrow='Illustrative Economics', title='Revenue per Charger', intro='Figures from the CityCharge brochure, based on the stated assumptions. They illustrate the model and are not a guarantee.', cols=[
   dict(head=('Charger utilisation', '6 hrs/day  ·  3 hrs/day'), rows=[('Energy consumed per day', '40 units  ·  20 units'), ('Net income per day', '₹160  ·  ₹80'), ('Net income per month', '₹4,800  ·  ₹2,400'), ('Net income per year', '₹57,600  ·  ₹28,800'), ('Break-even period', 'Approx. 2.5 months  ·  4.5 months')],
        note='Assumptions: input energy ₹10/unit, CMS cost ₹1/unit, consumer tariff ₹15/unit. Additional cost of CityCharge CCMS vs a traditional CCMS: ₹10,000.'),
   dict(title='Shared infrastructure costs', rows=[('Grid connection / power upgrades', 'Shared'), ('Cabling and trenching', 'Shared'), ('Site preparation / civil works', 'Shared'), ('Land or leasing', 'Shared'), ('Permits, site lighting, safety equipment', 'Shared'), ('Operational systems, networking, AMC', 'Shared')], head=('Cost item', 'With combined CCMS + EV'),
        note='For a CCMS or an AC EV charger setup, around 40–60 % of the total cost typically goes into infrastructure, installation and civil works — installing both together reduces the overall setup cost.')])],
 cards=[dict(id='benefits', eyebrow='Key Benefits', title='Why Combine CCMS and EV Charging', cols=3, items=[
   ('Optimum use of infrastructure', 'Adds EV charging on top of the existing CCMS — no extra cabling or control system.'), ('Revenue-generating asset', 'Paid EV charging and socket usage turn lighting infrastructure into income.'), ('Smart-city ready', 'Smart lighting and smart mobility on one centralised platform.'), ('Faster rollout', 'CCMS and EV charging in one compact unit makes deployment simple and quick.')]),
  dict(id='platform', eyebrow='UrbanLink Platform', title='Manage More Than Lights', cols=4, items=[
   ('Smart City Management Platform', 'UrbanLink is a secure, flexible, user-friendly SCMP that can be tailored to manage street lights and other smart-city assets.'), ('Assets it can manage', 'Smart street lights, billboards, smart poles, parking sensors, gateways, EV charging stations, cameras and environmental sensors.')])],
 related=['street', 'lms', 'dt', 'electric'], cta=('Turn Street-Light Panels into EV Charging Points', 'Talk to us about CityCharge CCMS for your smart-city project.'), accent='#059669'))


# ═════════ PLACEHOLDER PAGES — dummy copy until the PDFs arrive. No specs, numbers or certifications are claimed. Replace text/images when real data is available.
PAGES.append(dict(dir='services', slug='lorawan-network-server', parent=('Services', 'services.html'), crumb='LoRaWAN Network Server (LNS)',
 title='LoRaWAN Network Server (LNS) | Nebulae',
 desc='Nebulae LoRaWAN Network Server (LNS): onboard, manage and secure LoRaWAN gateways and end devices and route data to your applications.',
 keywords='LoRaWAN network server, LNS, LoRaWAN gateway management, device onboarding, Nebulae',
 eyebrow='Software · LoRaWAN', h1='LoRaWAN Network Server (LNS)',
 lead='The core of a LoRaWAN deployment — it connects your gateways and end devices, secures the radio network and delivers device data to your applications.',
 pills=[('overview', 'Overview'), ('capabilities', 'Capabilities')],
 overview=dict(img='elec-nms.jpg', alt='Network management dashboard', stats=[('LoRaWAN', 'Gateways + devices'), ('Cloud', 'Or on-premise'), ('API', 'Application integration')],
  tag='Network Server · Placeholder content', title='Manage Your LoRaWAN Network',
  desc=['The LoRaWAN Network Server manages the communication between gateways, end devices and your applications. It handles device activation, message routing and network health in one place.',
        'Detailed specifications, supported regions and deployment options will be published here shortly. Contact our team for the latest information.'],
  metrics=[('Gateways', 'Centralised management'), ('Devices', 'Onboarding and monitoring'), ('Data', 'Forwarded to your apps')],
  features=[('Device onboarding', 'register and activate end devices'), ('Gateway management', 'monitor gateway status and connectivity'), ('Secure communication', 'encrypted device-to-application data path'), ('Application integration', 'forward device data to your platform'), ('Network monitoring', 'view device and network health')],
  chips=[('LoRaWAN Gateways', '../products.html?proto=lora&type=gateway'), ('LoRaWAN Nodes', '../products.html?proto=lora&type=node'), ('LoRa Management System', '../services/lora-management-system.html')]),
 cards=[dict(id='capabilities', eyebrow='Capabilities', title='What the Network Server Does', cols=3, items=[
   ('Device management', 'Add, group and monitor LoRaWAN devices.'), ('Gateway management', 'Keep track of gateway health and coverage.'), ('Secure data routing', 'Authenticate devices and deliver data to applications.'), ('Integration', 'Connect to cloud platforms and your own applications.'), ('Monitoring', 'Dashboards for network and device status.'), ('Flexible deployment', 'Details to be confirmed.')])],
 related=['lms', 'street', 'hes-g', 'hes-w'], cta=('Plan Your LoRaWAN Network', 'Talk to our team about a network server for your deployment.'), accent='#7c3aed'))

PAGES.append(dict(dir='industries', slug='iot-logistics', parent=('Industries', 'industries.html'), crumb='IoT in Logistics',
 title='IoT in Logistics — Asset Tracking & Monitoring | Nebulae',
 desc='IoT for logistics: connected tracking and condition monitoring for assets, shipments and fleets, from Nebulae IoT hardware and software.',
 keywords='IoT logistics, asset tracking, cold chain monitoring, shipment tracking, supply chain IoT, Nebulae',
 eyebrow='Industry · Logistics', h1='IoT in Logistics',
 lead='Connected devices give logistics teams live visibility of assets and shipments across the supply chain.',
 pills=[('overview', 'Overview'), ('benefits', 'Benefits')],
 overview=dict(img='elec-hw-lineup.jpg', alt='Nebulae IoT hardware', stats=[('Track', 'Assets & shipments'), ('Monitor', 'Conditions in transit'), ('Alert', 'Exceptions in real time')],
  tag='Logistics · Placeholder content', title='Visibility Across the Supply Chain',
  desc=['IoT devices report location and condition data from vehicles, containers and goods, helping teams plan better and react faster when something goes off-plan.',
        'Detailed solution information for logistics will be published here shortly. Contact our team to discuss your requirements.'],
  metrics=[('Location', 'Where assets are'), ('Condition', 'How goods are stored'), ('Alerts', 'When to act')],
  features=[('Asset tracking', 'know where vehicles, containers and equipment are'), ('Condition monitoring', 'track conditions that matter for your goods'), ('Real-time alerts', 'be notified of delays or exceptions'), ('Reports', 'review movement and performance history'), ('Custom hardware', 'Nebulae can design devices for your use case')],
  chips=[('Products', '../products.html'), ('IoT Product Development', '../services/iot-product-development.html'), ('Telematics & Fleet', 'telematics-fleet.html')]),
 cards=[dict(id='benefits', eyebrow='Benefits', title='Why IoT for Logistics', cols=3, items=[
   ('Live visibility', 'See assets and shipments as they move.'), ('Fewer losses', 'Spot problems early and act on them.'), ('Better planning', 'Use movement data to improve routes and schedules.'), ('Accountability', 'Keep a record of what happened and when.'), ('Scalable', 'Start small and grow the network.'), ('Tailored to you', 'Hardware and software built around your operation.')])],
 related=['lns', 'lms', 'electric', 'street'], cta=('Talk to Us About Logistics IoT', 'Tell us what you need to track and we will propose a solution.'), accent='#ea580c'))
