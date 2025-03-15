# task_manager_bot
Bu, Discord üzerinde görev yönetimi yapmak için kullanılan bir bot örneğidir. Bot, kullanıcıların görev eklemesine, silmesine, listelemesine ve tamamlanmış olarak işaretlemesine olanak tanır. Aşağıdaki adımları izleyerek botunuzu çalıştırabilirsiniz.

Özellikler
Görev Ekleme: Kullanıcılar yeni görevler ekleyebilir.
Görev Silme: Kullanıcılar var olan görevleri silebilir.
Görev Listeleme: Mevcut görevler listelenebilir.
Görev Tamamlama: Görevler tamamlanmış olarak işaretlenebilir.

Gereksinimler
Bu botu çalıştırabilmek için aşağıdaki kütüphanelere ihtiyacınız olacak:

discord.py: Discord API'sini kullanarak botu oluşturmak için gerekli.
sqlite3: Veritabanı işlemleri için.
aiohttp: HTTP isteklerini asenkron olarak göndermek için.
ssl: SSL doğrulamasını devre dışı bırakmak için.
Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:
pip install discord.py sqlite3 aiohttp

Kullanım
1. Botu Başlatma
Botu çalıştırmak için, kodun sonunda yer alan bot.run('TOKEN') satırındaki TOKEN kısmını kendi Discord bot token'ınızla değiştirdiğinizden emin olun.

Not: Eğer token ile ilgili sorun yaşarsanız, SSL doğrulamasını devre dışı bırakabilirsiniz. Bu, sertifikasız bağlantılarda botun çalışmasını sağlar. Ancak, bu güvenlik açığı oluşturabilir ve sadece gelişim ortamında kullanılması önerilir.

2. Bot Komutları
Botun sağladığı komutlar şunlardır:

!add_task <görev açıklaması>: Yeni bir görev ekler.
!delete_task <görev ID>: Belirtilen ID'ye sahip görevi siler.
!show_tasks: Tüm görevleri listeler.
!complete_task <görev ID>: Belirtilen görevi tamamlanmış olarak işaretler.
3. Veritabanı
Bu bot, görevleri saklamak için tasks.db adlı bir SQLite veritabanı kullanır. Veritabanı, bot çalıştırıldığında otomatik olarak oluşturulacaktır.

Veritabanı yapısı şu şekildedir:

id: Görev ID'si (otomatik artan).
description: Görev açıklaması.
completed: Görev tamamlandıysa 1, aksi takdirde 0.
4. SSL Problemleri
Bot token'ı kullanarak botu başlatırken SSL sertifikalarıyla ilgili bir sorun yaşamanız durumunda, SSL doğrulamasını devre dışı bırakmak için aşağıdaki satırları kullanabilirsiniz:

# SSL doğrulamasını devre dışı bırak
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
Bu kod, botun SSL sertifikalarıyla ilgili sorunları bypass etmesini sağlar. Ancak bu güvenlik açısından önerilmez. Bu yöntem yalnızca geliştirme aşamasında kullanılmalıdır.

5. Güvenlik Uyarısı
Dikkat: Botunuzu canlı ortamda çalıştırmadan önce, bot.run('TOKEN') kısmındaki token'ı güvenli bir şekilde sakladığınızdan emin olun. Token'ınızı kimseyle paylaşmayın ve versiyon kontrol sistemlerine (örneğin GitHub) yüklemeyin.
