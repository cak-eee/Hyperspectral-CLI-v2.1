🛰️ Hyperspectral-CLI v2.4

Hyperspectral-CLI, yüksek boyutlu spektral verilerin (Hyperspectral Imagery) işlenmesi ve sınıflandırılması için geliştirilmiş, terminal tabanlı interaktif bir analiz aracıdır. Özellikle Indian Pines veri seti üzerinde PCA ve SVM algoritmalarını kullanarak yüksek doğruluklu sonuçlar üretmek üzere optimize edilmiştir.

Bu proje, uzaydan (AVIRIS sensörü ile) alınan Indian Pines bölgesine ait yüksek boyutlu spektral verilerin yapay zeka ile sınıflandırılmasını sağlar. Analiz süreci ve sonuçların anlamı aşağıda adım adım açıklanmıştır:

🔍 Analiz Süreci (Pipeline)

-Veri Girişi: 224 farklı spektral banttan (gözle görülmeyen ışık imzaları) oluşan veri küpü sisteme yüklenir.

-PCA (Temel Bileşen Analizi): Veri setindeki 224 bant, bilgi kaybı minimize edilerek en anlamlı 30 bileşene indirgenir. Bu işlem, "Boyutun Laneti" (Curse of Dimensionality) problemini çözer ve işlem hızını artırır.

-SVM (Destek Vektör Makineleri): İndirgenmiş veriler, RBF (Radial Basis Function) çekirdeği kullanılarak eğitilir. Bu algoritma, pikseller arasındaki kimyasal benzerliği matematiksel olarak gruplandırır.

📊 Görseller Ne İfade Ediyor?

-SOLDAKİ HARİTA (Zemin Gerçeği / Ground Truth): Bu, arazinin "cevap anahtarı"dır. Uzmanlar tarafından sahada doğrulanmış gerçek ürün türlerini (mısır, soya fasulyesi, orman vb.) temsil eder. Renklerin bloklar halinde düzgün olmasının sebebi, gerçek tarlaların bir bütün olmasıdır.

-SAĞDAKİ HARİTA (SVM Tahmini): Yapay zekanın pikselleri analiz ederek kendi oluşturduğu haritadır.

-Noktalı Pikseller (Kumlanma): Sağdaki haritada görülen pikselli yapı, yapay zekanın iki benzer bitki türü (örneğin mısır ile soyanın spektral imzası) arasında kararsız kaldığı veya yanıldığı noktaları gösterir.

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
 
 *v2.2	Hardware & Export	psutil ile donanım bilgisi çekme özelliği ve analizi PNG olarak kaydetme yeteneği eklendi.
 
 *v2.3	Syntax & UI Polish	ASCII sanatı raw string yapılarak SyntaxWarning hatası giderildi. PNG altına teknik açıklama eklendi.
 
 *v2.4	Interpretive Report	Analiz sonuçlarını düşük seviyede (low-level) açıklayan "Anlamlandırılmış Rapor" sistemi terminale entegre edildi.

👨‍💻 Geliştirici

cak-eee & gemini ai
1.45
