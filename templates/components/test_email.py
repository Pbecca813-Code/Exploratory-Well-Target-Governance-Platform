from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = "Send a test email through the configured email backend."

    def handle(self, *args, **options):

        self.stdout.write("Testing email configuration...")
        self.stdout.write(f"Host: {settings.EMAIL_HOST}")
        self.stdout.write(f"Port: {settings.EMAIL_PORT}")

        try:
            result = send_mail(
                subject="WellTarget Test Email",
                message="This is a test email from the Exploratory Well Target Governance Platform.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["exploratory.welltarget@gmail.com"],
                fail_silently=False,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Email sent successfully. Result: {result}"
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(str(e))
            )
            raise