#!/bin/bash
set -e

echo checking secure access
openssl aes-256-cbc -K $encrypted_4d56ad91a2b0_key -iv $encrypted_4d56ad91a2b0_iv -in id_rsa.enc -out id_rsa -d
git config --global user.name 'Travis CI'
git config --global user.email 'travis@nobody.org'
git config --global push.default 'simple'
pip install -U --upgrade-strategy=eager pip setuptools wheel
pip install -U --upgrade-strategy=eager 'Nikola[extras]'
echo -e 'Host github.com\n    StrictHostKeyChecking no' >> ~/.ssh/config
eval "$(ssh-agent -s)"
chmod 600 id_rsa
ssh-add id_rsa
git remote rm origin
git remote add origin git@github.com:Unidata/python-training.git
git fetch origin gh-pages
git branch gh-pages FETCH_HEAD

echo github_deploy called
nikola build && nikola github_deploy -m 'Nikola auto deploy [ci skip]'