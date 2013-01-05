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


