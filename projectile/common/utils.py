from django.utils.text import slugify

def slug_generator(value, models):
    repeat_count = models.objects.filter(name=value).count()
    if repeat_count:
        return slugify(value + '.' + str(repeat_count), allow_unicode=True)
    else:
        return slugify(value, allow_unicode=True)
        

def get_website_title(url):
    import requests
    import bs4
    response = requests.get(url)
    html = bs4.BeautifulSoup(response.text)
    return html.title.text
