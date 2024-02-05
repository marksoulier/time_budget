import openai
from django.http import JsonResponse

@csrf_exempt
def chat_with_openai(request):
    # Load your API key from settings or environment variable
    api_key = "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"  # Preferably use an environment variable here

    # Initialize OpenAI client
    client = openai.OpenAI(api_key=api_key)

    # Get user input from request (handle GET or POST as needed)
    user_input = request.GET.get('input', '')  # or request.POST.get('input')

    # Create the completion
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are ATA Mentor (All things Aviation Mentor) and you are here to help students with their aviation related questions."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract the response
    response_content = completion.choices[0].message.content

    # Return the response as JSON
    return JsonResponse({'response': response_content})
