import subprocess
import optparse
print(r""" _______     _______    _________    _______ 
(  ____ \   (  ____ \   \__   __/   (  ____ \
| (    \/   | (    \/      ) (      | (    \/
| |         | |            | |      | (_____ 
| |         | |            | |      (_____  )
| |         | |            | |            ) |
| (____/\ _ | (____/\ _ ___) (___ _ /\____) |
(_______/(_)(_______/(_)\_______/(_)\_______)""")
print("\n****************************************************************")
print(r"""+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|M|A|C| |C|H|A|N|G|E|R| |L|I|N|U|X|
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")
print("\n* Developed by Team Proteger *")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface name to MAC its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Enter Interface name, use -- help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please Enter MAC address , use -- help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + "to" + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options=get_arguments()
change_mac(options.interface,options.new_mac)