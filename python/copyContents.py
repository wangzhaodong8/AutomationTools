from lxml import etree
import os,sys,glob
from subprocess import call
import argparse
from shutil import copy

__author__ = "David wang"
__version__ = "2.0"
__maintainer__ = "David wang"
__email__ = "zhaodong.wang@ivanti.com"

parser=argparse.ArgumentParser(description='Copy contents and products')
parser.add_argument('--host',help="this is the linux host.")
args=parser.parse_args()
host=args.host

vendor=""
osfolder=""
for v in glob.glob('./V[a-zA-Z0-9_-]*.xml'):
    gxml=etree.parse(v)
    vendor=gxml.xpath("/Vulnerability/Vendor")[0].text
    break
if vendor == "Redhat":
    osfolder="rhlinux"
elif vendor == "CentOS":
    osfolder="CentOS"
elif vendor == "Novell":
    osfolder="sles9"
else :
    osfolder="CentOS"
#for i in os.listdir("//172.29.0.153/CVSContent/PatchManagerContent/Vulnerabilities/"+osfolder):
for v in glob.glob('./V[a-zA-Z0-9_-]*.xml'):
    fxml=etree.parse(v)
    pids=fxml.xpath("//Products/ID")
    for i in pids:
       if os.path.isfile("P_"+i.text+".xml"):
               pass
       else:
               copy("//172.29.0.153/CVSContent/PatchManagerContent/Vulnerabilities/"+osfolder+"/P_"+i.text+".xml",os.getcwd())
call(["pscp.exe","-pw","landesk","./*.xml","root@"+host+":/contents/"])

