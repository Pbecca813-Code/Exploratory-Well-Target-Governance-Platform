from django.db import migrations


def create_demo_users(apps, schema_editor):
    User = apps.get_model("auth", "User")

    # Create Administrator
    if not User.objects.filter(username="admin").exists():

        admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="TestPassword2026!"
        )

        admin.first_name = "System"
        admin.last_name = "Administrator"
        admin.save()

    # Create Test User
    if not User.objects.filter(username="testuser01").exists():

        user = User.objects.create_user(
            username="testuser01",
            email="testuser01@gmail.com",
            password="TestPassword2026!"
        )

        user.first_name = "Test"
        user.last_name = "User"
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("governance", "0003_employeeprofile"),
    ]

    operations = [
        migrations.RunPython(create_demo_users),
    ]