# DNSServer.py
# CS-GY 6843 – Computer Networking – Python DNS Lab Part 2

import dns.message
import dns.rdatatype
import dns.rdataclass
import dns.rdtypes
import dns.rdata
from dns.rdtypes.ANY.MX import MX
from dns.rdtypes.ANY.SOA import SOA
import socket
import threading
import signal
import os
import sys
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


# ------------------ AES KEY GENERATION AND ENCRYPTION ------------------

def generate_aes_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
