# ぼっちエンジニア Python用テンプレート

## 環境構築

### Poetryを使う場合

poetryのコマンドでパッケージをインストールします。
内容としては `pyproject.toml` の中身が参照されます

```bash
$ poetry install
```

ローカルでの起動

```bash
$ cd src
$ poetry shell
$ uvicorn main:app --reload
```

localhost:8000で起動します🎉
試しに `http://localhost:8000` にGETリクエストを送ってみましょう

### グローバルで動かす場合

pipコマンドでパッケージをインストールします。
内容としては `requirements.txt` の中身が参照されます。

```bash
pip install -r requirements.txt
```

ローカルでの起動

```bash
$ cd src
$ uvicorn main:app --reload
```

localhost:8000で起動します🎉
試しに `http://localhost:8000` にGETリクエストを送ってみましょう
