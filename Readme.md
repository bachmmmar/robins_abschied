
# Generate sentences with google translator
Enter the following url in your browser: 
https://translate.google.com/translate_tts?ie=UTF-8&tl=de&client=tw-ob&text=

Add your text at the end of the url.


# Installation
SYSTEMD_SCRIPT_DIR=/etc/systemd/system/
sudo cp robinsAbschied.service $SYSTEMD_SCRIPT_DIR
sudo systemctl daemon-reload
sudo systemctl enable robinsAbschied.service