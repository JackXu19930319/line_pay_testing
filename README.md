# line_pay_testing

## 1. line_pay_request_response
```
    line_pay_response =  
     {
            "info": {
                "paymentAccessToken": "601463202015",
                "paymentUrl": {
                    "app": "line://pay/payment/MlBiOXRjQzI3NjlBdFF0UGdKTUJ5ME1zZWNLK1dZQ2R6NTU2THh5RkJqNGdob0FhaUpaSTdvdkpTa0NrRWk5eQ",
                    "web": "https://sandbox-web-pay.line.me/web/payment/wait?transactionReserveId=MlBiOXRjQzI3NjlBdFF0UGdKTUJ5ME1zZWNLK1dZQ2R6NTU2THh5RkJqNGdob0FhaUpaSTdvdkpTa0NrRWk5eQ"
                },
                "transactionId": 2024081302175916410
            },
            "returnCode": "0000",
            "returnMessage": "Success."
        } 
```

## 2. line_pay_confirm_response
```
{
    "info": {
        "orderId": "92a13de1-e2b5-4a8a-a66a-02c0ad53c8b8",
        "payInfo": [
            {
                "amount": 90,
                "maskedCreditCardNumber": "************1111",
                "method": "CREDIT_CARD"
            }
        ],
        "transactionId": 2024081302175916410
    },
    "returnCode": "0000",
    "returnMessage": "Success."
}
```