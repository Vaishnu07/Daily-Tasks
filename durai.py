from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True)




import boto3
bucket name = "athiva-training"
s3 = boto3.client('s3')
bucket_response = s3.list_buckets()
for bucket in bucket_responce["Buckets"]
    print(bucket)
