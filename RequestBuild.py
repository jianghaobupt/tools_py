#coding=UTF-8
import urllib2
		
def initRequest(url):
    request = urllib2.Request(url)
    return request

def setRequestHeader(request, header):
	keys = {'Cookie'}
	for key in keys:
		value = header.get(key)
		request.add_header(key, value)
	return request

def setRequestBody(request, data):
    request.add_data(data)
    return request

url="http://localhost:8080/logistics-backstage/third_billing/complaint_template/type_map"
req=initRequest(url)
header = dict(Cookie="__utma=119466140.630621376.1489546694.1489546694.1489546694.1; __utmz=119466140.1489546694.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); __utmv=119466140.No%20Silverlight; _env=gray; _uk=126402921; _cs=a85e8de49d7492aaa3723adc217d17bd; _cm=13588100640")
req=setRequestHeader(req, header)
resp=urllib2.urlopen(req)

print resp.info()
print resp.read()




