import os
import re
import time


def gameStart(token, numberndex, numberCounter, ):
    url = "curl 'https://ipm-tw.pragmaticplay.net/gs2c/v3/gameService' -H 'Referer: " \
          "https://ipm-tw.pragmaticplay.net/gs2c/html5Game.do?jackpotid=0&gname=888%20Dragons&extGame=1&ext=0&cb_target" \
          "=exist_tab&symbol=vs1dragon8&jurisdictionID=99&mgckey=AUTHTOKEN" \
          "@e6be865a65d3f713a33c5d67d3def97b21e403ba5c0565dd1263381acabce051~stylename@biggaming~SESSION@d3b1a3c3-b21e" \
          "-4f0e-8302-b3cd37ea5153&tabName=' -H 'Origin: https://ipm-tw.pragmaticplay.net' -H 'User-Agent: " \
          "Mozilla/5.0 (" \
          "Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 " \
          "Safari/537.36' " \
          "-H 'Content-type: application/x-www-form-urlencoded' --data " \
          "'action=doInit&symbol=vs1dragon8&cver=36308&index=1&counter=1&repeat=0&mgckey=AUTHTOKEN" \
          "@e6be865a65d3f713a33c5d67d3def97b21e403ba5c0565dd1263381acabce051~stylename@biggaming~SESSION@d3b1a3c3-b21e" \
          "-4f0e-8302-b3cd37ea5153' --compressed "

    indexNumber = int(url.split("&index=")[1].split("&counter=")[0]) + 1
    counter = int(url.split("&counter=")[1].split("&repeat=")[0]) + 2

    head = "curl" + url.split("curl")[1].split("--data")[0] + "--data "

    pattern = re.compile(r'\d+')

    while True:
        data = '\'action=doSpin&symbol=vs1dragon8&c=1&l=1&index=' + str(indexNumber) + '&counter=' + str(
            counter) + "&repeat=0" \
               + "&mgckey" + url.split("&mgckey")[-1]
        sendUrl = head + data
        result = os.popen(sendUrl).readlines()

        if result[0].startwith("nomoney="):
            print("没钱了，请充值")
            break

        if result == ['unlogged']:
            print("游戏发生错误")
            print("请输入正确的url")
            break

        print(result)
        if result[0].endswith("SystemError"):
            print("游戏停止，请重新复制url")
            break

        number = pattern.findall(result[0])
        if int(number[0]) == 0:
            print("没中奖")
            indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
            counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
            time.sleep(0.005)
        else:
            print("中奖了")
            indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
            counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2
            data = '\'symbol=vs1dragon8&action=doCollect&index=' + str(indexNumber) + '&counter=' + str(
                counter) + "&repeat=0" \
                   + '&mgckey' + url.split("&mgckey")[-1]
            sendUrl = head + data
            result = os.popen(sendUrl).readlines()
            print(result)
            indexNumber = int(result[0].split("&index=")[1].split("&balance_cash=")[0]) + 1
            counter = int(result[0].split("&counter=")[1].split("&l=")[0]) + 2

# print(head + data)
# print("\n\n")
# print(url)

# result = os.popen(head + data).readlines()
# print(result)
