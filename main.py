from weasyprint import HTML, CSS
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "card.html"
template = templateEnv.get_template(TEMPLATE_FILE)

# This data can come from database query
body = {
    "data": {
        "name_last": "Muster",
        "name_first": "Max",
        "birth_date": "01.04.1984",
        "street": "Erste Straße 17",
        "postcode": "52066",
        "city": "Aachen"
    }
}


# # Utility function
# def convertHtmlToPdf(sourceHtml, outputFilename):
#     # This renders template with dynamic data
#     sourceHtml = template.render(json_data=body["data"])
#     outputFilename = "invoice.pdf"
#
#     HTML(sourceHtml).write_pdf(outputFilename)
#
#     # return True on success and False on errors
#     return True

if __name__ == "__main__":
    sourceHtml = template.render(json=body["data"])

    html = HTML(string=sourceHtml)
    css = CSS(filename='card.css')

    outputFilename = "invoice.pdf"

    html.write_pdf(outputFilename, stylesheets=[css])
