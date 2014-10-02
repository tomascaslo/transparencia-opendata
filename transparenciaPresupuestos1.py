# -*- coding: utf-8 -*-

import httplib 
import urllib 
import urllib2 

from bs4 import BeautifulSoup

links = []
links1 = []
links2 = []
jsonData = "{ \n"
url = ''

count = 0

#PageSpecificData
primaryUrl = "http://sg.nl.gob.mx/OrdenCompra_2009/"
aspxPage1 = "BsqAnio.aspx?Anio=2012&Nombre=&EntidadId=1004&ConceptoId=308"
aspxPage2 = "BsqAnioProvMes.aspx?Anio=2012&EntidadId=1004&ConceptoId=308" #&ProveedorId=9687 &MesId=5

def dataPage1():
	for currPage in range(31): #MODIFICAR PARAMETRO A 31, CAMBIO SOLO PARA TEST RAPIDO
		headers = {
			'Host': 'sg.nl.gob.mx',
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Origin': 'http://sg.nl.gob.mx',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'http://sg.nl.gob.mx/OrdenCompra_2009/BsqAnio.aspx?Anio=2012&Nombre=&EntidadId=1004&ConceptoId=308',
			'Accept-Encoding': 'gzip,deflate,sdch',
			'Accept-Language': 'es-ES,es;q=0.8,en;q=0.6',
			'Cookie': 'ASP.NET_SessionId=tbmhxeuzlow11t45u1zmab45; __utma=57766901.338069635.1393101802.1393101802.1393101802.1; __utmc=57766901; __utmz=57766901.1393101802.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.3.338069635.1393101802'
		}

		#"__EVENTTARGET=ddlPagina&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJMTgyMjc2NzY3DxYEHgRBbmlvBQQyMDEyHgZOb21icmVlFgICAw9kFgQCAQ9kFgICAQ8PFgIeBFRleHQF9xI8cCBjbGFzcz0nbm90YSc%2BQ29uc3VsdGEgbGEgPGEgY2xhc3M9ICdMaWdhTm90YScgdGFyZ2V0PSdfdG9wJyBocmVmPSdodHRwOi8vd3d3Lm5sLmdvYi5teC8%2FUD10cmFuc3BhcmVuY2lhX3NmeXRnZSZhZG09MjAwMyc%2BaW5mb3JtYWNpw7NuIHDDumJsaWNhIGRlIGVzdGEgZGVwZW5kZW5jaWEgZ2VuZXJhZGEgZW4gbGEgcGFzYWRhIEFkbWluaXN0cmFjacOzbiAyMDAzLTIwMDkuPC9hPjwvcD48dGFibGUgY2xhc3M9J3RibEhlYWRlcicgY2VsbHBhZGluZz0nMCcgY2VsbHNwYWNpbmc9JzAnIGJvcmRlcj0nMCcgd2lkdGg9JzEwMCUnPjx0cj48dGQ%2BQ29uY2VwdG86Jm5ic3A7PHN0cm9uZz48YSBpZD0nbG5rQ29uY2VwdG8nIGNsYXNzPSdMaWdhJyB0YXJnZXQ9J19wYXJlbnQnIGhyZWY9J2h0dHA6Ly93d3cubmwuZ29iLm14Lz9QPXRyYW5zcGFyZW5jaWFfYXBlJmNvbmNlcHRvPW9yZGVuZXMtY29tcHJhJz4mbGFxdW87IMOTcmRlbmVzIGRlIGNvbXByYTwvYT48L3N0cm9uZz48L3RyPjx0cj48dGQgc3R5bGU9J2hlaWdodDo1cHg7Jz48L3RkPjwvdHI%2BPHRyPjx0ZD5JbmZvcm1hY2nDs24gcHVibGljYWRhIGRlIG9maWNpbyBkZTombmJzcDxzdHJvbmc%2BPGEgaWQ9J2xua09maWNpbycgY2xhc3M9J0xpZ2EnIHRhcmdldD0nX3BhcmVudCcgaHJlZj0naHR0cDovL3d3dy5ubC5nb2IubXgvP1A9dHJhbnNwYXJlbmNpYV9zZnl0Z2UnPiZsYXF1bzsgU2VjcmV0YXLDrWEgZGUgRmluYW56YXMgeSBUZXNvcmVyw61hIEdlbmVyYWwgZGVsIEVzdGFkbzwvYT48L3N0cm9uZz48L3RkPjwvdHI%2BPHRyPjx0ZCBzdHlsZT0naGVpZ2h0OjVweDsnPjwvdGQ%2BPC90cj48dHI%2BPHRkIHN0eWxlPSdoZWlnaHQ6NXB4Oyc%2BPC90ZD48L3RyPjx0cj48dGQgY2xhc3M9J2xibERlc2NyaXBjaW9uQ29uY2VwdG8nPkNvbnN1bHRhIGluZm9ybWFjacOzbiBhZGljaW9uYWwgcmVsYWNpb25hZGEgY29uIGVsIHByb2Nlc28gZGUgYWRxdWlzaWNpb25lcyB5IHNlcnZpY2lvcyBkZSBsYSBBZG1pbmlzdHJhY2nDs24gUMO6YmxpY2EgZGVsIEVzdGFkby48L3RkPjwvdHI%2BPHRyPjx0ZCBzdHlsZT0naGVpZ2h0OjVweDsnPjwvdGQ%2BPC90cj48dHI%2BPHRkPjwvdGQ%2BPC90cj48dHI%2BPHRkIHN0eWxlPSdoZWlnaHQ6NXB4Oyc%2BPC90ZD48L3RyPjwvdGFibGU%2BPGJyIC8%2BPHRhYmxlIGNlbGxzcGFjaW5nPSIwIiBjZWxscGFkZGluZz0iMiIgYm9yZGVyPSIwIiBzdHlsZT0iYm9yZGVyLXdpZHRoOjBweDt3aWR0aDoxMDAlO2JvcmRlci1jb2xsYXBzZTpjb2xsYXBzZTsiPgoJPHRyPgoJCTx0ZD48L3RkPjx0ZD48dGFibGUgY2VsbHNwYWNpbmc9IjAiIGNlbGxwYWRkaW5nPSIxIiBib3JkZXI9IjAiIHN0eWxlPSJib3JkZXItd2lkdGg6MHB4O3dpZHRoOjEwMCU7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlOyI%2BCgkJCTx0cj4KCQkJCTx0ZCB2YWxpZ249InRvcCIgc3R5bGU9IndpZHRoOjElOyI%2BPC90ZD48dGQgYWxpZ249ImxlZnQiIHN0eWxlPSJ3aWR0aDo5OSU7Ij48c3BhbiBjbGFzcz0iU3ViVGl0dWxvIj7Dk3JkZW5lcyBkZSBjb21wcmE8L3NwYW4%2BPC90ZD4KCQkJPC90cj48dHI%2BCgkJCQk8dGQgdmFsaWduPSJ0b3AiIHN0eWxlPSJ3aWR0aDoxJTsiPjwvdGQ%2BPHRkIGFsaWduPSJsZWZ0IiBzdHlsZT0id2lkdGg6OTklOyI%2BPHNwYW4gY2xhc3M9IkxhYmVsTWVuc2FqZSI%2BUmVzcG9uc2FibGU6IFNlY3JldGFyw61hIGRlIEZpbmFuemFzIHkgVGVzb3JlcsOtYSBHZW5lcmFsIGRlbCBFc3RhZG8gLSBEaXJlY2Npw7NuIGRlIEFkcXVpc2ljaW9uZXMgeSBTZXJ2aWNpb3MuPC9zcGFuPjwvdGQ%2BCgkJCTwvdHI%2BPHRyPgoJCQkJPHRkIHZhbGlnbj0idG9wIiBzdHlsZT0id2lkdGg6MSU7Ij48L3RkPjx0ZCBhbGlnbj0ibGVmdCIgc3R5bGU9IndpZHRoOjk5JTsiPjxzcGFuIGNsYXNzPSJMYWJlbE1lbnNhamUiPihBY3R1YWxpemFkbyBhIEZlYnJlcm8vMjAxNCk8L3NwYW4%2BPC90ZD4KCQkJPC90cj48dHI%2BCgkJCQk8dGQgdmFsaWduPSJ0b3AiIHN0eWxlPSJ3aWR0aDoxJTsiPjwvdGQ%2BPHRkIGFsaWduPSJsZWZ0IiBzdHlsZT0id2lkdGg6OTklOyI%2BPHNwYW4gY2xhc3M9IkxhYmVsTWVuc2FqZSI%2BRGVzZGUgYXF1w60gcG9kcsOhIGNvbnN1bHRhciBsYXMgw7NyZGVuZXMgZGUgY29tcHJhIGRlbCBHb2JpZXJubyBkZWwgRXN0YWRvOjwvc3Bhbj48L3RkPgoJCQk8L3RyPjx0cj4KCQkJCTx0ZD48L3RkPjx0ZD48dGFibGUgY2VsbHNwYWNpbmc9IjAiIGNlbGxwYWRkaW5nPSIxIiBib3JkZXI9IjAiIHN0eWxlPSJib3JkZXItd2lkdGg6MHB4O3dpZHRoOjEwMCU7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlOyI%2BCgoJCQkJPC90YWJsZT48L3RkPgoJCQk8L3RyPjx0cj4KCQkJCTx0ZCBzdHlsZT0id2lkdGg6MSU7Ij48L3RkPjx0ZCBzdHlsZT0id2lkdGg6OTklOyI%2BPC90ZD4KCQkJPC90cj4KCQk8L3RhYmxlPjwvdGQ%2BCgk8L3RyPgo8L3RhYmxlPmRkAgMPZBYIAgEPDxYCHwIFBDIwMTJkZAIDDw8WAh4HVmlzaWJsZWhkZAIHDw8WAh8DZ2QWDAIBDw8WAh8CBSozMDMgcmVnaXN0cm9zIGxvY2FsaXphZG8ocykgZW4gMzEgcMOhZ2luYXNkZAIDDw8WBB8CBS48aW1nIHNyYz1JbWFnZXMvaV9pbi5naWYgYWx0PUluaWNpYWwgYm9yZGVyPTA%2BHgdFbmFibGVkaGRkAgUPDxYEHwIFLzxpbWcgc3JjPUltYWdlcy9hX2luLmdpZiBhbHQ9QW50ZXJpb3IgYm9yZGVyPTA%2BHwRoZGQCBw8QZA8WH2YCAQICAgMCBAIFAgYCBwIIAgkCCgILAgwCDQIOAg8CEAIRAhICEwIUAhUCFgIXAhgCGQIaAhsCHAIdAh4WHxAFBzEgZGUgMzEFATBnEAUHMiBkZSAzMQUBMWcQBQczIGRlIDMxBQEyZxAFBzQgZGUgMzEFATNnEAUHNSBkZSAzMQUBNGcQBQc2IGRlIDMxBQE1ZxAFBzcgZGUgMzEFATZnEAUHOCBkZSAzMQUBN2cQBQc5IGRlIDMxBQE4ZxAFCDEwIGRlIDMxBQE5ZxAFCDExIGRlIDMxBQIxMGcQBQgxMiBkZSAzMQUCMTFnEAUIMTMgZGUgMzEFAjEyZxAFCDE0IGRlIDMxBQIxM2cQBQgxNSBkZSAzMQUCMTRnEAUIMTYgZGUgMzEFAjE1ZxAFCDE3IGRlIDMxBQIxNmcQBQgxOCBkZSAzMQUCMTdnEAUIMTkgZGUgMzEFAjE4ZxAFCDIwIGRlIDMxBQIxOWcQBQgyMSBkZSAzMQUCMjBnEAUIMjIgZGUgMzEFAjIxZxAFCDIzIGRlIDMxBQIyMmcQBQgyNCBkZSAzMQUCMjNnEAUIMjUgZGUgMzEFAjI0ZxAFCDI2IGRlIDMxBQIyNWcQBQgyNyBkZSAzMQUCMjZnEAUIMjggZGUgMzEFAjI3ZxAFCDI5IGRlIDMxBQIyOGcQBQgzMCBkZSAzMQUCMjlnEAUIMzEgZGUgMzEFAjMwZxYBZmQCCQ8PFgIfAgUvPGltZyBzcmM9SW1hZ2VzL3NfYS5naWYgYWx0PVNpZ3VpZW50ZSBib3JkZXI9MD5kZAILDw8WAh8CBSs8aW1nIHNyYz1JbWFnZXMvZl9hLmdpZiBhbHQ9RmluYWwgYm9yZGVyPTA%2BZGQCCQ88KwALAQAPFgweC18hSXRlbUNvdW50AgoeCERhdGFLZXlzFgAfA2ceCVBhZ2VDb3VudAIfHhVfIURhdGFTb3VyY2VJdGVtQ291bnQCrwIeEEN1cnJlbnRQYWdlSW5kZXhmZBYCZg9kFhQCAg9kFgZmDw8WAh8CBTwgUkFNSVJFWiBDQU5UVSBMVVogTUFSSUEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQskIDM1LDY3My40OGRkAgIPZBYCZg8VAgQyMDEyBDk2ODdkAgMPZBYGZg8PFgIfAgU8QUJBU1RFQ0VET1JBIEVNUFJFU0FSSUFMIElOVEVMSUdFTlRFLCBTLiBERSBSLkwuIERFIEMuVi4gICAgZGQCAQ8PFgIfAgUMJCA4MzUsMjAwLjAwZGQCAg9kFgJmDxUCBDIwMTIFMjU3MTRkAgQPZBYGZg8PFgIfAgU8QUNBQkFET1MgRE4sIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUMJCA3MDYsMDYzLjQ4ZGQCAg9kFgJmDxUCBDIwMTIFMjUwNzZkAgUPZBYGZg8PFgIfAgU8QUNUSVZJREFERVMgUFJPRkVTSU9OQUxFUyBJTlRFR1JBREFTLCBTLkEuIERFIEMuVi4gICAgICAgICAgZGQCAQ8PFgIfAgUMJCA2MzgsMDAwLjAwZGQCAg9kFgJmDxUCBDIwMTIFMjEwMTVkAgYPZBYGZg8PFgIfAgU8QURBTUUgT0NIT0EgQUxNQSBHRVJUUlVESVMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUMJCA0NDIsODA2LjgwZGQCAg9kFgJmDxUCBDIwMTIFMjIwNjRkAgcPZBYGZg8PFgIfAgU8QURBTiBOSUNPTEFTIFNFR1VSQSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUMJCA5NDYsMjEyLjAwZGQCAg9kFgJmDxUCBDIwMTIHODgxMDgyN2QCCA9kFgZmDw8WAh8CBTxBRFZBTlRBR0UgU0VDVVJJVFksIFMuIERFIFIuTC4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQ8kIDEzLDgwMSw2NjMuNjBkZAICD2QWAmYPFQIEMjAxMgUyNDgzNmQCCQ9kFgZmDw8WAh8CBTxBRVJPTkFVVElDQSBFTVBSRVNBUklBTCAgUy5BLiBERSBDLlYuICAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQ8kIDI2LDQxNyw1MzUuNTBkZAICD2QWAmYPFQIEMjAxMgQ3MTg3ZAIKD2QWBmYPDxYCHwIFPEFHRU5DSUEgRElHSVRBTCwgUy5BLiBERSBDLlYuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRkAgEPDxYCHwIFDyQgNDIsMDA2LDE2OS44NmRkAgIPZBYCZg8VAgQyMDEyBzg4MTA2ODlkAgsPZBYGZg8PFgIfAgU8QUxBWlJBS0kgVkVJTlRFIFZFSU5URSwgUy5BLiBERSBDLlYuICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUOJCAzLDY1NCwwMDAuMDBkZAICD2QWAmYPFQIEMjAxMgUyMjQ1M2Rkk%2FDrdZmQYduEOOLwqOwkWzxGQpc%3D&__EVENTVALIDATION=%2FwEWIwKv6KO0DQLM%2BoyvBQLclabBCQLDlabBCQLClabBCQLBlabBCQLAlabBCQLHlabBCQLGlabBCQLFlabBCQLUlabBCQLblabBCQLDlebCCQLDlerCCQLDle7CCQLDldLCCQLDldbCCQLDldrCCQLDld7CCQLDlcLCCQLDlYbBCQLDlYrBCQLClebCCQLClerCCQLCle7CCQLCldLCCQLCldbCCQLCldrCCQLCld7CCQLClcLCCQLClYbBCQLClYrBCQLBlebCCQKlwvGMCgKXkvnVC8iAzAFwI116x0xtC7AXkSDAyc0m&ddl"
		data = "__EVENTTARGET=ddlPagina&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJMTgyMjc2NzY3DxYEHgRBbmlvBQQyMDEyHgZOb21icmVlFgICAw9kFgQCAQ9kFgICAQ8PFgIeBFRleHQF9xI8cCBjbGFzcz0nbm90YSc%2BQ29uc3VsdGEgbGEgPGEgY2xhc3M9ICdMaWdhTm90YScgdGFyZ2V0PSdfdG9wJyBocmVmPSdodHRwOi8vd3d3Lm5sLmdvYi5teC8%2FUD10cmFuc3BhcmVuY2lhX3NmeXRnZSZhZG09MjAwMyc%2BaW5mb3JtYWNpw7NuIHDDumJsaWNhIGRlIGVzdGEgZGVwZW5kZW5jaWEgZ2VuZXJhZGEgZW4gbGEgcGFzYWRhIEFkbWluaXN0cmFjacOzbiAyMDAzLTIwMDkuPC9hPjwvcD48dGFibGUgY2xhc3M9J3RibEhlYWRlcicgY2VsbHBhZGluZz0nMCcgY2VsbHNwYWNpbmc9JzAnIGJvcmRlcj0nMCcgd2lkdGg9JzEwMCUnPjx0cj48dGQ%2BQ29uY2VwdG86Jm5ic3A7PHN0cm9uZz48YSBpZD0nbG5rQ29uY2VwdG8nIGNsYXNzPSdMaWdhJyB0YXJnZXQ9J19wYXJlbnQnIGhyZWY9J2h0dHA6Ly93d3cubmwuZ29iLm14Lz9QPXRyYW5zcGFyZW5jaWFfYXBlJmNvbmNlcHRvPW9yZGVuZXMtY29tcHJhJz4mbGFxdW87IMOTcmRlbmVzIGRlIGNvbXByYTwvYT48L3N0cm9uZz48L3RyPjx0cj48dGQgc3R5bGU9J2hlaWdodDo1cHg7Jz48L3RkPjwvdHI%2BPHRyPjx0ZD5JbmZvcm1hY2nDs24gcHVibGljYWRhIGRlIG9maWNpbyBkZTombmJzcDxzdHJvbmc%2BPGEgaWQ9J2xua09maWNpbycgY2xhc3M9J0xpZ2EnIHRhcmdldD0nX3BhcmVudCcgaHJlZj0naHR0cDovL3d3dy5ubC5nb2IubXgvP1A9dHJhbnNwYXJlbmNpYV9zZnl0Z2UnPiZsYXF1bzsgU2VjcmV0YXLDrWEgZGUgRmluYW56YXMgeSBUZXNvcmVyw61hIEdlbmVyYWwgZGVsIEVzdGFkbzwvYT48L3N0cm9uZz48L3RkPjwvdHI%2BPHRyPjx0ZCBzdHlsZT0naGVpZ2h0OjVweDsnPjwvdGQ%2BPC90cj48dHI%2BPHRkIHN0eWxlPSdoZWlnaHQ6NXB4Oyc%2BPC90ZD48L3RyPjx0cj48dGQgY2xhc3M9J2xibERlc2NyaXBjaW9uQ29uY2VwdG8nPkNvbnN1bHRhIGluZm9ybWFjacOzbiBhZGljaW9uYWwgcmVsYWNpb25hZGEgY29uIGVsIHByb2Nlc28gZGUgYWRxdWlzaWNpb25lcyB5IHNlcnZpY2lvcyBkZSBsYSBBZG1pbmlzdHJhY2nDs24gUMO6YmxpY2EgZGVsIEVzdGFkby48L3RkPjwvdHI%2BPHRyPjx0ZCBzdHlsZT0naGVpZ2h0OjVweDsnPjwvdGQ%2BPC90cj48dHI%2BPHRkPjwvdGQ%2BPC90cj48dHI%2BPHRkIHN0eWxlPSdoZWlnaHQ6NXB4Oyc%2BPC90ZD48L3RyPjwvdGFibGU%2BPGJyIC8%2BPHRhYmxlIGNlbGxzcGFjaW5nPSIwIiBjZWxscGFkZGluZz0iMiIgYm9yZGVyPSIwIiBzdHlsZT0iYm9yZGVyLXdpZHRoOjBweDt3aWR0aDoxMDAlO2JvcmRlci1jb2xsYXBzZTpjb2xsYXBzZTsiPgoJPHRyPgoJCTx0ZD48L3RkPjx0ZD48dGFibGUgY2VsbHNwYWNpbmc9IjAiIGNlbGxwYWRkaW5nPSIxIiBib3JkZXI9IjAiIHN0eWxlPSJib3JkZXItd2lkdGg6MHB4O3dpZHRoOjEwMCU7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlOyI%2BCgkJCTx0cj4KCQkJCTx0ZCB2YWxpZ249InRvcCIgc3R5bGU9IndpZHRoOjElOyI%2BPC90ZD48dGQgYWxpZ249ImxlZnQiIHN0eWxlPSJ3aWR0aDo5OSU7Ij48c3BhbiBjbGFzcz0iU3ViVGl0dWxvIj7Dk3JkZW5lcyBkZSBjb21wcmE8L3NwYW4%2BPC90ZD4KCQkJPC90cj48dHI%2BCgkJCQk8dGQgdmFsaWduPSJ0b3AiIHN0eWxlPSJ3aWR0aDoxJTsiPjwvdGQ%2BPHRkIGFsaWduPSJsZWZ0IiBzdHlsZT0id2lkdGg6OTklOyI%2BPHNwYW4gY2xhc3M9IkxhYmVsTWVuc2FqZSI%2BUmVzcG9uc2FibGU6IFNlY3JldGFyw61hIGRlIEZpbmFuemFzIHkgVGVzb3JlcsOtYSBHZW5lcmFsIGRlbCBFc3RhZG8gLSBEaXJlY2Npw7NuIGRlIEFkcXVpc2ljaW9uZXMgeSBTZXJ2aWNpb3MuPC9zcGFuPjwvdGQ%2BCgkJCTwvdHI%2BPHRyPgoJCQkJPHRkIHZhbGlnbj0idG9wIiBzdHlsZT0id2lkdGg6MSU7Ij48L3RkPjx0ZCBhbGlnbj0ibGVmdCIgc3R5bGU9IndpZHRoOjk5JTsiPjxzcGFuIGNsYXNzPSJMYWJlbE1lbnNhamUiPihBY3R1YWxpemFkbyBhIEZlYnJlcm8vMjAxNCk8L3NwYW4%2BPC90ZD4KCQkJPC90cj48dHI%2BCgkJCQk8dGQgdmFsaWduPSJ0b3AiIHN0eWxlPSJ3aWR0aDoxJTsiPjwvdGQ%2BPHRkIGFsaWduPSJsZWZ0IiBzdHlsZT0id2lkdGg6OTklOyI%2BPHNwYW4gY2xhc3M9IkxhYmVsTWVuc2FqZSI%2BRGVzZGUgYXF1w60gcG9kcsOhIGNvbnN1bHRhciBsYXMgw7NyZGVuZXMgZGUgY29tcHJhIGRlbCBHb2JpZXJubyBkZWwgRXN0YWRvOjwvc3Bhbj48L3RkPgoJCQk8L3RyPjx0cj4KCQkJCTx0ZD48L3RkPjx0ZD48dGFibGUgY2VsbHNwYWNpbmc9IjAiIGNlbGxwYWRkaW5nPSIxIiBib3JkZXI9IjAiIHN0eWxlPSJib3JkZXItd2lkdGg6MHB4O3dpZHRoOjEwMCU7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlOyI%2BCgoJCQkJPC90YWJsZT48L3RkPgoJCQk8L3RyPjx0cj4KCQkJCTx0ZCBzdHlsZT0id2lkdGg6MSU7Ij48L3RkPjx0ZCBzdHlsZT0id2lkdGg6OTklOyI%2BPC90ZD4KCQkJPC90cj4KCQk8L3RhYmxlPjwvdGQ%2BCgk8L3RyPgo8L3RhYmxlPmRkAgMPZBYIAgEPDxYCHwIFBDIwMTJkZAIDDw8WAh4HVmlzaWJsZWhkZAIHDw8WAh8DZ2QWDAIBDw8WAh8CBSozMDMgcmVnaXN0cm9zIGxvY2FsaXphZG8ocykgZW4gMzEgcMOhZ2luYXNkZAIDDw8WBB8CBS08aW1nIHNyYz1JbWFnZXMvaV9hLmdpZiBhbHQ9SW5pY2lhbCBib3JkZXI9MD4eB0VuYWJsZWRnZGQCBQ8PFgQfAgUuPGltZyBzcmM9SW1hZ2VzL2FfYS5naWYgYWx0PUFudGVyaW9yIGJvcmRlcj0wPh8EZ2RkAgcPEGQPFl1mAgECAgIDAgQCBQIGAgcCCAIJAgoCCwIMAg0CDgIPAhACEQISAhMCFAIVAhYCFwIYAhkCGgIbAhwCHQIeAh8CIAIhAiICIwIkAiUCJgInAigCKQIqAisCLAItAi4CLwIwAjECMgIzAjQCNQI2AjcCOAI5AjoCOwI8Aj0CPgI%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%2BZGQCCQ88KwALAQAPFgweC18hSXRlbUNvdW50AgoeCERhdGFLZXlzFgAfA2ceCVBhZ2VDb3VudAIfHhVfIURhdGFTb3VyY2VJdGVtQ291bnQCrwIeEEN1cnJlbnRQYWdlSW5kZXgCAmQWAmYPZBYUAgIPZBYGZg8PFgIfAgU8QVZBTkNFIElOVEVSTkFDSU9OQUwgWSBBU09DSUFET1MsIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgZGQCAQ8PFgIfAgULJCA2MSw0ODAuMDBkZAICD2QWAmYPFQIEMjAxMgUyNTY5M2QCAw9kFgZmDw8WAh8CBTxBVklPTkVTIFkgSEVMSUNPUFRFUk9TIERFTCBOT1JURSwgUy5BLiBERSBDLlYuICAgICAgICAgICAgICBkZAIBDw8WAh8CBQ4kIDgsNjY0LDc5Ny40OGRkAgIPZBYCZg8VAgQyMDEyBDY4NjRkAgQPZBYGZg8PFgIfAgU8QiBDIEVTUEVDVEFDVUxBUiwgUy5BLiBERSBDLlYuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUMJCAzNzUsODQwLjAwZGQCAg9kFgJmDxUCBDIwMTIHODgxMDkwNWQCBQ9kFgZmDw8WAh8CBTxCQVJBSkFTIEdBUkNJQSBDQU1JTE8gSkFWSUVSICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQskIDI5LDQ5OC44MGRkAgIPZBYCZg8VAgQyMDEyBDcyODhkAgYPZBYGZg8PFgIfAgU8QkFTRU1FTlQgQ09OU1RSVUNDSU9ORVMsIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgUMJCAxNDMsNTYxLjYwZGQCAg9kFgJmDxUCBDIwMTIFMjQyMDRkAgcPZBYGZg8PFgIfAgU8QkVTVCBJTVBBQ1QsIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGQCAQ8PFgIfAgULJCA0Myw1MjMuMjBkZAICD2QWAmYPFQIEMjAxMgUyNTAwN2QCCA9kFgZmDw8WAh8CBTxCTFVFIERJR0lUQUwsIFMuIERFIFIuTC4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQ4kIDEsOTg0LDAxNC43MWRkAgIPZBYCZg8VAgQyMDEyBTI1NDcwZAIJD2QWBmYPDxYCHwIFPEJPUlNBIENPTUVSQ0lBTElaQURPUkEgIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgIGRkAgEPDxYCHwIFDiQgMSw5NTcsMzA4LjUwZGQCAg9kFgJmDxUCBDIwMTIEMTY5OWQCCg9kFgZmDw8WAh8CBTxCVUZFVEUgVVJCQU5JU1RJQ08sIFMuQS4gREUgQy5WLiAgICAgICAgICAgICAgICAgICAgICAgICAgICBkZAIBDw8WAh8CBQ4kIDEsNzMzLDI5NS41M2RkAgIPZBYCZg8VAgQyMDEyBTIxNDU5ZAILD2QWBmYPDxYCHwIFPEJVUk8gQkxBTkNPLCBTLkEuIERFIEMuViAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRkAgEPDxYCHwIFDiQgMiwwMTgsNDAwLjAwZGQCAg9kFgJmDxUCBDIwMTIHODgxMDQ2OGRk9diRj21D0pMc1qSUTe6JSqJrjxE%3D&__EVENTVALIDATION=%2FwEWYwKEg7hbAuK4yIUNAvil7oIGAsz6jK8FAtyVpsEJAsOVpsEJAsKVpsEJAsGVpsEJAsCVpsEJAseVpsEJAsaVpsEJAsWVpsEJAtSVpsEJAtuVpsEJAsOV5sIJAsOV6sIJAsOV7sIJAsOV0sIJAsOV1sIJAsOV2sIJAsOV3sIJAsOVwsIJAsOVhsEJAsOVisEJAsKV5sIJAsKV6sIJAsKV7sIJAsKV0sIJAsKV1sIJAsKV2sIJAsKV3sIJAsKVwsIJAsKVhsEJAsKVisEJAsGV5sIJAtyVpsEJAsOVpsEJAsKVpsEJAsGVpsEJAsCVpsEJAseVpsEJAsaVpsEJAsWVpsEJAtSVpsEJAtuVpsEJAsOV5sIJAsOV6sIJAsOV7sIJAsOV0sIJAsOV1sIJAsOV2sIJAsOV3sIJAsOVwsIJAsOVhsEJAsOVisEJAsKV5sIJAsKV6sIJAsKV7sIJAsKV0sIJAsKV1sIJAsKV2sIJAsKV3sIJAsKVwsIJAsKVhsEJAsKVisEJAsGV5sIJAtyVpsEJAsOVpsEJAsKVpsEJAsGVpsEJAsCVpsEJAseVpsEJAsaVpsEJAsWVpsEJAtSVpsEJAtuVpsEJAsOV5sIJAsOV6sIJAsOV7sIJAsOV0sIJAsOV1sIJAsOV2sIJAsOV3sIJAsOVwsIJAsOVhsEJAsOVisEJAsKV5sIJAsKV6sIJAsKV7sIJAsKV0sIJAsKV1sIJAsKV2sIJAsKV3sIJAsKVwsIJAsKVhsEJAsKVisEJAsGV5sIJAqXC8YwKApeS%2BdUL5OU6YZnhltHdhOcWvr0PIuscgEk%3D&ddl"
		
		data += "Pagina=" + str(currPage)

		#data = urllib.urlencode(data) 
		#print data 

		url = primaryUrl + aspxPage1
		req = urllib2.Request(url, data, headers) 
		response = urllib2.urlopen(req)
		the_page = response.read()

		soup = BeautifulSoup(the_page)

		#soup=soup.find_all('tr')

		soup = soup.find_all('a', { "class" : "DataGrid_Link" })

		for a in soup:
			links.append(a['href'])

def dataPage2():

	providersIds = []

	for link in links:
		str = link.split('&')[1]
		providersIds.append(str.split('=')[1])

	for providerId in providersIds:
		for currMonth in range(12):
			currUrl = primaryUrl + aspxPage2 + "&ProveedorId=" + providerId + "&MesId="
			currUrl += unicode(currMonth + 1)
			links1.append(currUrl)
			print currUrl

	for link in links1:
		req = urllib2.Request(link)
		response = urllib2.urlopen(req)
		page = response.read()
		soup = BeautifulSoup(page)
		soup = soup.find_all('a', { "class" : "DataGrid_Link" })
		for a in soup:
			links2.append(primaryUrl + a['href'])
			print a['href']
		#break;#
		#	print a['href']

def buildJSONObj(labelsText, detallesText):
	obj = "{"
	global count
	obj += "'aid': " + str(count) + ', '
	count += 1
	print 'labelsTextLen: ' + str(len(labelsText)) + ' detallesText: ' + str(len(detallesText))
	if len(labelsText) == len(detallesText):
		for index in range(len(labelsText)):
			obj += "'" + labelsText[index] + "'" + ":" + "'" + detallesText[index] + "'" 
			if index != len(labelsText) - 1:
				obj += ",\n"
	obj += "}," 
	return obj
	#print obj ##

def retrieveData():
	for link in links2:
		#print link ##
		labelsText = []
		detallesText = []
		req = urllib2.Request(link)
		response = urllib2.urlopen(req)
		page = response.read()
		soup = BeautifulSoup(page)
		#soup = soup.find_all('span', { "class" : "Error" }) DetalleEmpleado

		if len(soup.find_all('span', { "class" : "Error" })) == 0:
			#soup = soup.find_all('table', { "class" : "DetalleEmpleado"})
			#print str(soup[0])
			labels = soup.find_all('td', { "class" : "DetalleEmpleadoFondoGris" })
			campoMoneda = soup.find_all('td', { "class" : "DetalleProveedorMoneda" })
			detalles = soup.find_all('td', { "class" : "DetalleEmpleadoFondoBco" })
			#soup.find_all('td', { "class" : "DetalleEmpleadoFondoGris" }).string.encode("utf-8"))
			#detalles.append

			for label in labels:
				labelsText.append(label.string.encode("utf-8"))

			if len(labelsText) == 13:
				labelsText.pop()

			for detalle in detalles:
				detallesText.append(detalle.string.encode("utf-8"))

			for adicional in campoMoneda:
				detallesText.insert(8, adicional.string.encode("utf-8"))

			global jsonData 
			jsonData += buildJSONObj(labelsText, detallesText)

def saveData():
	global jsonData 
	jsonData += "}"
	fo = open('data1.json', 'w')
	fo.write(jsonData)
	fo.close()

dataPage1()

dataPage2()

retrieveData()

saveData()

#for link in links:
#	print link

