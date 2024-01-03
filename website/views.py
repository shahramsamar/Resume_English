from django.shortcuts import render



def index_view(request):
    context ={'name':'shahram', 'lastname':'samar','number':'+98 917 788 3411','email':'shahramsamar2010@gmail.com',
              'entertainment':'Travel, Mountaineering,watching a movie','location':'Shiraz, Iran','jobposition':'Backend Developer',
              'aboutme':"I'm Shahram Samar. I am a junior software engineering. I have been working as a junior Python Developer.Strong engineering professional with a Bachelor's Degree focused on Computer Software Engineering from Azad Islamic University of Shiraz Iran.I'm always open to take up new challenges, helping me to improve myself and making me move forward."}
    return render(request, 'website/index.html', context)
