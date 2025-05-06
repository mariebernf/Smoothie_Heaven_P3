from django.shortcuts import render

smoothies = [
  {

    'author': 'marie',
    'name': 'berry blitz',
    'description': 'refreshing berry smoothie',
    'ingredients': 'blueberries, stawberries, rasberries,'
    ' coconut water, honey',
    'date_posted': 'May 01, 2025',
},
{
    'author': 'marie',
    'name': 'banana bononza',
    'description': 'delicious banana smoothie',
    'ingredients': 'bananas, almond milk, peanut butter, honey',
    'date_posted': 'May 05, 2025',
  },
{
    'author': 'marie',
    'name': 'green glow',
    'description': 'nutritous green smoothie',
    'ingredients': 'kale, spinach, greek yogurt, pineapple',
    'date_posted': 'May 07, 2025',
  }
]

# Create your views here.
def home(request):
    context = {
        'smoothies': smoothies
    }
    return render(request, 'smoothies/home.html', context)


def about(request):
    return render(request, 'smoothies/about.html')
