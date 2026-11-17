# -*- coding: utf-8 -*-
"""Extra sections for the industry pages (merged into IND_PAGES by industries_data.py).

Per industry:
  ch   = [(challenge, how Nebulae helps), ...]                 -> "Challenges we help solve"
  uc   = [(title, what is sensed, how it connects, what you get), ...]   -> detailed use cases   [use-case]
  flow = [(layer, description), ...]   -> "Typical system" (only where the page has no `arch`)
  faq  = [(question, answer), ...]                              -> FAQ block + FAQPage structured data

Rules: product facts come from tools/products/*.json and tools/solutions_data.py. Everything marked [use-case] is general
industry knowledge about typical applications — NOT a customer claim, case study or certification. Review before launch.
Optional keys you can add later (rendered only when present, otherwise nothing shows on the page):
  case_study = dict(title=..., text=..., link=...)      certs = [('Name', 'detail'), ...]
"""
EXTRA = {}

# ═════════ 1. ENERGY & UTILITIES (real data) ═════════
EXTRA['iot-energy-utilities'] = dict(
 ch=[('Meters spread over wide, mixed areas', 'Wi-SUN mesh for dense electricity-meter clusters and LoRaWAN for gas and water meters that are far apart, so each network fits its terrain.'),
     ('Gas and water meters have no mains power', 'Battery-powered AMR devices with built-in pulse detection and a battery life of 5+ years, so nobody needs to climb to the meter for years.'),
     ('Data has to reach billing and analytics systems', 'The Head End Systems collect readings (DLMS/COSEM for IS 16444 meters) and pass them on through REST APIs to MDM and billing.'),
     ('Transformers fail without warning', 'The DTMS measures electrical and physical parameters and raises alarms for over-voltage, over-current and phase imbalance.')],
 uc=[('Smart electricity metering', 'IS 16444 meter data', 'Wi-SUN module or RF NIC card in the meter, a Wi-SUN DCU (NLG8520 / NLG6770-IN) as the data concentrator, 4G LTE backhaul', 'Remote reading, tamper events and consumption data in the Head End.'),
     ('Gas meter reading', 'Pulses from a diaphragm gas meter, tamper and magnetic alerts', 'Gas Meter AMR on LoRaWAN with a LoRaWAN gateway', 'Readings without site visits and alerts if the meter is interfered with.'),
     ('Water meter reading', 'Magnetic, inductive or RS485 water meter output', 'Water Meter AMR on LoRaWAN or Sigfox', 'Regular readings for billing and a clearer picture of network losses.'),
     ('Distribution transformer health', 'Voltage, current, power factor, oil and winding temperature, oil level', 'DTMS with GSM, GPS and RS-485 or Ethernet interfaces', 'Live loading and temperature data, with alarms before a fault becomes an outage.'),
     ('Prepaid and postpaid billing support', 'Meter readings and consumption history', 'Head End System REST APIs to the billing platform', 'Net and gross metering data and grid versus DG consumption history.')],
 faq=[('Which meters does Nebulae support?', 'IS 16444 electricity meters over Wi-SUN or sub-GHz RF, and gas and water meters through LoRaWAN or Sigfox AMR devices. Water meters can be magnetic, inductive or RS485 types.'),
      ('How many meters can one Wi-SUN data concentrator handle?', 'The NLG8520 supports up to 250 nodes and the NLG6770-IN up to 200 nodes. The exact number in your network depends on topology and reporting interval, so we plan it with you.'),
      ('How long does the gas or water AMR battery last?', 'The AMR devices are designed for a battery life of 5+ years. Actual life depends on how often readings are sent.'),
      ('Can the Head End connect to our billing system?', 'Yes. The HES exposes REST APIs and standard connectors for third-party MDM and billing systems.'),
      ('Can you monitor existing transformers without a shutdown?', 'The DTMS can use clamp-on Rogowski coil sensors (up to 2500 A), which are fitted without switching the transformer off.')])

# ═════════ 2. SMART CITY (real data) ═════════
EXTRA['smart-city-solutions'] = dict(
 ch=[('Many separate systems, many dashboards', 'Street lighting, EV charging, metering and transformer monitoring can all report to one set of Nebulae management platforms.'),
     ('Wiring a whole city is slow and costly', 'Long-range LoRaWAN gateways cover large areas, and Wi-SUN builds a mesh where devices are dense.'),
     ('Light faults are found by complaints, not data', 'Controllers and CCMS panels report lamp burnout, abnormal power and low power factor to the cloud, with e-mail or SMS alerts.'),
     ('Adding EV charging needs new infrastructure', 'The CityCharge unit adds EV charging to an existing street-lighting control panel, with load management between charger and CCMS.')],
 uc=[('Street lighting control', 'Lamp status, voltage, current, power and kWh', 'Pole controllers and CCMS panels on LoRaWAN, managed from the LoRa Management System map', 'Scheduled ON / OFF / dimming, group control and fault alerts for the whole city.'),
     ('EV charging at light poles', 'Charger load and CCMS load', 'CityCharge unit with dual utility sockets, RFID or app access', 'Charging points on existing infrastructure for two-wheelers, e-rickshaws or cars.'),
     ('City utility metering', 'Gas, water and electricity meter readings', 'AMR devices and Wi-SUN / LoRaWAN networks into the Head End', 'One reading network for several utilities.'),
     ('Transformer monitoring', 'Electrical and physical transformer parameters', 'DTMS with GSM, GPS and RS-485', 'Live asset health instead of periodic inspection visits.'),
     ('Coverage surveys', 'LoRaWAN signal quality on site', 'Handheld NLG8140 concentrator and AFL0003 filter for the 865 MHz Indian band', 'A proper coverage check before gateways are installed.')],
 faq=[('Which platform controls the street lights?', 'The LoRa Management System: a cloud-based platform with a live map, individual and group control, a light planner, ticket management, alerts and reports.'),
      ('Can the same LoRaWAN network carry other devices?', 'Yes. A LoRaWAN gateway network can also carry sensor nodes such as environmental or parking sensors, and AMR devices for meters, because it is a standard protocol.'),
      ('What gateways are suitable for outdoor use?', 'The NLG6X40H-IN is IP67 and the NLG6X40G-IN is IP65. Both are 8-channel industrial LoRaWAN gateways with an 85–528 VAC input.'),
      ('How do we check coverage before installing?', 'Use the portable NLG8140 8-channel LoRaWAN concentrator for field testing, or ask us to plan a survey.'),
      ('Can the platforms connect to our existing city systems?', 'The Head End and management platforms offer REST APIs. Tell us the systems you use and we will confirm the integration route.')])

# ═════════ 3. INDUSTRIAL IOT (real data) ═════════
EXTRA['industrial-iot'] = dict(
 ch=[('Remote sites with no wired network', 'The NLG8600 and NLG8400 SCADA RTUs connect over 4G LTE, so remote pumps, panels and stations can report without laid cables.'),
     ('Mixed equipment and interfaces', 'RS232 / RS485, analog and digital I/O on the RTUs connect PLCs, meters and instruments, so existing equipment can report without replacement.'),
     ('Cabling sensors is expensive', 'LoRaWAN nodes and industrial gateways collect sensor data wirelessly over long distances, with low power use.'),
     ('Off-the-shelf boxes rarely fit exactly', 'The i.MX6ULL system on module with a Yocto Linux BSP is a base for your own controller or gateway design.')],
 uc=[('Remote site monitoring', 'Pump, tank or panel status via analog / digital I/O', 'NLG8600 or NLG8400 RTU over 4G LTE', 'Remote visibility and control without site visits.'),
     ('Equipment connectivity', 'PLC, meter or instrument data over RS232 / RS485', 'RTU with RS232 / RS485 serial interfaces', 'Existing equipment data in your monitoring system.'),
     ('Wireless sensor network', 'Temperature, level, vibration or other sensor values', 'LoRaWAN nodes (NLN500a) to an IP65 / IP67 industrial LoRaWAN gateway', 'Long-range monitoring where cabling is costly.'),
     ('Energy monitoring', 'Meter readings across a site', 'Gateways and AMR / LoRaWAN links', 'Consumption data per area for energy reviews.'),
     ('Custom industrial controller', 'Your own application', 'SLS-SoM-MX6 with Yocto BSP, or Nebulae design services', 'A purpose-built product without starting from a blank board.')],
 flow=[('Field equipment', 'PLCs, meters, instruments and wireless sensors'), ('Interfaces and radio', 'RS232 / RS485, analog and digital I/O, LoRaWAN nodes'), ('RTU or gateway', 'NLG8600 / NLG8400 RTU, industrial LoRaWAN gateway'), ('Network backhaul', '4G LTE or Ethernet with SSL/TLS (NLG8600)'), ('Your SCADA or cloud', 'Monitoring, alarms and analytics')],
 faq=[('Which interfaces does the SCADA RTU offer?', 'The NLG8600 has 4G LTE, Ethernet, RS232 / RS485, analog and digital I/O, an RTC and SSL/TLS. The NLG8400 offers 4G LTE, RS232 / RS485 and analog and digital I/O.'),
      ('Do the gateways support Modbus?', 'Modbus support depends on the gateway model and firmware. Tell us the protocol and equipment you need to connect, and we will confirm what each model can do.'),
      ('Can the LoRaWAN gateways run on site mains power?', 'Yes. The industrial LoRaWAN gateways take 85–528 VAC input, and the IP65 model includes battery backup.'),
      ('Can you customise the firmware or hardware?', 'Yes. Nebulae offers embedded hardware and firmware design, and the SLS-SoM-MX6 system on module for building your own product.'),
      ('Is communication encrypted?', 'The NLG8600 supports SSL/TLS. Security options for other models depend on the configuration, so please ask us for your case.')])

# ═════════ 4. BUILDING MANAGEMENT (real data) ═════════
EXTRA['building-management-system'] = dict(
 ch=[('Retrofit without rewiring', 'Wireless Zigbee, Thread / Matter and BLE modules let you add lighting and sensing to existing buildings without new cable runs.'),
     ('Devices from different vendors', 'Matter, OpenThread and Zigbee support on the EFR32 modules helps devices work with each other.'),
     ('Large campuses and plant rooms', 'LoRaWAN gateways cover a whole campus and reach basements and rooftops where 2.4 GHz is weak.'),
     ('Tenant and floor level billing', 'AMR devices for water and other meters report consumption per floor or tenant.')],
 uc=[('Lighting control', 'Light status and schedules', 'Zigbee or Thread nodes on the NLN111P / NLN811P modules', 'Scheduling and dimming without new wiring.'),
     ('Environmental sensing', 'Temperature, occupancy and air quality', 'Low-power Zigbee / BLE sensors or LoRaWAN nodes', 'Data for comfort control and energy savings.'),
     ('Energy and water sub-metering', 'Consumption per floor or tenant', 'AMR devices and LoRaWAN gateway', 'Clear usage data and fair cost allocation.'),
     ('Plant-room and rooftop equipment', 'Status of pumps, chillers and tanks', 'Wi-Fi (NM0442-P) or LoRaWAN links', 'Early warning on equipment issues.'),
     ('Commissioning by phone', 'Device set-up and diagnostics', 'Bluetooth 5 on the EFR32 modules', 'Faster installation by the site team.')],
 flow=[('Building devices', 'Lights, sensors, meters and equipment'), ('Wireless radios', 'Zigbee, Thread / Matter, BLE 5, Wi-Fi, LoRaWAN'), ('Gateways', 'LoRaWAN gateway or your building hub'), ('Platform', 'Your BMS, or Nebulae Head End for meters'), ('Facility team', 'Dashboards, alerts and reports')],
 faq=[('Which radios do your building modules support?', 'The NLN811P (EFR32MG24) supports Matter, OpenThread, Zigbee and Bluetooth 5. The NLN111P (EFR32MG21) supports Zigbee, Thread and Bluetooth 5. The NM0442-P is a 2.4 GHz Wi-Fi module.'),
      ('Can we retrofit an existing building?', 'Yes. Wireless modules avoid new wiring, and LoRaWAN is a good fit for hard-to-reach areas.'),
      ('Can the meters report to our BMS?', 'Meter data can be collected through the Head End Systems and passed on via REST APIs. We confirm the integration route for your platform.'),
      ('Do you design the finished device as well?', 'Yes. Nebulae provides embedded hardware and firmware design alongside the modules.')])

# ═════════ 5. TELEMATICS & FLEET (real data) ═════════
EXTRA['telematics-fleet'] = dict(
 ch=[('Vehicles move across areas without Wi-Fi', 'The NLG7644 and NLG8600 combine 4G LTE with GPS for mobile and remote installations.'),
     ('Trailers and equipment have no power', 'Low-power LoRaWAN nodes, 434 MHz modules and LoRa point-to-point links keep battery tags running for long periods.'),
     ('Yards and depots need local coverage', 'A LoRaWAN gateway collects tag and sensor data across the site and passes it on over 4G.'),
     ('OEMs need their own branded tracker', 'The i.MX6ULL system on module and modules like the NLN500b are building blocks for your own device and software.')],
 uc=[('Vehicle tracking', 'Position and vehicle status', 'NLG7644 (4G + GPS) or NLG8600 RTU', 'Live location and status in your fleet platform.'),
     ('Trailer and equipment tags', 'Presence and location in a yard', 'LoRaWAN nodes (NLN500a / NLN500b) or OTAG-433 to a yard gateway', 'Know which asset is where, without driver check-ins.'),
     ('Depot coverage', 'Tag and sensor readings across a depot', 'LoRaWAN gateway with 4G backhaul', 'One network for the whole site.'),
     ('Onboard equipment data', 'Data from onboard instruments', 'RS232 / RS485 on the RTU', 'Vehicle and equipment data beside GPS.'),
     ('OEM tracker design', 'Your own functions', 'SLS-SoM-MX6 plus Nebulae hardware and firmware services', 'A branded tracker built on proven modules.')],
 flow=[('Vehicles and assets', 'Trucks, trailers, containers, equipment'), ('Tracking hardware', 'GPS + 4G gateway, LoRa tags, 434 MHz modules'), ('Site gateway', 'LoRaWAN or P2P gateway at yards and depots'), ('Backhaul', '4G LTE / Ethernet'), ('Fleet platform', 'Maps, alerts and reports (yours or custom-built)')],
 faq=[('Do you provide a fleet software platform?', 'Nebulae supplies the tracking hardware and can design the firmware and application with you. Tell us whether you have a platform or need one built.'),
      ('Does the gateway have GPS?', 'The NLG7644 includes GPS together with 4G LTE. The NLG8600 offers optional GPS.'),
      ('What are the options for battery-powered trackers?', 'The NLN500a and NLN500b LoRaWAN modules and the OTAG-433 434 MHz module are low-power radio options.'),
      ('Is any specific vehicle-tracking standard supported?', 'Standards differ by country and device class. Please contact us with the standard you need, and we will confirm what is achievable.')])

# ═════════ 6. LOGISTICS [use-case] ═════════
EXTRA['iot-logistics'] = dict(
 ch=[('Assets go missing inside large sites', 'Low-power LoRa tags (NLN500a / NLN500b / OTAG-433) report to a gateway covering the whole warehouse or yard.'),
     ('Tags must last without maintenance', 'LoRa radios are designed for low power, so battery-powered tags are practical for long deployments.'),
     ('Handover points lack visibility', 'Cellular gateways with GPS (NLG7644) report position at transit points and vehicles.'),
     ('Planning gateway placement', 'The portable NLG8140 lets you test LoRaWAN coverage on site before installation.')],
 uc=[('Warehouse asset tracking', 'Location of pallets, roll cages and equipment', 'LoRa tags to a LoRaWAN gateway', 'Fewer lost assets and faster searches.'),
     ('Yard management', 'Which trailer or container is in which bay', 'Tags and a yard gateway with 4G backhaul', 'A clearer yard picture for dispatch.'),
     ('Vehicle visibility', 'Vehicle position', 'NLG7644 with GPS and 4G LTE', 'Live position through the shipment.'),
     ('Condition monitoring', 'Temperature or shock values from attached sensors', 'LoRa nodes with your sensors', 'Alerts when conditions go out of range.'),
     ('Point-to-point links', 'Data between two fixed locations', 'Single-channel P2P gateway', 'A low-cost link where no network exists.')],
 flow=[('Assets and vehicles', 'Pallets, containers, trailers, vehicles'), ('Tags and trackers', 'LoRa nodes, 434 MHz tags, GPS + 4G gateway'), ('Site gateways', 'LoRaWAN gateway at warehouse or yard'), ('Network server', 'LoRaWAN Network Server (LoRa Management System)'), ('Logistics software', 'WMS / TMS or a dashboard')],
 faq=[('How far do the LoRa tags reach?', 'The NLN500a is rated up to 10 km line of sight. Indoors and in dense yards, the range is less, so the gateway layout matters.'),
      ('Can tags run on batteries?', 'Yes. LoRa nodes are designed for low power, and battery life depends on how often a tag reports.'),
      ('Can we connect to our WMS or TMS?', 'A LoRaWAN network server delivers device data to your application over standard interfaces. Tell us the system and we will confirm the route.'),
      ('Do you build custom tags?', 'Yes. Nebulae offers hardware and firmware design to build tags around your requirements.')])

# ═════════ 7. SMART AGRICULTURE [use-case] ═════════
EXTRA['smart-agriculture'] = dict(
 ch=[('Fields are far from mains and networks', 'Battery-powered LoRaWAN nodes and a solar or mains-powered gateway cover wide areas with a few gateways.'),
     ('Cellular coverage is patchy', 'A gateway with a 4G backhaul at one good-signal point serves many nodes across the farm.'),
     ('Water management needs timely data', 'Sensors on tanks, pumps and water meters report regularly, so irrigation decisions use data.'),
     ('Teams want to try ideas quickly', 'The NLN0651-i LoRa evaluation kit supports fast prototyping with the Arduino IDE.')],
 uc=[('Soil and weather sensing', 'Soil moisture, temperature, rainfall', 'LoRaWAN nodes (NLN500a) with sensors to an IP67 gateway', 'Irrigation planned from measured conditions.'),
     ('Irrigation monitoring', 'Pump status and tank levels', 'LoRaWAN nodes or RTU', 'Know whether pumps ran and tanks are full.'),
     ('Remote pump control', 'Pump on / off commands', 'RTU or LoRa actuator nodes', 'Fewer trips to switch pumps.'),
     ('Greenhouse monitoring', 'Temperature and humidity', 'Low-power LoRa sensors', 'Alerts when conditions drift.'),
     ('Cold storage monitoring', 'Storage temperature', 'LoRa temperature nodes', 'Alerts before produce is affected.'),
     ('Water usage', 'Consumption from water meters', 'Water Meter AMR on LoRaWAN', 'Usage data per block or user.')],
 flow=[('Field sensors', 'Soil, weather, tank, pump and meter signals'), ('LoRa nodes', 'NLN500a / NLN500b battery-powered nodes'), ('Farm gateway', 'IP65 / IP67 LoRaWAN gateway with 4G backhaul'), ('Network server', 'LoRaWAN Network Server'), ('Farm dashboard', 'Alerts, trends and reports')],
 faq=[('How many gateways does a farm need?', 'It depends on terrain and layout. LoRa reaches up to 10 km line of sight for the NLN500a, so one gateway often covers a large area. We can plan the layout with you.'),
      ('Do the sensors need mains power?', 'No. The LoRaWAN nodes are low-power and battery-friendly. Gateways run on mains, and the IP65 model has battery backup.'),
      ('Can I try a prototype first?', 'Yes. The NLN0651-i evaluation kit is based on the NLN500a and works with the Arduino IDE.'),
      ('Does the gateway need internet?', 'Gateways connect through Ethernet or 4G LTE (on some models) to reach the network server.')])

# ═════════ 8. FARM & ANIMAL MANAGEMENT [use-case] ═════════
EXTRA['farm-animal-management'] = dict(
 ch=[('Animals roam over large areas', 'Long-range LoRa links and a small number of gateways cover grazing land.'),
     ('Tags must be small and light', 'The NLN500b is the smallest STM32WL module (26.68 × 16 mm), and the OTAG-433 is a low-cost 434 MHz option.'),
     ('Battery changes disturb the herd', 'Low-power radios help tags run for long periods between maintenance.'),
     ('Remote pastures lack networks', 'A P2P or LoRaWAN gateway with 4G backhaul brings remote data back to the farm office.')],
 uc=[('Herd location', 'Position or presence of tagged animals', 'LoRa or 434 MHz tags to a gateway', 'See where the herd is without walking the land.'),
     ('Grazing boundaries', 'Whether tags are in or out of a zone', 'Tags with your boundary logic', 'Alerts when animals leave a zone.'),
     ('Activity tracking', 'Movement data from tag sensors', 'LoRa tag with an accelerometer you choose', 'A basis for health and behaviour insights.'),
     ('Shed and barn monitoring', 'Temperature and humidity', 'LoRa sensor nodes', 'Alerts for poor housing conditions.'),
     ('Custom tag development', 'Your tag requirements', 'Nebulae hardware and firmware design', 'A tag made for your animals and your software.')],
 flow=[('Animals', 'Cattle, sheep or other livestock'), ('Tags', 'NLN500b / NLN500a LoRa tags, OTAG-433'), ('Farm gateway', 'LoRaWAN or P2P gateway'), ('Backhaul', '4G LTE or Ethernet'), ('Herd application', 'Location, alerts and reports')],
 faq=[('Which tags do you offer?', 'Nebulae supplies the radio modules and design services for tags, rather than a finished branded collar. The NLN500b, NLN500a and OTAG-433 are the main building blocks.'),
      ('How far can the tags communicate?', 'The NLN500a reaches up to 10 km line of sight. Terrain, vegetation and the animal itself reduce range, so we help plan the layout.'),
      ('How long can a tag run on a battery?', 'It depends on the battery, reporting interval and design. Low-power LoRa makes long intervals between maintenance achievable.'),
      ('Can you integrate with our herd software?', 'Yes, through the LoRaWAN network server interfaces. Tell us the system you use.')])

# ═════════ 9. HEALTHCARE [use-case] ═════════
EXTRA['iot-healthcare'] = dict(
 ch=[('Devices must be small and low-power', 'The NLN811P and NLN111P are compact 2.4 GHz modules with Bluetooth 5, and the NLN500b is a small LoRa module.'),
     ('Equipment must connect to existing networks', 'The NM0442-P Wi-Fi module (802.11 b/g/n, up to 150 Mbps) connects devices to hospital Wi-Fi.'),
     ('Equipment is hard to find', 'LoRa tags and gateways locate carts, pumps and supplies across a campus.'),
     ('Developing a device takes in-house skills', 'Nebulae provides embedded hardware and firmware design to take a device from idea to production.')],
 uc=[('Wearable and handheld devices', 'Patient or device data', 'Bluetooth 5 modules to a phone or hub', 'Device data in your own app.'),
     ('Connected hospital equipment', 'Equipment status and readings', 'NM0442-P Wi-Fi module', 'Data from bedside or ward equipment.'),
     ('Equipment tracking', 'Location of carts and assets', 'LoRa tags with a gateway on campus', 'Quicker equipment search.'),
     ('Cold-chain sensing', 'Storage temperature', 'LoRa temperature nodes', 'Alerts for stored supplies out of range.'),
     ('Smart-home care devices', 'Door and activity sensors', 'Zigbee or Matter modules', 'Home-care sensors that work together.')],
 flow=[('Devices and sensors', 'Wearables, equipment, tags and temperature probes'), ('Wireless modules', 'BLE 5, Wi-Fi, Zigbee / Matter, LoRa'), ('Gateway or phone', 'Hospital Wi-Fi, LoRaWAN gateway or phone app'), ('Your platform', 'Clinical or asset systems'), ('Care and facility teams', 'Alerts and dashboards')],
 faq=[('Are your modules certified for medical devices?', 'The modules are radio building blocks. Medical-device approval applies to the finished product, and requirements vary by country. We have not made medical certification claims here.'),
      ('Which radios can I use for a wearable?', 'Bluetooth 5 on the NLN811P or NLN111P is the usual choice for phone connectivity.'),
      ('Can the Wi-Fi module work across a wide temperature range?', 'Yes. The NM0442-P operates from -40 to +105 °C.'),
      ('Do you help with firmware and hardware design?', 'Yes. Embedded hardware and firmware design is a core Nebulae service.')])

# ═════════ 10. DEFENCE [use-case] ═════════
EXTRA['iot-in-defence'] = dict(
 ch=[('Remote, unmanned sites', 'Long-range LoRa, 4G LTE gateways and RTUs provide links where no network infrastructure exists.'),
     ('Tough environments', 'Industrial gateways with IP65 / IP67 housings and wide input voltage handle outdoor installation.'),
     ('Custom requirements', 'The i.MX6ULL system on module and Nebulae design services support purpose-built embedded systems.'),
     ('Dependence on one network type', 'LoRaWAN, point-to-point LoRa and 4G LTE can be combined for resilience.')],
 uc=[('Perimeter and site sensing', 'Sensor signals around a site', 'LoRa nodes to an IP67 LoRaWAN gateway', 'Wireless sensing without long cable runs.'),
     ('Remote installation monitoring', 'Status of remote equipment', 'NLG8600 RTU over 4G LTE', 'Remote visibility of unmanned sites.'),
     ('Point-to-point links', 'Data between two fixed points', 'P2P LoRa gateway', 'A simple long-range link.'),
     ('Field coverage checks', 'Radio signal quality', 'Portable NLG8140 concentrator', 'Verify coverage before deployment.'),
     ('Custom embedded systems', 'Your requirements', 'SLS-SoM-MX6 and Nebulae hardware / firmware design', 'A system tailored to the mission.')],
 flow=[('Field sensors and equipment', 'Perimeter sensors, remote installations'), ('LoRa / cellular radios', 'LoRa nodes, P2P links, 4G LTE'), ('Rugged gateways', 'IP65 / IP67 LoRaWAN gateways, RTUs'), ('Secure backhaul', '4G LTE / Ethernet; your own security layer'), ('Control room', 'Your monitoring system')],
 faq=[('Do you claim defence certifications?', 'No. The pages describe general-purpose industrial products. If your programme needs specific approvals, please contact us to discuss what is possible.'),
      ('What kind of range can I expect?', 'The NLG7644 gateway is specified for 15 km line of sight and the NLN500a for up to 10 km line of sight. Real range depends on terrain and installation.'),
      ('Can the hardware be customised?', 'Yes. Nebulae offers custom embedded hardware and firmware design.'),
      ('Can data be encrypted?', 'The NLG8600 supports SSL/TLS, and LoRaWAN includes its own encryption. Additional security depends on your design, so please discuss your requirements.')])

# ═════════ 11. SOS & PERSONAL SAFETY [use-case] ═════════
EXTRA['sos-devices'] = dict(
 ch=[('Alerts must go out when no phone network is nearby', 'LoRa and 434 MHz links reach a gateway on site, which forwards the alert over Ethernet or 4G.'),
     ('Devices must be tiny and last long', 'The NLN500b is the smallest STM32WL module, and the OTAG-433 offers a low-cost 434 MHz option.'),
     ('Wearers need phone connectivity too', 'Bluetooth 5 on the NLN811P / NLN111P pairs a device with a phone app.'),
     ('Alerts must reach the right people', 'Gateways pass alerts to your own dispatch or messaging system.')],
 uc=[('Panic buttons', 'A button press', 'LoRa or 434 MHz module to a site gateway', 'Instant alert to a control room.'),
     ('Lone-worker devices', 'Worker alert or check-in', 'LoRa module, or BLE to a phone app', 'A way to raise help for people working alone.'),
     ('Campus and site alerts', 'Alerts across a large site', 'LoRaWAN gateway coverage', 'Coverage in buildings and open areas.'),
     ('Elderly care pendants', 'Button press or fall sensor you add', 'BLE or LoRa module', 'Family or carers get alerts.'),
     ('Vehicle alerts', 'Alert button in a vehicle', 'NLG7644 with 4G and GPS', 'Location sent with the alert.')],
 flow=[('SOS device', 'Button, pendant or wearable'), ('Radio module', 'LoRa NLN500b, 434 MHz OTAG-433, BLE 5 NLN811P'), ('Gateway', 'LoRaWAN or P2P gateway; phone for BLE devices'), ('Backhaul', '4G LTE / Ethernet'), ('Alert system', 'Control room, SMS or app')],
 faq=[('Do you sell finished SOS devices?', 'Nebulae supplies the modules, gateways and design services. Finished device design can be done with you.'),
      ('Can the device send location?', 'GPS can be added in your design, and the NLG7644 gateway includes GPS for vehicle-mounted use.'),
      ('How far does the alert reach?', 'The NLN500a is rated up to 10 km line of sight, but buildings reduce range. A site survey helps place gateways.'),
      ('How long will the battery last?', 'It depends on the design and how often the device checks in. We can advise on low-power design.')])

# ═════════ 12. CONSUMER IOT [use-case] ═════════
EXTRA['consumer-iot'] = dict(
 ch=[('Product must work with major smart-home standards', 'The NLN811P supports Matter, OpenThread, Zigbee and Bluetooth 5 on a single module.'),
     ('Time to market', 'Evaluation kits and ready modules let you prototype before committing to a custom board.'),
     ('Small, cost-sensitive devices', 'Compact modules with on-board PCB antennas keep the board size and bill of materials small.'),
     ('Mix of hardware and software skills', 'Nebulae offers hardware, firmware and mobile-app services alongside modules.')],
 uc=[('Smart-home devices', 'Sensors, switches and lights', 'NLN811P / NLN111P modules', 'Devices that join Matter or Zigbee networks.'),
     ('Wearables and accessories', 'Motion or button data', 'Bluetooth 5 modules', 'Phone-connected accessories.'),
     ('Wi-Fi appliances', 'Appliance status', 'NM0442-P Wi-Fi module', 'Appliances that connect to home Wi-Fi.'),
     ('Long-range trackers', 'Location or presence of belongings', 'NLN500b LoRa module', 'A low-power tracker with long range.'),
     ('Linux-based devices', 'Your application', 'SLS-SoM-MX6 with Yocto Linux BSP', 'A cost-effective compute base.')],
 flow=[('Your product', 'Sensor, appliance or accessory'), ('Wireless module', 'Matter / Zigbee / BLE, Wi-Fi or LoRa'), ('Gateway or phone', 'Home hub, router or phone app'), ('Cloud', 'Your or a third-party cloud'), ('Consumer app', 'Control and notifications')],
 faq=[('Is the NLN811P Matter-ready?', 'It is based on the EFR32MG24 and supports Matter, OpenThread, Zigbee and Bluetooth 5. Product certification for Matter depends on your final device.'),
      ('Which module is best for a Wi-Fi appliance?', 'The NM0442-P is a 2.4 GHz 802.11 b/g/n module with an Xtensa LX6 processor and up to 150 Mbps.'),
      ('Can I try something before building a board?', 'The NLN0651-i LoRa evaluation kit is available, and we can discuss kits for other modules.'),
      ('Do you build the mobile app too?', 'Nebulae offers IoT mobile app and cloud services. Tell us about your product and we will scope it.')])

# ═════════ 13. HOME SECURITY & AUTOMATION [use-case] ═════════
EXTRA['home-security-automation'] = dict(
 ch=[('Many devices need to cooperate', 'Zigbee, Thread and Matter support on the EFR32 modules helps sensors, sirens and hubs work together.'),
     ('Battery-powered sensors must last', 'Low-power radios suit door, window and motion sensors that run on small batteries.'),
     ('Large properties and outbuildings', 'LoRa nodes and gateways reach gates, sheds and distant buildings.'),
     ('Installers want quick setup', 'Bluetooth 5 on the modules supports set-up from a phone.')],
 uc=[('Door and window sensors', 'Open / closed state', 'Zigbee or Thread sensor on the NLN111P / NLN811P', 'Instant alerts when something opens.'),
     ('Sirens and alarms', 'Alarm commands', 'Zigbee or Wi-Fi module', 'Local sirens triggered by the hub.'),
     ('Smart switches and plugs', 'Power state', 'Matter / Zigbee module', 'Control from a phone or by schedule.'),
     ('Hubs and gateways', 'All device traffic', 'NM0442-P Wi-Fi plus Zigbee / Thread modules, or SLS-SoM-MX6', 'A hub that connects devices to the internet.'),
     ('Large-property sensing', 'Gate or outbuilding sensors', 'LoRa node (NLN500a) and LoRaWAN gateway', 'Coverage beyond Zigbee range.')],
 flow=[('Home devices', 'Sensors, sirens, switches, locks'), ('Wireless modules', 'Zigbee, Thread / Matter, BLE 5, Wi-Fi, LoRa'), ('Hub or gateway', 'Wi-Fi hub or LoRaWAN gateway'), ('Cloud', 'Your service'), ('Home-owner app', 'Notifications and control')],
 faq=[('Which radio is best for door and window sensors?', 'Zigbee or Thread on the NLN111P / NLN811P modules, because they are low-power and widely supported.'),
      ('Can the hub use Wi-Fi?', 'Yes. The NM0442-P is a 2.4 GHz Wi-Fi module, and the SLS-SoM-MX6 can power a Linux-based hub.'),
      ('How do I cover a large property?', 'Use LoRa nodes and a LoRaWAN gateway for outbuildings and gates that are out of Zigbee range.'),
      ('Do you design the finished product?', 'Yes. Nebulae provides hardware and firmware design alongside the modules.')])
