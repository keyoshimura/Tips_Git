# coding:utf-8
# Git�̊�{�I�Ȏg�����ɂ��Ẵ����ł�


"""
Github�̃R�}���h����

���LURL���Q�Ƃ��邱��
https://techacademy.jp/magazine/6235


�@Github�Ƀ��O�C�����ă��|�W�g�����쐬����
�uNew Repository�v�A�uCreate repository�v�{�^��������
���̉�ʂŃ����[�g���|�W�g���̃A�h���X���\�������̂ŁA�T���Ă�������

�A�t�@�C�����쐬
���ۂɏ���������t�@�C�����쐬����
�e�L�X�g�G�f�B�^�ł�Pycharm�ł��Ȃ�ł������ł��B

�B���[�J��PC�Ɂu���[�J�����|�W�g���v���쐬����
���[�J�����|�W�g���ɂ������t�H���_�Ɉړ�(cmd��)���āA�ugit init�v�����s

===========,awesome�f�B���N�g���Ɉړ����āA���������[�J�����|�W�g���ɂ�����=====
mkdir awesome
cd awesome
git init
===========,awesome�f�B���N�g���Ɉړ����āA���������[�J�����|�W�g���ɂ�����A�ȏ�

�ugit init�v�R�}���h�����s���邱�ƂŁA�J�����g�f�B���N�g����Git���|�W�g���ɕϊ��ł���

�C�����[�g���|�W�g���ɔ��f���������t�@�C�����u�C���f�b�N�X�v�ɒǉ�����(git add)
��قǍ쐬�����t�@�C�������[�J�����|�W�g���ɒǉ�����B
��̓I�ɂ͉��L�̂悤�ȃR�}���h�Łu�C���f�b�N�X�v�ɒǉ�����B
�C���f�b�N�X�Ƃ́A���|�W�g���Ɂu�R�~�b�g���邽�߂ɕύX���e���ꎞ�I�ɕۑ�����ꏊ�̂��Ƃł���B

======================�uhello.html�v�t�@�C�����C���f�b�N�X�ɒǉ������=======
git add hello.html

�D�u�C���f�b�N�X�v�̓��e�����[�J�����|�W�g���Ɂu�R�~�b�g�v����(git commit)
��قǃC���f�b�N�X�ɒǉ������t�@�C�������[�J�����|�W�g���ɃR�~�b�g����B
git commit -m �gadd new file�h

�܂��A���L�̃R�}���h�Łu�t�@�C�����ǉ�����Ă��邩�v���m�F���邱�Ƃ��\
git status

�E�����[�g���|�W�g���̏���ǉ�(git remote)
git remote�R�}���h

====================�菇�@�Ń��|�W�g���쐬���ɏo��URL���uhttps://github.com//awesome.git�v�������ꍇ�̗�
git remote add origin https://github.com//awesome.git

�F���[�J�����|�W�g�����v�b�V�����ă����[�g���|�W�g���ɔ��f������(git push)
���[�J�����|�W�g���̕ύX�������[�g���|�W�g���ɔ��f������
git push origin master

���̂Ƃ����[�U�[���ƃp�X���[�h�𕷂����̂œ��͂��邱��



�����𓙂��폜����R�}���h
���L��URL�������폜�������t�@�C����URL�ɕύX���邱��
git filter-branch --tree-filter "rm -f [URL]" HEAD

"""

��remote url�ύX
�@���݂̃A�h���X���m�F
git remote -v
�A�������ύX
git remote set-url origin https://github.com/keyoshimura/work_20171004.git


���N���[���쐻
��ƊJ�n���ɁA�����[�g���|�W�g���̏������[�J���Ɏ擾����K�v������B
���L�̃R�}���h�ɂđΉ�

�@�Ώۃt�H���_�Ɉړ�

�A�N���[���쐻
(URL)
git clone https://github.com/keyoshimura/work_20171004.git
(ssh_��Г��ł͂��̌`���嗬��)
git clone ssh://user@hostname/path/to/repo


��pull(���M�r��)
��Ɠ��e�𔽉f������O�ɁA�u�����[�g���|�W�g����master�u�����`�̍ŐV�Łv�����擾����K�v������
���̂��߁A�����ƃf�B���N�g���ɏ�L�̓��e�𔽉f������K�v������B
��̓I�ɂ́A���L�̎菇�ɏ]���čŐV�ł̏����擾����B

�@��̃t�H���_���쐬����
���ʂɋ�̃t�H���_���쐬����

�A�����[�g���|�W�g�������Z�b�g
�܂��A�V�����쐬�����t�H���_�̃����[�g���|�W�g�������m�F����B
git remote -v

�����āA�R�s�[���Ă������u�����`�������[�g���|�W�g��URL�Ƃ��ăZ�b�g(URL�ł͂Ȃ�ssh��)
git remote set-url origin git@github.com:keyoshimura/Git_Tips.git

�Bpull
��L�Ŏw�肵�������[�g���|�W�g��URL�̃f�[�^�������Ă���(pull)
git pull origin master


���LURL���Q�l�ɂ��܂����B
https://qiita.com/minoringo/items/917e325892733e0d606e


