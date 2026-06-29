# Project description

In this project I have made the design for a PCB that will keep track of the position of a target that it is mounted to.

It is the prototype of a tracker that will update the position using a GPS sensor and a LoRa modem for communication with a server.
The board is made to connect to the Orande LiveObjects servver from which the data is put inside a MongoDB database and later a template is made in Grafana with the longitude and latitude coordinates.

The programming of the pcb was done in STM32CubeIDE and all communications between The GPS, Lora and COM port were UART communications.

# The Electrical Scheme

<img width="1365" height="947" alt="image" src="https://github.com/user-attachments/assets/821140e4-9348-4c54-9e7a-1efc7d389eb7" />

# The layout of the PCB

<img width="1184" height="911" alt="image" src="https://github.com/user-attachments/assets/f9091a72-54da-4ce1-a0ad-e1be79efe718" />

