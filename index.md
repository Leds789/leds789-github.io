---
layout: default
---

Hello, world!

I am Matthew, a cybersec student and professional chef with a strong passion for computer science and hand-on learning. My journey has taken me from cooking to the world of IT where I'm currently trying to build my skills and certs up and hoping to eventually work in IT.

This site is where I plan to showcase my projects and learning 

[LedsLabs.com](https://ledslabs.com/)

# My Home Server

I turned my old laptop into a home webserver. Installing ubuntu, setting up a media server, VPN, Pi-Hole for DNS and DHCP allocation. 

- Tech Used
  - Ubuntu / Docker / Pi-Hole / Wireguard 
- Skills Learned
    - Server Management / Network Setup / Firewall

## Education Projects

*   Cert 4 CyberSecurity
*   Cisco CCST networking
*   TryHackMe Courses 


### Write-Ups & CTFs

*  PicoCTF
*  OverTheWire
*  HackThisSite

### Technical SKills

*  Networking: LAN/WAN Setup / ip config / firewalls
*  Operating Systems: Windows / Linux / MacOS
*  Tools: Wireshark / Metasploit / nMap / VMbox

```python
### Port Scanner (Python)
This script scans a target IP for open ports, showcasing basic networking skills.

import socket

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
target_ip = '192.168.1.1'
port_list = [22, 80, 443]
port_scanner(target_ip, port_list)

```

```python
### Password Hashing Script

import hashlib

# This function generates a SHA-256 hash for a given password.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage of hashing
original = "my_password"
hashed = hash_password(original)
print("Hashed password:", hashed)

# Function to compare a given password with a stored hash
def compare_passwords(password, hashed):
    return hash_password(password) == hashed

# Example usage of comparison
print("Password match:", compare_passwords("my_password", hashed))  # True
print("Password match:", compare_passwords("wrong_password", hashed))  # False

```

* * *

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching]




```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
