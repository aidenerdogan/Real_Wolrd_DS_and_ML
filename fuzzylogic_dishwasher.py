#!/usr/bin/env python
# coding: utf-8

# In[172]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pylab as plt


# In[173]:


#girdiler
b_miktar = np.arange(0,101,1)
b_derece = np.arange(0,101,1)
b_cins = np.arange(0,101,1)


# In[174]:


#üyelik fonksiyonunu oluşturma ve kullanma
miktar_az = fuzz.trimf(b_miktar, [0,0,35])
miktar_ort = fuzz.trimf(b_miktar, [15,50,85])
miktar_cok = fuzz.trimf(b_miktar, [65,100,100])
derece_az = fuzz.trimf(b_derece, [0,0,35])
derece_ort = fuzz.trimf(b_derece, [15,50,85])
derece_cok = fuzz.trimf(b_derece, [65,100,100])
cins_has = fuzz.trimf(b_cins, [0,0,35])
cins_kar = fuzz.trimf(b_cins, [15,50,85])
cins_guc = fuzz.trimf(b_cins, [65,100,100])


# In[175]:


#değer ve üyelik fonksiyonlarının gösterilmesi
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(b_miktar, miktar_az, 'b', linewidth = 1.5, label = "az")
ax0.plot(b_miktar, miktar_ort, 'g', linewidth = 1.5, label = "orta")
ax0.plot(b_miktar, miktar_cok, 'r', linewidth = 1.5, label = "çok")
ax0.set_title("bulaşık miktarı miktar")
ax0.legend()

ax1.plot(b_derece, derece_az, 'b', linewidth = 1.5, label = "düşük")
ax1.plot(b_derece, derece_ort, 'g', linewidth = 1.5, label = "orta")
ax1.plot(b_derece, derece_cok, 'r', linewidth = 1.5, label = "yüksek")
ax1.set_title("Bulaşık derecesi")
ax1.legend()

ax2.plot(b_cins, cins_has, 'b', linewidth= 1.5, label = "hassas")
ax2.plot(b_cins, cins_kar, 'g', linewidth= 1.5, label = "karma")
ax2.plot(b_cins, cins_guc, 'r', linewidth= 1.5, label = "güçlü")
ax2.set_title("kirlilik cinsi")
ax2.legend()

#tepedeki ve sağdaki eksenleri kaldırma
for ax in (ax0, ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
plt.tight_layout()



# In[216]:


#çıktılar
y_zamanı = np.arange(30,161,1)
d_miktarı = np.arange(0,101,1)
s_sicakligi = np.arange(35,71,1)


# In[217]:


#cıkıs fonksiyonunu oluşturma ve kullanma
yıkama_za_ck = fuzz.trimf(y_zamanı, [30,30,60])
yıkama_za_k = fuzz.trimf(y_zamanı, [40,65,90])
yıkama_za_ort = fuzz.trimf(y_zamanı, [70,95,120])
yıkama_za_u = fuzz.trimf(y_zamanı, [100,125,150])
yıkama_za_cu = fuzz.trimf(y_zamanı, [130,160,160])

deterjan_mi_ca = fuzz.trimf(d_miktarı, [17.5,17.5,17.5])
deterjan_mi_a = fuzz.trimf(d_miktarı, [17.5,30,42.5])
deterjan_mi_nor = fuzz.trimf(d_miktarı, [32.5,50,67.5])
deterjan_mi_c = fuzz.trimf(d_miktarı, [57.5,75,92.5])
deterjan_mi_cf = fuzz.trimf(d_miktarı, [82.5,100,100])

su_si_dus = fuzz.trimf(s_sicakligi, [35,35,50])
su_si_nor = fuzz.trimf(s_sicakligi, [37.5,52,67.5])
su_si_yuk = fuzz.trimf(s_sicakligi, [55,71,71])


# In[218]:


#değer ve üyelik fonksiyonlarının gösterilmesi
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(y_zamanı, yıkama_za_ck, 'b', linewidth = 1.5, label = "çok kısa")
ax0.plot(y_zamanı, yıkama_za_k, 'g', linewidth = 1.5, label = "kısa")
ax0.plot(y_zamanı, yıkama_za_ort, 'r', linewidth = 1.5, label = "orta")
ax0.plot(y_zamanı, yıkama_za_u, 'y', linewidth = 1.5, label = "uzun")
ax0.plot(y_zamanı, yıkama_za_cu, 'y', linewidth = 1.5, label = "çok uzun")
ax0.set_title("yıkama zamanı")
ax0.legend()

ax1.plot(d_miktarı, deterjan_mi_ca, 'b', linewidth = 1.5, label = "cok az")
ax1.plot(d_miktarı, deterjan_mi_a, 'b', linewidth = 1.5, label = "az")
ax1.plot(d_miktarı, deterjan_mi_nor, 'y', linewidth = 1.5, label = "normal")
ax1.plot(b_derece, deterjan_mi_c, 'g', linewidth = 1.5, label = "cok")
ax1.plot(b_derece, deterjan_mi_cf, 'r', linewidth = 1.5, label = "cok fazla")
ax1.set_title("deterjan miktarı")
ax1.legend()

ax2.plot(s_sicakligi, su_si_dus, 'b', linewidth= 1.5, label = "düşük")
ax2.plot(s_sicakligi, su_si_nor, 'g', linewidth= 1.5, label = "normal")
ax2.plot(s_sicakligi, su_si_yuk, 'r', linewidth= 1.5, label = "yüksek")
ax2.set_title("su sıacaklığı")
ax2.legend()

#tepedeki ve sağdaki eksenleri kaldırma
for ax in (ax0, ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
plt.tight_layout()


# ♦ Eğer bulaşık miktarı az ve kirlilik derecesi az kirli ve
# bulaşık cinsi hassas (kırılabilir) ise yıkama zamanı çok kısa ve deterjan miktarı çok az ve su sıcaklığı düşük 
# 
# ♦ Eğer bulaşık miktarı az ve kirlilik derecesi çok kirli ve
# bulaşık cinsi karma ise yıkama zamanı orta ve deterjan
# miktarı normal ve su sıcaklığı yüksek 
# 
# ♦ Eğer bulaşık miktarı orta ve kirlilik derecesi orta kirli ve
# bulaşık cinsi güçlü (sağlam, dayanıklı) ise yıkama zamanı
# orta ve deterjan miktarı normal ve su sıcaklığı normal 
# 
# ♦ Eğer bulaşık miktarı çok ve kirlilik derecesi çok kirli ve
# bulaşık cinsi karma ise yıkama zamanı çok uzun ve
# deterjan miktarı çok fazla ve su sıcaklığı yüksek

# In[243]:


miktar_sev_az = fuzz.interp_membership(b_miktar, miktar_az,22)
miktar_sev_ort = fuzz.interp_membership(b_miktar, miktar_ort, 22)
miktar_sev_cok = fuzz.interp_membership(b_miktar, miktar_cok, 22)

derece_sev_az = fuzz.interp_membership(b_derece, derece_az,70.4)
derece_sev_ort = fuzz.interp_membership(b_derece, derece_ort,70.4)
derece_sev_cok = fuzz.interp_membership(b_derece, derece_cok,70.4)

cins_sev_has = fuzz.interp_membership(b_cins, cins_has, 50)
cins_sev_karma = fuzz.interp_membership(b_cins, cins_kar, 50)
cins_sev_guc = fuzz.interp_membership(b_cins, cins_guc, 50)


# Gerekli Kurallar

# In[249]:


kural1 = np.fmin(cins_sev_has,np.fmin(miktar_sev_az,derece_sev_az))
yıkama_zamanı_ck = np.fmax(kural1, yıkama_za_ck)
deterjan_miktarı_ca = np.fmax(kural1, deterjan_mi_ca)
su_sicakligi_dus = np.fmax(kural1, su_si_dus)


# In[250]:


kural2 = np.fmin(cins_sev_karma, np.fmin(miktar_sev_az, derece_sev_cok))
yıkama_zamanı_ort = np.fmax(kural2,yıkama_za_ort)
deterjan_miktarı_nor = np.fmax(kural2, deterjan_mi_nor)
su_sicakligi_yuk = np.fmax(kural2, su_si_yuk)


# In[251]:


kural3 = np.fmin(cins_sev_guc, np.fmin(miktar_sev_ort, derece_sev_ort))
yıkama_zamanı_ort = np.fmax(kural2,yıkama_za_ort)
deterjan_miktarı_nor = np.fmax(kural2, deterjan_mi_nor)
su_sicakligi_nor = np.fmax(kural2, su_si_nor)


# In[262]:


kural2 = np.fmin(cins_sev_karma, np.fmin(miktar_sev_cok, derece_sev_cok))
yıkama_zamanı_cu = np.fmax(kural2,yıkama_za_cu)
deterjan_miktarı_cf = np.fmax(kural2, deterjan_mi_cf)
su_sicakligi_yuk = np.fmax(kural2, su_si_yuk)
yıkama0 = np.zeros_like(y_zamanı)
deterjan0 = np.zeros_like(d_miktarı)
su0 = np.zeros_like(s_sicakligi)


# In[263]:


kümelemeYıkama = np.fmax(np.fmax(yıkama_zamanı_ck, yıkama_zamanı_cu),yıkama_zamanı_ort)
kümelemeDeterjan = np.fmax(deterjan_miktarı_ca, np.fmax(deterjan_miktarı_nor, deterjan_miktarı_cf))
kümelemeSuSıcaklıgı = np.fmax(su_sicakligi_dus, np.fmax(su_sicakligi_nor, su_sicakligi_yuk))


# In[264]:


#sonuçları bulanıklaştırma
yıkama = fuzz.defuzz(y_zamanı, kümelemeYıkama, 'centroid')
yıkama_aktivasyon = fuzz.interp_membership(y_zamanı, kümelemeYıkama, yıkama)#grafik için

#sonuçları bulanıklaştırma
deterjan = fuzz.defuzz(d_miktarı, kümelemeDeterjan, 'centroid')
deterjan_aktivasyon = fuzz.interp_membership(d_miktarı, kümelemeDeterjan, deterjan)#grafik için

#sonuçları bulanıklaştırma
su = fuzz.defuzz(s_sicakligi, kümelemeSuSıcaklıgı, 'centroid')
su_aktivasyon = fuzz.interp_membership(s_sicakligi, kümelemeSuSıcaklıgı, su)#grafik için


# In[265]:


#değer ve üyelik fonksiyonlarının gösterilmesi
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(y_zamanı, yıkama_za_ck, 'b', linewidth = 1.5, label = "--")
ax0.plot(y_zamanı, yıkama_za_ort, 'g', linewidth = 1.5, label = "--")
ax0.plot(y_zamanı, yıkama_za_cu, 'r', linewidth = 1.5, label = "--")
ax0.fill_between(y_zamanı, yıkama0, kümelemeYıkama, facecolor= 'Orange', alpha = 0.7)
ax0.plot([yıkama, yıkama], [0, yıkama_aktivasyon], 'k', linewidth= 1.5, alpha = 0.7)
ax0.set_title("Kümelenmiş üyelik ve sonuç")
ax0.legend()

#tepedeki ve sağdaki eksenleri kaldırma
for ax in (ax0, ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
plt.tight_layout()


# In[266]:


#değer ve üyelik fonksiyonlarının gösterilmesi
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(d_miktarı, deterjan_miktarı_ca, 'b', linewidth = 1.5, label = "--")
ax0.plot(d_miktarı, deterjan_miktarı_nor, 'g', linewidth = 1.5, label = "--")
ax0.plot(d_miktarı, deterjan_miktarı_cf, 'r', linewidth = 1.5, label = "--")
ax0.fill_between(d_miktarı, deterjan0, kümelemeDeterjan, facecolor= 'Orange', alpha = 0.7)
ax0.plot([deterjan, deterjan], [0, deterjan_aktivasyon], 'k', linewidth= 1.5, alpha = 0.7)
ax0.set_title("Kümelenmiş üyelik ve sonuç")
ax0.legend()

#tepedeki ve sağdaki eksenleri kaldırma
for ax in (ax0, ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
plt.tight_layout()


# In[267]:


#değer ve üyelik fonksiyonlarının gösterilmesi
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(s_sicakligi, su_sicakligi_dus, 'b', linewidth = 1.5, label = "--")
ax0.plot(s_sicakligi, su_sicakligi_nor, 'g', linewidth = 1.5, label = "--")
ax0.plot(s_sicakligi, su_sicakligi_yuk, 'r', linewidth = 1.5, label = "--")
ax0.fill_between(s_sicakligi, su0, kümelemeSuSıcaklıgı, facecolor= 'Orange', alpha = 0.7)
ax0.plot([su, su], [0, su_aktivasyon], 'k', linewidth= 1.5, alpha = 0.7)
ax0.set_title("Kümelenmiş üyelik ve sonuç")
ax0.legend()

#tepedeki ve sağdaki eksenleri kaldırma
for ax in (ax0, ax1, ax2):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
plt.tight_layout()


# In[ ]:




