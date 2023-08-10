from .models import District

def district_dropdown(request):
    district=District.objects.all()
    district_link= [{'name': district.name,'link':f'https://en.wikipedia.org/wiki/{district.name}'}for district in district]
    return {'district_links':district_link}