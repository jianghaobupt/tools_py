#coding=utf-8
import xlrd

def getOrgToken(org_id, orgs):
	for rn in range(1, orgs.nrows):
		org = orgs.row_values(rn)
		if org:
			if org_id == org[0]:
				return org[1]

shop_data = xlrd.open_workbook('excelFile.xls')
# org_data = xlrd.open_workbook('org_token.xls')
orgs = shop_data.sheets()[1]
shops = shop_data.sheets()[0]
isp = "1"
status = "1"
s_type = "1"
sqlf = open('sql.txt', 'a')

for rownum in range(1, shops.nrows):
	shop = shops.row_values(rownum)
	if shop:
		outer_shop_id = shop[2]
		appkey = shop[0]
		org_id = shop[4]
		org_token = getOrgToken(org_id, orgs)
		attributes = '''{"tokens":{"1":{"appkey":"''' + appkey + '''"},''' + org_token + '''}}'''

		sqlstr = "INSERT INTO outway.outway_outershop_repository (outer_shop_id, app_key, isp, status, type, belong_to_shop_group_id, attributes) VALUES " + "('" + outer_shop_id + "', '" + appkey + "', '" + isp + "', '" + status + "', '" + s_type + "', '" + org_id + "', '" + attributes + "');\n\n"
		sqlf.write(sqlstr)

sqlf.close()
