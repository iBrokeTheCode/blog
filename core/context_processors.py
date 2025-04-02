# Business information, categories, social media

from .models import Category, BusinessInformation, Post


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


def grouped_dates(request):
    dates = Post.objects.dates(
        field_name='created',
        kind='month',
        order='DESC'
    ).distinct()
    month_year_list = []

    for d in dates:
        month_year_list.append({
            'year': d.year,
            'month': d.month,
            'month_name': d.strftime('%B')
        })

    context = {
        'dates': month_year_list,
    }

    return context
