# 📊 EVALUASI MODEL - Penjelasan Singkat

---

## 🎯 APA ITU EVALUASI MODEL?

Evaluasi = **Mengecek seberapa bagus model kami membuat prediksi**

Analoginya:
- Setelah belajar, kita buat ujian → Check nilai → Tahu seberapa pintar kita

---

## 3️⃣ METRIK UTAMA

### 1. ACCURACY (Akurasi)
**"Dari 100 prediksi, berapa yang benar?"**

```
Rumus:
Accuracy = (Jumlah Prediksi Benar) / (Total Prediksi) × 100%

Contoh:
- Total review test: 10,000
- Prediksi benar: 8,750
- Accuracy = 8,750 / 10,000 × 100% = 87.5% ✅

Artinya: 87.5% prediksi kita BENAR, 12.5% SALAH
```

---

### 2. PRECISION (Presisi)
**"Dari yang diprediksi POSITIF, berapa yang benar-benar POSITIF?"**

```
Rumus:
Precision = (TP) / (TP + FP)
  TP = True Positive (prediksi positif, benar-benar positif)
  FP = False Positive (prediksi positif, tapi negatif)

Contoh:
- Prediksi POSITIF: 5,000 reviews
- Yang benar POSITIF: 4,400
- Precision = 4,400 / 5,000 = 88% ✅

Artinya: Ketika kita bilang positif, 88% benar
```

---

### 3. RECALL (Recall)
**"Dari review yang sebenarnya POSITIF, berapa yang terdeteksi?"**

```
Rumus:
Recall = (TP) / (TP + FN)
  TP = True Positive
  FN = False Negative (sebenarnya positif, diprediksi negatif)

Contoh:
- Review benar POSITIF: 5,000 total
- Terdeteksi positif: 4,400
- Recall = 4,400 / 5,000 = 88% ✅

Artinya: 88% review positif berhasil kita tangkap
```

---

## 📈 CONFUSION MATRIX

**Ini tabel yang menunjukkan hasil prediksi:**

```
                 PREDIKSI
                 Positif   Negatif
SEBENARNYA Positif  [TP]     [FN]
           Negatif  [FP]     [TN]

TP (True Positive):   ✅ Prediksi Positif, BENAR Positif
FP (False Positive):  ❌ Prediksi Positif, tapi NEGATIF
FN (False Negative):  ❌ Prediksi Negatif, tapi POSITIF
TN (True Negative):   ✅ Prediksi Negatif, BENAR Negatif
```

### Contoh Nyata:

```
                DIPREDIKSI
                Pos      Neg
SEBENARNYA Pos  4,400    600    ← 5,000 reviews positif
           Neg  600      4,400  ← 5,000 reviews negatif
                ↑
           Total prediksi positif: 5,000

TP = 4,400 (benar prediksi positif)
FP = 600   (salah prediksi positif, sebenarnya negatif)
FN = 600   (salah prediksi negatif, sebenarnya positif)
TN = 4,400 (benar prediksi negatif)

Accuracy = (4,400 + 4,400) / 10,000 = 88%
Precision = 4,400 / 5,000 = 88%
Recall = 4,400 / 5,000 = 88%
```

---

## 🔍 CONTOH EVALUASI NYATA

### Output dari `python evaluate.py`:

```
Loading data...
Loading model...
Predicting...

Accuracy: 0.8750

Report:
              precision    recall  f1-score   support
    negative       0.87      0.87      0.87      5000
    positive       0.88      0.88      0.88      5000
   accuracy                           0.88     10000
  macro avg       0.87      0.87      0.87     10000
weighted avg       0.88      0.88      0.88     10000
```

### Penjelasan:

| Metric | Negative | Positive | Artinya |
|--------|----------|----------|---------|
| **Precision** | 0.87 (87%) | 0.88 (88%) | Ketika prediksi positif, 88% benar |
| **Recall** | 0.87 (87%) | 0.88 (88%) | Dari review positif, 88% terdeteksi |
| **F1-Score** | 0.87 | 0.88 | Gabungan precision & recall |
| **Support** | 5000 | 5000 | Jumlah test data |

**Kesimpulan:** Model cukup bagus! 87-88% akurat 👍

---

## 🎬 CARA JALANKAN EVALUASI

### Command:
```bash
# Masuk ke folder src
cd src

# Jalankan evaluate script
python evaluate.py
```

### Output akan muncul:
```
Loading data...
Loading model...
Predicting...
Accuracy: 0.8750
Report:
...
```

---

## ❓ KAPAN EVALUASI BAGUS?

```
EXCELLENT (>90%):
  • Accuracy > 90% ✅✅✅
  • Precision > 90% ✅✅✅
  • Recall > 90% ✅✅✅
  
GOOD (80-90%):
  • Accuracy 80-90% ✅✅
  • Precision 80-90% ✅✅
  • Recall 80-90% ✅✅
  
ACCEPTABLE (70-80%):
  • Accuracy 70-80% ✅
  • Precision 70-80% ✅
  • Recall 70-80% ✅
  
POOR (<70%):
  • Accuracy < 70% ❌
  • Precision < 70% ❌
  • Recall < 70% ❌
```

**Model kita: 87-88% → GOOD! 👍**

---

## 🎯 KAPAN EVALUATE DIJALANKAN?

```
1. Setelah Training
   python model.py
        ↓
   Lihat: Accuracy saat training
   
2. Check Kualitas Model
   python evaluate.py
        ↓
   Lihat: Precision, Recall, F1-Score
   
3. Sebelum Deploy
   - Pastikan Accuracy >= 80%
   - Pastikan Precision tinggi
   - Pastikan Recall tinggi
```

---

## 📊 VISUALIZATION (SIMPLE)

```
Model TRAINING vs TESTING:

Training Accuracy: 88%  ✅
Testing Accuracy:  87.5% ✅

→ Bagus! Tidak overfitting (training ≈ testing)

Jika:
- Training: 99%, Testing: 70% → OVERFITTING ❌
- Training: 70%, Testing: 70% → UNDERFITTING ❌
```

---

## 🔑 KEY TAKEAWAY

**Evaluasi Model = Mengecek Kualitas Prediksi**

```
3 Metrik Penting:
1. Accuracy (87.5%)   → Overall correctness
2. Precision (88%)    → Confidence saat prediksi positif
3. Recall (88%)       → Coverage positif yang terdeteksi
```

**Semakin tinggi ketiga metrik ini, semakin bagus model! 🚀**

---

## 💡 ANALOGI MUDAH

Bayangkan model kita sebagai dokter:

```
ACCURACY = Dari 100 pasien, berapa yang diagnosis tepat?
  Dokter kita: 87 dari 100 benar (87%) ✅

PRECISION = Dari pasien yang kita bilang "sakit", berapa yang benar sakit?
  Dokter kita: 88 dari 100 diagnosis sakit yang benar (88%) ✅

RECALL = Dari pasien yang benar sakit, berapa yang kita deteksi?
  Dokter kita: 88 dari 100 pasien sakit terdeteksi (88%) ✅

→ Dokter yang cukup kompeten! 👨‍⚕️
```

---

**Created: January 2026**
**Untuk: Memahami Evaluasi Model**
