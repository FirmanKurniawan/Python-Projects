import speedtest
st = speedtest.Speedtest()

#menu
print("----- Internet speed test -----")
option = int(input('''- What speed would you like to test?
 - 1.Download speed
 - 2.Upload speed
- Your choice --> '''))

#download speed test
if option == 1:
    print("-",st.download()/1000000,"Mbps.")

#upload speed test
elif option == 2:
    print("-", st.upload()/1000000,"Mbps.")

else:
    print("- Invalid choice!")
