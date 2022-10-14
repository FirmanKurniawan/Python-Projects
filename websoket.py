from websocket_server import WebsocketServer
import threading
import helpers as helpers
import helpersws as helpersws

# Called for every client connecting (after
# handshake)


def new_client(client, server):
    print("New client connected and was given id) %d" % client["id"])
    server.send_message_to_all("Hey all, a new client has joined us")
    d = threading.Thread(name="daemon", target=_send_to_client, args=[client, server])
    d.setDaemon(True)
    d.start()


# Called for a specific client when a server event
# such as a sensitive single is detected
def _send_to_client(client, server):
    message = input() + str("BROOOO")
    print(message)
    server.send_message(client, message)
    d = threading.Thread(name="daemon", target=_send_to_client, args=[client, server])
    d.setDaemon(True)
    d.start()


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client["id"])


# Called when a client sends a message
def message_received(client, server, message):
    # if len(message) > 200:
    #     message = message[:200]+'..'
    # print("Client(%d) said: %s" % (client['id'], message))
    # server.send_message(client,"BALIKAN "+message)
    if len(message) > 200:
        message = message[:200] + ".."

    helperswsny = helpersws.HelpersWS()

    if message == "check_wa":
        print("Check WA")
        data = helperswsny.getAllAccounts()
        server.send_message(client, str(data))
    else:
        split = message.split("|")
        print(split)
        method = split[0]
        device_idny = split[1]

        helpersny = helpers.QueryHelp(device_idny)
        data = helpersny.getAccounts()
        account_id = str(data[0])
        job_type = split[2]
        if method == "APPIUM":
            print("APPIUM USE")

            helpersny.createJob(
                "INSERT INTO jobs_data ('acc_id', 'job_type', 'status_job', 'method') VALUES ("
                + account_id
                + ", "
                + job_type
                + ", 0, 'APPIUM')"
            )
        else:
            print("FULL ADB")
            target_no = split[3]
            message = split[4]

            device_id = data[2]

            try:

                filename = split[5]
                print("SINI")
                check_job = helpersny.createJob(
                    "INSERT INTO jobs_data ('acc_id', 'job_type', 'target', 'filename', 'status_job', 'message', 'method') VALUES ("
                    + account_id
                    + ", "
                    + job_type
                    + ", '"
                    + target_no
                    + "', '"
                    + filename
                    + "', 0, '"
                    + message
                    + "', 'ADB FULL')"
                )
            except:
                print("EXPECT")
                check_job = helpersny.createJob(
                    "INSERT INTO jobs_data ('acc_id', 'job_type', 'target', 'status_job', 'message', 'method') VALUES ("
                    + account_id
                    + ", "
                    + job_type
                    + ", '"
                    + target_no
                    + "', 0, '"
                    + message
                    + "', 'ADB FULL')"
                )
    print("Client(%d) said: %s" % (client["id"], message))


PORT = 9305
server = WebsocketServer(host="0.0.0.0", port=PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
