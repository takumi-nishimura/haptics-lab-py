#!/bin/bash

script_dir=$(cd $(dirname $0); pwd) # このスクリプトがあるディレクトリを取得
cd $script_dir # 上で取得したスクリプトのディレクトリに移動
source .venv/bin/activate # 仮想環境を有効化, $script_dirからの相対パスで指定
source haptics_lab_py/run/config/activate.sh # 環境変数を設定, $script_dirからの相対パスで指定
python haptics_lab_py/run/main.py # Pythonのスクリプトを実行, $script_dirからの相対パスで指定
