# Project description

In this project i have designed and coded a shield for the STM32 Nucleo board L476RG.

The shield is the prototype of a tracker that will update the position using a GPS module and a LoRa modem for communication with a server.
The board is made to connect to the Orange LiveObjects server from which the data is put inside a MongoDB database and later a template is made in Grafana with the longitude and latitude coordinates.
Two Python scripts are present in the project. One for getting the data from the LiveObjects through MQTT protocol, and the other links the data received to a endpoint. That endpoint in later linked to a Grafana JSON plugin to gather that data.

The programming of the board was done in STM32CubeIDE and all communications between The GPS, Lora and COM port were UART communications.

# The Electrical Schematic

<img width="1365" height="947" alt="image" src="https://github.com/user-attachments/assets/821140e4-9348-4c54-9e7a-1efc7d389eb7" />

# The layout of the PCB

<img width="1184" height="911" alt="image" src="https://github.com/user-attachments/assets/f9091a72-54da-4ce1-a0ad-e1be79efe718" />

