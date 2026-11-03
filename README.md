# Briganti LNİ Hesaplayıcı

Prostat kanserinde lenf nodu invazyonu riskini hesaplayan, telefona kurulabilen web uygulaması.

- **MR var:** Briganti 2019 (Gandaglia ve ark., Eur Urol 2019). ePLND eşiği %7.
- **MR yok:** Briganti 2012 (Briganti ve ark., Eur Urol 2012). ePLND eşiği %5.

## Güncelleme

1. Katsayı ve eşikler `src/briganti-nomogram.html` içindeki `MODEL_CONFIG` bloğundadır. `version` ve `reviewed` alanlarını güncelleyin.
2. `python3 build_app.py` çalıştırın; `index.html` ve `sw.js` önbellek sürümü yeniden üretilir.
3. Commit + push. GitHub Pages yeni sürümü yayınlar, telefonlar bir sonraki açılışta günceller.

Karar destek aracıdır; klinik değerlendirmenin yerini almaz.
