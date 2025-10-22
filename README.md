# 🚀 My First Serverless Function+ - Cloud Link Generator

## 🎯 Proje Amacı ve Özellikleri

Bu proje, AWS Lambda ve API Gateway kullanarak basit, sunucusuz bir **URL Kısaltma API'si** (Serverless URL Shortener) geliştirmeyi amaçlamaktadır.

| Ödev Gereksinimi | Durum | Açıklama |
| :--- | :--- | :--- |
| **HTTP Tetikleyicisi** | ✅ Tamamlandı | AWS API Gateway üzerinden HTTP isteği ile tetiklenir. |
| **Parametre İşleme (API)** | ✅ Tamamlandı | URL'den `longUrl` parametresini alır, rastgele bir `short_id` oluşturur ve **JSON** döndürür. |
| **CloudWatch Logları** | ✅ Aktif | Fonksiyonun tüm çalışma çıktıları ve hata logları CloudWatch'a yazılmaktadır. |
| **IAM Yetkileri** | ✅ Minimal (Least Privilege) | Lambda rolü, sadece **CloudWatch Logs'a yazma** izni ile sınırlandırılmıştır. |

## ⚙️ Cloud Yapılandırması ve Dağıtım

**Platform:** AWS Lambda (Python 3.11) + AWS API Gateway

**API Endpoint URL:** `https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction`

### Nasıl Dağıtılır (Deployment Steps)

1.  Bu depodaki `lambda_handler.py` kodu, AWS Konsolu üzerinden Lambda'ya yüklenir veya VS Code **AWS Toolkit** uzantısı ile deploy edilir.
2.  Lambda yürütme rolü otomatik olarak oluşturulur ve `AWSLambdaBasicExecutionRole` politikası ile minimal yetkilendirilir.
3.  API Gateway (HTTP API türünde) Lambda'ya tetikleyici olarak eklenir ve yukarıdaki endpoint oluşturulur.

---

## 🧪 Test Senaryosu ve Çalışma Çıktıları

Aşağıdaki çıktı, projenin iki ana gerekliliğini kanıtlar.

### 1. Başarılı Fonksiyon Çağrısı (URL Kısaltma)

* **İstek URL'si:**
  `[API_ENDPOINT]?longUrl=https://www.linkedin.com/in/yourprofile/`

* **Çıktı Kanıtı (Tarayıcı/Terminal Ekran Görüntüsü):**
  [screenshots/1_successful_output.png](screenshots/1_successful_output.png)

* **Örnek Çıktı:**
```
{
  "original_url": "[https://www.linkedin.com/in/yourprofile/](https://www.linkedin.com/in/yourprofile/)",
  "short_id": "e91kCx",
  "short_url_example": "[https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction/e91kCx](https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction/e91kCx)",
  "message": "URL successfully simulated and shortened on the cloud!"
}
```

### 2. CloudWatch Log Kayıtları Kanıtı

  * **Kanıt:** [screenshots/2_cloudwatch_logs.png](https://www.google.com/search?q=screenshots/2_cloudwatch_logs.png)

-----

## 👤 Değerlendirme (Ödev Sorularının Cevapları)

### 1. Neden serverless tercih ettin?

Sunucu yönetimi gerektirmediği için geliştirme sürecini hızlandırıyor. Otomatik ölçeklenebilir ve kullandıkça ödeme modeli sayesinde maliyet avantajı sağlıyor.

### 2. Karşılaştığın en büyük zorluk neydi?

Karşılaştığım en büyük zorluk başlangıçta AWS servislerinin birbiriyle bağlantısını kurmaktı. Lambda, API Gateway ve IAM izinleri ilk başta karmaşık görünüyordu ama deneme-yanılma ve dökümantasyona bakarak çözdüm.

### 3. Bu yaklaşım hangi gerçek dünya senaryolarında işe yarar?

Küçük API servisleri, webhook işlemleri, otomatik mesaj/bildirim sistemleri ve event-driven (olay tabanlı) uygulamalarda yaygın olarak kullanılır. URL kısaltıcı ve resim işleme gibi mikroservisler için idealdir.


