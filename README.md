<div align="center">
<h2 align="center">Back Up Microservice</h3>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#instruction">Instruction</a>
      <ul>
        <li><a href="#request-data">Request Data</a></li>
      </ul>
      <ul>
        <li><a href="#receive-data">Receive Data</a></li>
      </ul>
    </li>
    <li><a href="#uml">UML sequence diagram</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a microservice where the program creates backup file of path specified by the user.

The backup automation will begin once the client program is connected to the server by `Socket`.
The backup files will be saved in `./backup_file` directory.

The microservice sends back the path of the latest backup file when a request is made from the client program.

### Uses
  * `Python`
  * `Socket`
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Instruction -->
## Instruction

Communication between the server(microservice) and the client program is made via `Socket`.



### Request Data
How to request data from the microservice:
1. Import socket module
   ```sh
   import socket
   ```
2. Create a socket object
   ```sh
   s = socket.socket()
   ```
3. Define the port on which you want to connect
   ```sh
   port = 12345
   ```
4. Connect to the server on local computer
   ```sh
   s.connect(('127.0.0.1', port))
   ```
5. Send request data by encoding the string
   ```sh
   request = "revert"
   s.send(request.encode())
   ```
   * The microservice will respond to `"Backup"` and `"backup"` for creating a backup file.
   * The microservice will respond to `"Revert"` and `"revert"` for retrieval of lastest backup file. 


### Receive Data
How to receive data from the microservice:
* Receive the data by decoding to get the string
   ```sh
   s.recv(1024).decode()
   ```
   * The decoded string will the absolute path of the backup file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## UML

![Assignment 9 UML](https://github.com/yohanmoon/cs361_backup_service/assets/90400063/ef87a658-59a3-49cd-8a91-b8452b4d3d33)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


