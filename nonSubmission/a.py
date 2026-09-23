"""realThaiPlus"""
gWalletBalace = int(input())
monthly = 1000
daily = 200
success = 0
anutinHelp = 0
goBuy = int(input())
for i in range(goBuy):
    i += 0
    daily = 200
    n = int(input())
    for j in range(n):
        j += 0
        bill = int(input())
        peoplePay = (0.4 *  bill) // 1
        anutinPay = bill - peoplePay
        if anutinPay > daily:
            anutinPay = daily
            peoplePay = bill - anutinPay
        if anutinPay > monthly:
            anutinPay = monthly
            peoplePay = bill - anutinPay

        if gWalletBalace >= peoplePay:
            gWalletBalace -= peoplePay
            daily -= anutinPay
            monthly -= anutinPay
            success += 1
            anutinHelp += anutinPay

print(int(success))
print(int(gWalletBalace))
print(int(anutinHelp))
