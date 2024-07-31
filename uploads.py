import requests, sys, os




nameimg = 'P4dbiE9csi4hgIveWkGOisssshjhhjhjss.jpg'
filename = '2.jpg'
imagesize = os.path.getsize(filename)







head = {
	'content-type': 'application/json; charset=UTF-8',
	'authorization': f'jwt',
	'x-goog-upload-protocol': 'resumable',
	'accept': '*/*',
	'x-goog-upload-command': 'start',
	'x-goog-upload-content-length': f'{imagesize}',
	'accept-language': 'vi-VN,vi;q=0.9',
	'x-firebase-storage-version': 'ios/10.13.0',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)',
	'x-goog-upload-content-type': 'image/webp',
	'x-firebase-gmpid': '1:641029076083:ios:cc8eb46290d69b234fa606'
}

data = '{"name":"users\\/e9yEHBoGlYgF1hfsbha8cX8iliw1\\/moments\\/thumbnails\\/'+nameimg+'","contentType":"image\\/*","bucket":"","metadata":{"creator":"e9yEHBoGlYgF1hfsbha8cX8iliw1","visibility":"private"}}'

url = 'https://firebasestorage.googleapis.com:443/v0/b/locket-img/o/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?uploadType=resumable&name=users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+''
res = requests.post(url, headers=head, data=data)

head = {
	
	'content-type': 'application/octet-stream',
	'x-goog-upload-protocol': 'resumable',
	'x-goog-upload-offset': '0',
	'x-goog-upload-command': 'upload, finalize',
	'upload-incomplete': '?0',
	'upload-draft-interop-version': '3',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)'
}
data = open('2.jpg','rb').read()
res = requests.put(res.headers['X-Goog-Upload-URL'], headers=head, data=data)


head = {
	'content-type': 'application/json; charset=UTF-8',
	'authorization': f'jwt',
	'accept': '*/*',
	'accept-language': 'vi-VN,vi;q=0.9',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)',
	'x-firebase-gmpid': '1:641029076083:ios:cc8eb46290d69b234fa606'
}

ress = requests.get('https://firebasestorage.googleapis.com:443/v0/b/locket-img/o/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'', headers=head)
downLoad_Token = ress.json()['downloadTokens']

headers = {
	'content-type': 'application/json',
	'accept': '*/*',
	'authorization': f'jwt',
	'accept-language': 'vi-VN,vi;q=0.9',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3'
}

data = '{"data":{"analytics":{"platform":"ios","google_analytics":{"app_instance_id":"7A58F101E5B043519DC9783D63D0A07F"},"amplitude":{"device_id":"5E1F6CFD-1FC9-4DED-82B1-03743DD1FE09","session_id":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"1722307848648"}}},"thumbnail_url":"https:\\/\\/firebasestorage.googleapis.com:443\\/v0\\/b\\/locket-img\\/o\\/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?alt=media&token='+downLoad_Token+'","sent_to_all":false,"migration":{"database":"locket"},"recipients":["r77mY315k8OSFUHhe8jmV7Vq8rG2"],"md5":"b9e295674e4a3bb56d8e09ee78cc7748"}}';

res = requests.post("https://api.locketcamera.com/postMoment", headers=headers, data=data)
print(res.text)