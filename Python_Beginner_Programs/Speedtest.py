import speedtest

wifi = speedtest.Speedtest()

print('Now wifi upload speed is ',wifi.upload())
print('Now wifi downlaod speed is ',wifi.download())