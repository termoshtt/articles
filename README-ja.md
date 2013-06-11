# articles

BibTeXベースの文献管理アプリケーション

## 特徴
+ WebApp(HTML+JavaScript)とCGIサーバーで構成
+ 文献の検索、タグ付けによる分類機能
+ エディタ(vim,emacs)へのBibTeXキーの補完機能
+ 静的なHTMLを生成するため、iPadで使用可能
+ PDFからBibTeX情報の自動取得

BibTeXに基づいた、
WebApp(HTML+JavaScript)とCGIサーバーからなる文献管理アプリケーションです。
BibTeXファイルをパースして文献のリストをHTMLとして出力します。
さらに文献の検索機能、タグ付けによる分類機能をJavaScriptで実装してあります。
WebApp単独で使用することもできますが、
CGIサーバーを併用すると文献にタグ付けを行なうことができます。
一度付加したタグはHTMLにも記録されますので、
タグによる検索機能はWebApp単独でも使用可能です。
このアプリケーションを用いればBibTeXで管理してある論文の情報を
お気に入りのブラウザで閲覧する事ができます。
またHTMLファイルが静的に生成されるので、
iPad等のタブレットPCでも用いる事ができます。
さらにBibTeXキーをエディタ(vim,emacs)から補完するためのソースを用意してあります。
BibTeXキーを現在管理していない場合でも、
PDFから自動的にdoiを取得し、そこからBibTeXの情報を取得できます。

つまり、サーバーの無い場合に使用できるのは、
+ 静的なHTMLファイルの生成
+ 文献の検索(タイトル、著者、雑誌名、日付)
+ .bibファイルの自動生成
+ エディタでのBibTeX-keyの補完機能
さらにサーバーがあれば、
+ 文献へのタグ付け
+ WebApp経由でのHTMLの更新
+ WebApp経由でのBibTeX情報の登録
が可能となります。

現在のバージョンはFedora18, Mac OS X(10.8)で開発されています。

## インストール

### 要件(BibTeX key)
このアプリケーションを使用するには
論文のPDFファイルのファイル名が[bibtexkey].pdfになっている必要があります。
これはHTMLからPDFへのリンクを埋めこむためのもので、
ファイル名が異なる場合はリンクが機能しません。
尚、後述するように、
PDFからBibTeXの情報を取得する際、PDFのファイル名をBibTeXキー.pdf
に変換されるため、
現在違うファイル名で管理している場合でも導入可能です。

### 依存するライブラリ
このアプリケーションの基幹部分はpython2で書かれています。
さらに次のサードパーティのライブラリに依存しています。
* pybtex : BibTeXのパース
* jinja2 : HTMLの生成

主要なLinuxディストリビューションにおいては
jinja2はパッケージ管理アプリケーション(yum,apt等)によって
導入できるでしょう。
しかしpybtexはあまりメジャーではないので、
見つからない事があるでしょう。
幸運にもpybtexではeasy\_installによってインストールする事が可能です。
```shell
easy_install pybtex
```
(通常、管理者権限が必要です)
もしBibTeXキーの自動取得機能を使用する場合、
*pybtexのversionが0.16以降である必要があります*。
パッケージ管理アプリケーションは古いバージョンのpybtexをインストールする事があります。

### インストール手順 (Linux)
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
* [name.logfile]    : CGIのエラーメッセージを出力するファイル名
* [server.address]  : CGIサーバーのアドレス
* [server.port]     : CGIサーバーのポート番号

設定を変更したらHTMLを生成し必要な物をコピーするため、次のコマンドを実行します。
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
以上で[path.outputdir]にarticles.html他必要なものがコピーされます。
これでお気に入りのブラウザで
```
file:///home/yourname/[path.outputdir]/articles.html
```
を開けば論文のリストが閲覧できます。

## 使い方

### PDFへのリンク
要件の所に書いてあるように、PDFファイルのファイル名は[bibtexkey].pdfとしておいてください。
リンクを機能させるには[path.outputdir]/pdf/以下にPDFファイルを置いておきます。
こうする事で、HTMLから相対パスによりfile://でPDFを取得できます。
file://で取得する事によりPDFに対する変更を保存する事ができます。

### タグ付け
タグ付けの機能を使用するにはCGIサーバーを立てる必要があります。
ただし単独のPCで使う場合はapache等の本格的なCGIサーバーを立てる必要はありません。
pythonにはCGIのテスト用のため簡易CGIサーバーを容易に構築できるライブラリが付属していますので、
この機能を使用してCGIサーバーを構築します。
ファイアウォールの内側で行なうため、
ファイアウォールの設定をしない限り外部からこのサーバーはアクセスできない点に注意してください。

サーバーを立てるにはやはりstart.pyを使用します。
```shell
./start.py
```
これにより.htmlを更新した上でCGIサーバーが立ちます。
このプロセスは中断しない限りCGIのリクエストを待ちつづけるので、
終了する場合はCtrl-C等で終了してください。

CGIサーバーを起動しておけばタグ付け機能を使用する事ができます。
各文献のタイトルの左にあるタグのボタンをクリックする事によりタグの操作UIが出現します。
Tag Nameを入力し、createボタンを押すことにより文献にタグを付ける事ができます。
付加されたタグはタイトル下のナビ部分に表示され、
タグ名をクリックする事でタグ付けされた文献を搾り込むことができます。
タグの情報は[name.database]で指定されたデータベースに保管されます。

### BibTeXキーの自動取得
PDFからBibTeX情報を取得するには
```shell
./start.py --getbib
```
あるいは
```shell
./start.py -b
```
を実行します。
これにより対応するBibTeXキーが存在しないPDFの一覧が表示され、
取得するか問います。
PDFからまずpdftotextを用いて平文テキストに変換した後、
doiをパースし、dx.doi.orgに問い合わせる事によりBibTeX情報を取得します。
取得したBibTeXキーを用いてPDFがリネームされ、処理は完了します。

### iPad/GoodReaderで使用する
iPadのPDFリーダーGoodReaderでアプリケーションを使用する方法を簡単に説明します。
#### WebApp単独の場合
まずGoodReaderに[path.outputdir]ごと同期します。
同期はDropbox,Google Drive等のオンラインストレージの他にssh(sftp)が使用できます。
sftpはsshサーバーを利用して22番（デフォルト）ポートを使用するため
別個にサーバーを構築する必要がなく便利です。
GoodReaderはHTMLを読めるので、同期したarticles.htmlを開けば使用できます。
さらに相対パスでのリンクが可能ですので、
HTMLの各文献のタイトル部分のリンクは機能します。

#### CGIサーバーを立てる場合
現在の所、iPad内にCGIサーバーを構築できないので、
外部にサーバーを構築する必要があります。
CGIサーバーのアドレス、ポート番号は設定ファイルで指定可能です。

## ライセンス
3条項BSDライセンス
