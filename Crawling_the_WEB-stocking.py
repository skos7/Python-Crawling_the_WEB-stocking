import re
import urllib.request

url = "https://www.google.com/finance?q="
stock = input("Enter your stock:")

url = url + stock
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

m = re.search('class="kf1m0"',data1)
start = m.end()
end = start + 50
newString = data1[start:end]


m = re.search('">', newString)
start = m.end()
newString1 = newString[start:]


m = re.search("<", newString1)
end = m.end() - 1
final = newString1[0:end]
print("The value of " + stock + " is " + final)
