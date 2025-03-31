# Business information, categories, social media

from .models import Category, BusinessInformation


def categories(request):
    context = {
        'categories': Category.objects.filter(active=True),
    }

    return context


def business_information(request):
    business = BusinessInformation.objects.first()
    context = {
        'business': business,
        # Default:  business.socialmedia_set.all()
        'social_media': business.social_media.all() if business else [],  # type: ignore
    }

    return context
