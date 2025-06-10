# Gelişmiş Güvenli Dosya Transfer Sistemi


Bu proje, ağ üzerinden güvenli ve verimli bir şekilde dosya transferi yapmayı amaçlayan bir sistemdir. RSA ve AES şifreleme algoritmaları, SHA256 hash fonksiyonu ve düşük seviye IP başlık işleme teknikleri kullanılarak geliştirilmiştir.

## İçindekiler

- [Proje Tanımı](#proje-tanımı)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Teknoloji Yığını](#teknoloji-yığını)
- [Proje Yapısı](#proje-yapısı)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)

## Proje Tanımı

Bu proje, günümüzde giderek artan veri güvenliği ihtiyacına cevap vermek amacıyla geliştirilmiştir. Amacımız, ağ üzerinden güvenli ve verimli bir şekilde dosya transferi yapabilen bir sistem oluşturmaktı. Projemizin potansiyel kullanım alanları arasında güvenli veri depolama, hassas bilgilerin iletimi ve ağ güvenliği testleri bulunmaktadır.

## Özellikler

- **Güvenli Dosya Transferi:** RSA ve AES şifreleme algoritmaları ile güvenli dosya transferi.
- **Veri Bütünlüğü:** SHA256 hash fonksiyonu ile veri bütünlüğünün sağlanması.
- **Düşük Seviye IP İşleme:** IP başlıklarının manipülasyonu ve analizi.
- **Ağ Performans Ölçümü:** Gecikme, bandwidth ve paket kaybı gibi ağ performans metriklerinin ölçülmesi.
- **Saldırı Simülasyonu:** Ortadaki adam (MITM) saldırıları ve paket enjeksiyonu gibi saldırıların simülasyonu.
- **Hibrit TCP/UDP Anahtarlama (Opsiyonel):** TCP ve UDP protokolleri arasında dinamik geçiş.
- **Dinamik Tıkanıklık Kontrolü (Opsiyonel):** Ağ tıkanıklığına göre adaptif veri transferi.
- **Grafiksel Kullanıcı Arayüzü (GUI) (Opsiyonel):** Kullanıcı dostu arayüz.

## Kurulum

1.  **Gerekli Kütüphaneleri Yükleyin:**

    ```bash
    pip install pycryptodome scapy
    ```

2.  **Proje Dosyalarını İndirin:**

    ```bash
    git clone [proje_reposu_url]
    cd guvenli-dosya-transfer-sistemi
    ```

## Kullanım

1.  **Sunucuyu Başlatın:**

    ```bash
    python server.py
    ```

2.  **İstemciyi Başlatın:**

    ```bash
    python client.py
    ```

3.  **Dosya Transferini Gerçekleştirin:**
    *   İstemci tarafında, sunucu adresini ve transfer etmek istediğiniz dosyanın adını belirtin.
    *   Sunucu ve istemci arasındaki iletişimi takip edin.

## Teknoloji Yığını

- **Programlama Dilleri:** Python, C (opsiyonel)
- **Kütüphaneler:**
    - PyCryptodome (Şifreleme)
    - Scapy (Ağ Paketleri)
    - hashlib (Hashleme)
- **Ağ Analiz Araçları:**
    - Wireshark
    - iPerf
    - netstat
    - ping
    - tc

## Proje Yapısı


## Katkıda Bulunma

1.  **Fork Edin:** Projeyi kendi GitHub hesabınıza fork edin.
2.  **Branch Oluşturun:** Yeni bir özellik veya düzeltme için bir branch oluşturun.

    ```bash
    git checkout -b yeni-ozellik
    ```

3.  **Değişikliklerinizi Yapın:** Kodunuzu yazın ve test edin.
4.  **Commit Edin:** Değişikliklerinizi açıklayıcı bir mesajla commit edin.

    ```bash
    git commit -m "Yeni özellik eklendi: [özellik adı]"
    ```

5.  **Push Edin:** Branch'inizi GitHub'a push edin.

    ```bash
    git push origin yeni-ozellik
    ```

6.  **Pull Request Oluşturun:** GitHub üzerinden orijinal projeye bir pull request gönderin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır 

## İletişim

ESRA ÖZCAN - esraozcn_9@outlook.com

[GitHub Profiliniz](https://github.com/esraozcn)

[LinkedIn Profiliniz](https://www.linkedin.com/in/esra-özcan-38328b21a/)

---

Bu README dosyası, projenizin temel bilgilerini içermektedir. Projenize özgü detayları eklemeyi ve gerekli gördüğünüz değişiklikleri yapmayı unutmayın. Başarılar dilerim!
