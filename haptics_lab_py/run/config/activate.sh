#!/usr/bin/env sh

# activate.sh.envに記述された環境変数を，このスクリプトの環境変数としてエクスポートする

while read -r line; do
    LINE="$(eval echo $line)";  # ファイルの1行を読む
    export "$LINE";  # 環境変数をエクスポート
done < "haptics_lab_py/run/config/activate.sh.env" # 読むファイルのパスを指定
