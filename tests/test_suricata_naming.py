import os
import sys

if sys.version_info[:2] < (3, 8):
    sys.exit("You are running an incompatible version of Python, please use >= 3.8")

CUCKOO_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(CUCKOO_ROOT)

from lib.cuckoo.common.suricata_detection import get_suricata_family


def test_suricata_naming():
    assert "Sharik" == get_suricata_family("ET MALWARE Sharik/Smoke CnC Beacon 11")
    assert "Revenge-RAT" == get_suricata_family("ETPRO TROJAN MSIL/Revenge-RAT CnC Checkin")
    assert "Predator" == get_suricata_family("ETPRO TROJAN Win32/Predator The Thief Initial CnC Checkin")
    assert "MedusaHTTP" == get_suricata_family("ET TROJAN MedusaHTTP Variant CnC Checkin M2")
    assert False is get_suricata_family("ETPRO TROJAN Virus.Win32.Lamer.bd checkin")
    assert False is get_suricata_family("ETPRO TROJAN Custom Cobalt Strike Beacon UA")
    assert False is get_suricata_family("ET TROJAN Unit42 PoisonIvy Keepalive to CnC")
    assert False is get_suricata_family("ET TROJAN Hacking Team Implant Exfiltration")
    assert False is get_suricata_family("ET MALWARE User Agent (TEST) - Likely Webhancer Related Spyware")
    assert False is get_suricata_family("ET MALWARE Media Pass ActiveX Install")
    assert False is get_suricata_family("ETPRO TROJAN Google Docs Phishing Landing Dec 18 2016")
    assert False is get_suricata_family("ETPRO TROJAN PowerShell Downloader CnC Checkin")
    assert False is get_suricata_family("ET TROJAN Self-Signed Cert Observed in Various Zbot Strains")
    assert False is get_suricata_family("ETPRO TROJAN Multi Locker CnC Beacon 1")
    assert False is get_suricata_family("ETPRO TROJAN MSIL/Agent.SNQ POST with System Info")
    assert False is get_suricata_family("ET TROJAN WScript/VBScript XMLHTTP downloader likely malicious get?src=")
    assert False is get_suricata_family("ET TROJAN Fileless infection dropped by EK CnC Beacon")
    assert "Raccoon" == get_suricata_family("ETPRO TROJAN Win32.Raccoon Stealer Checkin")
    assert "Vidar" == get_suricata_family("ETPRO TROJAN Vidar/Arkei/Megumin Stealer HTTP POST Pattern")
    assert False is get_suricata_family("ETPRO TROJAN Win32/VBInject.T User-Agent ([Mozilla Firefox Cool])")
    assert False is get_suricata_family("ETPRO TROJAN F-AV CnC Host Checkin")
    assert False is get_suricata_family("ETPRO TROJAN MSIL/Agent.SNQ POST with System Info")
    assert False is get_suricata_family("ET TROJAN WScript/VBScript XMLHTTP downloader likely malicious get?src=")
    assert False is get_suricata_family("ET TROJAN Fileless infection dropped by EK CnC Beacon")
    assert False is get_suricata_family("ETPRO TROJAN Win32/VBInject.T User-Agent ([Mozilla Firefox Cool])")
    assert False is get_suricata_family("ETPRO TROJAN F-AV CnC Host Checkin")
    assert "Malex" == get_suricata_family("ETPRO TROJAN Win32/Malex.gen!E Checkin")
    assert False is get_suricata_family("ET TROJAN Win32-Dynamer.dtc Reporting")
    assert False is get_suricata_family("ETPRO TROJAN Perfect Keyloger sending stolen data")
    assert False is get_suricata_family("ETPRO TROJAN Trojan.Win32.KillProc.dfwkin DNS TXT Checkin Response")
    assert False is get_suricata_family("ETPRO TROJAN Trojan-PSW.Win32.KeyLogger.j CnC Beacon")
    assert False is get_suricata_family("ETPRO TROJAN FakeAV-BT Checkin")
    assert False is get_suricata_family("ETPRO TROJAN W32.Fakeoff Checkin")
    assert False is get_suricata_family("ETPRO TROJAN MSIL/Owned Bot CnC Checkin")
    assert False is get_suricata_family("ETPRO TROJAN Win-Python-Backdoor Config Inbound")
    assert False is get_suricata_family("ETPRO TROJAN VBS/Susp.Enumerator Script Inbound")
    assert "CrazyCrypt" == get_suricata_family("ETPRO TROJAN CrazyCrypt Ransomware CnC Activity")
    assert "Virut" == get_suricata_family("ET TROJAN Win32.Virut - GET")
    assert False is get_suricata_family("ET TROJAN Trojan.FakeMS Checkin")
    assert False is get_suricata_family("ET TROJAN iOS/WireLurker CnC Beacon")
    assert False is get_suricata_family("ETPRO TROJAN Mal/Banker-EV CnC Beacon")
    assert False is get_suricata_family("ETPRO TROJAN Win32.Agent-AOCW Downloading a3x file")
    assert "Carbanak" == get_suricata_family("ETPRO TROJAN Carbanak/FIN7 Bateleur SSL Certificate Detected")
    assert False is get_suricata_family("ETPRO TROJAN W97M.Dropper Downloading EXE")
    assert False is get_suricata_family("ET MALWARE ABX Toolbar ActiveX Install")
    assert "Tinba" == get_suricata_family("ET MALWARE [PTsecurity] Tinba Checkin 4")
    assert False is get_suricata_family("ET TROJAN Suspicious User-Agent (WindowsNT) With No Separating Space")
    assert "Photoloader" == get_suricata_family("ET MALWARE W32/Photoloader.Downloader Request Cookie")
    assert "pcrat" == get_suricata_family("ET MALWARE Backdoor family PCRat/Gh0st CnC traffic")
    assert "Stealc" == get_suricata_family("ET MALWARE [SEKOIA.IO] Win32/Stealc C2 Check-in")


if __name__ == "__main__":
    print("Suricata detects as:", get_suricata_family(sys.argv[1]))
