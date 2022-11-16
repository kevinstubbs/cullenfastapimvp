# this script is used to populate a word document template with data
import datetime as dt
from docx2pdf import convert
from docxtpl import DocxTemplate, InlineImage

doc = DocxTemplate("photoExhibitionTemplate2.docx")

# simulating data that I imagine would be received from Egnyte API in the future
processedImages = [
    {'images' :  InlineImage(doc, 'images/img1.jpg'), 'captions': 'I think this is a cat, the breed is: ___'},
    {'images' : InlineImage(doc, 'images/img2.jpg'), 'captions': 'I think this is a dog, the breed is: ___'},
    {'images' : InlineImage(doc,'images/img3.jpg'), 'captions': 'I think this is a puppy, the breed is: ___'} ]


# I will later figure out how to control image size
# processedImages = [
#     {'images' :  InlineImage(doc, 'images/catTest.jpg'), 'captions': 'I think this is a cat, the breed is: ___'},
#     {'images' : InlineImage(doc, 'images/dogTest.jpg'), 'captions': 'I think this is a dog, the breed is: ___'},
#     {'images' : InlineImage(doc,'images/dogTest2.jpg'), 'captions': 'I think this is a puppy, the breed is: ___'}, 
#     {'images' : InlineImage(doc,'images/dunnoTest.jpg'), 'captions': 'I have no clue what this is'}]

todayStr = dt.datetime.now().strftime("%d-%b-%Y")

# create context to pass data to template
context = {
    "reportDtStr": todayStr,
    "processedImages": processedImages
}

# render context into the document object
doc.render(context)

# save the document object as a word file
reportWordPath = 'reports/report_{0}.docx'.format(todayStr)
doc.save(reportWordPath)

# convert the word file as pdf file
convert(reportWordPath, reportWordPath.replace(".docx", ".pdf"))
