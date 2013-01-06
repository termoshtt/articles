articles
==========

BibTeXに基づく文献管理アプリケーション

# 特徴
BibTeXに基づいたWebApp(HTML+JavaScript)とCGIサーバーからなる
の文献管理アプリケーションです。
BibTeXファイルをパースして文献のリストをHTMLとして出力します。
さらに文献の検索、タグ付けの機能をJavaScriptで実装してあります
(タグの情報はサーバーに記録されます)。
WebApp単独で使用することもできますが、
CGIサーバーを併用すると文献にタグ付けを行なうことができます。
このアプリケーションを用いればBibTeXで管理してある論文の情報を
お気に入りのブラウザで閲覧する事ができます。
また.htmlファイルが静的に生成されるので、
iPad等のタブレットPCでも用いる事ができます。

尚、現在のバージョンではLinuxにのみ対応しています。
(Macでは動くかもしれませんが確認していません)

# インストール
## 依存するライブラリ
このアプリケーションの基幹部分はpython2で書かれています。
さらに次のサードパーティのライブラリに依存しています。
* pybtex : BibTeXのパース
* jinja2 : HTMLの生成

主要なLinuxディストリビューションにおいては
jinja2はパッケージ管理アプリケーション(yum,apt等)によって
導入できるでしょう。
しかしpybtexはあまりメジャーではないので、
見つからない事があるでしょう。
幸運にもpybtexではeasy-installが使用できるため、
次のようにしてインストールできます。
```shell
# easy-install pybtex
```

## インストール手順 (Linux)
インストール作業を始める前にjinja2,pybtexをインストールしておいて下さい。
まずソースコードを取得します。
```shell
    git clone http://github.com/termoshtt/ariticles.git
```
あるいは.zipをダウンロードし展開してください。
次にダウンロードしたディレクトリに移動し、
設定ファイルを$HOMEにコピーします。
```shell
    cd articles
    cp sample.ini $HOME/.articles.ini
```
ここで必要に応じて設定を変更します。
* [path.bib]        : .bibファイルへのパス
* [path.outputdir]  : インストール先のパス .html, js/, css/, icons/がインストールされる
* [name.template]   : HTMLを生成するテンプレートの名前
* [name.html]       : 生成されるHTMLの名前
* [name.database]   : タグの情報を保管するデータベースの名前
* [server.port]     : CGIサーバーのポート番号
設定を変更したら.htmlを生成し、必要な物をコピーします。
```shell
    ./start.py --install
```
もし設定ファイルを$HOME/.articles.iniにおきたくない場合は
--configオプション(あるいは-c)で指定します。
```shell
    ./start.py --install --config=/path/to/your/ini
```
または(-iは--installの省略系)
```shell
    ./start.py -i -c /path/to/your/ini
```
以上で[path.outputdir]にarticles.html他必要なものがコピーされる。
これでお気に入りのブラウザで
```
    file:///home/yourname/path/to/articles.html
```
を開けば論文のリストが閲覧できる。

次回以降に.htmlを更新するには
```shell
    ./start.py -n
```
とする。

## タグ付け
タグ付けの機能を使用するにはCGIサーバーを立てる必要がある。
ただし単独のPCで使う場合はapache等の本格的なCGIサーバーを立てる必要はない。
pythonにはCGIのテスト用のため簡易CGIサーバーを容易に構築できるライブラリが付属している。
このアプリケーションではこの機能を使用してCGIサーバーを構築する。
ファイアウォールの内側で行なうため、
ファイアウォールの設定をしない限り外部からこのサーバーはアクセスできない。

サーバーを立てるにはやはりstart.pyを使用する。
```shell
    ./start.py
```
これにより.htmlを更新した上でCGIサーバーを立てる。
このプロセスは中断しない限りCGIのリクエストを待ちつづけるので、
終了する場合はCtrl-C等で終了する。

CGIサーバーを起動しておけばタグ付け機能を使用する事ができる。
articles.htmlの各文献の情報の下に"Tags of article"の文字があるが、
これをクリックする事によりタグの操作UIが出現する。
Tag Nameを入力し、createボタンを押すことにより文献にタグを付ける事ができる。
付加されたタグはタイトル下のナビ部分に表示され、
タグ名をクリックする事でタグ付けされた文献を搾り込むことができる。

