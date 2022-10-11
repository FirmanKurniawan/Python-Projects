import requests

print("Input URL started with http:// or https://")
input_str = input()
sample_url = "https://da.gd/s?url={}".format(input_str)
response_api = requests.get(sample_url).text
if response_api:
    print(
        "\n=======================\nGenerated: {}\nInput URL: {}".format(
            response_api,
            input_str))
else:
    print("Something is wrong. please try again later.")
