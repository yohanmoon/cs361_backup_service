<div align="center">
<h3 align="center">Automatic Back Up Microservice</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Instruction -->
## Instruction

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Request Data

This is an example of how to list things you need to use the software and how to install them.
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
   request = "abc"
   s.send(request.encode())
   ```

### Receive Data


* Receive the data by decoing to get the string
   ```sh
   s.recv(1024).decode()
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## UML

example sentence

<p align="right">(<a href="#readme-top">back to top</a>)</p>


