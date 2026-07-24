from governance.email_service import send_email


response = send_email(

    to_email="exploratory.welltarget@gmail.com",

    to_name="Patricia",

    subject="WellTarget Governance Test",

    html_content="""

    <h1>Congratulations!</h1>

    <p>

    Your Brevo API integration is working.

    </p>

    <p>

    Exploratory Well Target Governance Platform

    </p>

    """,

)

print(response)