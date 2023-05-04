import os
from functools import cache
from typing import Dict

import requests

from .schemas import *


class API:
    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()
        self._set_headers()
        self._set_hooks()

    def _set_headers(self):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        self.session.headers = headers

    def _set_hooks(self):
        self.session.hooks = {
            "response": lambda r, *args, **kwargs: r.raise_for_status()
        }

    @cache
    def get_me(self) -> UserProfile:
        """Get the current user profile using LinkedIn Apis

        Usage:

        The reply looks like

        ```
        {
            "localizedLastName": "Zuppichini",
            "profilePicture": {
                "displayImage": "urn:li:digitalmediaAsset:C4D03AQFpbPOqpBlh_A"
            },
            "firstName": {
                "localized": {
                    "it_IT": "Francesco Saverio"
                },
                "preferredLocale": {
                    "country": "IT",
                    "language": "it"
                }
            },
            "lastName": {
                "localized": {
                    "it_IT": "Zuppichini"
                },
                "preferredLocale": {
                    "country": "IT",
                    "language": "it"
                }
            },
            "id": "<YOUR_ID>",
            "localizedFirstName": "Francesco Saverio"
        }
        ```

        Returns:
            UserProfile: A dictionary containing the request reply
        """
        return self.session.get("https://api.linkedin.com/v2/me").json()

    def create_post(self, body: Dict) -> CreatePostResponse:
        """Create a post using LinkedIn Apis, keep in mind this is just a wrapper around the official APIs, I suggest you to use `User.create_post` that offers a better interface.

        Unfortunately, due to linkedIn Apis required keys, I cannot create a TypeDict for it since they have '.' in their names

        The body should follow the [official doc](https://learn.microsoft.com/en-gb/linkedin/consumer/integrations/self-serve/share-on-linkedin#request-body-schema)

        For a post **without media**:

        ```json
        {
            "author": "urn:li:person:<YOUR_USER_ID>",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": "Testing APIs with url https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" | "CONNECTIONS"
            }
        }
        ```

        For a post **with media**


        ```json
        {
            "author": "urn:li:person:<YOUR_USER_ID>",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": "Testing APIs with Image Upload"
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "My Media Description"
                            },
                            "media": "urn:li:digitalmediaAsset:D4E22AQFaLDfRCXr8lg",
                            "title": {
                                "text": "Grogu!!!"
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        ```

        To get your user id, you can call `.get_me()['id]`

        Args:
            body (Dict): The request's body

        Returns:
            CreatePostResponse: A dictionary containing the requests reply
        """
        return self.session.post("https://api.linkedin.com/v2/ugcPosts", json=body).json()

    def register_upload(self, body: RegisterUploadBody) -> RegisterUploadResponse:
        return self.session.post(
            "https://api.linkedin.com/v2/assets?action=registerUpload", json=body
        ).json()

    def upload_image(self, file_path: str, upload_url: str) -> requests.Response:
        with open(file_path, "rb") as file:
            response = requests.put(
                upload_url, data=file, headers={"Authorization": f"Bearer {self.token}"}
            )
        return response

    @classmethod
    def from_env(cls):
        try:
            token = os.environ["LINKEDIN_TOKEN"]
            return cls(token)
        except KeyError:
            raise KeyError("`LINKEDIN_TOKEN` not found in your enviroment variables. Follow this tutorial (https://youtu.be/YJoof1kX_kQ and run `export LINKEDIN_TOKEN=<YOUR_TOKEN> in your current shell")
