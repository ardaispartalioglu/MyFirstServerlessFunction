# My First Serverless Function+ | Cloud Link Generator

Bu depo, AWS Lambda ve API Gateway kullanarak basit bir URL kısaltma API'si (Serverless URL Shortener) örneği sağlar.

##  Proje Özellikleri ve Gereklilikleri

| Gereksinim | Durum | Açıklama |
| :--- | :--- | :--- |
| **HTTP Tetikleyicisi** |  | AWS API Gateway (HTTP API) üzerinden dışarıdan tetiklenir. |
| **Parametre İşleme** |  | `longUrl` sorgu parametresini işleyerek JSON yanıt üretir. |
| **CloudWatch Log Kaydı** |  | Fonksiyonun çalışma logları aktiftir. |
| **IAM Yetkileri** |  | Yürütme rolü için **`AWSLambdaBasicExecutionRole`** yeterlidir (Least Privilege). |

---

##  Platform ve Hızlı Kullanım

* **Platform:** AWS Lambda (Python 3.11) + AWS API Gateway (HTTP API)
* **Fonksiyon Kodu:** `lambda_handler.py`

**API Uç Noktası (Endpoint):**
`https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction`

**Örnek İstek:**
`GET [API_ENDPOINT]?longUrl=https://example.com/long/url`

### Örnek JSON Yanıt

```json
{
  "original_url": "https://example.com/long/url",
  "short_id": "e91kCx",
  "short_url_example": "https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction/e91kCx",
  "message": "URL successfully simulated and shortened on the cloud!"
}
```

