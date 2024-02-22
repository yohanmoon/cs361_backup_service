<div align="center">
<h2 align="center">Automated Back Up Microservice</h3>

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

This is a microservice where the program starts automated backup of the file specified by the user at every interval specified by the user. 
The automated back-up will begin once the client program is connected to the server by `Socket`, this will continue without any data requested by the client program.

The microservice sends back the file path of the latest back-up when a request is made from the client program.

### Uses
  * `Python`
  * `Socket`
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Instruction -->
## Instruction

Communication between the server(microservice) and the client program is made via `Socket`.
Currently, the source file path and the backup interval are entered at the beginning of the program as
the microservice does not know where the client plans to hold the source file.

Start the client program after above user inputs are made.


### Request Data

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
4. connect to the server on local computer
   ```sh
   s.connect(('127.0.0.1', port))
   ```
5. send request data by encoding the string
   ```sh
   request = "revert"
   s.send(request.encode())
   ```
   * The microservice will respond to `"Revert"` and `"revert"` for retrieval of lastest backup file. 


### Receive Data

* Receive the data by decoing to get the string
   ```sh
   s.recv(1024).decode()
   ```
   * The data received from the server will the absolute path of the backup file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## UML

example sentence

<p align="right">(<a href="#readme-top">back to top</a>)</p>


