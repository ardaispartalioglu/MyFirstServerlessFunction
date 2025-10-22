#  My First Serverless Function+  Cloud Link Generator

Bu depo, AWS Lambda ve API Gateway kullanarak basit bir URL kısaltma API'si örneği sağlar. README teslim için sadeleştirilmiş ve hazır hâle getirilmiştir.

## Özellikler
- HTTP tetikleyicisi (API Gateway)
- `longUrl` sorgu parametresini işleyerek JSON yanıt üretme
- CloudWatch log kaydı

## Platform
- AWS Lambda (Python 3.11)
- AWS API Gateway (HTTP API)

## Hızlı kullanım
- Örnek endpoint: `https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction`
- Örnek istek: `GET /?longUrl=https://example.com`

## Örnek JSON yanıt
```
{
  "original_url": "https://example.com",
  "short_id": "e91kCx",
  "short_url_example": "https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction/e91kCx",
  "message": "URL successfully simulated and shortened on the cloud!"
}
```

## Dağıtım (özet)
1. `lambda_handler.py` dosyasını Lambda'ya yükleyin veya VS Code AWS Toolkit ile deploy edin.
2. Lambda yürütme rolü için `AWSLambdaBasicExecutionRole` yeterlidir (CloudWatch yazma izni).
3. API Gateway (HTTP API) üzerinden Lambda'ya tetikleyici ekleyin.

## Test ve kanıt
- Başarılı çağrı örneği: `GET [API_ENDPOINT]?longUrl=https://example.com`
- Kendi ekran görüntülerinizi `screenshots/` klasörüne koyabilirsiniz (isteğe bağlı).

## Değerlendirme
- Neden serverless: Sunucu yönetimi gerektirmez, ölçeklenebilir ve maliyet etkindir.
- Karşılaşılan zorluklar: AWS servisleri arası bağlantı ve izinlerin doğru yapılandırılması.
- Uygulama alanları: Küçük API servisleri, webhooklar ve event-driven işlemler.

## Ek opsiyonlar
- README'nin farklı formatta dışa aktarılmasını sağlayabilirim (PDF/HTML).
- Basit `pytest` testi ve GitHub Actions CI ekleyebilirim.
- AWS SAM `template.yaml` oluşturarak otomatik deploy desteği ekleyebilirim.

Bu README teslim için uygundur.
