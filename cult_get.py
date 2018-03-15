import http.client
import time
import json

counter = 0


bookCoon = http.client.HTTPSConnection("api.curefit.co")

headersBook = {
    'apikey': "9d153009-e961-4718-a343-2a36b0a1d1fd",
    'appversion': "7",
    'at': "04c787b6-9548-492d-9bae-3f20660b76fb",
    'content-type': "application/json",
    'deviceid': "fc063ca9-1910-af17-0eee-35392146847e",
    'origin': "https://www.cure.fit",
    'osname': "browser",
    'referer': "https://www.cure.fit/cult/classbooking/15?pageFrom=cultCLP&centerId=15&pageType=classbooking",
    'st': "b3e3840a-469a-4966-ace5-c147f9378ba8",
    'cache-control': "no-cache",
    'postman-token': "5fa1301d-4434-14bf-d964-934bf86b6c8d"
    }

while 1:
    time.sleep(5)
    counter += 5

    print ('Script has been looping for', counter, 'seconds...' ,'current time is',time.asctime( time.localtime(time.time())))

    conn = http.client.HTTPSConnection("api.curefit.co")

    headers = {
    'apikey': "9d153009-e961-4718-a343-2a36b0a1d1fd",
    'origin': "https://www.cure.fit",
    'at': "04c787b6-9548-492d-9bae-3f20660b76fb",
    'deviceid': "4faaad6f-950b-ef17-3406-682e89b80918",
    'appversion': "7",
    'content-type': "application/json",
    'if-none-match': "W/\"a315-8G81Mgp4jSeZyEeQoSmmRFQYJB0\"",
    'osname': "browser",
    'referer': "https://www.cure.fit/cult/classbooking/15?pageFrom=cultCLP&centerId=15&pageType=classbooking",
    'st': "b3e3840a-469a-4966-ace5-c147f9378ba8",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'cache-control': "no-cache",
    'postman-token': "e38d8b54-1594-9496-d921-f03d5ba912f3"
    }

    conn.request("GET", "/cult/classes?center=15", headers=headers)

    res = conn.getresponse()
    data = res.read()
    dataJson = data.decode("utf-8")
    dataJsonToJson = json.loads(dataJson)
    print(dataJsonToJson["classByDateList"][0]["classByTimeList"][1]["classes"][1])
    availableSeats = dataJsonToJson["classByDateList"][0]["classByTimeList"][1]["classes"][1]["availableSeats"]
    availableSeats = int(availableSeats)
    if(availableSeats>0):
        print ("got avaiable seates for morning football",availableSeats)
        print ("trying to book class")
        bookCoon.request("POST", "/cult/class/124273/book", headers=headersBook)
        res = bookCoon.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        
    