# coding:utf-8
# clone_push_pullreq_mergeまでの流れ(リポジトリ共有式の方法)
# http://blog.qnyp.com/2013/05/28/pull-request-for-github-beginners/を参考にしました




========================おおまかな手順、以下==========================
A.ローカルで、Pull Request用のブランチを作成してpushする
B.GitHub上で、Pull Requestを作成する
C.GitHub上で、Pull Requestをマージする
========================おおまかな手順、以上==========================




========================具体的な手順、以下============================
下記の手順に沿ってやること
�@〜�Eまでは上記のA、�FがB、�G〜�IがCに対応する。

�@フォルダを作成してcloneを作成
git clone https://github.com/keyoshimura/Tips_Git.git

�A作成したcloneに移動
cd Tips_Git

�B新しいブランチを作成
git checkout -b work_pullreq

�Cファイルを修正
修正内容を同名ファイルに反映する

�Dインデックスに反映、&commit
git add 
git commit -m "変更内容をローカルコミット"

�Eリモートに反映
git push origin work_pullreq

�FPull Request作成ページに移動
Github上の「Compare & pull request」をクリック
必要ならばコメントを記述し、送信相手に送信
(create pull requestボタンをクリック)
(これでpull requestがオープンになったので、この後は管理者の反応を待つこと)

�Gpullrequest内容を確認する(管理者がやることですよ)
pull request上に存在する「Commit」、「Files Changed」ボタンをクリックし差分や変更内容を確認する

�Hpull request内容をmergeする
上記で確認した内容に問題がないようであれば、pull request内容をマージする
(「Merge pull request」ボタンをクリック)

�I不要なブランチを削除する
一般的に、マージが完了してしまえばそのために利用していたブランチは不要となる。
そのため、マージ後に不要ブランチを削除すること
(Delete branchボタンをクリック)