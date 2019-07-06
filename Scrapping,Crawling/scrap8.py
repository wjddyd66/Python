import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

print()
data = {"b":3.4, "a":0, "c":"hello world", "d":{"sbs":5}}
print(type(data))

json_data = json.dumps(data)
print(type(json_data))

print()
json_data2 = json.loads(json_data)
print(type(json_data2))

json_data = json.dumps(data, sort_keys=True)
print(json_data)

print("*"*50)
import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

print()
data = {"b":3.4, "a":0, "c":"hello world", "d":{"sbs":5}}
print(type(data))

json_data = json.dumps(data)
print(type(json_data))

print()
json_data2 = json.loads(json_data)
print(type(json_data2))

json_data = json.dumps(data, sort_keys=True)
print(json_data)

print("*"*50)
json_data = {}

def readData(fileName):
    f = open(fileName, "r", encoding="utf-8")
    lines = f.read()
    f.close()
    #print(lines)
    jdata = json.loads(lines)
    return jdata
    
def main():
    json_data = readData("ftest3.json")
    #print(json_data)
    #print(type(json_data))
    d1 = json_data["직원"]["이름"]
    d2 = json_data["직원"]["직급"]
    d3 = json_data["직원"]["전화"]
    print("이름: "+d1+", 직급: "+d2+", 전화: "+d3)
    d4 = json_data["웹사이트"]["카페명"]
    d5 = json_data["웹사이트"]["userid"]
    print("카페명: "+d4+", userid: "+d5)
    

if __name__ == "__main__":
    main()

'''
"\"foo\bar"
"\u1234"
"\\"
{"a": 0, "b": 0, "c": 0}

<class 'dict'>
<class 'str'>

<class 'dict'>
{"a": 0, "b": 3.4, "c": "hello world", "d": {"sbs": 5}}
**************************************************
"\"foo\bar"
"\u1234"
"\\"
{"a": 0, "b": 0, "c": 0}

<class 'dict'>
<class 'str'>

<class 'dict'>
{"a": 0, "b": 3.4, "c": "hello world", "d": {"sbs": 5}}
**************************************************
이름: 홍길동, 직급: 과장, 전화: 111-1111
카페명: cafe.daum.net/flowlife, userid: good

'''



