🛰️ Hyperspectral-CLI v2.1

Hyperspectral-CLI, yüksek boyutlu spektral verilerin (Hyperspectral Imagery) işlenmesi ve sınıflandırılması için geliştirilmiş, terminal tabanlı interaktif bir analiz aracıdır. Özellikle Indian Pines veri seti üzerinde PCA ve SVM algoritmalarını kullanarak yüksek doğruluklu sonuçlar üretmek üzere optimize edilmiştir.

🛠️ Teknik Özellikler & Mimari

-Boyut İndirgeme (PCA): 224 spektral banttan oluşan ağır veri küpü, en yüksek varyansı temsil eden ilk 30 temel bileşene indirgenerek işlem hızı optimize edilmiştir.

-Sınıflandırma (SVM): Uzaktan algılamada doğrusal olmayan ayrıştırma kapasitesine sahip RBF Kernel SVM algoritması kullanılmıştır.

-Modern Terminal UI: rich kütüphanesi entegrasyonu ile progress barlar ve dinamik tablolar sunan bir CLI oluşturulmuştur.

-Donanım Avantajı: Yazılım, Sapphire Nitro+ RX 6900 XT GPU ve 48GB RAM kapasiteli yüksek performanslı bir sistemde geliştirilmiştir.

🚀 Hızlı Başlangıç (Quick Start)

    irm bit.ly/hypes-x | python -

📊 Analiz Akışı (Flowchart)

-Input: Indian Pines .mat dosyalarının okunması.

-Preprocessing: Veri küpünün 2D matrise dönüştürülmesi.

-PCA: Boyutun 30'a düşürülerek verinin hafifletilmesi.

-SVM Training: %70 eğitim verisi ile modelin eğitilmesi.

-Output: Karşılaştırmalı harita gösterimi ve Accuracy raporu.

🛠️ Versiyon	Başlık	Değişiklikler
 *v1.0	Initial Commit	PCA ve SVM algoritmalarının temel entegrasyonu.
 *v1.1	Path & Arch Fix	64-bit mimari optimizasyonu ve PATH düzeltmeleri.
 *v2.0	Rich UI Integration	rich kütüphanesi ile progress barlar ve tablolar eklendi.
 *v2.1	Interactive & IRM	Çıkış döngüsü (Loop) eklendi, geliştirici adı cak-eee olarak güncellendi.

👨‍💻 Geliştirici

cak-eee
