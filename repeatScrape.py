from discordScrape import retrieve_messages
import time

# fill out with channel IDs
channels = []

def repeatScrape(timeframe):
    while(True): 
        seconds = time.time()
        if(seconds % 3600 == 0):  # substitute 3600 with timeframe representation

            # forloop that extracts messages and adds newline after each individual entry
            # for x in channels:
            #   retrieve_messages('1051059403287175198')
            #   fdLog = open("LogMessages.txt", "a+")
            #   fdLog.write("\n")
            #   fdLog.close()

            retrieve_messages('1051059403287175198')
            # from other channels
            # retrieve_messages('1051059403287175198')
            # retrieve_messages('1051059403287175198')
            # retrieve_messages('1051059403287175198')
            # retrieve_messages('1051059403287175198')
            # retrieve_messages('1051059403287175198')

            # Newline between log message entries
            fdLog = open("LogMessages.txt", "a+")
            fdLog.write("\n")
            fdLog.close()

    # handle keyboard interrupt. Include stopage entry in LogMessages.txt 

# main

# def main():
#     retrieve_messages('1051059403287175198') 

# if __name__ == "__main__":
#     main()