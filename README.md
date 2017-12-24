Installation instructions:

brew install dependencies:

mpg321
swig
portaudio

Install or upgrade to python3
- Install virtualenv
`pip3 install virtualenv`


- Set up a virtual env folder:
`mkdir ~/Python_envs`
`virtualenv -p /usr/local/bin/python3 ~/Python_envs/Voiceminder`

- Install Swig:
`brew install swig`

- activate the virtualenv enviornment in the text-speech folder
`source ~/Python_envs/Voiceminder/bin/activate`
- install requirements
`pip3 install -r requirements.txt`

now you can run the code in this isolated python3 enviornment

-deactivate env
`deactivate`
