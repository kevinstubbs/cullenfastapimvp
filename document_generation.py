import datetime as dt
from docx.shared import Mm
from docx2pdf import convert  # type: ignore
from docxtpl import DocxTemplate, InlineImage  # type: ignore
from models import MetaData


# CHANGE
TEMPLATE = "photoExhibitionTemplate2.docx"
# TEMPLATE = "MVP/photoExhibitionTemplate2.docx"


def create_report(image_data: list[MetaData]) -> str:
    doc = DocxTemplate(TEMPLATE)

    process_data = []

    for data in image_data:
        # SECURITY: Don't allow the user to provide arbitrary paths to a file.
        # Best: Just accept a file id, and then look up the location of that file (based on id - not name) in a database.
        # When you upload => store the file path w/ random ID in the database, return the ID to the user.
        temp_dict = {"image": InlineImage(doc, ''.join([data.folder_name, '/', data.file_name]), width=Mm(20), height=Mm(10)), "caption": data.caption, "confidence": data.confidence}
        process_data.append(temp_dict)

    today = dt.datetime.now().strftime("%d-%b-%Y")

    # create context to pass data to template
    context = {
        "reportDtStr": today,
        "processedImages": process_data
    }

    # render context into the document object
    doc.render(context)

    # save the document object as a word file
    # CHANGE
    reportWordPath = 'reports/report_{0}.docx'.format(today)
    # reportWordPath = 'MVP/reports/report_{0}.docx'.format(today)
    doc.save(reportWordPath)

    # convert the word file as pdf file
    # convert(reportWordPath, reportWordPath.replace(".docx", ".pdf"))
    return reportWordPath
