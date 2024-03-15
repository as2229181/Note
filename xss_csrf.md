# 我以為我瞭解CSRF
最近開始了瘋狂面試期，在某個面試官問我時，照著我的認知回答，以為表現得不錯，終場休息時，默默地看到紙上寫著，CSRF 60分.....。因此想著不行少得理解到80分才行...打算從新認識這個CSRF ATTACK!

## 甚麼是CSRF ATTACK
 CSRF( Cross Site Request Forgery)，跨站請求偽造，
 > 跨網站偽造要求攻擊是一種混淆代理*網路攻擊，它會誘使使用者意外使用其認證來叫用狀態變更活動，例如從他們的帳戶轉移資金、變更他們的電子郵件地址和密碼或其他一些不受歡迎的動作。( *-節自 cloudflare*)

看起來是不是很危險，但又有點看不懂，下面舉的例子希望能幫助大家理解:

> 某天你登入了www.moneybank.com網站，在你的瀏覽器留下了**sessionID**，保存你的登入狀態，但最近沙丘剛上串流了，你又沒有訂閱netflix，所以你就想說"嗯!我來找看看有沒有盜版線上看的片源"，於是開始在google 搜尋 "DUNE ONLINE FREE"，果真被你找到了些片源，你便迫不及待地點開網址，跳出了些廣告，你隨手按了個叉叉，過沒幾分鐘，Email 傳來，"Dear xxxx , 1btc has been transfer from your account!"，你才驚覺大事不妙....

這其中就發生了csrf Attack

而事情是這樣發生的:
在進入到盜版片的網站時，裡面其實可能埋有一個隱藏的form表單
類似於這樣
```html
<form action="http://moneybank.com/pay" method="POST">
  <input type="hidden" name="amount" value="1000" />
  <input type="hidden" name="to_account" value="攻擊者帳號" />
  <input type="submit" value="立即贏得一百萬美金！" />
</form>
```
觸發這個form 表單的機制可能不單單只有點擊submit這個方法，攻擊者也有可能寫一些javascripts來觸發這個表單，例如:一載入這個網頁就送，或是滑鼠滑到某個圖片上就送，總之很難題防這個表單被送出，有些甚至把轉帳的url 寫在 image 上
```html
<img src="http://moneybank.com/pay/pay?form=a&to=b" />
```
request 就在你不經意的瞬間發出去了

剛好你在瀏覽器上還存放著moneybank的sessionID並且還未過期，瀏覽器就自動地在這個的reqeust帶上這個
sessionID，www.moneybank.com 就覺得"嗯! 他有session ID 且沒有過期應該是合法的用戶"，就准許了這個request的操作，就很樣偽造你的身分去執行某些壞壞的事情，但這期間，**攻擊方並未竊取到任何使用者的資料**，因為並未從server獲得任何的response。

既然CSRF Attack 看起來是這麼容易發生的，那該怎麼預防呢?

方法有下面幾個:

1. Referer: 因為request還是在攻擊者的server所發出的，確認這個referer 是不是可以信任的，如果不行就不接受這個request，但前提是這些攻擊者不會偽造referer，所以這個也算是初步的防範!

    關於referer : https://www.maxlist.xyz/2020/08/03/chrome-85-referer-policy/

2. CSRF的






