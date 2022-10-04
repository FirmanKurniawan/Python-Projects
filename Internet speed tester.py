import speedtest
st = speedtest.Speedtest()

def download():
    print("-",st.download()/1000000,"Mbps.")

def upload():
    print("-", st.upload()/1000000,"Mbps.")

print("----- Internet speed test -----")
#menu
while True:
    option = int(input('''- What speed would you like to test?
     - 1.Download speed
     - 2.Upload speed
    - Your choice --> '''))

    #download speed test
    if option == 1:
        download()
        nextOption = input("- Would you like to check the upload speed? (Y/N): ").lower()
        if nextOption == 'y':
            upload()
        print("Thank you!")
        break

    #upload speed test
    elif option == 2:
        upload()
        nextOption = input("- Would you like to check the download speed? (Y/N): ").lower()
        if nextOption == 'y':
            download()
        print("Thank you!")
        break

    else:
        print("- Invalid choice! Please try again..")
