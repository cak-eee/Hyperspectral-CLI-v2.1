import sys
import time
import platform
import psutil

def check_libs():
    libs = ["rich", "scipy", "sklearn", "matplotlib", "numpy", "psutil"]
    missing = [l for l in libs if __import__(l) is None] # Basit kontrol
    # Not: Gerçekte ImportError yakalanmalı ama check_libs mantığı aynı.

try:
    import scipy.io as sio
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.panel import Panel
except: pass

console = Console()

CAK_ART = r"""
[bold cyan]
   ___   _   _  _     _____ _____ _____ 
  / __| /_\ | |/ /___| ____| ____| ____|
 | (__ / _ \| ' <|___|  _| |  _| |  _|  
  \___/_/ \_\_|\_\   |_____|_____|_____|
[/bold cyan]
[bold white]   HYPERSPECTRAL ANALYSIS SYSTEM v2.4[/bold white]
"""

def get_sys_info():
    table = Table(show_header=False, box=None)
    table.add_row("İşlemci:", platform.processor().split(',')[0])
    table.add_row("Bellek:", f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB RAM")
    table.add_row("OS:", f"{platform.system()} {platform.release()}")
    return table

def run_analysis():
    console.print(CAK_ART)
    console.print(Panel(get_sys_info(), title="[bold yellow]Donanım Analizi[/bold yellow]", border_style="blue"))

    while True:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=console) as progress:
            
            # 1. Veri Yükleme
            task1 = progress.add_task("[cyan]Veri yükleniyor...", total=100)
            try:
                data = sio.loadmat('Indian_pines_corrected.mat')['indian_pines_corrected']
                gt = sio.loadmat('Indian_pines_gt.mat')['indian_pines_gt']
                progress.update(task1, completed=100)
            except:
                console.print("[bold red]HATA:[/] Veri dosyaları (.mat) bulunamadı!")
                break

            # 2. PCA Analizi
            task2 = progress.add_task("[magenta]PCA (Boyut İndirgeme)...", total=100)
            pixels = data.reshape(-1, data.shape[2])
            pca = PCA(n_components=30)
            pixels_pca = pca.fit_transform(pixels)
            progress.update(task2, completed=100)

            # 3. Yapay Zeka (SVM) Eğitimi
            task3 = progress.add_task("[yellow]Yapay Zeka Eğitiliyor...", total=100)
            indices = np.where(gt.ravel() > 0)[0]
            X = pixels_pca[indices]
            y = gt.ravel()[indices]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            clf = SVC(kernel='rbf', C=100, gamma=0.01)
            clf.fit(X_train, y_train)
            progress.update(task3, completed=100)

        # --- TERMINAL RAPORU (DÜŞÜK SEVİYE ANLATIM) ---
        acc = accuracy_score(y_test, clf.predict(X_test)) * 100
        
        console.print("\n" + "="*60)
        console.print("[bold green]✅ ANALİZ BAŞARIYLA TAMAMLANDI[/bold green]")
        console.print("="*60)
        
        console.print("\n[bold cyan]🔍 BU GÖRSELLER NE ANLAMA GELİYOR?[/bold cyan]")
        console.print("[white]1. SOLDAKİ HARİTA (Referans):[/white] Tarlaların gerçek halidir (Cevap Anahtarı).")
        console.print("[white]2. SAĞDAKİ HARİTA (Tahmin):[/white] Yapay zekanın pikselleri analiz ederek çıkardığı haritadır.")
        console.print("[white]3. NOKTALI PİKSELLER:[/white] Yapay zekanın iki ürün arasında kararsız kaldığı veya yanıldığı yerlerdir.")
        console.print(f"\n[bold yellow]Sistem Doğruluk Oranı: %{acc:.2f}[/bold yellow]")
        console.print("="*60)

        # Görselleştirme
        all_preds = clf.predict(pixels_pca)
        result_map = all_preds.reshape(gt.shape)
        result_map[gt == 0] = 0
        
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1); plt.title("Zemin Gerçeği (Referans)"); plt.imshow(gt, cmap='nipy_spectral')
        plt.subplot(1, 2, 2); plt.title(f"SVM Tahmini (Doğruluk: %{acc:.2f})"); plt.imshow(result_map, cmap='nipy_spectral')
        
        plt.savefig('analiz_sonuc.png', dpi=300, bbox_inches='tight')
        plt.show()

        console.print("\n[bold yellow][1][/bold yellow] Analizi Tekrarla | [bold red][0][/bold red] Güvenli Çıkış")
        if console.input("\n[bold cyan]Komut: [/bold cyan]") == '0': break

if __name__ == "__main__":
    run_analysis()