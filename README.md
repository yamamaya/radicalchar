# 部首文字正規化ライブラリ

Google Chromeで作成したPDFファイル等にありがちな、UnicodeのCJK部首補助文字や康煕部首文字に関連する文字化けを修正するためのライブラリです。

例えば、文字化けした文字列「⼤⻨」(U+2F24 U+2EE8)を、本来の漢字に置き換えて「大麦」(U+5927 U+9EA6)に変換します。

文字化けの現象について、詳細はこちらを参照してください。  
➡ [PDFをコピペするとなぜ“文字化け”が起きてしまうのか](https://logmi.jp/tech/articles/324366)

## 使い方

それぞれの言語用の変換テーブルと、簡単に使える関数を用意しています。

### JavaScriptの場合

```javascript
<script type="text/javascript" src="radicalchar.js"></script>

<script>
var str = "⼤⻨";
var str2 = RadicalChar.Normalize( str );
</script>
```

### C#の場合

```csharp
string str = "⼤⻨";
string str2 = RadicalChar.Normalize( str );
```

### Pythonの場合

```python
import radicalchar;

str = "⼤⻨"
str2 = radicalchar.normalize( str )
```
