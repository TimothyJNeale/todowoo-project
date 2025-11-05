from django.conf import settings

def protected_mode(request):
    """
    Context processor to make PROTECTED_MODE setting available in all templates
    """
    return {
        'PROTECTED_MODE': settings.PROTECTED_MODE
    }
