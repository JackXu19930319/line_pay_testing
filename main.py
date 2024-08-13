# coding=UTF-8
import datetime
import json
import os
from flask_cors import CORS
from flask import Flask, jsonify, request, Response, redirect
import uuid
import requests
from linepay import LinePayApi as api

app = Flask(__name__)

# 从环境变量中获取 LINE Pay 的配置信息
LINE_PAY_CHANNEL_ID = os.environ.get('LINE_PAY_CHANNEL_ID', '2006027897')
LINE_PAY_CHANNEL_SECRET = os.environ.get('LINE_PAY_CHANNEL_SECRET', '54fa80b894261a3c80726c2022fe4554')
# LINE_PAY_MERCHANT_DEVICE_PROFILE_ID = os.environ.get('LINE_PAY_MERCHANT_DEVICE_PROFILE_ID')
# LINE_PAY_MERCHANT_DEVICE_TYPE = os.environ.get('LINE_PAY_MERCHANT_DEVICE_TYPE')
LINE_PAY_API_URL = '"https://sandbox-api-pay.line.me/v2/payments/request'

CORS(app)


# 发起支付请求
@app.route('/linepay/payment', methods=['POST'])
def linepay_payment():
    # 获取支付请求中的数据
    data = request.json
    # one_time_key = data['oneTimeKey']
    # amount = data['amount']
    # currency = data['currency']
    # order_id = data['orderId']
    # product_name = data['productName']

    # 设置请求头信息
    headers = {
        'X-LINE-ChannelId': LINE_PAY_CHANNEL_ID,
        'X-LINE-ChannelSecret': LINE_PAY_CHANNEL_SECRET,
        # 'X-LINE-MerchantDeviceProfileId': LINE_PAY_MERCHANT_DEVICE_PROFILE_ID,
        # 'X-LINE-MerchantDeviceType': LINE_PAY_MERCHANT_DEVICE_TYPE,
        'Content-Type': 'application/json'
    }

    # 设置请求体
    payload = {
        "amount": 90,
        "productName": "iBot",
        "productImageUrl": "https://xxxxx/image.png",
        "confirmUrl": "https://xxxxx/api/linebot/pay/confirm",
        "orderId": str(uuid.uuid4()),  # 訂單編號，不能重複
        "currency": "TWD"
    }

    # 发起请求到 LINE Pay 的 API
    response = requests.post(
        "https://sandbox-api-pay.line.me/v2/payments/request",
        headers=headers,
        data=json.dumps(payload),
        timeout=10
    )



    # 返回 API 的响应内容
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Payment request failed', 'details': response.json()}), response.status_code

@app.route('/linepay/confirm', methods=['POST'])
def pay_confirm():
    data = request.json
    transaction_id ="2024081302175916410"
    amount = 90
    currency = "TWD"
    # order_id = data['info']['orderId']

    headers = {
        'X-LINE-ChannelId': LINE_PAY_CHANNEL_ID,
        'X-LINE-ChannelSecret': LINE_PAY_CHANNEL_SECRET,
        'Content-Type': 'application/json'
    }

    payload = {
        "amount": amount,
        "currency": currency
    }

    response = requests.post(
        f"https://sandbox-api-pay.line.me/v2/payments/{transaction_id}/confirm",
        headers=headers,
        data=json.dumps(payload),
        timeout=10
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Payment confirm failed', 'details': response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=False)
