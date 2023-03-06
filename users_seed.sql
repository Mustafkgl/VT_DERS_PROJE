-- Kullanıcı Verileri - Kütüphane Yönetim Sistemi
-- Bu dosya sistem kullanıcılarını (admin ve üyeler) içerir
-- Tüm şifreler güvenli hash algoritması (scrypt) ile şifrelenmiştir

-- Önce mevcut kullanıcıları temizle (isteğe bağlı)
-- DELETE FROM fines;
-- DELETE FROM borrowings;
-- DELETE FROM users;

-- Admin ve Üye Kullanıcıları Ekle
INSERT INTO users (username, password, email, role) VALUES
('admin', 'scrypt:32768:8:1$9sUw004ORhAha9ly$c4117d4d9de85a5def98adbe6e0ff6a602d877dba7bed521d39cd458ea793ac5777981d9048ec9bc842102ec3cd44c5ad8624fb310f4d6c0de9785a6acc00097', 'admin@library.com', 'admin'),
('ahmet_yilmaz', 'scrypt:32768:8:1$v1QcvmbmaWaTJjeS$036037093de80d58b29a39677a03af66e18b72390c3e9c4ae36a605d3bf14bd88d254b7e8509aad0bcd7e5f1a0765b247b181c8c7c197cd8736a2cc9fc35fea1', 'ahmet@email.com', 'member'),
('ayse_demir', 'scrypt:32768:8:1$qTjhOiy9Q9shs8LE$4c28052bb08941dc3a0bd287a80cdf5c53be034c729eff9150180703f6c82a130127551127cb0bda7c017d58b320fe7da149e91be82207edbe8d71c756b05650', 'ayse@email.com', 'member'),
('mehmet_kaya', 'scrypt:32768:8:1$EbYhW0EwTSVXRzem$25b03e0de28a597b947b0817ca5740aeb7808ec6656b7ba1f32e70a72b951411b5b91ee4636dd691d5b5d9a227af7ba748f89b1e5a50d6fd399f3a127c4ca5cb', 'mehmet@email.com', 'member'),
('fatma_celik', 'scrypt:32768:8:1$bZtsoL5V1bBTjrhU$86ad56e6c19e363db1ed05464e5d7a37b95c7ec9ebb95f28c88bcff992a878883e262d7fe64a72ba5ee83f024854c25b434673ce213c1b99b9a7214860597540', 'fatma@email.com', 'member'),
('mustafa_arslan', 'scrypt:32768:8:1$zymtRpHfPzZgu4Al$a45f31c67e04859386b03978c2b047fcc901cb016ac3f0c72f2f54df7178fca7ab3fb169d8cde085a1b58da811402463fbd7fc7c485a42177c2ceba676cf99c0', 'mustafa@email.com', 'member'),
('zeynep_ozturk', 'scrypt:32768:8:1$wAgd65lTUHXNEycT$0262ff112e254bf77dfab04418046cd25e9edb6a84c908d7c99656cb05882d3f9c4c7088b5e7e0653f9b44e947f93be9470dbbadb272cc0bd3dda114e65e1164', 'zeynep@email.com', 'member'),
('ali_yildiz', 'scrypt:32768:8:1$RtOgJwtVQ4nEagbm$3f99c89747a6804a43b518dcc2e6dc5ada892e27778c41603302407665f8385fe5325be42c3d569d1310bc0aa151d1facabf75084ef198c45d0b4ad7f1638915', 'ali@email.com', 'member'),
('elif_sahin', 'scrypt:32768:8:1$us8zwBodmK254Kon$99ba1b6e42f19d692c996d316d49c19fb4b0d49260b0e08608ed8a27248fb0f1e44633b2be608dfe1bda6315fba4257d229bf6f9275a1ae0854dce0ab6632c01', 'elif@email.com', 'member'),
('can_kara', 'scrypt:32768:8:1$A4HQ30Nl8BnjLzab$bbb4eb46d0abe8c5d0c6c9787cb92731a39ecd6ef0a5166c63197e587abec803f13a7d7b31c21753cf978cf613da02ff4b5eaa27f3bdaeea2d25057b39609489', 'can@email.com', 'member'),
('selin_kurt', 'scrypt:32768:8:1$L3JOShBisqGJMgTW$22b93ef01dd86b0f3db192277125a99d7593b00700d350f6ecb9678bb7455cf8593b60c7911dc2f865019eb14ba36182c2dfe1fd6a2e81acab2671ae230e7dce', 'selin@email.com', 'member')
ON CONFLICT (username) DO NOTHING;

-- Kullanıcı bilgileri
SELECT 'Kullanıcılar başarıyla eklendi!' as mesaj;
SELECT 'Toplam kullanıcı sayısı:' as info, COUNT(*) as sayi FROM users;

-- Giriş Bilgileri
-- ====================
-- Admin Hesabı:
--   Kullanıcı Adı: admin
--   Şifre: admin123
--
-- Üye Hesapları:
--   Kullanıcı Adı: ahmet_yilmaz, ayse_demir, mehmet_kaya, vb.
--   Şifre: 123456 (Tüm üyeler için aynı)
-- ====================
