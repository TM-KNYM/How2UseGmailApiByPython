#Python��GmailAPI���g���Ă݂悤


GmailApi���g���Ă݂��̂Ŕ��Y�^  
�����ł̓T���v���R�[�h�����s����܂ł̎菇���L��
�ŏI�I��sample.py�����s����ƃ��[���{�b�N�X�ɂ��郁�[���̃��X�g�݂����Ȃ��̂��\���o���܂�


##�K�v�Ȃ���

* Python2.7
* google-api-python-client�FPython�p��GoogleAPI���C�u����
* Google �A�J�E���g


##�����

�����ɗL��Ƃ���ɂ����߂Ă�����OK�ł��B  
https://developers.google.com/gmail/api/quickstart/quickstart-python
�Ƃ����̂͗��\�Ȃ̂Ŏ��̏��ԂŃ������Ă����܂�

1. GoogleAPI��L���ɂ���  
2. google-api-python-client���C���X�g�[������  
3. �T���v���R�[�h�𗎂Ƃ�  
4. sample.py�����s���Ă݂�  

###GoogleAPI��L���ɂ���

1. google�A�J�E���g��K���ɍ���ă��O�C��  
2. ���Ɂ��ɃA�N�Z�X���āu�v���W�F�N�g���쐬�v�������ēK���Ȗ��O�̃v���W�F�N�g�����  
  https://console.developers.google.com/project  
3. ���̃��j���[�ɂ���uAPI�ƔF�؁v��API���N���b�N�AGmailApi��L���ɂ���  
4. �����āuAPI�ƔF�؁v�̔F�؏����N���b�N���āA�u�V�����N���C�A���g���쐬�v���N���b�N    
5. �����Python�A�v������A�N�Z�X����̂�InstalledApplication��I��  
6. ��������Ɓu�l�C�e�B�u �A�v���P�[�V�����̃N���C�A���g ID�v�\���E���ɏo����̂�  
�@�uJson���_�E�����[�h]�Ń_�E�����[�h����B  


###google-api-python-client���C���X�g�[������  

* easy install���g���ꍇ  
sudo easy_install --upgrade google-api-python-client  
* pip���g���ꍇ  
sudo pip install --upgrade google-api-python-client

###�T���v���R�[�h�𗎂Ƃ�

git clone https://github.com/TM-KNYM/How2UseGmailApiByPython.git

���ŃN���[������sample.py��gmailapi.py�����Ƃ���܂��B  
gmailapi.py�E�E�Egoogle-api-python-client���g���ĐF�X���Ă݂Ă郂�W���[��  
sample.py �E�E�Egmailapi.py���Ăяo���T���v���R�[�h  


###sample.py�����s���Ă݂�

�^�[�~�i�����̓R�}���h���C���ŃT���v���R�[�h�𗎂Ƃ����f�B���N�g���Ɉړ�  
�����ŉ��L�̂悤�ɃR�}���h�����s����  
JSON�t�@�C����GoogleAPI��L���ɂ���Ń_�E�����[�h�������̂ł�

python sample.py [JSON�t�@�C��]

�ڂ����������e��GmailApi.py��sample.py�����ĂˁB
GmailAPI��API�̏ڍׂ�google Developer��apis-explorer������ƕ�����₷���ł�  
http://developers.google.com/apis-explorer/#p/gmail/v1/  

##���̑�����

OAuth2.0�ɂ���  
https://developers.google.com/api-client-library/python/guide/aaa_oauth?hl=ja#oauth

gmail��API��scope�ɂ���  
https://developers.google.com/gmail/api/auth/scopes?hl=ja

