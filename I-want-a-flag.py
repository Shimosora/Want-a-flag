#! /usr/bin/env python
#! -*- codinf:utf-8 -*-

#pcapファイルを引っ張る
from scapy.all import *
p = rdpcap('icmp_data.pcap')

#データ部の連結
data = ""
for i in range(len(p)):
	if p[i]['IP'].src == "10.29.31.177" and p[i]['ICMP'].type ==0:
		load = p[i]['Raw'].load
		data += load

#データをjpgで保存
f = open('flag.jpg','wb')
f.write(data)
f.close()