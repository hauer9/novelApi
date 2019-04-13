from qiniu import Auth


class Storage(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

    def get_upload_token(self):
        q = Auth(self.access_key, self.secret_key)
        bucket_name = self.bucket_name
        upload_token = q.upload_token(bucket_name, None, 3600)
        return upload_token
