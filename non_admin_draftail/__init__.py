import django


if django.VERSION < (3, 2):
      default_app_config = "non_admin_draftail.apps.NonAdminDraftailConfig"
