from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .ai_resume_analyzer import ResumeAnalyzer
import os

@csrf_exempt
def analyze_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')
        job_description = request.POST.get('job_description')

        if not resume_file or not job_description:
            return JsonResponse({'error': 'Resume file and job description are required.'}, status=400)

        # Save the resume file
        fs = FileSystemStorage(location='data/')
        filename = fs.save(resume_file.name, resume_file)
        resume_path = os.path.join('data', filename)

        # Analyze the resume
        analyzer = ResumeAnalyzer()
        try:
            results = analyzer.analyze_documents(resume_path, job_description)
            return JsonResponse({'analysis': results})  # Wrap the results in JsonResponse
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405) 