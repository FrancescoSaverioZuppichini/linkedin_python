import requests
from linkedin_python.api import API
from linkedin_python.schemas import *
from requests import Response

class MockAPI(API):
    def get_me(self) -> UserProfile:
        return {
            "localizedLastName": "Kenobi",
            "profilePicture": {
                "displayImage": "urn:li:digitalmediaAsset:foo"
            },
            "firstName": {
                "localized": {
                    "it_IT": "Obi Wan"
                },
                "preferredLocale": {
                    "country": "IT",
                    "language": "it"
                }
            },
            "lastName": {
                "localized": {
                    "it_IT": "Kenobi"
                },
                "preferredLocale": {
                    "country": "IT",
                    "language": "it"
                }
            },
            "id": "foo123",
            "localizedFirstName": "Obi Wan"
        }
    
    def create_post(self, body: Dict) -> CreatePostResponse:
        return {
            "id": "urn:li:share:foo"
        }
 
    def register_upload(self, body: RegisterUploadBody) -> RegisterUploadRequest:
        return {
            "value": {
                "mediaArtifact": "urn:li:digitalmediaMediaArtifact:(urn:li:digitalmediaAsset:foo,urn:li:digitalmediaMediaArtifactClass:uploaded-image)",
                "uploadMechanism": {
                    "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest": {
                        "uploadUrl": "https://api.linkedin.com/mediaUpload/foo",
                        "headers": {
                            "media-type-family": "STILLIMAGE"
                        }
                    }
                },
                "asset": "urn:li:digitalmediaAsset:foo",
                "assetRealTimeTopic": "urn:li-realtime:digitalmediaAssetUpdatesTopic:urn:li:digitalmediaAsset:D4E22AQHF4Z7r16iVyw"
            }
        }

    def upload_image(self, file_path: str, upload_url: str) -> Response:
        res = Response()
        res.status_code = 2001
        return res
    
    @classmethod
    def from_env(cls):
        return cls()