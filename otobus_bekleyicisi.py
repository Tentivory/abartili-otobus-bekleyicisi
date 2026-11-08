#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Otobüs Bekleyicisi
============================
Dünyanın en ciddi otobüs bekleme simülatörü.
Otobüs gelmez. Sen beklersin. Evren izler.
"""

import random
import time

bahaneler = [
    "Otobüs şu anda varoluşsal bir kriz yaşıyor ve kendini sorguluyor.",
    "Şoför, kırmızı ışıkta çay demledi ve çay soğumasın diye bekliyor.",
    "Otobüs, 'bugün biraz geç kalsam da olur' diye düşündü. Düşündü ve uyguladı.",
    "Yolcuların hepsi aynı anda 'bir durak sonra ineceğim' dedi, şoför kilitlendi.",
    "Otobüs aslında geldi ama sen onu görmedin çünkü telefonuna bakıyordun. Klasik.",
    "Evrenin ısı ölümüne kadar beklemeyi planlıyor. Sabır.",
    "Şoför, 'bir fincan daha içsem' dedi. Bir fincan 47 dakikadır sürüyor.",
    "Otobüs, trafik ışığına kızıp greve gitti."
]

felsefeler = [
    "Beklemek, insanın en yüce eylemidir. Otobüs ise bu eylemin somutlaşmış halidir.",
    "Her geçen saniye, otobüsün gelmeme ihtimalini bilimsel olarak artırır.",
    "Belki otobüs gelmiyor değildir. Belki sen yanlış durakta bekliyorsundur. Ya da yanlış hayattasındır.",
    "Zaman, otobüsün gelmemesiyle ölçülür."
]

def otobüs_bekleniyor_mu():
    print("Otobüs bekleyicisi başlatılıyor...")
    print("Lütfen sabırlı olun. Otobüs gelmeyecek.")
    print("-" * 50)
    
    for i in range(5):
        print(f"\n[{i+1}. dakika]")
        print(random.choice(bahaneler))
        time.sleep(0.5)
        if random.random() > 0.6:
            print(f"Felsefe notu: {random.choice(felsefeler)}")
    
    print("\n" + "=" * 50)
    print("SONUÇ: Otobüs gelmedi.")
    print("Ama sen artık daha bilge bir insansın. Veya değilsin.")
    print("Tekrar denemek için programı yeniden çalıştır. Sonsuza kadar.")

if __name__ == "__main__":
    otobüs_bekleniyor_mu()

# Gizli not (base64 decode etmeyin, etseniz de bir şey yok): 
# Siyaset mi? Yok ya, otobüs gecikti diye kimse hükümeti suçlamaz. Suçlar mı? Bilmiyorum.

# --- DAMGA VE İMZA ---
# İmza: Kayyum Grok (mahkemeden atanmış, gönülden değil)
# Tarih: 8 Kasım 2026
# Damga: Bu kod resmi olarak otobüsün gelmeyeceğini teyit eder. Teyit etmez. Kararsız.
