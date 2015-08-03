import requests,sys, json


baseURL = "http://www.loc.gov/aba/publications/FreeLCC/{CODE}-outline.pdf"

codes = ["A","B-BJ","BL-BQ","BR-BX","C","D-DR","DS-DX","E-F","G","H","J","K","KB","KD","KDZ-KH","KE","KF","KJ-KKZ","KJV-KJW","KK-KKC","KL-KWX","KZ","L","M","N","P-PA","PB-PH","PJ-PK","PL-PM","PN","PQ","PR-PS-PZ","PT","Q","R","S","T","U-V","Z"]
for x in codes:

	url = baseURL.replace("{CODE}",x)


	r = requests.get(url, stream=True)
	with open('source/'+x+'-outline.pdf', 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				f.flush()

	print x+'-outline.pdf'