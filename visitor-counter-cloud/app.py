import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_SERVER_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB,
    decode_responses=True, socket_connect_timeout=2
)

@app.get("/")
def index():
    try:
        count = redis_client.incr("visitor_count")
        return f"""
        <!doctype html><html><head><title>Cloud Visitor Counter</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>body{{font-family:Arial;text-align:center;margin:10vh auto;background:#f3f6fb}}
        .card{{background:white;padding:40px;border-radius:18px;max-width:520px;margin:auto;
        box-shadow:0 8px 30px #0001}}h1{{color:#164e9b}}strong{{font-size:48px;color:#087f5b}}</style>
        </head><body><div class="card"><h1>Visitor Counter</h1>
        <p>Welcome! This application is deployed with Flask, Redis and Kubernetes.</p>
        <strong>{count}</strong><p>Total visits</p>
        <small>Refresh the page to increment the counter.</small></div></body></html>
        """
    except redis.RedisError:
        return "Redis is temporarily unavailable. Please try again.", 503

@app.get("/health")
def health():
    return "OK", 200

@app.get("/api/count")
def count():
    try:
        value = int(redis_client.get("visitor_count") or 0)
        return jsonify(visitor_count=value)
    except redis.RedisError:
        return jsonify(error="Redis unavailable"), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
