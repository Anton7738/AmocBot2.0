import requests
import json
import datetime
# Testing for later
# import doctest
# import unittest

# channel aliases to better differentiate btw channel IDs?
# dictionary key:value pairs for efficiency?

def retrieve_messages(channelid):
    """
    Authorization code will need to be changed before local usage
    Step 1: Navigate to Discord's web client
    Step 2: Locate channel and open dev tools (ctrl + shift + i)
    Step 3: In dev tools, find "Network" tab
    Step 4: Refresh page
    Step 5: Type into the text box of channel
    Step 6: Under "Name" tab on lower left, scroll down and click on "typing"
    Step 7: Find "Headers" tab on right side of dev tools pane
    Step 8: Scroll down to "Request Headers" > "authorization"
    Step 9: Copy and paste code into parameter below
    """ 
    # ------------------------------------------------------------------------------------
    # WARNING: Once code is pushed to GitHub, Discord will sign out user and request login
    #          Password will need to be reset prior to login
    #          This is to prevent unauthorized access for outside users
    # ------------------------------------------------------------------------------------
    #          Workaround: comment out authorization parameter prior to pushing
    #                      use auth code ONLY for testing session
    #                      same auth code can be reused as long as password wasn't reset
    # ------------------------------------------------------------------------------------

    headers = {
                        # insert authorization code here
        'authorization': 'NzAzMTY4MTY2NzE2NTA2MjQy.GFpGiq.0oSo4HWj6x9oGC2Nf9KNyq0teAmoLRgZJ1V8jI'
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)

    # json object holds 26 elements
    jsonn = json.loads(r.text)
    # print(jsonn)
    
    amocMessagesBuffer = []
    
    for value in jsonn:
        if (value['author']['username']) == 'amoc':
            amocMessagesBuffer.append(value['content'])

    print(amocMessagesBuffer)

    # open AmocMessages.txt
    # load last 26 list elements into temporary buffer
    # if new messages from 

    
    # open AmocMessages.txt for appending and reading, creating file if it doesn't exist
    fdAmoc = open("AmocMessages.txt", "a+")
    fdLog = open("LogMessages.txt", "a+")

    lastExtraction = []

    # fd.seek(0)
    # lastLine = fd.readlines()
    # lastExtraction = lastLine[len(lastLine) - 1]

    # repeatScrape.py should call fdLog.write("\n") to add newline btw entries
    fdLog.write("=============== EXTRACTION ===============")
    fdLog.write("\n\tChannel ID: " + channelid)
    fdLog.write("\n\tDate/Time: " + str(datetime.datetime.now()))

    messageCounter = 0

    for x in amocMessagesBuffer:
        if not x in lastExtraction:
            if (x == ''):
                fdAmoc.write("\n" + "## dynamic file type ##")
            else:
                fdAmoc.write("\n" + x)       
            messageCounter += 1

    
    fdLog.write("\n\tTotal Messages: " + str(messageCounter))
    fdLog.write("\n\tOld Messages: ")
    fdLog.write("\n\tNew Messages: ")

    fdLog.write("\n==========================================\n")
    fdAmoc.close()
    fdLog.close()
    
    # Go through line by line in messagesBuffer
    # for x in amocMessagesBuffer:
    #     # Check if the current buffer message is not in AmocMessages.txt
    #     if not amocMessagesBuffer[x] in fd.read():
    #         # If not in AmocMessages.txt, append to the .txt file
    #         fd.write(amocMessagesBuffer[x] + "\n")

    # logMessages.txt

    # Extraction Process started at: <Timestamp>

    # Extraction at <Timestamp>
    #         Channel: <channel>
    #         Total Messages: <#>      <--- (should be 26)
    #         Old Messages: <#>
    #         New Messages: <#>
    #         Total processing time: <Timestamp>

    # Extraction at <Timestamp>
    #         Channel: <channel>
    #         Total Messages: <#>      
    #         Old Messages: <#>
    #         New Messages: <#>
    #         Total processing time: <Timestamp>

    # ...


def main():
    retrieve_messages('1051059403287175198') 

if __name__ == "__main__":
    main()