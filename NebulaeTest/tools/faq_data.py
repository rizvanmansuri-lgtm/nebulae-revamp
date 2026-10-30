# -*- coding: utf-8 -*-
"""FAQ content for faq.html  (source: the FAQ text supplied by Nebulae — typos fixed, exact duplicates merged, meaning unchanged).
Answer = list of blocks:  'paragraph'  |  ('ul', [..])  |  ('ol', [..])   (a trailing paragraph may follow a list).
Edit here, then run:  python3 tools/build_faq.py
Items marked  # REVIEW  contain statements that may be out of date (old product names, regions, dates) — please confirm."""

GENERAL = [
 ('What is Nebulae?', ['Nebulae is a tangible framework for the Internet of Things. Nebulae provides networking hardware as well as SDKs and cloud services designed and engineered to simplify the implementation of IoT solutions.']),
 ('What are the Nebulae devices?', ['Nebulae devices are divided into two categories:',
   ('ul', ['NebuLink Node — a board-level component that provides IPv6 internet connectivity for sensors, devices and equipment. A NebuLink Node may be categorised either as a Full Function Device (FFD) or a Reduced Function Device (RFD), operating on battery supply or power line.',
           'NebuLink Gateway — a device that builds and maintains an auto-configuring, self-tuning, redundant, self-healing network of NebuLink Nodes in a mesh, star, tree or hybrid topology, and securely connects them to Nebulae Cloud.'])]),
 ('What are the system requirements to run Nebulae IoT products?', ['A host build system running Windows or Linux.']),
 ('What connectivity protocols does Nebulae IoT support?', ['Zigbee, 6LoWPAN, Wi-Fi, Cellular, Ethernet, Bluetooth and more.']),
 ('What is the RF range for each gateway?', ['Each NebuLink Gateway has Zigbee and 6LoWPAN with 100 metres range (line of sight).']),  # REVIEW
 ('How can I develop my application on the Nebulae platform?', ['You can build an IoT application using the Nebulae SDKs, with the help of the Doxygen documentation provided on the Nebulae platform.']),
 ('Do you provide APIs for developing applications?', ['Yes. The APIs are documented in the Doxygen section of the respective SDK.']),
 ('What kind of applications can be built on the Nebulae IoT platform?', ['Any IoT-based application can be built on the Nebulae IoT platform.']),
 ('How are you different from other IoT providers?', ['We are scalable in terms of devices, and the Nebulae IoT platform is interoperable.']),
 ('How many nodes or end devices can be connected to one gateway?', [('ul', ['Zigbee devices — 15 to 20', '6LoWPAN devices — 70'])]),  # REVIEW
 ('Which operating systems does the gateway support?', ['FreeRTOS and Linux.']),
 ('Which communication protocols do you support?', ['IEEE 802.11 b/g/n, IEEE 802.15.4, Ethernet, Cellular, Bluetooth Classic and BLE.']),
 ('What is the bandwidth or range of each connectivity protocol?', [('ul', ['IEEE 802.11 b/g/n — 802.11n (2.4 GHz), up to 150 Mbps', 'Ethernet — 10 or 100 Mbps', 'Bluetooth Classic or BLE — 10 to 100 metres range'])]),
 ('How easily can the dashboard be customised to my requirements?', ['It is very easily customisable. Reach out to us at support@nebulae.io for details.']),
 ('Do you provide SDKs along with the Nebulae products?', ['We provide SDKs after an NDA is signed, and with additional charges.']),
 ('What is NebuLink Middleware?', ['NebuLink Middleware is a mediator between the hardware and the application. It integrates nodes and gateways with the application.']),
 ('How much data can be stored in Nebulae Middleware?', ['Nebulae Middleware is scalable in terms of storage. It can be scaled by adding more servers to the Middleware cluster.']),
 ('What other data storage options do you provide?', ['The NebuLink RTOS Gateway provides SPI flash memory (NLG1XXX) and an SD card (NLG2200) to store other data as your application requires.']),  # REVIEW
 ('How does the Nebulae IoT gateway talk to the cloud, and which messaging protocol is used?', [('ul', ['Wi-Fi, Ethernet or Cellular', 'TCP with an encryption protocol'])]),
 ('Do you provide a FOTA service? How can the firmware be updated?', ['Yes, a FOTA (firmware over the air) service is provided.']),
 ('Which programming languages are used?', ['C, Java and JavaScript.']),
 ('Can the gateways replace the gateways in a customer’s existing application?', ['Yes.']),
 ('Which projects has Nebulae worked on?', ['Some of the projects under Nebulae:',
   ('ul', ['IoTargetting Project', 'IoTraffic Project', 'Kwikpay Gaming and Arcade Device', 'Electric Vehicle Charging System', 'Bio-Medical Device-101', 'Web Guiding System (BST Company)', 'Force Controller 19 (BST Company)',
           'HAT (Home Area Network Assist Tool) Project', 'Temperature Sensor Probe POC', 'KonnetSys Project', 'SunSights Solar System', 'ViaLights (Street Light) Project', 'IITM PLC Test Bed (G3-PLC + 6LoWPAN)',
           'CSMOS Online Monitoring Gateway', 'DEMU Data Concentration', 'DEMU Remote Monitoring', 'Nebulae Evaluation Portal']),
   'and many more.']),  # REVIEW (client names)
 ('How many Nebulae devices have been tested to date?', ['We have tested 70 6LoWPAN nodes and 15 to 20 Zigbee nodes with a single gateway and cloud system.']),  # REVIEW
 ('How are the gateways suited to industrial use?', ['We have the NLG2200 and NLG5100 for industry use. They support M2M communication, which allows devices to share data with each other and results in better optimisation of resources.']),  # REVIEW
 ('Can multiple connectivity protocols be used at once?', ['Yes. The SDK supports switching from one connectivity protocol to another.']),
 ('Do you provide VPN services for the gateway?', ['Currently, we do not provide VPN services.']),
 ('What does zero configuration mean?', ['NebuLink Nodes and Gateways are tightly integrated with Nebulae Cloud Services to provide zero-configuration connection of sensors, devices and equipment. It does not require manual operator intervention or special configuration servers, provided that you white-list the nodes in the gateway.']),
 ('What warranty do you provide on hardware?', ['SLS provides a one-year warranty on hardware. Damage caused on the customer’s side while using the product is not replaceable.']),
 ('Where is the data collected from the IoT gateways stored?', ['Data is stored in NebuLink Middleware or in the cloud server you specify.']),
 ('Which security and authentication protocols does Nebulae IoT support?', ['We have built-in crypto security with PKI certificates (X.509), message digest (RSA / SHA-256), encryption (AES-CCM 128-bit) and authentication (ECDSA as specified by RFC 6979).']),
 ('In what form does a developer receive the data?', ['Application developers receive data as a JSON string.']),
 ('What if we do not pay the SDK subscription fees? Will the services stop?', ['Yes. If you do not subscribe, the services will stop.']),  # REVIEW
 ('For GSM gateways, what kind of SIM should be used? Do you provide SIMs?', ['Any kind of SIM can be used. We do not provide SIMs along with the gateway.']),
 ('Which programming languages and hardware platforms does the Nebulae IoT Device SDK support?', ['Nebulae works with any hardware platform that supports 802.15.4, 802.11 b/g/n Wi-Fi, BLE or Cellular.']),
 ('What certificates do you provide with Nebulae products?', ['Certificates are provided on request.']),
]

TECH = [
 ('NebuLink Node', [
  ('What is the range of each NebuLink Node?', ['The range differs for each NebuLink Node. See the individual product pages on this website for details.']),
  ('How many nodes or end devices can be connected to a single gateway?', ['The number of end nodes depends on the SDK configuration and the memory requirements of the application.']),
  ('Can data be stored in NebuLink Nodes?', ['Yes.']),
  ('Which programming language is used to program NebuLink Nodes?', ['C.']),
  ('Which WSN protocols does a NebuLink Node use?', ['Zigbee, 6LoWPAN and G3-PLC.']),
  ('Is a NebuLink Node suitable for urban, suburban and rural deployments?', ['Yes. However, range and connectivity depend on the location and surroundings.']),
  ('What kind of antenna is used?', ['NebuLink Nodes come with these antenna options:', ('ul', ['MIFA (on-board) antenna, gain −2 dBi', 'Whip (external) antenna, gain 2 dBi'])]),
  ('Can a NebuLink Node be configured as root, router or leaf from the NebuLink portal?', ['No.']),
  ('Which network topologies are supported?', ['Mesh and point-to-point.']),
  ('Does the NebuLink Node support OTA updates?', ['Yes.']),
  ('Does the NebuLink Node comply with European and North American radio regulations?', ['As of the time of writing, CE-RED and FCC compliance certification are ongoing and are expected to be in line with the standards.']),  # REVIEW
  ('What is the maximum TX power of a NebuLink Node?', ['10 dBm for the standard module and 20 dBm for the high-power module. These figures are measured under standard laboratory conditions. See the product pages for more information.']),
 ]),
 ('NebuLink Gateway — RTOS SDK', [
  ('What is the NebuLink Gateway RTOS SDK?', ['An SDK for developing IoT applications that can be used in smart IoT products and services, home automation, medical devices and industrial IoT. It provides end-to-end connectivity over Ethernet, Wi-Fi or GSM to connect RF / WSN sensors to NebuLink Middleware.']),
  ('What does the NebuLink Gateway RTOS SDK offer?', ['It supports ESP32 (Espressif Systems) and Nuvoton NUC472 (ARM Cortex-M4) targets, with FreeRTOS, a HAL, OSAL services and third-party libraries to create IoT applications. It provides network connectivity over Wi-Fi, Ethernet and cellular GSM, and Bluetooth for short-range communication.']),  # REVIEW
  ('How does the NebuLink Gateway RTOS SDK work?', ['Clone the SDK following the steps in the Doxygen documentation. It provides configurations to select targets as you need. It includes the toolchain, BSPs, OSAL services, protocols and examples, so you can build IoT applications quickly.']),
  ('Can I use the RTOS SDK on my own boards or hardware?', ['Yes. Options are provided for development boards as well as custom boards. You configure and write the code for your own board or hardware.']),
  ('How should I start with the RTOS SDK?', ['See the Doxygen documentation. Examples such as MQTT, ADC, RS485, CAN, flash, SD card, Wi-Fi, file system and HTTP server-client are included in the SDK for reference.']),
  ('Is there a commercial licence for the RTOS SDK?', ['Yes. You sign a commercial agreement with a defined interval to use it as your requirements need.']),
  ('Can I buy only Nebulae boards or hardware and use my own SDK?', ['Yes.']),
  ('Do you provide application examples in the SDK?', ['Yes. See the Examples section of the Doxygen documentation, for example MQTT, ADC, RS485, CAN, flash, SD card, Wi-Fi, file system and HTTP server-client.']),
  ('How can I update the image on the NebuLink Gateway?', ['You can update the image using UART or FOTA, as you need.']),
  ('Does the gateway provide Modbus slave?', ['Yes. Modbus slave support has been added in software for both the NLG1XXX and NLG2200 gateways. At present, only the NLG2200 provides Modbus slave from the hardware side.']),  # REVIEW
  ('Does the gateway provide Modbus master?', ['Yes. Modbus master support has been added in software for both the NLG1XXX and NLG2200 gateways. At present, only the NLG2200 provides Modbus master from the hardware side.']),  # REVIEW
  ('Does the gateway SDK use open-source libraries?', ['Yes. A few open-source libraries are used. They are listed under “Licenses of Third Party Software” in the Doxygen section.']),
  ('I cannot see any logs on USB. What should I check?', ['Check the following in order:', ('ol', ['The LED pattern, to see whether the board boots successfully.', 'If the board started successfully, check that the SLS USB-2-UART connection is correct. More details are in the Doxygen documentation (Debug Accessories section).'])]),
  ('How do I check serial logs on the console?', ['Use the SLS USB-2-UART connector to power the board and read the debug serial console logs at 115200 baud. More details are in the Doxygen documentation (Debug Accessories section).']),
  ('How do I enable a component or library in the SDK?', ['Enable the component through the configuration using “make menuconfig”. See the Doxygen documentation for details.']),
  ('I loaded the default example binaries but the gateway does not connect to Middleware. What should I do?', ['Check which connectivity-based example you loaded. Check the LED pattern to confirm the gateway is connected to the configured router or network. If the network LED pattern is correct, check that the cloud key is properly flashed or stored in the defined location, and check the cloud LED pattern. These checks help you find the problem.']),
  ('Can I use a third-party cloud service with the NebuLink Gateway and RTOS SDK?', ['Yes.']),
  ('Do you provide end-to-end development and technical support?', ['The SDK includes Doxygen documentation and examples for end-to-end development support.']),
  ('How is the SDK different from the chip vendor’s BSP / SDK?', ['The chip vendor’s BSP supports only the HAL and drivers with examples. The NebuLink Gateway RTOS SDK adds OSAL services, network connectivity support and examples on top of that BSP, so you can create IoT applications with much less effort. It also supports multiple targets in a single SDK.']),
  ('What development environment or OS is required?', ['Windows or Linux (Ubuntu). Details and steps are in the Doxygen documentation.']),
  ('Do you support an IDE for SDK development?', ['We do not provide an IDE, but we suggest the Eclipse IDE for development and debugging.']),
  ('How do I read the network connectivity state from the network LED (LED2)?', ['The network LED uses these pre-defined states:', ('ol', ['Solid glow — interface is starting and in progress.', 'Low-frequency blink (500 ms on/off) — external network connectivity.', 'Medium-frequency blink (250 ms on/off) — local network connectivity.', 'High-frequency blink (100 ms on/off) — error in connectivity.', 'Off — service has not started yet.', 'Five medium-frequency blinks every 4 seconds — Wi-Fi access point mode, network creation. For STA and AP+STA, the configurations above apply.']), 'See the Doxygen documentation for more details.']),
  ('How do I read the cloud connectivity state from the cloud LED (LED3)?', ['The cloud LED uses these pre-defined states:', ('ol', ['Solid glow — cloud service is starting.', 'Low-frequency blink — connection successful.', 'High-frequency blink — service disconnected.', 'Off — LED service has not started yet.']), 'See the Doxygen documentation for more details.']),
  ('How do I tell that the board has started successfully from the power LED (LED1)?', ['The power LED uses these pre-defined states:', ('ol', ['Night Rider pattern — firmware boot-up in progress (10-second timeout).', 'High-frequency blink — issue during firmware boot-up.', 'Solid glow — firmware booted successfully.', 'Off — firmware did not start.']), 'See the Doxygen documentation for more details.']),
  ('How do I check whether the NLG1XXX board has entered boot mode?', ['Check the SLS USB-2-UART settings for the boot / run mode switch. With these you can put the board into boot mode to flash new firmware using a tool or script. See the Doxygen documentation for more details.']),
 ]),
 ('NebuLink Gateway — OSGi SDK', [
  ('What is the NebuLink Gateway OSGi SDK?', ['A completely Java-based SDK that helps you create end applications for edge gateways, such as industrial control applications that operate locally and remotely, quickly and easily.']),
  ('What does the OSGi SDK offer?', ['It provides network connectivity over Wi-Fi, Ethernet and cellular GSM, and protocol support including Modbus, OPC-UA, BACnet and data acquisition.']),
  ('How does the OSGi SDK work?', ['Follow the API and user guide to create your end application quickly. The build generates a .dp file, which you install on the board as described in the guide.']),
  ('Can I use the OSGi SDK on my own boards or hardware?', ['Yes. Any board with at least one network interface can use the SDK.']),
  ('How should I start with the OSGi SDK?', ['Follow the API / user guide document. A sample application is provided for quick support.']),
  ('Is there a commercial licence for the OSGi SDK?', ['Yes. You sign a commercial agreement with a defined interval to use it as your requirements need.']),
  ('Can I buy only Nebulae boards or hardware and use my own SDK?', ['Yes.']),
  ('Do you provide an application example?', ['Yes. We provide a sample application with a YALGAAR connection that pushes dummy data to the cloud.']),
  ('How can I update the image on the gateway?', ['You can update the image using USB, SD card or TFTP (Ethernet).']),
  ('Does the gateway provide Modbus slave?', ['No.']),
  ('Does the gateway provide Modbus master?', ['Yes.']),
  ('Does the gateway use open-source libraries?', ['Yes. The OSGi SDK uses a few open-source libraries, which are listed in the Excel file provided.']),
  ('Does the gateway provide protocol conversion?', ['Not yet. Modbus to OPC-UA conversion is planned for the future.']),  # REVIEW
  ('Can I see logs over USB?', ['No. Use the serial console instead (see the next question).']),
  ('How do I check serial logs on the console?', ['Connect a USB-to-UART converter (BAFO cable) to the RS232 port at 115200 baud, as described in the document.']),
  ('I loaded the default example binaries but the gateway does not connect to Middleware. What should I do?', ['Use the LED pattern to identify whether the problem is the interface connection or the cloud.']),
  ('Can I use a third-party cloud service with the OSGi SDK?', ['Yes.']),
  ('Do you provide end-to-end development and technical support?', ['We do not have an end-to-end facility right now, but we provide online remote support if the customer needs it.']),  # REVIEW
  ('How is the SDK different from the chip vendor’s BSP / SDK?', ['Our BSP SDK is the same as the Yocto SDK, but no one else provides Windows SDK support. We provide Yocto support for both Windows and Linux systems, which reduces development time.']),
  ('What development environment or OS is required?', ['Windows or Linux.']),
  ('Do you support an IDE for SDK development?', ['Yes, we support the Eclipse IDE.']),
  ('How do I tell that the board has started successfully from the power LEDs?', [('ul', ['LED1 on — 5 V supply is OK.', 'LED2 on — 3.3 V supply is OK.'])]),
  ('How do I tell that a firmware update has completed?', ['LED5, LED6, LED7 and LED8 blink 5 times when a firmware update completes successfully over SD card, USB or TFTP.']),
 ]),
 ('NebuLink Middleware', [
  ('What is NebuLink Middleware?', ['NebuLink Middleware is a mediator between the hardware and the application. It lets connected devices interact easily and securely with your applications and with other devices.']),
  ('What are the best features of NebuLink Middleware?', ['Absolute control, continuous integration, quick response, and secure data transmission with encryption.']),
  ('How does Nebulae Middleware work?', ['Connected devices such as sensors, actuators, embedded devices, smart appliances and wearables connect to Nebulae Middleware over WebSockets or secure MQTT. The Nebulae Middleware SDK allows secure, low-latency, low-overhead, bi-directional communication.']),
  ('How does the Nebulae IoT gateway talk to the cloud, and which messaging protocol is used?', ['A hybrid encryption system based on RSA with a 2048-bit key pair and AES with a 256 (512)-bit key. The messaging protocols are MQTT and HTTPS.']),
  ('Do you provide a FOTA service? How can the firmware be updated?', ['Yes, the NebuLink FOTA service is provided. To update the firmware, refer to our SDKs or contact us.']),
  ('Which programming language is used for cloud applications?', ['Cloud applications can be developed in any language you prefer.']),
  ('What security does NebuLink Middleware provide?', ['HTTPS, and RSA with a 2048-bit key pair and AES with a 256 (512)-bit key.']),
  ('Which authentication protocols does NebuLink Middleware support?', ['OAuth 2.0 with HTTPS for application communication, and RSA with a 2048-bit key pair and AES with a 256 (512)-bit key for device communication.']),
  ('Is my data secure with NebuLink Middleware?', ['Yes.']),
  ('Can I use other cloud services if I do not want NebuLink Middleware?', ['Yes. We provide third-party cloud integration.']),
  ('In which regions is Nebulae Middleware available?', ['Currently Nebulae Middleware is available in the Canada region. It can also be hosted on a private cloud, and we provide dedicated-server hosted Nebulae Middleware.']),  # REVIEW
  ('Which communication and authentication protocols does Nebulae Middleware support?', ['For control-plane operations, Nebulae Middleware supports HTTPS. For data-plane operations it supports HTTPS, WebSockets and secure MQTT, a protocol often used in IoT scenarios. You can use certificates generated by Nebulae Middleware, or certificates signed by your preferred Certificate Authority (CA).']),
  ('What is the Device Gateway?', ['The Device Gateway is the backbone of communication between connected devices and the cloud. It supports the publish/subscribe (pub/sub) messaging pattern, which enables scalable, low-latency, low-overhead communication, and is useful where very large numbers of devices communicate frequently with minimal delay. Clients publish messages on logical channels called “topics”, and other clients subscribe to topics to receive them. The Device Gateway handles the communication between publishers and subscribers, so organisations no longer have to provision, operate, scale and maintain their own servers as device gateways.']),
  ('What is MQTT?', ['MQTT is a lightweight pub/sub protocol designed to minimise network bandwidth and device resource requirements. It also supports secure communication using TLS and is often used in IoT. MQTT v3.1.1 is an OASIS standard, and the Device Gateway supports most of the MQTT specification.']),
  ('What is the Nebulae Middleware Device SDK?', ['The Device SDKs simplify and speed up the development of code that runs on connected devices (microcontrollers, sensors, actuators, smart appliances, wearables and more). Devices can optimise memory, power and network bandwidth use, and communicate securely with low latency and low overhead over WebSockets and MQTT. The SDKs also speed up application development with higher-level abstractions, such as synchronising a device’s state with its Device Shadow in Nebulae Middleware.']),
  ('Which device SDKs does Nebulae Middleware provide?', ['Currently the device SDK is provided in Java, Android, C++, C and Objective-C.']),
  ('Is Nebulae Middleware free? What is the pricing?', ['Please reach out to us for pricing.']),
  ('Can I use Nebulae Middleware with any device?', ['Yes, but you need to install the Nebulae Middleware device SDK on the device.']),
 ]),
]
