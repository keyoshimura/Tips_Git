# coding:utf-8
# clone_push_pullreq_merge�܂ł̗���(���|�W�g�����L���̕��@)
# http://blog.qnyp.com/2013/05/28/pull-request-for-github-beginners/���Q�l�ɂ��܂���




========================�����܂��Ȏ菇�A�ȉ�==========================
A.���[�J���ŁAPull Request�p�̃u�����`���쐬����push����
B.GitHub��ŁAPull Request���쐬����
C.GitHub��ŁAPull Request���}�[�W����
========================�����܂��Ȏ菇�A�ȏ�==========================




========================��̓I�Ȏ菇�A�ȉ�============================
���L�̎菇�ɉ����Ă�邱��
�@�`�E�܂ł͏�L��A�A�F��B�A�G�`�I��C�ɑΉ�����B

�@�t�H���_���쐬����clone���쐬
git clone https://github.com/keyoshimura/Tips_Git.git

�A�쐬����clone�Ɉړ�
cd Tips_Git

�B�V�����u�����`���쐬
git checkout -b work_pullreq

�C�t�@�C�����C��
�C�����e�𓯖��t�@�C���ɔ��f����

�D�C���f�b�N�X�ɔ��f�A&commit
git add 
git commit -m "�ύX���e�����[�J���R�~�b�g"

�E�����[�g�ɔ��f
git push origin work_pullreq

�FPull Request�쐬�y�[�W�Ɉړ�
Github��́uCompare & pull request�v���N���b�N
�K�v�Ȃ�΃R�����g���L�q���A���M����ɑ��M
(create pull request�{�^�����N���b�N)
(�����pull request���I�[�v���ɂȂ����̂ŁA���̌�͊Ǘ��҂̔�����҂���)

�Gpullrequest���e���m�F����(�Ǘ��҂���邱�Ƃł���)
pull request��ɑ��݂���uCommit�v�A�uFiles Changed�v�{�^�����N���b�N��������ύX���e���m�F����

�Hpull request���e��merge����
��L�Ŋm�F�������e�ɖ�肪�Ȃ��悤�ł���΁Apull request���e���}�[�W����
(�uMerge pull request�v�{�^�����N���b�N)

�I�s�v�ȃu�����`���폜����
��ʓI�ɁA�}�[�W���������Ă��܂��΂��̂��߂ɗ��p���Ă����u�����`�͕s�v�ƂȂ�B
���̂��߁A�}�[�W��ɕs�v�u�����`���폜���邱��
(Delete branch�{�^�����N���b�N)