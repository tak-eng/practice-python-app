from django.db import models
# Create your models here.
class Seiyuu(models.Model):  # SeiyuuというTableを宣言する、頭文字が大文字が流儀
    """声優さんの一覧"""
  #  性別を選択する選択肢を宣言
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    # フィールドを定義します
    # verbose_name：人間に表示する名前を決める、adminサイトとかで使う
    name = models.CharField(max_length=255, verbose_name='名前')  # max_lengthは長さの最大値
    # choicesにタプルを指定することで選択肢のエリアにできる、
    # blankやnullをOKにするかどうか
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    birth_day = models.DateField(verbose_name='誕生日', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # レコードが追加された時にその時間を保存します
    updated_at = models.DateTimeField(auto_now=True)  # レコードが更新されたタイミングで現在時間が保存されます。

    def __str__(self):  # クラスを呼び出したときに何が帰るか？(基本何でも良いです)
        return self.name