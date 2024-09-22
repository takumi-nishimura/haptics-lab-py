# haptics-lab-py

Pythonのサンプルプログラムをまとめたリポジトリ

## グラフの作成 haptics_lab_py/plot

- 論文に適したグラフのスタイル．  
  matplotlibやseabornを使用する際，importするとスタイルが変化する．
  - plot_style.py
- 箱ひげ図のサンプル
  - box_plot.ipynb
- 相関図のサンプル
  - corr_plot.ipynb

## モーションキャプチャー haptics_lab_py/mocap

1. ライブラリをインストール

   ```python
   poetry add git+ssh://git@github.com:takumi-nishimura/NatNetPy.git
   ```

2. ライブラリをインポート(/mocap/test_mocap.py)

   ```python
   from natnetpy import OptiClient
   ```

## シリアル通信 haptics_lab_py/serial

M5StackとPythonで，シリアル通信の送受信を行うサンプル．

## バッチファイル haptics_lab_py/run

Pythonのコードをバッチファイルで実行する．  
ダブルクリックで実行することができる．

- Macの場合
  1. 実行権限の付与

    ```shell
    chmod u+x run.command
    ```

  2. バッチファイルの実行

    ```shell
    source run.command
    ```

- Windowsの場合
  1. バッチファイルの実行

    ```shell
    run.bat
    ```
