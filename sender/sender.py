from Sky-CLI.LoRa-RaspberryPi import loralib                                                          
loralib.init(0, 868000000, 7)                                           
loralib.send(b'hello');