from django.shortcuts import render
from django.http import HttpResponse

import instaloader


def form(request):

    if request.method == 'POST':
        palavra = request.POST['palavra']

        tipo = request.POST['seletor']

        bot = instaloader.Instaloader()

        trending = instaloader.TopSearchResults(bot.context, palavra)

        if tipo == 'hashtag':
            list_hashtags = trending.get_hashtags()

            hashtags = []

            for hashtag in list_hashtags:
                hashtags.append(hashtag.name)

            return render(request, 'hashtags.html', {'hashtags': hashtags})
        else:
            list_profiles = trending.get_profiles()

            profiles = []

            for profile in list_profiles:
                profiles.append(profile.username)

            return render(request, 'hashtags.html', {'profiles': profiles})
    else:
        return render(request, 'form.html')

# Create your views here.
