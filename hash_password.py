"""
password.encode(): Converts the password from a string to bytes using UTF-8 encoding, we must use .encode() to specify the encoding
hashlib.sha256(...): Initializes a SHA-256 hash object from the hashlib module.
.hexdigest(): Returns the hexadecimal representation of the hash."""

#Importing hashlib from builtin python libary
import hashlib

# This function convert the actual password into hash SHA 256 .
def hash_password(password):
  """
  This function return the actual password into hash SHA 256 .
  Use hashlib to securely hash the password
  first password.encode() this will run then hashlib.sha256(password.encode()) then this will then whole will run
  """
  return hashlib.sha256(password.encode()).hexdigest()
