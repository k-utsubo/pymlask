from __future__ import unicode_literals
from nose.tools import assert_equals, assert_true, assert_false, assert_raises
from mlask import MLAsk

emotion_analyzer = MLAsk()
jdata = emotion_analyzer.analyze("未だにマイナンバーカードを持つメリットが理解できません。行政側にメリットがあるにしろ、今までの生活で保険証も現代は１人１つを持っていますから家族で共有しているわけでもなく、住民票などもそれほど頻繁に必要でもないし、お薬手帳は手帳のままのほうが自分で管理しやすいし、、、。５年に１度の運転免許更新ですら何かと手間なのに、マイナンバーカードにも更新があると知ってから尚更作りたくない気持ちが大きくなりました。これだけ政府が推進しているのを知るだけでも、メリットは国にあって国民にではない気がします。大手銀行の度重なるシステムエラーのような事があるかもしれないし、ハッカーやウィルスによるサイバー攻撃に遭う可能性もあります。義務化されるまで作りません。")
print(jdata)