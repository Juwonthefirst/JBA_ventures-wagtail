from .base import *
import os

DEBUG = False

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
MEDIA_URL = None
MEDIA_ROOT = None
STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
}
DATABASES["default"]["OPTIONS"] = {
    "sslmode": "require",
}
AWS_ACCESS_KEY_ID = os.getenv("STORAGE_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("STORAGE_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("STORAGE_REGION_ENDPOINT")
AWS_S3_FILE_OVERWRITE = True
AWS_S3_REGION_NAME = os.getenv("STORAGE_REGION")
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
AWS_S3_USE_SSL = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"

DEBUG = False

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

ALLOWED_HOSTS = [
    os.getenv("HOST_NAME"),
]

try:
    from .local import *
except ImportError:
    pass
