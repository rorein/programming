"""
http://pydub.com/

git clone https://github.com/jiaaro/pydub.git

help:
/mnt/hgfs/Data/github/programming/python/audio.pydub.markdown

pip install pydub

sudo apt-add-repository ppa:jon-severinsson/ffmpeg
sudo apt-add-repository ppa:samrog131/ffmpeg

sudo apt-get install ffmpeg

"""

from pydub import AudioSegment

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")


