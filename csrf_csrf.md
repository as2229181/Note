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

在**OWASP**的文件中有以下幾點是不能夠防範CSRF Attack的(OWASP, 開放網路軟體安全計畫, 每年會排名出當年度最常見的網路應用程式所面臨的風險):

1. **Using a secret cookie** : 這很好理解，因為不管cookies有沒有被加密，該domain的cookies在每次的request還是會被瀏覽器帶上，所以有沒有加密沒有差。

2. **Only accepting POST requests** : 這點主要是因為，attacker 可以用hidden的form搭配javascsripts，讓使用者被動的送出具有攻擊性的post request，所以這樣也沒辦法防範。

3. **Multi-Step Transactions** : 沒有辦法有效的阻擋，因為如果attacker 可以猜測出交易開始後每一步的商業操作，那他都有辦法去達成這些動作。

4. **URL Rewriting** : 確實可能可以防止attacker的攻擊，因為他可能必須猜到sessionId才能完成這個攻擊，但這樣等於是把sessionid暴露在URL，這就產生了另一個風險了，因此也不建議

5. **HTTPS** : 對於防止CSRF攻擊沒有任何的幫助，ssl/tls只是幫忙加密request而已。

6. **Validating the Referrer Header** : 驗證特定的 http referer header 也對於CSRF attack沒有幫助，因為attacker 可以竄改 referer，雖然現在瀏覽器的政策改成只要是跨域的request一定要包含referer，但還是沒辦法阻止attacker 竄改referer。



而其推薦的唯一做法為使用csrf token 的方式來防泛，但前提是網站不能有**XXS**的漏洞(因為這樣attacker 就可以透過腳本拿到csrftoken了):

**概念**

- 發給使用者一個Token，這個Token在User 發送請求的時候必須傳給後端，後端就會驗證這個Token，如果Token 驗證成功就可以進行後端的邏輯，沒有驗證成功，request就會被擋下來。


## Synchronizer Token Pattern:

**Token 發放**

- 可以分為根據user session 發放Token或是每個request都要發放一個Token，但是OWASP不建議以cookies的方式傳送   CSRFToken，而csrftoken 會儲存在後端的資料庫用以比對。

- CSRFToken 的規則 :
  - 對於每個user session 的Token 都要是唯一的
  - 需要加密
  - Unpredictable

**Token 驗證**

  一般來說會在form 表單 input hidden來藏token，或是在header set一個token(有same-origin policy相對來說比較安全，只會把cookies傳給你信任的domain)，從前端傳入的 CSRFToken 跟後端資料庫存的CSRFtoken 去比對，如果是對的就驗證通過。一樣如果有xxs得漏洞，attacker就用javascripts拿到cstftoken。



## Double Submit Cookies Pattern:

與前一個方法不一樣的是，這裡是把csrftoken儲存在client的cookies裡面，可以減輕後端的負擔。

  - Signed Double-Submit Cookie (RECOMMENDED):後端透過sessionid以及secret hash產生的csrftoke回傳到前端並set在cookies上，當client 發出reqeust，必須含有csrf token(不管是在form input 或是在request header)，這時候端就會比對這個傳入的csrf token 和set cookies 的csrftoken 是不是一樣的，如果是一樣的，那就驗證通過。



## 總結

在之前對於csrftoken 可能都只有片面的了解，才發現其實csrf attack 跟xxs 很有關係，難怪面試的時候是這兩個一起問的，下一次再來分享Django 如何去抵禦CSRF attack!


















