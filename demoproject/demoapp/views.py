from django.shortcuts import render

#create your views here
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from docxtpl import DocxTemplate
from datetime import datetime
import json
from docx2pdf import convert
import subprocess
from django.http import JsonResponse


def home(request):
    return HttpResponse("Welcome to the home page.")

@csrf_exempt
def submit_form(request):
    if request.method == 'OPTIONS':
        return JsonResponse({'message': 'OPTIONS request allowed'}, status=200)
    elif request.method == 'POST':
        # parse the JSON data from the request
        data = json.loads(request.body)

        # extract form data
        risk = data.get('risk')
        opportunity = data.get('opportunity')
        climate = data.get('climate')
        esg = data.get('esg')
        investment = data.get('investment')
        task = data.get('task')
        publi = data.get('publi')
        republic = data.get('republic')
        climates = data.get('climates')
        scenario = data.get('scenario')
        riskk = data.get('riskk')

        # Generate the document
        file_path = generate_docx(risk, opportunity, climate, esg, investment, task, publi, republic, climates, scenario, riskk)
        return JsonResponse({'message': f'DOCX file generated and saved at: {file_path}'}, status=200)

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

        # if export_format == 'doc':
        #     # Generate the document
        #     file_path = generate_docx(client, company_desc, directors, independent, no_of_meetings, reporting_year, budget, team_responsibility, management_reporting_line)
        #     return HttpResponse(f'DOCX file generated and saved at: {file_path}')
        # elif export_format == 'pdf':
        #     docx_file_path = generate_docx(client, company_desc, directors, independent, no_of_meetings, reporting_year, budget, team_responsibility, management_reporting_line)
        #     opt = docx_to_pdf(docx_file_path)
        #     return HttpResponse(f'PDF file generated and saved')
        # else:
        #     return HttpResponse(f'Invalid export format: {export_format}')
    
    # context = {
    #     'client': '',
    #     'company_desc': '',
    #     'directors': '',
    #     'independent': '',
    #     'no_of_meetings': '',
    #     'reporting_year': '',
    #     'budget': '',
    #     'team_responsibility': '',
    #     'management_reporting_line': ''
    # }

    # return render(request, 'form.html', context)


# def generate_docx(client, company_desc, directors, independent, no_of_meetings, reporting_year, budget, team_responsibility, management_reporting_line):
#     # Load the document template
#     template = DocxTemplate('/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/templates/Governance Analysis_V2.docx')

#     # Define the context data to be merged with the template
#     context = {
#         'client': client,
#         'company_desc': company_desc,
#         'directors': directors,
#         'independent': independent,
#         'no_of_meetings': no_of_meetings,
#         'reporting_year': reporting_year,
#         'budget': budget,
#         'team_responsibility': team_responsibility,
#         'management_reporting_line': management_reporting_line
#         }

#     # Render the template with the context data
#     template.render(context)

#     # Generate a unique file name with timestamp
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     file_name = f'Governance_Output_{timestamp}.docx'
#     global file_path
#     file_path = f'/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/templates/{file_name}'

#     # Save the rendered document to the new file
#     template.save(file_path)

#     return file_path




def generate_pdf(docx_file_path):
    # Convert DOCX to PDF
    print("Entering generate pdf")
    pdf_file_path = docx_file_path.replace('.docx', '.pdf')
    docx_file_path = file_path
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'Governance_Output_{timestamp}.pdf'
    pdf_file_path = f'/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/templates/{file_name}'
    convert(docx_file_path, pdf_file_path)

    return pdf_file_path


# def docx_to_pdf(input_file, output_file):
def docx_to_pdf(docx_file_path):
    print("Entering generate pdf")

    docx_file_path = file_path
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'Governance_Output_{timestamp}.pdf'

    output = subprocess.run(['/Applications/LibreOffice.app/Contents/MacOS/soffice', '--headless', '--convert-to', 'pdf', docx_file_path, '--outdir', file_name])

    # pdf_file_path = f'/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/templates/{file_name}'

    return output

def generate_docx(risk, opportunity, climate, esg, investment, task, publi, republic, climates, scenario, riskk):
    # Load the document template
    template = DocxTemplate('/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/documents/US-SEC/SEC Draft Manual.docx')

    # Define the context data to be merged with the template
    context = {
        'risk': risk,
        'opportunity': opportunity,
        'climate': climate,
        'esg': esg,
        'investment': investment,
        'task': task,
        'publi': publi,
        'republic': republic,
        'climates': climates,
        'scenario': scenario,
        'riskk': riskk
    }

    # Render the template with the context data
    template.render(context)

    # Generate a unique file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'SEC_Output_{timestamp}.docx'
    file_path = f'/Users/harsha/Desktop/workspace/Django/demoproject/demoapp/documents/US-SEC/{file_name}'

    # Save the rendered document to the new file
    template.save(file_path)

    return file_path