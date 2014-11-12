#PythonでGmailAPIを使ってみよう


GmailApiを使ってみたので備忘録  
ここではサンプルコードを実行するまでの手順を記載
最終的にsample.pyを実行するとメールボックスにあるメールのリストみたいなものが表示出来ます


##必要なもの

* Python2.7
* google-api-python-client：Python用のGoogleAPIライブラリ
* Google アカウント


##環境作り

ここに有るとおりにすすめていけばOKです。  
https://developers.google.com/gmail/api/quickstart/quickstart-python
というのは乱暴なので次の順番でメモしておきます

1. GoogleAPIを有効にする  
2. google-api-python-clientをインストールする  
3. サンプルコードを落とす  
4. sample.pyを実行してみる  

###GoogleAPIを有効にする

1. googleアカウントを適当に作ってログイン  
2. 次に↓にアクセスして「プロジェクトを作成」を押して適当な名前のプロジェクトを作る  
  https://console.developers.google.com/project  
3. 左のメニューにある「APIと認証」のAPIをクリック、GmailApiを有効にする  
4. 続いて「APIと認証」の認証情報をクリックして、「新しいクライアントを作成」をクリック    
5. 今回はPythonアプリからアクセスするのでInstalledApplicationを選択  
6. そうすると「ネイティブ アプリケーションのクライアント ID」表が右側に出来るので  
　「Jsonをダウンロード]でダウンロードする。  


###google-api-python-clientをインストールする  

* easy installを使う場合  
sudo easy_install --upgrade google-api-python-client  
* pipを使う場合  
sudo pip install --upgrade google-api-python-client

###サンプルコードを落とす

git clone https://github.com/TM-KNYM/How2UseGmailApiByPython.git

↑でクローンするsample.pyとgmailapi.pyが落とされます。  
gmailapi.py・・・google-api-python-clientを使って色々してみてるモジュール  
sample.py ・・・gmailapi.pyを呼び出すサンプルコード  


###sample.pyを実行してみる

ターミナル又はコマンドラインでサンプルコードを落としたディレクトリに移動  
そこで下記のようにコマンドを実行する  
JSONファイルはGoogleAPIを有効にするでダウンロードしたものです

python sample.py [JSONファイル]

詳しい処理内容はGmailApi.pyとsample.pyを見てね。
GmailAPIのAPIの詳細はgoogle Developerのapis-explorerを見ると分かりやすいです  
http://developers.google.com/apis-explorer/#p/gmail/v1/  

##その他メモ

OAuth2.0について  
https://developers.google.com/api-client-library/python/guide/aaa_oauth?hl=ja#oauth

gmailのAPIのscopeについて  
https://developers.google.com/gmail/api/auth/scopes?hl=ja

