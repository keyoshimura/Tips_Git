# coding:utf-8
# Gitの基本的な使い方についてのメモです


"""
Githubのコマンド流れ

下記URLを参照すること
https://techacademy.jp/magazine/6235


①Githubにログインしてリポジトリを作成する
「New Repository」、「Create repository」ボタンを押す
次の画面でリモートリポジトリのアドレスが表示されるので、控えておくこと

②ファイルを作成
実際に処理させるファイルを作成する
テキストエディタでもPycharmでもなんでもいいです。

③ローカルPCに「ローカルリポジトリ」を作成する
ローカルリポジトリにしたいフォルダに移動(cmdで)して、「git init」を実行

===========,awesomeディレクトリに移動して、そこをローカルリポジトリにした例=====
mkdir awesome
cd awesome
git init
===========,awesomeディレクトリに移動して、そこをローカルリポジトリにした例、以上

「git init」コマンドを実行することで、カレントディレクトリをGitリポジトリに変換できる

④リモートリポジトリに反映させたいファイルを「インデックス」に追加する(git add)
先ほど作成したファイルをローカルリポジトリに追加する。
具体的には下記のようなコマンドで「インデックス」に追加する。
インデックスとは、リポジトリに「コミットするために変更内容を一時的に保存する場所のことである。

======================「hello.html」ファイルをインデックスに追加する例=======
git add hello.html

⑤「インデックス」の内容をローカルリポジトリに「コミット」する(git commit)
先ほどインデックスに追加したファイルをローカルリポジトリにコミットする。
git commit -m “add new file”

また、下記のコマンドで「ファイルが追加されているか」を確認することが可能
git status

⑥リモートリポジトリの情報を追加(git remote)
git remoteコマンド

====================手順①でレポジトリ作成時に出たURLが「https://github.com//awesome.git」だった場合の例
git remote add origin https://github.com//awesome.git

⑦ローカルリポジトリをプッシュしてリモートリポジトリに反映させる(git push)
ローカルリポジトリの変更をリモートリポジトリに反映させる
git push origin master

このときユーザー名とパスワードを聞かれるので入力すること



●履歴等を削除するコマンド
下記のURL部分を削除したいファイルのURLに変更すること
git filter-branch --tree-filter "rm -f [URL]" HEAD

"""

●remote url変更
①現在のアドレスを確認
git remote -v
②向き先を変更
git remote set-url origin https://github.com/keyoshimura/work_20171004.git


●クローン作製
作業開始時に、リモートリポジトリの情報をローカルに取得する必要がある。
下記のコマンドにて対応

①対象フォルダに移動

②クローン作製
(URL)
git clone https://github.com/keyoshimura/work_20171004.git
(ssh_会社等ではこの形が主流か)
git clone ssh://user@hostname/path/to/repo


●pull(執筆途中)
作業内容を反映させる前に、「リモートリポジトリのmasterブランチの最新版」情報を取得する必要がある
そのため、特定作業ディレクトリに上記の内容を反映させる必要がある。
具体的には、下記の手順に従って最新版の情報を取得する。

①空のフォルダを作成する
普通に空のフォルダを作成する

②リモートリポジトリ情報をセット
まず、新しく作成したフォルダのリモートリポジトリ情報を確認する。
git remote -v

続いて、コピーしてきたいブランチをリモートリポジトリURLとしてセット(URLではなくsshね)
git remote set-url origin git@github.com:keyoshimura/Git_Tips.git

③pull
上記で指定したリモートリポジトリURLのデータを持ってくる(pull)
git pull origin master


下記URLを参考にしました。
https://qiita.com/minoringo/items/917e325892733e0d606e



●Pushしてもうまくいかない時
ローカルリポジトリ、リモートリポジトリをちゃんと指定しないとダメな場合もある。
例えば、下記のように指定してPUSHすることでうまくいくかもしれない。

$git push origin [ローカルリポジトリ]:[リモートリポジトリ]
