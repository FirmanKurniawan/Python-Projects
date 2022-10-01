import requests

print("Input URL:")
input_str = input()
sample_url = "https://da.gd/dns/{}".format(input_str)
response_api = requests.get(sample_url).text
if response_api:
    print(
        "\n=======================\nDNS records of {} are \n{}".format(
            input_str,
            response_api))
else:
    print("Can't seem to find {} on the internet".format(input_str))
