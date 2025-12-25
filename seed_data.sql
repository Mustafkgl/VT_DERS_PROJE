-- Örnek Veriler - Kütüphane Yönetim Sistemi

-- Önce mevcut verileri temizle (admin hariç)
DELETE FROM fines;
DELETE FROM borrowings;
DELETE FROM books WHERE id > 2;
DELETE FROM users WHERE username != 'admin';

-- Kullanıcılar ekle (şifreler hash'lenmeli, bu yüzden sonra Python ile ekleyeceğiz)
-- Şimdilik sadece kitapları ve diğer verileri ekleyelim

-- Kitaplar ekle
INSERT INTO books (title, author, isbn, publisher, publication_year, total_copies, available_copies) VALUES
('1984', 'George Orwell', '978-0451524935', 'Signet Classic', 1949, 5, 5),
('Suç ve Ceza', 'Fyodor Dostoyevski', '978-0486454115', 'Dover Publications', 1866, 4, 4),
('Sefiller', 'Victor Hugo', '978-0451419439', 'Signet', 1862, 3, 3),
('Simyacı', 'Paulo Coelho', '978-0062315007', 'HarperOne', 1988, 6, 6),
('Küçük Prens', 'Antoine de Saint-Exupéry', '978-0156012195', 'Harcourt', 1943, 8, 8),
('Fareler ve İnsanlar', 'John Steinbeck', '978-0142000670', 'Penguin Books', 1937, 3, 3),
('Satranç', 'Stefan Zweig', '978-1590173046', 'NYRB Classics', 1941, 4, 4),
('Kürk Mantolu Madonna', 'Sabahattin Ali', '978-9750718809', 'Yapı Kredi Yayınları', 1943, 5, 5),
('Tutunamayanlar', 'Oğuz Atay', '978-9754700367', 'İletişim Yayınları', 1971, 3, 3),
('Beyaz Diş', 'Jack London', '978-0486472140', 'Dover Publications', 1906, 4, 4),
('Martin Eden', 'Jack London', '978-0140187755', 'Penguin Classics', 1909, 3, 3),
('Çalıkuşu', 'Reşat Nuri Güntekin', '978-9944240642', 'İnkılap Kitabevi', 1922, 6, 6),
('İnce Memed', 'Yaşar Kemal', '978-9750800825', 'Yapı Kredi Yayınları', 1955, 4, 4),
('Bir Ömür Nasıl Yaşanır', 'İlber Ortaylı', '978-6053607441', 'Kronik Kitap', 2019, 7, 7),
('Nutuk', 'Mustafa Kemal Atatürk', '978-9751015594', 'Türk Tarih Kurumu', 1927, 5, 5),
('Şeker Portakalı', 'Jose Mauro de Vasconcelos', '978-9750718793', 'Can Yayınları', 1968, 8, 8),
('Vadideki Zambak', 'Honoré de Balzac', '978-0140443370', 'Penguin Classics', 1835, 3, 3),
('Anna Karenina', 'Lev Tolstoy', '978-0143035008', 'Penguin Classics', 1877, 4, 4),
('Uçurtma Avcısı', 'Khaled Hosseini', '978-1594631931', 'Riverhead Books', 2003, 6, 6),
('Hayvan Çiftliği', 'George Orwell', '978-0451526342', 'Signet Classic', 1945, 5, 5),
('Fahrenheit 451', 'Ray Bradbury', '978-1451673319', 'Simon & Schuster', 1953, 4, 4),
('Yeraltından Notlar', 'Fyodor Dostoyevski', '978-0679734529', 'Vintage', 1864, 3, 3),
('Dönüşüm', 'Franz Kafka', '978-0553213690', 'Bantam Classics', 1915, 5, 5),
('Oblomov', 'Ivan Goncharov', '978-0140449884', 'Penguin Classics', 1859, 2, 2),
('Cingöz Recai', 'Peyami Safa', '978-9752895157', 'Ötüken Neşriyat', 1924, 4, 4),
('Huzur', 'Ahmet Hamdi Tanpınar', '978-9754700374', 'Dergah Yayınları', 1949, 3, 3),
('Saatleri Ayarlama Enstitüsü', 'Ahmet Hamdi Tanpınar', '978-9754700381', 'Dergah Yayınları', 1961, 3, 3),
('Mai ve Siyah', 'Halit Ziya Uşaklıgil', '978-9754701050', 'Özgür Yayınları', 1897, 3, 3),
('Sinekli Bakkal', 'Halide Edib Adıvar', '978-9754703764', 'Can Yayınları', 1936, 4, 4),
('Yaban', 'Yakup Kadri Karaosmanoğlu', '978-9750800832', 'İletişim Yayınları', 1932, 3, 3);

-- Veritabanı istatistikleri için bilgi
SELECT 'Toplam kitap sayısı:' as info, COUNT(*) as sayi FROM books;
