from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Person])
Person.create(name="ゆうや", age=11)

class Traveler(Model):
    name = CharField()
    age = IntegerField()
    from_area = CharField()
    allergy = CharField()
    dislike = CharField()
    interest = CharField()
    from_date = IntegerField()
    to_date = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Traveler])

class Destination(Model):
    name = CharField()
    address = CharField()
    contents = CharField()
    access = CharField()
    parkingarea = CharField()
    closeddays = CharField()
    price = CharField()
    cashless = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Destination])
Destination.create(name="あかれんが館",address="岩手県盛岡市中ノ橋通１丁目２−２０",contents="紹介文",access="盛岡駅よりバスで10分 →「盛岡バスセンター」のバス停で下車 → 徒歩1分",parkingarea="なし",closeddays="年末年始、毎週火曜日",price="盛岡銀行ゾーン一般300円、小中学生100円、未就学児童無料",cashless="当館窓口では、クレジットカード、電子マネー、QRコード決済をご利用いただけます。")
Destination.create(name="盛岡城跡公園",address="岩手県盛岡市内丸1番37号",contents="紹介文",access="盛岡駅からバスで10分（都心循環バスでんでんむし乗車、「盛岡城跡公園」下車）",parkingarea="あり、岩手県盛岡市内丸１−５５",closeddays="なし",price="駐車場を使うのならば、基本料金	22時から翌8時まで	80円（1時間ごと）上限額（最大料金）	8時から18時まで	1100円、18時から翌8時まで	800円、回数駐車券	150円券11枚つづり	1500円、また、盛岡歴史文化館によるのならば[1F]無料 [2F入場料]一般300円、高校生200円、小中学生100円",cashless="ミュージアムショップのみOKとせせています。入場料は現金のみとなっています。")
Destination.create(name="福田パン",address="岩手県盛岡市長田町１２−１１",contents="紹介文",access="JR・IGR盛岡駅東口から徒歩13分1km バスは12乗り場から、県立中央病院循環など。本町交番前が近いです。",parkingarea="あり、長田町１２−１１",closeddays="金曜日7時00分～16時00分、土曜日7時00分～16時00分、日曜日7時00分～16時00分、月曜日7時00分～16時00分、火曜日定休日、水曜日7時00分～16時00分、木曜日7時00分～16時00分",price="最低でも500円ほどあれば足ります",cashless="カード不可. 電子マネー不可. QRコード決済不可")
Destination.create(name="高松の池",address="岩手県盛岡市高松１丁目２６−１",contents="紹介文",access="JR盛岡駅から岩手県交通11番線「松園営業所行き」バスで約15分 「高松の池口」にて下車 徒歩約1分か東北自動車道盛岡ICより、車で約15分が良いと思います",parkingarea="あり、盛岡市高松１丁目２６−１ 高松の池",closeddays="なし",price="お金は入りません",cashless="ありません")
Destination.create(name="御所湖BBQ場",address="雫石町西安庭第１１地割７−４ ",contents="紹介文",access="バスで（岩手県交通）で（JR盛岡駅から）約25分～40分 ※路線バスはつなぎ温泉が終点です",parkingarea="あり、このBBQエリアの横にあります",closeddays="4月1日～11月30日、9:00～17:00（4月～10月、11月は～16:30）",price="無料",cashless="ありません")
Destination.create(name="東家",address="中ノ橋通１丁目８−３",contents="紹介文",access="岩手県交通バス盛岡駅→盛岡バスセンター行き最寄りバス停は盛岡バスセンター下車、徒歩3分",parkingarea="なし、近隣の有料駐車場をご利用ください",closeddays="金曜日11時00分～15時00分, 17時00分～19時00分、土曜日11時00分～15時00分, 17時00分～19時00分、日曜日11時00分～15時00分, 17時00分～19時00分、月曜日11時00分～15時00分, 17時00分～19時00分、火曜日11時00分～15時00分, 17時00分～19時00分、水曜日11時00分～15時00分, 17時00分～19時00分、木曜日11時00分～15時00分, 17時00分～19時00分と毎月第1水曜日 （5月GW、8月を除く）",price="4200円あれば足りると思います",cashless="クレジットカード, カード可また、電子マネー可QRコード決済不可")
Destination.create(name="盛楼閣",address="岩手県盛岡市盛岡駅前通１５−５",contents="紹介文",access="JR盛岡駅より、徒歩3分. 盛岡駅から177m",parkingarea="なし、近隣の有料駐車場をご利用ください",closeddays="金曜日	11時00分～0時00分土曜日	11時00分～0時00分日曜日	11時00分～0時00月曜日	11時00分～0時00分火曜日	11時00分～0時00分水曜日	11時00分～0時00分木曜日	11時00分～0時00分また、年中無休",price="4200円あれば足りると思います",cashless="クレジットカード, カード可また、電子マネー可QRコード決済不可")
Destination.create(name="髭",address="岩手県盛岡市繋字尾入野47-15",contents="紹介文",access="盛岡駅から97M歩く→盛岡駅前で雫石線に乗る→尾入野で降りて徒歩2分",parkingarea="あり",closeddays="※平日のみランチ営業有、11:00～14:00（L.O 14:00）定休日, 木※木曜定休※8月は無休で営業致します",price="4200円あれば足りると思います",cashless="スマート支払い, 利用不可. クレジットカード, 利用可、VISA､マスター､アメックス､DINERS､JCB. 電子マネー, 利用不可. QRコード決済, 利用不可")
Destination.create(name="白龍",address="岩手県盛岡市内丸5-15",contents="紹介文",access="盛岡駅前から岩手県交通バス（盛岡都心循環バス「でんでんむし」左回り）で9分「県庁・市役所前」下車、徒歩2分。桜山神社の参道沿い。",parkingarea="なし、近隣の有料駐車場をご利用ください",closeddays="土曜日	9時00分～20時45分日曜日	11時30分～16時00分月曜日	9時00分～20時45分火曜日	9時00分～20時45分水曜日	9時00分～20時45分木曜日	9時00分～20時45分金曜日	9時00分～20時45分。また、定休日無し（盆時期休、年始休)。",price="1000円あれば足りると思います",cashless="カード可. （VISA、Master、JCB、AMEX、Diners）. 電子マネー可. （交通系電子マネー（Suicaなど）、楽天Edy、nanaco、QUICPay）. QRコード決済可. ")
Destination.create(name="クラムボン",address="岩手県盛岡市紺屋町5-33",contents="紹介文",access="R盛岡駅→バスで、バス停、上の橋下車、徒歩3分",parkingarea="なし、近隣の有料駐車場をご利用ください",closeddays="月・火・金・土. 10:00 - 17:00 · 水・木・日. 定休日.",price="850円あれば足りると思います",cashless="カード不可。現金のみとなっております。")
Destination.create(name="よ市",address="岩手県盛岡市材木町７−３８ 材木町",contents="紹介文",access=" 盛岡駅: 東口から 徒歩 9分",parkingarea="無料駐車場はございませんので、近隣のパーキングをご利用ください。",closeddays="土 4月上旬～11月下旬 15:10～18:30",price="その人その人によりますが、2000ほどあれば良いと僕は思います。",cashless="カード不可。現金のみとなっております。")