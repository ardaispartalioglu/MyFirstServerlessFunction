import json
import logging
import random
import string

# CloudWatch loglarını yapılandır (Configure CloudWatch logging)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Kısa ID oluşturma fonksiyonu (Function to generate a random short ID)
def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def lambda_handler(event, context):
    
    # API Gateway URL'si (API Endpoint URL)
    # Bu, çıktıdaki short_url_example alanı için kullanılır.
    api_endpoint = "https://ng38wk72se.execute-api.eu-north-1.amazonaws.com/default/MyFirstServerlessFunction"
    
    # 1. HTTP tetikleyicisinden sorgu parametrelerini al (Get query parameters)
    query_params = event.get('queryStringParameters')
    
    logger.info(f"Incoming Event: {event}")
    
    # Hata kontrolü: 'longUrl' parametresi zorunludur (Error check: 'longUrl' parameter is required)
    if not query_params or 'longUrl' not in query_params:
        logger.warning("Missing 'longUrl' parameter.")
        return {
            'statusCode': 400,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({
                "error": "Missing 'longUrl' parameter. Please provide the URL to shorten."
            })
        }
        
    long_url = query_params['longUrl']
    
    # --- Fonksiyon Mantığı: Kısa ID Oluşturma --- (Function Logic: Generate Short ID)
    short_id = generate_short_id()
    short_url = f"{api_endpoint}/{short_id}" 
    
    logger.info(f"URL Shortened: {long_url} -> {short_id}")
    
    # JSON cevabını oluştur (Create the JSON response)
    response_body = {
        "original_url": long_url,
        "short_id": short_id,
        "short_url_example": short_url,
        "message": "URL successfully simulated and shortened on the cloud!"
    }
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(response_body)
    }
