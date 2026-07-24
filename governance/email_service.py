import os

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from dotenv import load_dotenv

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


configuration = sib_api_v3_sdk.Configuration()

configuration.api_key["api-key"] = os.getenv("BREVO_API_KEY")


api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)


def send_email(
    to_email,
    to_name,
    subject,
    html_content,
):

    sender = {

        "name": "Exploratory WellTarget",

        "email": "exploratory.welltarget@gmail.com",

    }

    receiver = [

        {

            "email": to_email,

            "name": to_name,

        }

    ]

    email = sib_api_v3_sdk.SendSmtpEmail(

        sender=sender,

        to=receiver,

        subject=subject,

        html_content=html_content,

    )

    try:

        response = api_instance.send_transac_email(email)

        return response

    except ApiException as e:

        print(e)

        return None