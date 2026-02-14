# Hyperspectral-CLI-v2.1
🛰️ Hyperspectral-CLI v2.1

Hyperspectral-CLI, yüksek boyutlu spektral verilerin (Hyperspectral Imagery) işlenmesi, analiz edilmesi ve sınıflandırılması için geliştirilmiş, terminal tabanlı interaktif bir analiz aracıdır. Özellikle Indian Pines veri seti üzerinde PCA ve SVM algoritmalarını kullanarak yüksek doğruluklu sonuçlar üretmek üzere optimize edilmiştir.
🛠️ Teknik Özellikler & Mimari

Bu proje, karmaşık uzaktan algılama verilerini saniyeler içinde işleyebilecek şekilde modernize edilmiştir:

    Boyut İndirgeme (PCA): 224 spektral banttan oluşan ağır veri küpü, en yüksek varyansı temsil eden ilk 30 temel bileşene (Principal Components) indirgenerek işlem hızı %85 oranında artırılmıştır.

    Sınıflandırma (SVM): Uzaktan algılama literatüründe başarısı kanıtlanmış, doğrusal olmayan ayrıştırma kapasitesine sahip RBF (Radial Basis Function) Kernel SVM algoritması kullanılmıştır.

    Modern Terminal UI: rich kütüphanesi entegrasyonu ile progress barlar, dinamik tablolar ve interaktif seçim menüleri sunan bir kullanıcı arayüzü (CLI) oluşturulmuştur.

    Donanım Optimizasyonu: Yazılım, 64-bit mimari üzerinde Sapphire Nitro+ RX 6900 XT GPU ve 48GB RAM kapasiteli yüksek performanslı bir sistemde geliştirilmiş ve test edilmiştir.

🚀 Hızlı Başlangıç (Quick Start)

Bu projeyi herhangi bir cihazda kütüphane kurma derdi olmadan çalıştırmak için irm (Invoke-RestMethod) yöntemini kullanabilirsiniz:
PowerShell

# PowerShell üzerinden tek satırda çalıştırma (Planlanan)
irm bit.ly/hypes-x | python -

Manuel Kurulum

    Depoyu Klonlayın: git clone https://github.com/CumaAliKocak/Hyperspectral-CLI.git

    Bağımlılıkları Yükleyin: pip install rich scipy scikit-learn matplotlib

    Çalıştırın: python analiz.py

📊 Analiz Akışı (Flowchart)

    Input: Indian Pines .mat dosyalarının okunması.

    Preprocessing: Veri küpünün (145x145x224) 2D matrise dönüştürülmesi.

    PCA: Bilgi kaybını minimize ederek boyutun 30'a düşürülmesi.

    SVM Training: %30 test, %70 eğitim verisi ile modelin eğitilmesi.

    Output: Terminal üzerinde detaylı Accuracy raporu ve Matplotlib ile karşılaştırmalı harita gösterimi.

👨‍💻 Geliştirici

Cuma Ali Koçak
Elektrik-Elektronik Mühendisliği (EEM) - Son Sınıf Öğrencisi
