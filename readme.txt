Discord Görev Botu
Bu projede, kullanıcıların görevleri yönetmesine olanak tanıyan bir Discord botu bulunmaktadır. Kullanıcılar, görev ekleyebilir, görevleri silebilir, tamamlanmış görevleri işaretleyebilir ve görev listesini görüntüleyebilirler.

Gereksinimler
Python 3.7+
Aşağıdaki Python kütüphaneleri:
discord.py (discord botunu çalıştırmak için)
sqlite3 (veritabanı işlemleri için)
aiohttp (HTTP istekleri için)

Kullanım
tasks.db veritabanı, görevlerin saklandığı SQLite veritabanıdır. Bu veritabanının başlangıçta oluşturulması gerekir.

Bot, !add_task <açıklama> komutu ile yeni bir görev ekler.

!delete_task <id> komutu ile bir görevi siler.

!show_tasks komutu ile tüm görevleri listeler.

!complete_task <id> komutu ile bir görevi tamamlanmış olarak işaretler.

Güvenlik Notu
Botu çalıştırırken, bot token'ını güvenli bir şekilde sakladığınızdan emin olun. bot.run('<TOKEN>') kısmında token'ın yanlışlıkla dışarıya sızmaması için dikkatli olun.
SSL sertifikası doğrulaması devre dışı bırakılmıştır. Bu, token hataları veya SSL bağlantı sorunları nedeniyle botun güvenliksiz olarak çalışmasını sağlar. Gerçek projelerde SSL doğrulamanın devre dışı bırakılmaması önemlidir.


Botu Çalıştırma
Botu çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
python bot.py
