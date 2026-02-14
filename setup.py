import PyInstaller.__main__

params = [
    'analiz.py',
    '--onefile',
    '--name=cak-eee-Hyperspectral-v2.4',
    '--collect-submodules=rich',
    '--hidden-import=rich._unicode_data',
    # Gereksiz kütüphaneleri dışarıda bırakıyoruz
    '--exclude-module=torch',
    '--exclude-module=bitsandbytes',
    '--exclude-module=cuda',
    '--clean'
]

print("🚀 CAK-EEE Üretim Hattı: Gereksiz DLL'ler Ayıklanıyor...")
PyInstaller.__main__.run(params)
print("✅ Temiz EXE Oluşturuldu! dist klasörünü kontrol et.")