from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, send_file, jsonify
import b2sdk.v2

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

def accound_credentials():
    info = b2sdk.v2.InMemoryAccountInfo()
    api = b2sdk.v2.B2Api(info)
    appKeyId = os.getenv("ACCOUNT_ID")
    appKey = os.getenv("APPLICATION_KEY")
    api.authorize_account("production", appKeyId, appKey)
    return api

@app.route('/')
def index():
    return render_template('upload.html')

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filePath = file.filename
    api = accound_credentials()
    bucket = api.get_bucket_by_name(os.getenv("BUCKET_NAME"))
    bucket.upload_bytes(file.read(), filePath)
    return f"Archivo {filePath} subido a Backblaze exitosamente"


@app.route("/list_files")
def list_files():
    api = accound_credentials()
    bucket = api.get_bucket_by_name(os.getenv("BUCKET_NAME"))
    files = list(bucket.ls())

    file_info = []
    for file, _ in files:
        file_info.append({
            'name': file.file_name,
            'size': file.size
        })

    return render_template('list_files.html', files=file_info)


@app.route("/download/<file_name>")
def download_file(file_name):
    try:
        api = accound_credentials()
        bucket = api.get_bucket_by_name(os.getenv("BUCKET_NAME"))
        local_file_name = f"/tmp/{file_name}"
        downloaded_file = bucket.download_file_by_name(file_name)
        downloaded_file.save_to(local_file_name)
        return send_file(local_file_name, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)