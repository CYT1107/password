#設定密碼
password = 'a123456'
#輸入密碼
i = 3
while True:
    #if 密碼正確
    pwd = input ('請輸入密碼：')
    if pwd == password:
        print ('密碼正確！')
        break
    #else 密碼錯誤
    else :
        i = i - 1
        print ('密碼錯誤，還有', i, '次機會')
        if i == 0:
            break